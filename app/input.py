import sqlite3

def inputPercentage(rate, base):
    print("Input Percentage function is called, validating the rate and base input to calculate percentage...")
    if rate == None:
        if base == None:
            return "Can't calculate percentage without rate and base."
        else:
            return "Can't calculate percentage without rate."
    else:
        if base == None:
            return "Can't calculate percentage without base."
        else:
            return "Calculate"

def inputRate(percentage, base):
    print("Input Rate function is called, validating the percentage and base input to calculate percentage...")
    if percentage == None:
        if base == None:
            return "Can't calculate rate without percentage and base."
        else:
            return "Can't calculate rate without percentage."
    else:
        if base == None:
            return "Can't calculate rate without base."
        else:
            return "Calculate"

def inputBase(percentage, rate):
    print("Input Base function is called, validating the rate and percentage input to calculate percentage...")
    if percentage == None:
        if rate == None:
            return "Can't calculate rate without percentage and rate."
        else:
            return "Can't calculate without percentage."
    else:
        if rate == None:
            return "Can't calculate without rate."
        else:
            return "Calculate"       

def inputPercentageChange(dbPath, new):
    print("Input Percentage Change function is called, validating the old and new percentage input to calculate percentage change...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old percentage...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1
            """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["percentage"]
            print("Identified the value of the old percentage.")
            if old == None:
                if new == None:
                    return "Can't calculate without the old percentage and the new percentage."
                else:
                    return "Can't calculate without the old percentage."
            else:
                if new == None:
                    return "Can't calculate without the new percentage."
                else:
                    return "Calculate"   
        except:
            return "Failed to identify the value of the old percentage."
    except:
        return "Failed to connect to the database to get the value of the old percetage."

def inputPercentIncrease(percentage, dbPath):
    print("Input Percentage Increase function is called, validating the old and new percentage input to calculate percentage change...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old percentage...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["percentage"]
            print("Identified the value of the old percentage.")
            if old == None:
                if percentage == None:
                    return "Can't calculate without the old percentage and the new percentage."
                else:
                    return "Can't calculate without the old percentage."
            else:
                if percentage == None:
                    return "Can't calculate without the new percentage."
                else:
                    return "Calculate"  
        except:
            return "Failed to identify the value of the old percentage."
    except:
            return "Failed to connect to the database to get the value of the old percetage."

def inputPercentDecrease(percentage, dbPath):
    print("Input Percentage Increase function is called, validating the old and new percentage input to calculate percentage change...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old percentage...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["percentage"]
            print("Identified the value of the old percentage.")
            decrease = percentage
            if decrease == None:
                if old == None:
                    return "Can't calculate without the old percentage and the new percentage."
                else:
                    return "Can't calculate without the old percentage."
            else:
                if decrease == None:
                    return "Can't calculate without the new percentage."
                else:
                    return "Calculate" 
        except:
                return "Failed to identify the value of the old percentage."
    except:
        return "Failed to connect to the database to get the value of the old percetage."

def inputMarkup(sellingPrice, cost):
    print("Input Base function is called, validating the cost and selling price input to calculate markup...")
    if sellingPrice == None:
        if cost == None:
            return "Can't calculate without without selling price and the cost."
        else:
            return "Can't calculate wiyhout selling price."
    else:
        if cost == None:
            return "Can't calculate without the cost"
        else:
            return "Calculate"

def inputMarkupRateOnCost(markup, cost):
    print("Input Markup Rate on Cost function is called, validating the markup and cost input to calculate markup rate on cost...")
    if markup == None:
        if cost == None:
            return "Can't calculate without markup and cost."
        else:
            return "Can't calculate without markup."
    else:
        if cost == None:
            return "Can't calculate without cost."
        else:
            return "Calculate"  

def inputMarkupRateOnSellingPrice(markup, sellingPrice):
    print("Input Markup Rate on Selling Price function is called, validating the markup and selling price input to calculate markup...")
    if markup == None:
        if sellingPrice == None:
            return "Can't calculate without markup and selling price."
        else:
            return "Can't calculate without markup."
    else:
        if sellingPrice == None:
            return "Can't calculate without selling price."
        else:
            return "Calculate"  

def inputSellingPrice(cost, markup):
    print("Input Selling Price function is called, validating the cost and markup input to calculate selling price...")
    if markup == None:
        if cost == None:
            return "Can't calculate without markup and cost"
        else:
            return "Can't calculate without markup."
    else:
        if cost == None:
            return "Can't calculate without cost."
        else:
            return "Calculate"  

def inputSellingPriceFromMarkupRate(cost, markupRate):
    print("Input Selling Price from Markup Rate function is called, validating the cost and markup rate input to calculate Selling Price from Markup Rate...")
    if markupRate == None:
        if cost == None:
            return "Can't calculate without markup markup rate and cost"
        else:
            return "Can't calculate without markup rate."
    else:
        if cost == None:
            return "Can't calculate without cost."
        else:
            return "Calculate"  

def inputCost(sellingPrice, markup):
    print("Input Cost function is called, validating the selling price and markup input to calculate cost...")
    if sellingPrice == None:
        if markup == None:
            return "Can't calculate without markup and selling price"
        else:
            return "Can't calculate without selling price."
    else:
        if markup == None:
            return "Can't calculate without markup."
        else:
            return "Calculate"  

def inputMarkdown(sellingPrice, dbPath):
    print("Input Markdown function is called, validating the original price and sale price input to calculate markdown...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old selling price...")
        try:
            cursor.execute("""
                SELECT sellingPrice
                FROM mam_db
                WHERE sellingPrice IS NOT NULL
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["sellingPrice"]
            print("Identified the value of the old selling price.")
            conn.close()
            new = sellingPrice
            if new == None:
                if old == None:
                    return "Can't calculate without old selling price and new selling price"
                else:
                    return "Can't calculate without new selling price."
            else:
                if old == None:
                    return "Can't calculate without old selling price."
                else:
                    return "Calculate"  
        except:
            return "Can't identify the old selling price."
    except:
        return "Can't connect to the database."

def inputMarkdownRate(markdown, dbPath):
    print("Input Markdown Rate function is called, validating the old selling price and markdown to calculate markdown rate...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old selling price...")
        try:
            cursor.execute("""
                SELECT sellingPrice
                FROM mam_db
                WHERE sellingPrice IS NOT NULL
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["sellingPrice"]
            conn.close()
            print("Identified the value of the old selling price.")
            if markdown == None:
                if old == None:
                    return "Can't calculate without old selling price and markdown."
                else:
                    return "Can't calculate without markdown."
            else:
                if old == None:
                    return "Can't calculate without old selling price."
                else:
                    if old == 0:
                        return "Can't calculate markdown rate if old selling price is zero."
                    else:
                        return "Calculate"
        except:
            conn.close()
            return "Can't identify the old selling price."
    except:
        return "Can't connect to the database."

def inputSalePrice(sellingPrice, markdown, dbPath):
    print("Input Sale Price function is called, validating the old selling price, new selling price and markdown to calculate sale price...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old selling price...")
        try:
            cursor.execute("""
                SELECT sellingPrice
                FROM mam_db
                WHERE sellingPrice IS NOT NULL
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["sellingPrice"]
            conn.close()
            print("Identified the value of the old selling price.")
            if sellingPrice == None:
                return "Can't calculate without new selling price."
            else:
                if old == None:
                    return "Can't calculate without old selling price."
                else:
                    if markdown == None:
                        return "Can't calculate without markdown."
                    else:
                        if markdown <= 0:
                            return "There is no markdown, sale price is not needed."
                        else:
                            return "Calculate"
        except:
            conn.close()
            return "Can't identify the old selling price."
    except:
        return "Can't connect to the database."

def inputSalePriceFromMarkdownRate(markdownRate, markdown, dbPath):
    print("Input Sale Price from Markdown Rate function is called, validating the old selling price and markdown rate to calculate sale price...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the value of the old selling price...")
        try:
            cursor.execute("""
                SELECT sellingPrice
                FROM mam_db
                WHERE sellingPrice IS NOT NULL
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            if row is None:
                old = None
            else:
                old = row["sellingPrice"]
            conn.close()
            print("Identified the value of the old selling price.")
            if markdownRate == None:
                if old == None:
                    return "Can't calculate without old selling price and markdown rate."
                else:
                    return "Can't calculate without markdown rate."
            else:
                if old == None:
                    return "Can't calculate without old selling price."
                else:
                    if markdown == None:
                        return "Can't calculate without markdown."
                    else:
                        if markdown <= 0:
                            return "There is no markdown, sale price from markdown rate is not needed."
                        else:
                            return "Calculate"
        except:
            conn.close()
            return "Can't identify the old selling price."
    except:
        return "Can't connect to the database."


def inputRequiredValues(calculationName, *values):
    print("Input " + calculationName + " function is called, validating inputs...")
    for value in values:
        if value == None:
            return "Can't calculate " + calculationName + " because one or more required inputs are missing."
    return "Calculate"

def inputDiscounts(listPrice, discountRate, secondDiscountRate):
    return inputRequiredValues("Discounts", listPrice, discountRate, secondDiscountRate)

def inputProfitAndLoss(cost, sellingPrice, desiredProfitRate):
    return inputRequiredValues("Profit and Loss", cost, sellingPrice, desiredProfitRate)

def inputSimpleInterest(principal, rate, time):
    return inputRequiredValues("Simple Interest", principal, rate, time)

def inputCompoundInterest(principal, rate, time, compoundsPerYear):
    return inputRequiredValues("Compound Interest", principal, rate, time, compoundsPerYear)

def inputAnnuities(payment, periodicRate, periods):
    return inputRequiredValues("Annuities", payment, periodicRate, periods)

def inputLoans(principal, periodicRate, periods, paymentsMade):
    return inputRequiredValues("Loans", principal, periodicRate, periods, paymentsMade)

def inputPresentAndFutureValue(presentValue, rate, periods, time, compoundsPerYear):
    return inputRequiredValues("Present and Future Value", presentValue, rate, periods, time, compoundsPerYear)

def inputDepreciation(cost, salvageValue, usefulLife, time, decliningRate):
    return inputRequiredValues("Depreciation", cost, salvageValue, usefulLife, time, decliningRate)

def inputCommission(sales, commissionRate, salary):
    return inputRequiredValues("Commission", sales, commissionRate, salary)

def inputPayrollAndWages(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings):
    return inputRequiredValues("Payroll and Wages", hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings)

def inputTaxes(grossIncome, allowableDeductions, taxRate, otherDeductions):
    return inputRequiredValues("Taxes", grossIncome, allowableDeductions, taxRate, otherDeductions)

def inputBreakEvenAnalysis(sellingPrice, variableCostPerUnit, fixedCost, quantity):
    return inputRequiredValues("Break-Even Analysis", sellingPrice, variableCostPerUnit, fixedCost, quantity)

def inputBusinessRevenueAndCost(price, quantity, fixedCost, variableCostPerUnit):
    return inputRequiredValues("Business Revenue and Cost", price, quantity, fixedCost, variableCostPerUnit)

def inputRatiosAndProportions(a, b, c, d, quantity, units, k, x):
    return inputRequiredValues("Ratios and Proportions", a, b, c, d, quantity, units, k, x)

def inputStatistics(values, weights):
    if values == None or len(values) == 0:
        return "Can't calculate Statistics because the values list is missing."
    if weights == None or len(weights) == 0:
        return "Calculate"
    if len(values) != len(weights):
        return "Can't calculate Statistics because the values and weights must have the same length."
    return "Calculate"

def inputProbability(favorable, total, pA, pB, pAandB):
    return inputRequiredValues("Probability", favorable, total, pA, pB, pAandB)

def inputPercentageAndRateConversions(decimal, percentage, fraction, annualRate):
    return inputRequiredValues("Percentage and Rate Conversions", decimal, percentage, fraction, annualRate)

def inputFinancialRatios(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue):
    return inputRequiredValues("Financial Ratios", currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue)

def inputCapitalBudgeting(initialInvestment, annualCashFlow, discountRate, cashFlows):
    if initialInvestment == None or annualCashFlow == None or discountRate == None:
        return "Can't calculate Capital Budgeting because one or more required inputs are missing."
    if cashFlows == None or len(cashFlows) == 0:
        return "Can't calculate Capital Budgeting because future cash flows are missing."
    return "Calculate"

def inputStocksAndBonds(annualDividend, sharePrice, annualCoupon, bondPrice):
    return inputRequiredValues("Stocks and Bonds", annualDividend, sharePrice, annualCoupon, bondPrice)

def inputInsurance(faceValue, rate, annualPremium, shortRateFactor):
    return inputRequiredValues("Insurance", faceValue, rate, annualPremium, shortRateFactor)

def inputPromissoryNotes(principal, rate, time, discountRate):
    return inputRequiredValues("Promissory Notes", principal, rate, time, discountRate)
