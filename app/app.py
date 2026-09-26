from flask import Flask, render_template, request, redirect, url_for, Response
import sqlite3
import csv
import io
from collections import Counter
import database
import tne

DB_PATH = database.initialize_database()

app = Flask(__name__)

MODULES = {
    "bbm": {"title": "Basic Business Math", "table": "bbm_db"},
    "mam": {"title": "Markup and Markdown", "table": "mam_db"},
    "dis": {"title": "Discounts", "table": "dis_db"},
    "pnl": {"title": "Profit and Loss", "table": "pnl_db"},
    "sin": {"title": "Simple Interest", "table": "sin_db"},
    "cin": {"title": "Compound Interest", "table": "cin_db"},
    "ann": {"title": "Annuities", "table": "ann_db"},
    "loa": {"title": "Loans", "table": "loa_db"},
    "pfv": {"title": "Present and Future Value", "table": "pfv_db"},
    "dep": {"title": "Depreciation", "table": "dep_db"},
    "com": {"title": "Commission", "table": "com_db"},
    "paw": {"title": "Payroll and Wages", "table": "paw_db"},
    "tax": {"title": "Taxes", "table": "tax_db"},
    "bea": {"title": "Break-Even Analysis", "table": "bea_db"},
    "brc": {"title": "Business Revenue and Cost", "table": "brc_db"},
    "rnp": {"title": "Ratios and Proportions", "table": "rnp_db"},
    "sta": {"title": "Statistics", "table": "sta_db"},
    "pro": {"title": "Probability", "table": "pro_db"},
    "prc": {"title": "Percentage and Rate Conversions", "table": "prc_db"},
    "fra": {"title": "Financial Ratios", "table": "fra_db"},
    "cbu": {"title": "Capital Budgeting", "table": "cbu_db"},
    "sbo": {"title": "Stocks and Bonds", "table": "sbo_db"},
    "inc": {"title": "Insurance", "table": "inc_db"},
    "pno": {"title": "Promissory Notes", "table": "pno_db"}
}

def _getModuleColumns(tableName):
    columns = []
    for columnName, columnType in database.TABLES[tableName]:
        if columnName != "id":
            columns.append(columnName)
    return columns

