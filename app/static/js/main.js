const nav = document.getElementById("nav-links");
const leftButton = document.getElementById("nav-left");
const rightButton = document.getElementById("nav-right");

if (nav && leftButton && rightButton) {
    leftButton.addEventListener("click", function() {
        nav.scrollBy({
            left: -300,
            behavior: "smooth"
        });
    });

    rightButton.addEventListener("click", function() {
        nav.scrollBy({
            left: 300,
            behavior: "smooth"
        });
    });
}

function getCanvasContext(canvas, minimumHeight) {
    if (!canvas) {
        return null;
    }

    const parent = canvas.parentElement;
    const width = Math.max(parent.clientWidth, 320);
    const height = Math.max(parent.clientHeight, minimumHeight || 260);
    const ratio = window.devicePixelRatio || 1;

    canvas.width = Math.floor(width * ratio);
    canvas.height = Math.floor(height * ratio);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";

    const context = canvas.getContext("2d");
    context.setTransform(ratio, 0, 0, ratio, 0, 0);

    return {
        context: context,
        width: width,
        height: height
    };
}

function parseNumericValue(text) {
    if (text == null) {
        return null;
    }

    const cleaned = String(text)
        .replace(/,/g, "")
        .replace(/[$₱€£¥%]/g, "")
        .trim();

    if (cleaned === "" || cleaned.toLowerCase() === "n/a" || cleaned.toLowerCase() === "none") {
        return null;
    }

    const match = cleaned.match(/-?\d+(?:\.\d+)?/);
    if (!match) {
        return null;
    }

    const value = Number(match[0]);
    return Number.isFinite(value) ? value : null;
}

function shortDate(value) {
    if (!value) {
        return "";
    }

    const text = String(value);
    const datePart = text.slice(0, 10);
    const parts = datePart.split("-");

    if (parts.length !== 3) {
        return datePart;
    }

    return parts[1] + "/" + parts[2];
}

function formatAxisNumber(value) {
    const absoluteValue = Math.abs(value);

    if (absoluteValue >= 1000000) {
        return (value / 1000000).toFixed(1).replace(/\.0$/, "") + "M";
    }

    if (absoluteValue >= 1000) {
        return (value / 1000).toFixed(1).replace(/\.0$/, "") + "K";
    }

    if (absoluteValue < 1 && absoluteValue !== 0) {
        return value.toFixed(2);
    }

    return Number(value.toFixed(2)).toString();
}

function drawEmptyChart(canvas, message) {
    const data = getCanvasContext(canvas, 260);
    if (!data) {
        return;
    }

    const context = data.context;
    context.clearRect(0, 0, data.width, data.height);
    context.fillStyle = "#64748b";
    context.font = "14px Arial";
    context.textAlign = "center";
    context.fillText(message || "No chart data yet", data.width / 2, data.height / 2);
}

