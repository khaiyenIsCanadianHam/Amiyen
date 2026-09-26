from pathlib import Path
import sqlite3

TABLES = {
    "bbm_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("percentage", "NUMERIC"), ("rate", "NUMERIC"), ("base", "NUMERIC"),
        ("percentageChange", "NUMERIC"), ("percentIncrease", "NUMERIC"), ("percentDecrease", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "mam_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("markup", "NUMERIC"), ("markupRateOnCost", "NUMERIC"), ("markupRateOnSellingPrice", "NUMERIC"),
        ("sellingPrice", "NUMERIC"), ("sellingPriceFromMarkupRate", "NUMERIC"), ("cost", "NUMERIC"),
        ("markdown", "NUMERIC"), ("markdownRate", "NUMERIC"), ("salePrice", "NUMERIC"),
        ("salePriceFromMarkdownRate", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "dis_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("listPrice", "NUMERIC"), ("discountRate", "NUMERIC"), ("secondDiscountRate", "NUMERIC"),
        ("tradeDiscount", "NUMERIC"), ("netPrice", "NUMERIC"), ("netPriceEquivalent", "NUMERIC"),
        ("calculatedDiscountRate", "NUMERIC"), ("seriesDiscount", "NUMERIC"), ("equivalentDiscount", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "pnl_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("cost", "NUMERIC"), ("sellingPrice", "NUMERIC"), ("desiredProfitRate", "NUMERIC"),
        ("profit", "NUMERIC"), ("loss", "NUMERIC"), ("profitRateOnCost", "NUMERIC"),
        ("profitMargin", "NUMERIC"), ("sellingPriceForDesiredProfit", "NUMERIC"),
        ("costFromSellingPrice", "NUMERIC"), ("lossRate", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "sin_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("simpleInterest", "NUMERIC"), ("principal", "NUMERIC"), ("rate", "NUMERIC"), ("time", "NUMERIC"),
        ("maturityValue", "NUMERIC"), ("maturityValueDirect", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "cin_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("inputPrincipal", "NUMERIC"), ("rate", "NUMERIC"), ("time", "NUMERIC"), ("compoundsPerYear", "NUMERIC"),
        ("compoundAmount", "NUMERIC"), ("compoundInterest", "NUMERIC"), ("calculatedPrincipal", "NUMERIC"),
        ("futureValue", "NUMERIC"), ("presentValue", "NUMERIC"), ("effectiveAnnualRate", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "ann_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("payment", "NUMERIC"), ("periodicRate", "NUMERIC"), ("periods", "NUMERIC"),
        ("futureValueOfOrdinaryAnnuity", "NUMERIC"), ("presentValueOfOrdinaryAnnuity", "NUMERIC"),
        ("futureValueOfAnnuityDue", "NUMERIC"), ("presentValueOfAnnuityDue", "NUMERIC"),
        ("regularPayment", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "loa_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("principal", "NUMERIC"), ("periodicRate", "NUMERIC"), ("periods", "NUMERIC"), ("paymentsMade", "NUMERIC"),
        ("periodicalLoanPayment", "NUMERIC"), ("loanPayment", "NUMERIC"), ("totalPayment", "NUMERIC"),
        ("totalInterest", "NUMERIC"), ("outstandingBalance", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "pfv_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("inputPresentValue", "NUMERIC"), ("rate", "NUMERIC"), ("periods", "NUMERIC"), ("time", "NUMERIC"),
        ("compoundsPerYear", "NUMERIC"), ("futureValue", "NUMERIC"), ("presentValue", "NUMERIC"),
        ("simpleInterestFutureValue", "NUMERIC"), ("compoundInterestFutureValue", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "dep_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("cost", "NUMERIC"), ("salvageValue", "NUMERIC"), ("usefulLife", "NUMERIC"), ("time", "NUMERIC"),
        ("decliningRate", "NUMERIC"), ("straightLineDepreciation", "NUMERIC"), ("bookValue", "NUMERIC"),
        ("totalDepreciation", "NUMERIC"), ("decliningBalanceDepreciation", "NUMERIC"),
        ("decliningBalanceBookValue", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "com_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("inputSales", "NUMERIC"), ("inputCommissionRate", "NUMERIC"), ("salary", "NUMERIC"),
        ("commission", "NUMERIC"), ("totalEarnings", "NUMERIC"), ("commissionRate", "NUMERIC"),
        ("sales", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "paw_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("hourlyRate", "NUMERIC"), ("regularHours", "NUMERIC"), ("overtimeRate", "NUMERIC"), ("overtimeHours", "NUMERIC"),
        ("taxes", "NUMERIC"), ("contributions", "NUMERIC"), ("otherDeductions", "NUMERIC"), ("otherEarnings", "NUMERIC"),
        ("grossPay", "NUMERIC"), ("regularPay", "NUMERIC"), ("overtimePay", "NUMERIC"), ("netPay", "NUMERIC"),
        ("totalDeductions", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "tax_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("grossIncome", "NUMERIC"), ("allowableDeductions", "NUMERIC"), ("taxRate", "NUMERIC"), ("otherDeductions", "NUMERIC"),
        ("basicTax", "NUMERIC"), ("taxableIncome", "NUMERIC"), ("netIncome", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "bea_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("sellingPrice", "NUMERIC"), ("variableCostPerUnit", "NUMERIC"), ("fixedCost", "NUMERIC"), ("quantity", "NUMERIC"),
        ("contributionMargin", "NUMERIC"), ("contributionMarginRatio", "NUMERIC"), ("breakEvenUnits", "NUMERIC"),
        ("breakEvenSales", "NUMERIC"), ("profit", "NUMERIC"), ("totalRevenue", "NUMERIC"), ("totalCost", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "brc_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("price", "NUMERIC"), ("quantity", "NUMERIC"), ("fixedCost", "NUMERIC"), ("variableCostPerUnit", "NUMERIC"),
        ("revenue", "NUMERIC"), ("totalCost", "NUMERIC"), ("variableCost", "NUMERIC"), ("profit", "NUMERIC"),
        ("averageCost", "NUMERIC"), ("averageRevenue", "NUMERIC"), ("unitProfit", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "rnp_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("a", "NUMERIC"), ("b", "NUMERIC"), ("c", "NUMERIC"), ("d", "NUMERIC"), ("quantity", "NUMERIC"),
        ("units", "NUMERIC"), ("k", "NUMERIC"), ("x", "NUMERIC"), ("ratio", "NUMERIC"),
        ("proportion", "NUMERIC"), ("crossMultiplication", "NUMERIC"), ("unitRate", "NUMERIC"),
        ("directVariation", "NUMERIC"), ("inverseVariation", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "sta_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("valuesInput", "TEXT"), ("weightsInput", "TEXT"), ("mean", "NUMERIC"), ("weightedMean", "NUMERIC"),
        ("rangeValue", "NUMERIC"), ("populationVariance", "NUMERIC"), ("populationStandardDeviation", "NUMERIC"),
        ("populationMean", "NUMERIC"), ("sampleMean", "NUMERIC"), ("median", "NUMERIC"), ("mode", "NUMERIC"),
        ("sampleVariance", "NUMERIC"), ("sampleStandardDeviation", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "pro_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("favorable", "NUMERIC"), ("total", "NUMERIC"), ("pA", "NUMERIC"), ("pB", "NUMERIC"), ("pAandB", "NUMERIC"),
        ("basicProbability", "NUMERIC"), ("complement", "NUMERIC"), ("additionRule", "NUMERIC"),
        ("multiplicationRule", "NUMERIC"), ("conditionalProbability", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "prc_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("inputDecimal", "NUMERIC"), ("inputPercentage", "NUMERIC"), ("inputFraction", "NUMERIC"), ("annualRate", "NUMERIC"),
        ("decimalToPercentage", "NUMERIC"), ("percentageToDecimal", "NUMERIC"), ("percentageToFraction", "NUMERIC"),
        ("fractionToPercentage", "NUMERIC"), ("monthlyRate", "NUMERIC"), ("quarterlyRate", "NUMERIC"),
        ("semiannualRate", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "fra_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("currentAssets", "NUMERIC"), ("currentLiabilities", "NUMERIC"), ("inventory", "NUMERIC"),
        ("netProfit", "NUMERIC"), ("investment", "NUMERIC"), ("netIncome", "NUMERIC"), ("totalAssets", "NUMERIC"),
        ("shareholderEquity", "NUMERIC"), ("totalDebt", "NUMERIC"), ("totalEquity", "NUMERIC"), ("revenue", "NUMERIC"),
        ("currentRatio", "NUMERIC"), ("quickRatio", "NUMERIC"), ("returnOnInvestment", "NUMERIC"),
        ("returnOnAssets", "NUMERIC"), ("returnOnEquity", "NUMERIC"), ("debtToEquityRatio", "NUMERIC"),
        ("netProfitMargin", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "cbu_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("initialInvestment", "NUMERIC"), ("annualCashFlow", "NUMERIC"), ("discountRate", "NUMERIC"),
        ("cashFlows", "TEXT"), ("netPresentValue", "NUMERIC"), ("internalRateOfReturn", "NUMERIC"),
        ("paybackPeriod", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "sbo_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("annualDividend", "NUMERIC"), ("sharePrice", "NUMERIC"), ("annualCoupon", "NUMERIC"), ("bondPrice", "NUMERIC"),
        ("dividendYield", "NUMERIC"), ("currentBondYield", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "inc_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("faceValue", "NUMERIC"), ("rate", "NUMERIC"), ("annualPremium", "NUMERIC"), ("shortRateFactor", "NUMERIC"),
        ("insurancePremium", "NUMERIC"), ("shortRatePremium", "NUMERIC"), ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ],
    "pno_db": [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("principal", "NUMERIC"), ("rate", "NUMERIC"), ("time", "NUMERIC"), ("discountRate", "NUMERIC"),
        ("maturityValue", "NUMERIC"), ("bankDiscount", "NUMERIC"), ("proceeds", "NUMERIC"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    ]
}

def _ensureTable(cursor, tableName, columns):
    definitions = ",\n            ".join(name + " " + columnType for name, columnType in columns)
    cursor.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + definitions + ")")
    cursor.execute("PRAGMA table_info(" + tableName + ")")
    existingColumns = {row[1].lower() for row in cursor.fetchall()}
    for columnName, columnType in columns:
        if columnName.lower() not in existingColumns:
            if columnName == "id":
                cursor.execute("ALTER TABLE " + tableName + " ADD COLUMN id INTEGER")
            elif columnName == "created_at":
                cursor.execute("ALTER TABLE " + tableName + " ADD COLUMN created_at TIMESTAMP")
            else:
                safeType = "TEXT" if columnType.startswith("TEXT") else "NUMERIC"
                cursor.execute("ALTER TABLE " + tableName + " ADD COLUMN " + columnName + " " + safeType)

def initialize_database():
    baseDir = Path(__file__).resolve().parent
    dbDir = baseDir / "data"
    dbDir.mkdir(parents=True, exist_ok=True)
    dbPath = dbDir / "amiyenDB.db"
    print("Connecting to the database...")
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    for tableName, columns in TABLES.items():
        _ensureTable(cursor, tableName, columns)
    conn.commit()
    conn.close()
    print(f"Database initialized: {dbPath}")
    return dbPath

def _insertRow(tableName, columns, values, dbPath):
    print("Updating the " + tableName + " table...")
    try:
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()
        columnText = ", ".join(columns)
        placeholderText = ", ".join("?" for column in columns)
        cursor.execute(
            "INSERT INTO " + tableName + " (" + columnText + ", created_at) VALUES (" + placeholderText + ", CURRENT_TIMESTAMP)",
            tuple(values)
        )
        conn.commit()
        conn.close()
        print("Database table updated.")
        return 1
    except Exception as e:
        print("Failed to update " + tableName + ": " + str(e))
        try:
            conn.close()
        except:
            pass
        return 0

def updateBbm_db(percentage, rate, base, percentChange, percentIncrease, percentDecrease, dbPath):
    return _insertRow("bbm_db", ["percentage", "rate", "base", "percentageChange", "percentIncrease", "percentDecrease"], [percentage, rate, base, percentChange, percentIncrease, percentDecrease], dbPath)

def updateMam_db(markup, markupRateOnCost, markupRateOnSellingPrice, sellingPrice, sellingPriceFromMarkupRate, cost, markdown, markdownRate, salePrice, salePriceFromMarkdownRate, dbPath):
    return _insertRow("mam_db", ["markup", "markupRateOnCost", "markupRateOnSellingPrice", "sellingPrice", "sellingPriceFromMarkupRate", "cost", "markdown", "markdownRate", "salePrice", "salePriceFromMarkdownRate"], [markup, markupRateOnCost, markupRateOnSellingPrice, sellingPrice, sellingPriceFromMarkupRate, cost, markdown, markdownRate, salePrice, salePriceFromMarkdownRate], dbPath)

def updateDis_db(listPrice, discountRate, secondDiscountRate, tradeDiscount, netPrice, netPriceEquivalent, calculatedDiscountRate, seriesDiscount, equivalentDiscount, dbPath):
    return _insertRow("dis_db", ['listPrice', 'discountRate', 'secondDiscountRate', 'tradeDiscount', 'netPrice', 'netPriceEquivalent', 'calculatedDiscountRate', 'seriesDiscount', 'equivalentDiscount'], [listPrice, discountRate, secondDiscountRate, tradeDiscount, netPrice, netPriceEquivalent, calculatedDiscountRate, seriesDiscount, equivalentDiscount], dbPath)

def updatePnl_db(cost, sellingPrice, desiredProfitRate, profit, loss, profitRateOnCost, profitMargin, sellingPriceForDesiredProfit, costFromSellingPrice, lossRate, dbPath):
    return _insertRow("pnl_db", ['cost', 'sellingPrice', 'desiredProfitRate', 'profit', 'loss', 'profitRateOnCost', 'profitMargin', 'sellingPriceForDesiredProfit', 'costFromSellingPrice', 'lossRate'], [cost, sellingPrice, desiredProfitRate, profit, loss, profitRateOnCost, profitMargin, sellingPriceForDesiredProfit, costFromSellingPrice, lossRate], dbPath)

def updateSin_db(simpleInterest, principal, rate, time, maturityValue, maturityValueDirect, dbPath):
    return _insertRow("sin_db", ['simpleInterest', 'principal', 'rate', 'time', 'maturityValue', 'maturityValueDirect'], [simpleInterest, principal, rate, time, maturityValue, maturityValueDirect], dbPath)

def updateCin_db(inputPrincipal, rate, time, compoundsPerYear, compoundAmount, compoundInterest, calculatedPrincipal, futureValue, presentValue, effectiveAnnualRate, dbPath):
    return _insertRow("cin_db", ['inputPrincipal', 'rate', 'time', 'compoundsPerYear', 'compoundAmount', 'compoundInterest', 'calculatedPrincipal', 'futureValue', 'presentValue', 'effectiveAnnualRate'], [inputPrincipal, rate, time, compoundsPerYear, compoundAmount, compoundInterest, calculatedPrincipal, futureValue, presentValue, effectiveAnnualRate], dbPath)

def updateAnn_db(payment, periodicRate, periods, futureValueOfOrdinaryAnnuity, presentValueOfOrdinaryAnnuity, futureValueOfAnnuityDue, presentValueOfAnnuityDue, regularPayment, dbPath):
    return _insertRow("ann_db", ['payment', 'periodicRate', 'periods', 'futureValueOfOrdinaryAnnuity', 'presentValueOfOrdinaryAnnuity', 'futureValueOfAnnuityDue', 'presentValueOfAnnuityDue', 'regularPayment'], [payment, periodicRate, periods, futureValueOfOrdinaryAnnuity, presentValueOfOrdinaryAnnuity, futureValueOfAnnuityDue, presentValueOfAnnuityDue, regularPayment], dbPath)

def updateLoa_db(principal, periodicRate, periods, paymentsMade, periodicalLoanPayment, loanPayment, totalPayment, totalInterest, outstandingBalance, dbPath):
    return _insertRow("loa_db", ['principal', 'periodicRate', 'periods', 'paymentsMade', 'periodicalLoanPayment', 'loanPayment', 'totalPayment', 'totalInterest', 'outstandingBalance'], [principal, periodicRate, periods, paymentsMade, periodicalLoanPayment, loanPayment, totalPayment, totalInterest, outstandingBalance], dbPath)

def updatePfv_db(inputPresentValue, rate, periods, time, compoundsPerYear, futureValue, presentValue, simpleInterestFutureValue, compoundInterestFutureValue, dbPath):
    return _insertRow("pfv_db", ['inputPresentValue', 'rate', 'periods', 'time', 'compoundsPerYear', 'futureValue', 'presentValue', 'simpleInterestFutureValue', 'compoundInterestFutureValue'], [inputPresentValue, rate, periods, time, compoundsPerYear, futureValue, presentValue, simpleInterestFutureValue, compoundInterestFutureValue], dbPath)

def updateDep_db(cost, salvageValue, usefulLife, time, decliningRate, straightLineDepreciation, bookValue, totalDepreciation, decliningBalanceDepreciation, decliningBalanceBookValue, dbPath):
    return _insertRow("dep_db", ['cost', 'salvageValue', 'usefulLife', 'time', 'decliningRate', 'straightLineDepreciation', 'bookValue', 'totalDepreciation', 'decliningBalanceDepreciation', 'decliningBalanceBookValue'], [cost, salvageValue, usefulLife, time, decliningRate, straightLineDepreciation, bookValue, totalDepreciation, decliningBalanceDepreciation, decliningBalanceBookValue], dbPath)

def updateCom_db(inputSales, inputCommissionRate, salary, commission, totalEarnings, commissionRate, sales, dbPath):
    return _insertRow("com_db", ['inputSales', 'inputCommissionRate', 'salary', 'commission', 'totalEarnings', 'commissionRate', 'sales'], [inputSales, inputCommissionRate, salary, commission, totalEarnings, commissionRate, sales], dbPath)

def updatePaw_db(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings, grossPay, regularPay, overtimePay, netPay, totalDeductions, dbPath):
    return _insertRow("paw_db", ['hourlyRate', 'regularHours', 'overtimeRate', 'overtimeHours', 'taxes', 'contributions', 'otherDeductions', 'otherEarnings', 'grossPay', 'regularPay', 'overtimePay', 'netPay', 'totalDeductions'], [hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings, grossPay, regularPay, overtimePay, netPay, totalDeductions], dbPath)

def updateTax_db(grossIncome, allowableDeductions, taxRate, otherDeductions, basicTax, taxableIncome, netIncome, dbPath):
    return _insertRow("tax_db", ['grossIncome', 'allowableDeductions', 'taxRate', 'otherDeductions', 'basicTax', 'taxableIncome', 'netIncome'], [grossIncome, allowableDeductions, taxRate, otherDeductions, basicTax, taxableIncome, netIncome], dbPath)

def updateBea_db(sellingPrice, variableCostPerUnit, fixedCost, quantity, contributionMargin, contributionMarginRatio, breakEvenUnits, breakEvenSales, profit, totalRevenue, totalCost, dbPath):
    return _insertRow("bea_db", ['sellingPrice', 'variableCostPerUnit', 'fixedCost', 'quantity', 'contributionMargin', 'contributionMarginRatio', 'breakEvenUnits', 'breakEvenSales', 'profit', 'totalRevenue', 'totalCost'], [sellingPrice, variableCostPerUnit, fixedCost, quantity, contributionMargin, contributionMarginRatio, breakEvenUnits, breakEvenSales, profit, totalRevenue, totalCost], dbPath)

def updateBrc_db(price, quantity, fixedCost, variableCostPerUnit, revenue, totalCost, variableCost, profit, averageCost, averageRevenue, unitProfit, dbPath):
    return _insertRow("brc_db", ['price', 'quantity', 'fixedCost', 'variableCostPerUnit', 'revenue', 'totalCost', 'variableCost', 'profit', 'averageCost', 'averageRevenue', 'unitProfit'], [price, quantity, fixedCost, variableCostPerUnit, revenue, totalCost, variableCost, profit, averageCost, averageRevenue, unitProfit], dbPath)

def updateRnp_db(a, b, c, d, quantity, units, k, x, ratio, proportion, crossMultiplication, unitRate, directVariation, inverseVariation, dbPath):
    return _insertRow("rnp_db", ['a', 'b', 'c', 'd', 'quantity', 'units', 'k', 'x', 'ratio', 'proportion', 'crossMultiplication', 'unitRate', 'directVariation', 'inverseVariation'], [a, b, c, d, quantity, units, k, x, ratio, proportion, crossMultiplication, unitRate, directVariation, inverseVariation], dbPath)

def updateSta_db(valuesInput, weightsInput, mean, weightedMean, rangeValue, populationVariance, populationStandardDeviation, populationMean, sampleMean, median, mode, sampleVariance, sampleStandardDeviation, dbPath):
    return _insertRow("sta_db", ['valuesInput', 'weightsInput', 'mean', 'weightedMean', 'rangeValue', 'populationVariance', 'populationStandardDeviation', 'populationMean', 'sampleMean', 'median', 'mode', 'sampleVariance', 'sampleStandardDeviation'], [valuesInput, weightsInput, mean, weightedMean, rangeValue, populationVariance, populationStandardDeviation, populationMean, sampleMean, median, mode, sampleVariance, sampleStandardDeviation], dbPath)

def updatePro_db(favorable, total, pA, pB, pAandB, basicProbability, complement, additionRule, multiplicationRule, conditionalProbability, dbPath):
    return _insertRow("pro_db", ['favorable', 'total', 'pA', 'pB', 'pAandB', 'basicProbability', 'complement', 'additionRule', 'multiplicationRule', 'conditionalProbability'], [favorable, total, pA, pB, pAandB, basicProbability, complement, additionRule, multiplicationRule, conditionalProbability], dbPath)

def updatePrc_db(inputDecimal, inputPercentage, inputFraction, annualRate, decimalToPercentage, percentageToDecimal, percentageToFraction, fractionToPercentage, monthlyRate, quarterlyRate, semiannualRate, dbPath):
    return _insertRow("prc_db", ['inputDecimal', 'inputPercentage', 'inputFraction', 'annualRate', 'decimalToPercentage', 'percentageToDecimal', 'percentageToFraction', 'fractionToPercentage', 'monthlyRate', 'quarterlyRate', 'semiannualRate'], [inputDecimal, inputPercentage, inputFraction, annualRate, decimalToPercentage, percentageToDecimal, percentageToFraction, fractionToPercentage, monthlyRate, quarterlyRate, semiannualRate], dbPath)

def updateFra_db(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue, currentRatio, quickRatio, returnOnInvestment, returnOnAssets, returnOnEquity, debtToEquityRatio, netProfitMargin, dbPath):
    return _insertRow("fra_db", ['currentAssets', 'currentLiabilities', 'inventory', 'netProfit', 'investment', 'netIncome', 'totalAssets', 'shareholderEquity', 'totalDebt', 'totalEquity', 'revenue', 'currentRatio', 'quickRatio', 'returnOnInvestment', 'returnOnAssets', 'returnOnEquity', 'debtToEquityRatio', 'netProfitMargin'], [currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue, currentRatio, quickRatio, returnOnInvestment, returnOnAssets, returnOnEquity, debtToEquityRatio, netProfitMargin], dbPath)

def updateCbu_db(initialInvestment, annualCashFlow, discountRate, cashFlows, netPresentValue, internalRateOfReturn, paybackPeriod, dbPath):
    return _insertRow("cbu_db", ['initialInvestment', 'annualCashFlow', 'discountRate', 'cashFlows', 'netPresentValue', 'internalRateOfReturn', 'paybackPeriod'], [initialInvestment, annualCashFlow, discountRate, cashFlows, netPresentValue, internalRateOfReturn, paybackPeriod], dbPath)

def updateSbo_db(annualDividend, sharePrice, annualCoupon, bondPrice, dividendYield, currentBondYield, dbPath):
    return _insertRow("sbo_db", ['annualDividend', 'sharePrice', 'annualCoupon', 'bondPrice', 'dividendYield', 'currentBondYield'], [annualDividend, sharePrice, annualCoupon, bondPrice, dividendYield, currentBondYield], dbPath)

def updateInc_db(faceValue, rate, annualPremium, shortRateFactor, insurancePremium, shortRatePremium, dbPath):
    return _insertRow("inc_db", ['faceValue', 'rate', 'annualPremium', 'shortRateFactor', 'insurancePremium', 'shortRatePremium'], [faceValue, rate, annualPremium, shortRateFactor, insurancePremium, shortRatePremium], dbPath)

def updatePno_db(principal, rate, time, discountRate, maturityValue, bankDiscount, proceeds, dbPath):
    return _insertRow("pno_db", ['principal', 'rate', 'time', 'discountRate', 'maturityValue', 'bankDiscount', 'proceeds'], [principal, rate, time, discountRate, maturityValue, bankDiscount, proceeds], dbPath)