def _getGlobalDashboard():
    print("Building the main dashboard...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    modules = []
    activityCounter = Counter()
    totalRecords = 0
    latestActivity = None
    mostUsedModule = "N/A"
    mostUsedCount = -1

    for moduleName, moduleData in MODULES.items():
        tableName = moduleData["table"]

        cursor.execute("SELECT COUNT(*) AS total FROM " + tableName)
        recordCount = cursor.fetchone()["total"]
        totalRecords += recordCount

        cursor.execute("SELECT created_at FROM " + tableName + " WHERE created_at IS NOT NULL ORDER BY rowid DESC LIMIT 1")
        latestRow = cursor.fetchone()
        latestDate = latestRow["created_at"] if latestRow != None else None

        if latestDate != None and (latestActivity == None or str(latestDate) > str(latestActivity)):
            latestActivity = latestDate

        if recordCount > mostUsedCount:
            mostUsedCount = recordCount
            mostUsedModule = moduleData["title"]

        cursor.execute("SELECT created_at FROM " + tableName + " WHERE created_at IS NOT NULL")
        for row in cursor.fetchall():
            dateText = str(row["created_at"])[0:10]
            activityCounter[dateText] += 1

        modules.append({
            "key": moduleName,
            "title": moduleData["title"],
            "recordCount": recordCount,
            "latestDate": latestDate
        })

    conn.close()

    activity = []
    for dateText in sorted(activityCounter.keys())[-30:]:
        activity.append({"date": dateText, "count": activityCounter[dateText]})

    summary = {
        "totalRecords": totalRecords,
        "modulesWithData": len([module for module in modules if module["recordCount"] > 0]),
        "totalModules": len(modules),
        "latestActivity": latestActivity,
        "mostUsedModule": mostUsedModule if totalRecords > 0 else "N/A"
    }

    return summary, modules, activity

@app.route('/dashboard')
def dashboard():
    summary, modules, activity = _getGlobalDashboard()
    return render_template('dashboard.html', summary=summary, modules=modules, activity=activity)

@app.route('/export/<moduleName>.csv')
def exportCsv(moduleName):
    if moduleName not in MODULES:
        return "Unknown calculator module.", 404

    moduleData = MODULES[moduleName]
    tableName = moduleData["table"]
    columns = _getModuleColumns(tableName)

    print("Exporting " + moduleData["title"] + " history to CSV...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT " + ", ".join(columns) + " FROM " + tableName + " ORDER BY rowid DESC")
    rows = cursor.fetchall()
    conn.close()

    csvFile = io.StringIO()
    writer = csv.writer(csvFile)
    writer.writerow(columns)

    for row in rows:
        writer.writerow([row[column] for column in columns])

    fileName = moduleName + "_history.csv"
    return Response(
        csvFile.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=" + fileName}
    )


def _numberInput(inputName):
    try:
        value = request.form.get(inputName)
        if value == None or value == "":
            return None
        print("Changing the data type of " + inputName + " input...")
        return float(value)
    except (ValueError, TypeError):
        print("Invalid value for " + inputName + ".")
        return None

def _listInput(inputName):
    try:
        value = request.form.get(inputName)
        if value == None or value.strip() == "":
            return None
        values = []
        for item in value.split(","):
            if item.strip() != "":
                values.append(float(item.strip()))
        return values
    except (ValueError, TypeError):
        print("Invalid list value for " + inputName + ".")
        return None

def _getRows(tableName, columns):
    print("Connecting to the database...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    columnText = ", ".join(columns)
    cursor.execute("SELECT " + columnText + ", created_at FROM " + tableName + " ORDER BY rowid DESC")
    rows = cursor.fetchall()
    conn.close()
    print("Obtained the values from " + tableName + ".")
    return rows

@app.route('/', methods=['POST', 'GET'])
def bbm():
    if request.method == 'POST':
        percentage = _numberInput("percentage")
        rate = _numberInput("rate")
        base = _numberInput("base")
        print("Calling the function for calculating the missing values...")
        try:
            percentage, rate, base, percentageChange, percentIncrease, percentDecrease = tne.calcVal_bbm(percentage, rate, base, DB_PATH)
            print("Calling the function for inserting the calculated values on the database...")
            updateResult = database.updateBbm_db(percentage, rate, base, percentageChange, percentIncrease, percentDecrease, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('bbm'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Basic Business Math: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    bbm_db = _getRows("bbm_db", ["percentage", "rate", "base", "percentageChange", "percentIncrease", "percentDecrease"])
    return render_template('bbm.html', bbm=bbm_db)

@app.route('/mam', methods=['POST', 'GET'])
def mam():
    if request.method == 'POST':
        sellingPrice = _numberInput("sellingPrice")
        markup = _numberInput("markup")
        if sellingPrice == None or markup == None:
            return "Selling price and markup are required."
        cost = None
        print("Calling the function for calculating the missing values...")
        try:
            markup, markupRateOnCost, markupRateOnSellingPrice, sellingPrice, sellingPriceFromMarkupRate, cost, markdown, markdownRate, salePrice, salePriceFromMarkdownRate = tne.calcVal_mam(sellingPrice, markup, cost, DB_PATH)
            updateResult = database.updateMam_db(markup, markupRateOnCost, markupRateOnSellingPrice, sellingPrice, sellingPriceFromMarkupRate, cost, markdown, markdownRate, salePrice, salePriceFromMarkdownRate, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('mam'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Markup and Markdown: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    mam_db = _getRows("mam_db", ["markup", "markupRateOnCost", "markupRateOnSellingPrice", "sellingPrice", "sellingPriceFromMarkupRate", "cost", "markdown", "markdownRate", "salePrice", "salePriceFromMarkdownRate"])
    return render_template('mam.html', mam=mam_db)

@app.route('/discounts', methods=['POST', 'GET'])
def dis():
    if request.method == 'POST':
        listPrice = _numberInput("listPrice")
        discountRate = _numberInput("discountRate")
        secondDiscountRate = _numberInput("secondDiscountRate")
        try:
            listPrice, discountRate, secondDiscountRate, tradeDiscount, netPrice, netPriceEquivalent, calculatedDiscountRate, seriesDiscount, equivalentDiscount = tne.calcVal_dis(listPrice, discountRate, secondDiscountRate)
            updateResult = database.updateDis_db(listPrice, discountRate, secondDiscountRate, tradeDiscount, netPrice, netPriceEquivalent, calculatedDiscountRate, seriesDiscount, equivalentDiscount, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('dis'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Discounts: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("dis_db", ['listPrice', 'discountRate', 'secondDiscountRate', 'tradeDiscount', 'netPrice', 'netPriceEquivalent', 'calculatedDiscountRate', 'seriesDiscount', 'equivalentDiscount'])
    return render_template('dis.html', dis=rows)

@app.route('/profit-and-loss', methods=['POST', 'GET'])
def pnl():
    if request.method == 'POST':
        cost = _numberInput("cost")
        sellingPrice = _numberInput("sellingPrice")
        desiredProfitRate = _numberInput("desiredProfitRate")
        try:
            cost, sellingPrice, desiredProfitRate, profit, loss, profitRateOnCost, profitMargin, sellingPriceForDesiredProfit, costFromSellingPrice, lossRate = tne.calcVal_pnl(cost, sellingPrice, desiredProfitRate)
            updateResult = database.updatePnl_db(cost, sellingPrice, desiredProfitRate, profit, loss, profitRateOnCost, profitMargin, sellingPriceForDesiredProfit, costFromSellingPrice, lossRate, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('pnl'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Profit and Loss: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("pnl_db", ['cost', 'sellingPrice', 'desiredProfitRate', 'profit', 'loss', 'profitRateOnCost', 'profitMargin', 'sellingPriceForDesiredProfit', 'costFromSellingPrice', 'lossRate'])
    return render_template('pnl.html', pnl=rows)

@app.route('/simple-interest', methods=['POST', 'GET'])
def sin():
    if request.method == 'POST':
        principal = _numberInput("principal")
        rate = _numberInput("rate")
        time = _numberInput("time")
        try:
            simpleInterest, principal, rate, time, maturityValue, maturityValueDirect = tne.calcVal_sin(principal, rate, time)
            updateResult = database.updateSin_db(simpleInterest, principal, rate, time, maturityValue, maturityValueDirect, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('sin'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Simple Interest: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("sin_db", ['simpleInterest', 'principal', 'rate', 'time', 'maturityValue', 'maturityValueDirect'])
    return render_template('sin.html', sin=rows)

@app.route('/compound-interest', methods=['POST', 'GET'])
def cin():
    if request.method == 'POST':
        principal = _numberInput("principal")
        rate = _numberInput("rate")
        time = _numberInput("time")
        compoundsPerYear = _numberInput("compoundsPerYear")
        try:
            inputPrincipal, rate, time, compoundsPerYear, compoundAmount, compoundInterest, calculatedPrincipal, futureValue, presentValue, effectiveAnnualRate = tne.calcVal_cin(principal, rate, time, compoundsPerYear)
            updateResult = database.updateCin_db(inputPrincipal, rate, time, compoundsPerYear, compoundAmount, compoundInterest, calculatedPrincipal, futureValue, presentValue, effectiveAnnualRate, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('cin'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Compound Interest: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("cin_db", ['inputPrincipal', 'rate', 'time', 'compoundsPerYear', 'compoundAmount', 'compoundInterest', 'calculatedPrincipal', 'futureValue', 'presentValue', 'effectiveAnnualRate'])
    return render_template('cin.html', cin=rows)

@app.route('/annuities', methods=['POST', 'GET'])
def ann():
    if request.method == 'POST':
        payment = _numberInput("payment")
        periodicRate = _numberInput("periodicRate")
        periods = _numberInput("periods")
        try:
            payment, periodicRate, periods, futureValueOfOrdinaryAnnuity, presentValueOfOrdinaryAnnuity, futureValueOfAnnuityDue, presentValueOfAnnuityDue, regularPayment = tne.calcVal_ann(payment, periodicRate, periods)
            updateResult = database.updateAnn_db(payment, periodicRate, periods, futureValueOfOrdinaryAnnuity, presentValueOfOrdinaryAnnuity, futureValueOfAnnuityDue, presentValueOfAnnuityDue, regularPayment, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('ann'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Annuities: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("ann_db", ['payment', 'periodicRate', 'periods', 'futureValueOfOrdinaryAnnuity', 'presentValueOfOrdinaryAnnuity', 'futureValueOfAnnuityDue', 'presentValueOfAnnuityDue', 'regularPayment'])
    return render_template('ann.html', ann=rows)

@app.route('/loans', methods=['POST', 'GET'])
def loa():
    if request.method == 'POST':
        principal = _numberInput("principal")
        periodicRate = _numberInput("periodicRate")
        periods = _numberInput("periods")
        paymentsMade = _numberInput("paymentsMade")
        try:
            principal, periodicRate, periods, paymentsMade, periodicalLoanPayment, loanPayment, totalPayment, totalInterest, outstandingBalance = tne.calcVal_loa(principal, periodicRate, periods, paymentsMade)
            updateResult = database.updateLoa_db(principal, periodicRate, periods, paymentsMade, periodicalLoanPayment, loanPayment, totalPayment, totalInterest, outstandingBalance, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('loa'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Loans: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("loa_db", ['principal', 'periodicRate', 'periods', 'paymentsMade', 'periodicalLoanPayment', 'loanPayment', 'totalPayment', 'totalInterest', 'outstandingBalance'])
    return render_template('loa.html', loa=rows)

@app.route('/present-and-future-value', methods=['POST', 'GET'])
def pfv():
    if request.method == 'POST':
        presentValue = _numberInput("presentValue")
        rate = _numberInput("rate")
        periods = _numberInput("periods")
        time = _numberInput("time")
        compoundsPerYear = _numberInput("compoundsPerYear")
        try:
            inputPresentValue, rate, periods, time, compoundsPerYear, futureValue, presentValue, simpleInterestFutureValue, compoundInterestFutureValue = tne.calcVal_pfv(presentValue, rate, periods, time, compoundsPerYear)
            updateResult = database.updatePfv_db(inputPresentValue, rate, periods, time, compoundsPerYear, futureValue, presentValue, simpleInterestFutureValue, compoundInterestFutureValue, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('pfv'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Present and Future Value: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("pfv_db", ['inputPresentValue', 'rate', 'periods', 'time', 'compoundsPerYear', 'futureValue', 'presentValue', 'simpleInterestFutureValue', 'compoundInterestFutureValue'])
    return render_template('pfv.html', pfv=rows)

@app.route('/depreciation', methods=['POST', 'GET'])
def dep():
    if request.method == 'POST':
        cost = _numberInput("cost")
        salvageValue = _numberInput("salvageValue")
        usefulLife = _numberInput("usefulLife")
        time = _numberInput("time")
        decliningRate = _numberInput("decliningRate")
        try:
            cost, salvageValue, usefulLife, time, decliningRate, straightLineDepreciation, bookValue, totalDepreciation, decliningBalanceDepreciation, decliningBalanceBookValue = tne.calcVal_dep(cost, salvageValue, usefulLife, time, decliningRate)
            updateResult = database.updateDep_db(cost, salvageValue, usefulLife, time, decliningRate, straightLineDepreciation, bookValue, totalDepreciation, decliningBalanceDepreciation, decliningBalanceBookValue, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('dep'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Depreciation: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("dep_db", ['cost', 'salvageValue', 'usefulLife', 'time', 'decliningRate', 'straightLineDepreciation', 'bookValue', 'totalDepreciation', 'decliningBalanceDepreciation', 'decliningBalanceBookValue'])
    return render_template('dep.html', dep=rows)

@app.route('/commission', methods=['POST', 'GET'])
def com():
    if request.method == 'POST':
        sales = _numberInput("sales")
        commissionRate = _numberInput("commissionRate")
        salary = _numberInput("salary")
        try:
            inputSales, inputCommissionRate, salary, commission, totalEarnings, commissionRate, sales = tne.calcVal_com(sales, commissionRate, salary)
            updateResult = database.updateCom_db(inputSales, inputCommissionRate, salary, commission, totalEarnings, commissionRate, sales, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('com'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Commission: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("com_db", ['inputSales', 'inputCommissionRate', 'salary', 'commission', 'totalEarnings', 'commissionRate', 'sales'])
    return render_template('com.html', com=rows)

@app.route('/payroll-and-wages', methods=['POST', 'GET'])
def paw():
    if request.method == 'POST':
        hourlyRate = _numberInput("hourlyRate")
        regularHours = _numberInput("regularHours")
        overtimeRate = _numberInput("overtimeRate")
        overtimeHours = _numberInput("overtimeHours")
        taxes = _numberInput("taxes")
        contributions = _numberInput("contributions")
        otherDeductions = _numberInput("otherDeductions")
        otherEarnings = _numberInput("otherEarnings")
        try:
            hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings, grossPay, regularPay, overtimePay, netPay, totalDeductions = tne.calcVal_paw(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings)
            updateResult = database.updatePaw_db(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings, grossPay, regularPay, overtimePay, netPay, totalDeductions, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('paw'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Payroll and Wages: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("paw_db", ['hourlyRate', 'regularHours', 'overtimeRate', 'overtimeHours', 'taxes', 'contributions', 'otherDeductions', 'otherEarnings', 'grossPay', 'regularPay', 'overtimePay', 'netPay', 'totalDeductions'])
    return render_template('paw.html', paw=rows)

@app.route('/taxes', methods=['POST', 'GET'])
def tax():
    if request.method == 'POST':
        grossIncome = _numberInput("grossIncome")
        allowableDeductions = _numberInput("allowableDeductions")
        taxRate = _numberInput("taxRate")
        otherDeductions = _numberInput("otherDeductions")
        try:
            grossIncome, allowableDeductions, taxRate, otherDeductions, basicTax, taxableIncome, netIncome = tne.calcVal_tax(grossIncome, allowableDeductions, taxRate, otherDeductions)
            updateResult = database.updateTax_db(grossIncome, allowableDeductions, taxRate, otherDeductions, basicTax, taxableIncome, netIncome, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('tax'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Taxes: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("tax_db", ['grossIncome', 'allowableDeductions', 'taxRate', 'otherDeductions', 'basicTax', 'taxableIncome', 'netIncome'])
    return render_template('tax.html', tax=rows)

@app.route('/break-even-analysis', methods=['POST', 'GET'])
def bea():
    if request.method == 'POST':
        sellingPrice = _numberInput("sellingPrice")
        variableCostPerUnit = _numberInput("variableCostPerUnit")
        fixedCost = _numberInput("fixedCost")
        quantity = _numberInput("quantity")
        try:
            sellingPrice, variableCostPerUnit, fixedCost, quantity, contributionMargin, contributionMarginRatio, breakEvenUnits, breakEvenSales, profit, totalRevenue, totalCost = tne.calcVal_bea(sellingPrice, variableCostPerUnit, fixedCost, quantity)
            updateResult = database.updateBea_db(sellingPrice, variableCostPerUnit, fixedCost, quantity, contributionMargin, contributionMarginRatio, breakEvenUnits, breakEvenSales, profit, totalRevenue, totalCost, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('bea'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Break-Even Analysis: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("bea_db", ['sellingPrice', 'variableCostPerUnit', 'fixedCost', 'quantity', 'contributionMargin', 'contributionMarginRatio', 'breakEvenUnits', 'breakEvenSales', 'profit', 'totalRevenue', 'totalCost'])
    return render_template('bea.html', bea=rows)

@app.route('/business-revenue-and-cost', methods=['POST', 'GET'])
def brc():
    if request.method == 'POST':
        price = _numberInput("price")
        quantity = _numberInput("quantity")
        fixedCost = _numberInput("fixedCost")
        variableCostPerUnit = _numberInput("variableCostPerUnit")
        try:
            price, quantity, fixedCost, variableCostPerUnit, revenue, totalCost, variableCost, profit, averageCost, averageRevenue, unitProfit = tne.calcVal_brc(price, quantity, fixedCost, variableCostPerUnit)
            updateResult = database.updateBrc_db(price, quantity, fixedCost, variableCostPerUnit, revenue, totalCost, variableCost, profit, averageCost, averageRevenue, unitProfit, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('brc'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Business Revenue and Cost: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("brc_db", ['price', 'quantity', 'fixedCost', 'variableCostPerUnit', 'revenue', 'totalCost', 'variableCost', 'profit', 'averageCost', 'averageRevenue', 'unitProfit'])
    return render_template('brc.html', brc=rows)

@app.route('/ratios-and-proportions', methods=['POST', 'GET'])
def rnp():
    if request.method == 'POST':
        a = _numberInput("a")
        b = _numberInput("b")
        c = _numberInput("c")
        d = _numberInput("d")
        quantity = _numberInput("quantity")
        units = _numberInput("units")
        k = _numberInput("k")
        x = _numberInput("x")
        try:
            a, b, c, d, quantity, units, k, x, ratio, proportion, crossMultiplication, unitRate, directVariation, inverseVariation = tne.calcVal_rnp(a, b, c, d, quantity, units, k, x)
            updateResult = database.updateRnp_db(a, b, c, d, quantity, units, k, x, ratio, proportion, crossMultiplication, unitRate, directVariation, inverseVariation, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('rnp'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Ratios and Proportions: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("rnp_db", ['a', 'b', 'c', 'd', 'quantity', 'units', 'k', 'x', 'ratio', 'proportion', 'crossMultiplication', 'unitRate', 'directVariation', 'inverseVariation'])
    return render_template('rnp.html', rnp=rows)

@app.route('/statistics', methods=['POST', 'GET'])
def sta():
    if request.method == 'POST':
        values = _listInput("values")
        weights = _listInput("weights")
        try:
            valuesInput, weightsInput, mean, weightedMean, rangeValue, populationVariance, populationStandardDeviation, populationMean, sampleMean, median, mode, sampleVariance, sampleStandardDeviation = tne.calcVal_sta(values, weights)
            updateResult = database.updateSta_db(valuesInput, weightsInput, mean, weightedMean, rangeValue, populationVariance, populationStandardDeviation, populationMean, sampleMean, median, mode, sampleVariance, sampleStandardDeviation, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('sta'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Statistics: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("sta_db", ['valuesInput', 'weightsInput', 'mean', 'weightedMean', 'rangeValue', 'populationVariance', 'populationStandardDeviation', 'populationMean', 'sampleMean', 'median', 'mode', 'sampleVariance', 'sampleStandardDeviation'])
    return render_template('sta.html', sta=rows)

@app.route('/probability', methods=['POST', 'GET'])
def pro():
    if request.method == 'POST':
        favorable = _numberInput("favorable")
        total = _numberInput("total")
        pA = _numberInput("pA")
        pB = _numberInput("pB")
        pAandB = _numberInput("pAandB")
        try:
            favorable, total, pA, pB, pAandB, basicProbability, complement, additionRule, multiplicationRule, conditionalProbability = tne.calcVal_pro(favorable, total, pA, pB, pAandB)
            updateResult = database.updatePro_db(favorable, total, pA, pB, pAandB, basicProbability, complement, additionRule, multiplicationRule, conditionalProbability, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('pro'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Probability: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("pro_db", ['favorable', 'total', 'pA', 'pB', 'pAandB', 'basicProbability', 'complement', 'additionRule', 'multiplicationRule', 'conditionalProbability'])
    return render_template('pro.html', pro=rows)

@app.route('/percentage-and-rate-conversions', methods=['POST', 'GET'])
def prc():
    if request.method == 'POST':
        decimal = _numberInput("decimal")
        percentage = _numberInput("percentage")
        fraction = _numberInput("fraction")
        annualRate = _numberInput("annualRate")
        try:
            inputDecimal, inputPercentage, inputFraction, annualRate, decimalToPercentage, percentageToDecimal, percentageToFraction, fractionToPercentage, monthlyRate, quarterlyRate, semiannualRate = tne.calcVal_prc(decimal, percentage, fraction, annualRate)
            updateResult = database.updatePrc_db(inputDecimal, inputPercentage, inputFraction, annualRate, decimalToPercentage, percentageToDecimal, percentageToFraction, fractionToPercentage, monthlyRate, quarterlyRate, semiannualRate, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('prc'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Percentage and Rate Conversions: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("prc_db", ['inputDecimal', 'inputPercentage', 'inputFraction', 'annualRate', 'decimalToPercentage', 'percentageToDecimal', 'percentageToFraction', 'fractionToPercentage', 'monthlyRate', 'quarterlyRate', 'semiannualRate'])
    return render_template('prc.html', prc=rows)

@app.route('/financial-ratios', methods=['POST', 'GET'])
def fra():
    if request.method == 'POST':
        currentAssets = _numberInput("currentAssets")
        currentLiabilities = _numberInput("currentLiabilities")
        inventory = _numberInput("inventory")
        netProfit = _numberInput("netProfit")
        investment = _numberInput("investment")
        netIncome = _numberInput("netIncome")
        totalAssets = _numberInput("totalAssets")
        shareholderEquity = _numberInput("shareholderEquity")
        totalDebt = _numberInput("totalDebt")
        totalEquity = _numberInput("totalEquity")
        revenue = _numberInput("revenue")
        try:
            currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue, currentRatio, quickRatio, returnOnInvestment, returnOnAssets, returnOnEquity, debtToEquityRatio, netProfitMargin = tne.calcVal_fra(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue)
            updateResult = database.updateFra_db(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue, currentRatio, quickRatio, returnOnInvestment, returnOnAssets, returnOnEquity, debtToEquityRatio, netProfitMargin, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('fra'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Financial Ratios: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("fra_db", ['currentAssets', 'currentLiabilities', 'inventory', 'netProfit', 'investment', 'netIncome', 'totalAssets', 'shareholderEquity', 'totalDebt', 'totalEquity', 'revenue', 'currentRatio', 'quickRatio', 'returnOnInvestment', 'returnOnAssets', 'returnOnEquity', 'debtToEquityRatio', 'netProfitMargin'])
    return render_template('fra.html', fra=rows)

@app.route('/capital-budgeting', methods=['POST', 'GET'])
def cbu():
    if request.method == 'POST':
        initialInvestment = _numberInput("initialInvestment")
        annualCashFlow = _numberInput("annualCashFlow")
        discountRate = _numberInput("discountRate")
        cashFlows = _listInput("cashFlows")
        try:
            initialInvestment, annualCashFlow, discountRate, cashFlows, netPresentValue, internalRateOfReturn, paybackPeriod = tne.calcVal_cbu(initialInvestment, annualCashFlow, discountRate, cashFlows)
            updateResult = database.updateCbu_db(initialInvestment, annualCashFlow, discountRate, cashFlows, netPresentValue, internalRateOfReturn, paybackPeriod, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('cbu'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Capital Budgeting: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("cbu_db", ['initialInvestment', 'annualCashFlow', 'discountRate', 'cashFlows', 'netPresentValue', 'internalRateOfReturn', 'paybackPeriod'])
    return render_template('cbu.html', cbu=rows)

@app.route('/stocks-and-bonds', methods=['POST', 'GET'])
def sbo():
    if request.method == 'POST':
        annualDividend = _numberInput("annualDividend")
        sharePrice = _numberInput("sharePrice")
        annualCoupon = _numberInput("annualCoupon")
        bondPrice = _numberInput("bondPrice")
        try:
            annualDividend, sharePrice, annualCoupon, bondPrice, dividendYield, currentBondYield = tne.calcVal_sbo(annualDividend, sharePrice, annualCoupon, bondPrice)
            updateResult = database.updateSbo_db(annualDividend, sharePrice, annualCoupon, bondPrice, dividendYield, currentBondYield, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('sbo'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Stocks and Bonds: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("sbo_db", ['annualDividend', 'sharePrice', 'annualCoupon', 'bondPrice', 'dividendYield', 'currentBondYield'])
    return render_template('sbo.html', sbo=rows)

@app.route('/insurance', methods=['POST', 'GET'])
def inc():
    if request.method == 'POST':
        faceValue = _numberInput("faceValue")
        rate = _numberInput("rate")
        annualPremium = _numberInput("annualPremium")
        shortRateFactor = _numberInput("shortRateFactor")
        try:
            faceValue, rate, annualPremium, shortRateFactor, insurancePremium, shortRatePremium = tne.calcVal_inc(faceValue, rate, annualPremium, shortRateFactor)
            updateResult = database.updateInc_db(faceValue, rate, annualPremium, shortRateFactor, insurancePremium, shortRatePremium, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('inc'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Insurance: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("inc_db", ['faceValue', 'rate', 'annualPremium', 'shortRateFactor', 'insurancePremium', 'shortRatePremium'])
    return render_template('inc.html', inc=rows)

@app.route('/promissory-notes', methods=['POST', 'GET'])
def pno():
    if request.method == 'POST':
        principal = _numberInput("principal")
        rate = _numberInput("rate")
        time = _numberInput("time")
        discountRate = _numberInput("discountRate")
        try:
            principal, rate, time, discountRate, maturityValue, bankDiscount, proceeds = tne.calcVal_pno(principal, rate, time, discountRate)
            updateResult = database.updatePno_db(principal, rate, time, discountRate, maturityValue, bankDiscount, proceeds, DB_PATH)
            if updateResult == 1:
                return redirect(url_for('pno'))
            return "Incomplete values or invalid values."
        except Exception as e:
            print("Failed to calculate Promissory Notes: " + str(e))
            return "Incomplete values or invalid values: " + str(e)
    rows = _getRows("pno_db", ['principal', 'rate', 'time', 'discountRate', 'maturityValue', 'bankDiscount', 'proceeds'])
    return render_template('pno.html', pno=rows)

if __name__ == '__main__':
    app.run(debug=True)