function drawLineChart(canvas, labels, values) {
    const usableValues = values.filter(function(value) {
        return value != null && Number.isFinite(value);
    });

    if (usableValues.length === 0) {
        drawEmptyChart(canvas, "No numeric history yet");
        return;
    }

    const data = getCanvasContext(canvas, 260);
    if (!data) {
        return;
    }

    const context = data.context;
    const width = data.width;
    const height = data.height;
    const left = 58;
    const right = 18;
    const top = 22;
    const bottom = 42;
    const chartWidth = Math.max(width - left - right, 1);
    const chartHeight = Math.max(height - top - bottom, 1);

    let minValue = Math.min.apply(null, usableValues);
    let maxValue = Math.max.apply(null, usableValues);

    if (minValue === maxValue) {
        const padding = Math.abs(minValue || 1) * 0.15;
        minValue -= padding;
        maxValue += padding;
    } else {
        const padding = (maxValue - minValue) * 0.12;
        minValue -= padding;
        maxValue += padding;
    }

    context.clearRect(0, 0, width, height);
    context.font = "12px Arial";
    context.textAlign = "right";
    context.textBaseline = "middle";

    for (let step = 0; step <= 4; step += 1) {
        const y = top + (chartHeight / 4) * step;
        const value = maxValue - ((maxValue - minValue) / 4) * step;

        context.strokeStyle = "rgba(148, 163, 184, 0.25)";
        context.lineWidth = 1;
        context.beginPath();
        context.moveTo(left, y);
        context.lineTo(width - right, y);
        context.stroke();

        context.fillStyle = "#64748b";
        context.fillText(formatAxisNumber(value), left - 9, y);
    }

    const pointCount = values.length;
    const xForIndex = function(index) {
        if (pointCount <= 1) {
            return left + chartWidth / 2;
        }
        return left + (chartWidth * index) / (pointCount - 1);
    };

    const yForValue = function(value) {
        return top + ((maxValue - value) / (maxValue - minValue)) * chartHeight;
    };

    context.strokeStyle = "#2563eb";
    context.lineWidth = 2.5;
    context.lineJoin = "round";
    context.lineCap = "round";
    context.beginPath();

    let started = false;

    values.forEach(function(value, index) {
        if (value == null || !Number.isFinite(value)) {
            started = false;
            return;
        }

        const x = xForIndex(index);
        const y = yForValue(value);

        if (!started) {
            context.moveTo(x, y);
            started = true;
        } else {
            context.lineTo(x, y);
        }
    });

    context.stroke();

    values.forEach(function(value, index) {
        if (value == null || !Number.isFinite(value)) {
            return;
        }

        const x = xForIndex(index);
        const y = yForValue(value);
        context.fillStyle = "#ffffff";
        context.strokeStyle = "#2563eb";
        context.lineWidth = 2;
        context.beginPath();
        context.arc(x, y, 3.5, 0, Math.PI * 2);
        context.fill();
        context.stroke();
    });

    context.fillStyle = "#64748b";
    context.font = "11px Arial";
    context.textAlign = "center";
    context.textBaseline = "top";

    const labelStep = Math.max(1, Math.ceil(labels.length / 6));
    labels.forEach(function(label, index) {
        if (index % labelStep !== 0 && index !== labels.length - 1) {
            return;
        }

        context.fillText(shortDate(label), xForIndex(index), height - bottom + 12);
    });
}

function drawBarChart(canvas, labels, values) {
    if (!values || values.length === 0) {
        drawEmptyChart(canvas, "No activity yet");
        return;
    }

    const data = getCanvasContext(canvas, 260);
    if (!data) {
        return;
    }

    const context = data.context;
    const width = data.width;
    const height = data.height;
    const left = 46;
    const right = 16;
    const top = 20;
    const bottom = 42;
    const chartWidth = Math.max(width - left - right, 1);
    const chartHeight = Math.max(height - top - bottom, 1);
    const maxValue = Math.max.apply(null, values.concat([1]));

    context.clearRect(0, 0, width, height);

    for (let step = 0; step <= 4; step += 1) {
        const y = top + (chartHeight / 4) * step;
        context.strokeStyle = "rgba(148, 163, 184, 0.25)";
        context.lineWidth = 1;
        context.beginPath();
        context.moveTo(left, y);
        context.lineTo(width - right, y);
        context.stroke();
    }

    const slotWidth = chartWidth / values.length;
    const barWidth = Math.max(4, slotWidth * 0.62);

    values.forEach(function(value, index) {
        const barHeight = (value / maxValue) * chartHeight;
        const x = left + index * slotWidth + (slotWidth - barWidth) / 2;
        const y = top + chartHeight - barHeight;

        context.fillStyle = "#0f766e";
        context.fillRect(x, y, barWidth, barHeight);
    });

    context.fillStyle = "#64748b";
    context.font = "11px Arial";
    context.textAlign = "center";
    context.textBaseline = "top";

    const labelStep = Math.max(1, Math.ceil(labels.length / 6));
    labels.forEach(function(label, index) {
        if (index % labelStep !== 0 && index !== labels.length - 1) {
            return;
        }

        const x = left + index * slotWidth + slotWidth / 2;
        context.fillText(shortDate(label), x, height - bottom + 12);
    });
}

function drawHorizontalBarChart(canvas, labels, values) {
    if (!values || values.length === 0) {
        drawEmptyChart(canvas, "No module data yet");
        return;
    }

    const data = getCanvasContext(canvas, 680);
    if (!data) {
        return;
    }

    const context = data.context;
    const width = data.width;
    const height = data.height;
    const left = Math.min(190, Math.max(125, width * 0.27));
    const right = 30;
    const top = 16;
    const bottom = 18;
    const chartWidth = Math.max(width - left - right, 1);
    const chartHeight = Math.max(height - top - bottom, 1);
    const maxValue = Math.max.apply(null, values.concat([1]));
    const slotHeight = chartHeight / values.length;
    const barHeight = Math.max(5, slotHeight * 0.58);

    context.clearRect(0, 0, width, height);
    context.font = "11px Arial";
    context.textBaseline = "middle";

    values.forEach(function(value, index) {
        const y = top + index * slotHeight + slotHeight / 2;
        const widthValue = (value / maxValue) * chartWidth;

        context.fillStyle = "#64748b";
        context.textAlign = "right";
        const label = labels[index].length > 24 ? labels[index].slice(0, 22) + "…" : labels[index];
        context.fillText(label, left - 10, y);

        context.fillStyle = "rgba(37, 99, 235, 0.13)";
        context.fillRect(left, y - barHeight / 2, chartWidth, barHeight);

        context.fillStyle = "#2563eb";
        context.fillRect(left, y - barHeight / 2, widthValue, barHeight);

        context.fillStyle = "#334155";
        context.textAlign = "left";
        context.fillText(String(value), Math.min(left + widthValue + 6, width - 22), y);
    });
}

function createMetricCard(label, value, secondaryText) {
    const card = document.createElement("article");
    card.className = "metric-card";

    const labelElement = document.createElement("span");
    labelElement.textContent = label;

    const valueElement = document.createElement("strong");
    valueElement.textContent = value;

    card.appendChild(labelElement);
    card.appendChild(valueElement);

    if (secondaryText) {
        const secondary = document.createElement("small");
        secondary.textContent = secondaryText;
        card.appendChild(secondary);
    }

    return card;
}

function buildCalculatorDashboard(section) {
    const sourceSelector = section.getAttribute("data-dashboard-source") || ".data-source-table";
    const table = document.querySelector(sourceSelector);

    if (!table || table.rows.length === 0) {
        return;
    }

    const headers = Array.from(table.rows[0].cells).map(function(cell) {
        return cell.textContent.trim();
    });

    const rows = Array.from(table.rows).slice(1);
    const metricGrid = section.querySelector("[data-metric-grid]");
    const recordCountElement = section.querySelector("[data-record-count]");
    const emptyDashboard = section.querySelector("[data-empty-dashboard]");
    const chartGrid = section.querySelector(".chart-grid");
    const dateIndex = headers.length - 1;

    recordCountElement.textContent = rows.length + (rows.length === 1 ? " record" : " records");
    metricGrid.innerHTML = "";

    if (rows.length === 0) {
        emptyDashboard.hidden = false;
        chartGrid.hidden = true;
        metricGrid.appendChild(createMetricCard("Saved records", "0", "Submit the form to begin"));
        return;
    }

    emptyDashboard.hidden = true;
    chartGrid.hidden = false;

    const latestRow = rows[0];
    const usableColumns = [];

    // Prefer calculated columns that have a value on the latest record.
    for (let index = headers.length - 2; index >= 0; index -= 1) {
        if (parseNumericValue(latestRow.cells[index].textContent) != null) {
            usableColumns.push(index);
        }

        if (usableColumns.length >= 4) {
            break;
        }
    }

    // If the newest row has missing values, fill the remaining cards with
    // columns that have numeric values somewhere in the saved history.
    if (usableColumns.length < 4) {
        for (let index = headers.length - 2; index >= 0; index -= 1) {
            if (usableColumns.includes(index)) {
                continue;
            }

            const hasNumericValue = rows.some(function(row) {
                return parseNumericValue(row.cells[index].textContent) != null;
            });

            if (hasNumericValue) {
                usableColumns.push(index);
            }

            if (usableColumns.length >= 4) {
                break;
            }
        }
    }

    metricGrid.appendChild(
        createMetricCard(
            "Saved records",
            String(rows.length),
            "Latest: " + latestRow.cells[dateIndex].textContent.trim()
        )
    );

    usableColumns.forEach(function(index) {
        const displayValue = latestRow.cells[index].textContent.trim() || "N/A";
        metricGrid.appendChild(createMetricCard(headers[index], displayValue, "Latest value"));
    });

    if (usableColumns.length === 0) {
        drawEmptyChart(section.querySelector(".history-chart"), "No numeric history yet");
    } else {
        const primaryColumn = usableColumns[0];
        const historyRows = rows.slice(0, 30).reverse();
        const labels = historyRows.map(function(row) {
            return row.cells[dateIndex].textContent.trim();
        });
        const values = historyRows.map(function(row) {
            return parseNumericValue(row.cells[primaryColumn].textContent);
        });

        const trendTitle = section.querySelector("[data-trend-title]");
        trendTitle.textContent = headers[primaryColumn] + " history";
        drawLineChart(section.querySelector(".history-chart"), labels, values);
    }

    const dateCounts = {};

    rows.forEach(function(row) {
        const dateText = row.cells[dateIndex].textContent.trim().slice(0, 10);
        if (!dateText) {
            return;
        }

        if (!dateCounts[dateText]) {
            dateCounts[dateText] = 0;
        }
        dateCounts[dateText] += 1;
    });

    const activityLabels = Object.keys(dateCounts).sort().slice(-14);
    const activityValues = activityLabels.map(function(label) {
        return dateCounts[label];
    });

    drawBarChart(section.querySelector(".activity-chart"), activityLabels, activityValues);

    section._redrawDashboard = function() {
        if (usableColumns.length > 0) {
            const primaryColumn = usableColumns[0];
            const historyRows = rows.slice(0, 30).reverse();
            const labels = historyRows.map(function(row) {
                return row.cells[dateIndex].textContent.trim();
            });
            const values = historyRows.map(function(row) {
                return parseNumericValue(row.cells[primaryColumn].textContent);
            });
            drawLineChart(section.querySelector(".history-chart"), labels, values);
        }
        drawBarChart(section.querySelector(".activity-chart"), activityLabels, activityValues);
    };
}

function buildGlobalDashboard() {
    const dataElement = document.getElementById("global-dashboard-data");
    if (!dataElement) {
        return;
    }

    let dashboardData;
    try {
        dashboardData = JSON.parse(dataElement.textContent);
    } catch (error) {
        return;
    }

    const modules = dashboardData.modules || [];
    const activity = dashboardData.activity || [];

    const moduleLabels = modules.map(function(module) {
        return module.title;
    });
    const moduleValues = modules.map(function(module) {
        return Number(module.recordCount) || 0;
    });

    const activityLabels = activity.map(function(item) {
        return item.date;
    });
    const activityValues = activity.map(function(item) {
        return Number(item.count) || 0;
    });

    const moduleCanvas = document.getElementById("module-count-chart");
    const activityCanvas = document.getElementById("global-activity-chart");

    drawHorizontalBarChart(moduleCanvas, moduleLabels, moduleValues);
    drawLineChart(activityCanvas, activityLabels, activityValues);

    dataElement._redrawGlobal = function() {
        drawHorizontalBarChart(moduleCanvas, moduleLabels, moduleValues);
        drawLineChart(activityCanvas, activityLabels, activityValues);
    };
}

function buildAllDashboards() {
    const sections = document.querySelectorAll(".calculator-dashboard");
    sections.forEach(function(section) {
        buildCalculatorDashboard(section);
    });

    buildGlobalDashboard();
}

buildAllDashboards();

let resizeTimer = null;
window.addEventListener("resize", function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
        document.querySelectorAll(".calculator-dashboard").forEach(function(section) {
            if (typeof section._redrawDashboard === "function") {
                section._redrawDashboard();
            }
        });

        const dataElement = document.getElementById("global-dashboard-data");
        if (dataElement && typeof dataElement._redrawGlobal === "function") {
            dataElement._redrawGlobal();
        }
    }, 120);
});
