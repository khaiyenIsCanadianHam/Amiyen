import statistics
import sqlite3

def calcPercentage(rate, base):
    print("Calculate Percentage function is called, calculating percentage now... ")
    return (rate / 100) * base

def calcRate(percentage, base):
    print("Calculate Rate function is called, calculating rate now... ")
    return (percentage / base) * 100

def calcBase(percentage, rate):
    print("Calculate Base function is called, calculating base now... ")
    return percentage / (rate / 100)

def calcPercentageChange(dbPath, new):
    print("Calculate Percentage Change function is called, calculating Percentage Change now... ")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old percentage from the database...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1""")
            row = cursor.fetchone()
            old = row["percentage"]
            print("Identified the old percentage from the database")
            change = ((new - old) / old) * 100
            return change
        except:
            print("Failed to identify the value of old percentage.")
            return 0
    except:
        print("Failed to connect to the database.")
        return 0

def calcPercentIncrease(increase, dbPath):
    print("Calculate Percentage Change function is called, calculating Percentage Change now... ")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old percentage from the database...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            original = row["percentage"]
            print("Identified the old percentage from the database")
            if original >= increase:
                return 0
            else:
                increaseRate = ((increase - original) / original) * 100
                return increaseRate
        except:
            print("Failed to identify the value of old percentage.")
            return 0
    except:
            print("Failed to connect to the database.")
            return 0

def calcPercentDecrease(decrease, dbPath):
    print("Calculate Percentage Change function is called, calculating Percentage Change now... ")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old percentage from the database...")
        try:
            cursor.execute("""
                SELECT percentage
                FROM bbm_db
                ORDER BY id DESC
                LIMIT 1
                """)
            row = cursor.fetchone()
            original = row["percentage"]
            print("Identified the old percentage from the database")
            if decrease >= original:
                return 0
            else:
                decreaseRate = ((original - decrease) / original) * 100
                return decreaseRate
        except:
            print("Failed to identify the value of old percentage.")
            return 0
    except:
        print("Failed to connect to the database.")
        return 0
    
def calcMarkup(sellingPrice, cost):
    print("Calculate Markup function is called, calculating markup now...")
    markup = sellingPrice - cost
    return markup

def calcMarkupRateOnCost(markup, cost):
    print("Calculate Markup Rate on Cost function is called, calculating markup rate on cost now...")
    markupRate = markup / cost * 100
    return markupRate

def calcMarkupRateOnSellingPrice(markup, sellingPrice):
    print("Calculate Markup Rate on Selling Price function is called, calculating markup rate on selling price now...")
    markupRateOnSellingPrice = markup / sellingPrice * 100
    return markupRateOnSellingPrice

def calcSellingPrice(cost, markup):
    print("Calculate Selling Price function is called, calculating selling price now...")
    sellingPrice = cost + markup
    return sellingPrice

def calcSellingPriceFromMarkupRate(cost, markupRate):
    print("Calculate Selling Price from Markup Rate function is called, calculating selling price now...")
    sellingPrice = cost * (1 + (markupRate / 100))
    return sellingPrice

def calcCost(sellingPrice, markup):
    print("Calculate Cost function is called, calculating cost now...")
    cost = sellingPrice - markup
    return cost

def calcMarkdown(sellingPrice, dbPath):
    print("Calculate Markdown function is called, calculating markdown now...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old selling price from the database...")
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
                oldSellingPrice = None
            else:
                oldSellingPrice = row["sellingPrice"]
            conn.close()
            print("Identified the old selling price from the database.")
            if oldSellingPrice == None:
                return None
            else:
                if sellingPrice < oldSellingPrice:
                    markdown = oldSellingPrice - sellingPrice
                    return markdown
                else:
                    return 0
        except:
            conn.close()
            print("Failed to identify the old selling price.")
            return None
    except:
        print("Failed to connect to the database.")
        return None

def calcMarkdownRate(markdown, dbPath):
    print("Calculate Markdown Rate function is called, calculating markdown rate now...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old selling price from the database...")
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
                oldSellingPrice = None
            else:
                oldSellingPrice = row["sellingPrice"]
            conn.close()
            print("Identified the old selling price from the database.")
            if oldSellingPrice == None:
                return None
            else:
                if oldSellingPrice == 0:
                    return None
                else:
                    markdownRate = markdown / oldSellingPrice * 100
                    return markdownRate
        except:
            conn.close()
            print("Failed to identify the old selling price.")
            return None
    except:
        print("Failed to connect to the database.")
        return None

def calcSalePrice(sellingPrice, dbPath):
    print("Calculate Sale Price function is called, calculating sale price now...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old selling price from the database...")
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
                oldSellingPrice = None
            else:
                oldSellingPrice = row["sellingPrice"]
            conn.close()
            print("Identified the old selling price from the database.")
            if oldSellingPrice == None:
                return None
            else:
                if sellingPrice < oldSellingPrice:
                    salePrice = sellingPrice
                    return salePrice
                else:
                    return None
        except:
            conn.close()
            print("Failed to identify the old selling price.")
            return None
    except:
        print("Failed to connect to the database.")
        return None

def calcSalePriceFromMarkdownRate(markdownRate, dbPath):
    print("Calculate Sale Price from Markdown Rate function is called, calculating sale price now...")
    print("Connecting to the database...")
    try:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        print("Connected to the database.")
        print("Identifying the old selling price from the database...")
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
                oldSellingPrice = None
            else:
                oldSellingPrice = row["sellingPrice"]
            conn.close()
            print("Identified the old selling price from the database.")
            if oldSellingPrice == None:
                return None
            else:
                if markdownRate <= 0:
                    return None
                else:
                    salePrice = oldSellingPrice * (1 - (markdownRate / 100))
                    return salePrice
        except:
            conn.close()
            print("Failed to identify the old selling price.")
            return None
    except:
        print("Failed to connect to the database.")
        return None


def calcTradeDiscount(listPrice, discountRate):
    print("Calculate Trade Discount function is called, calculating trade discount now...")
    return listPrice * (discountRate / 100)

def calcNetPrice(listPrice, discount):
    print("Calculate Net Price function is called, calculating net price now...")
    return listPrice - discount

def calcNetPriceEquivalent(listPrice, discountRate):
    print("Calculate Net Price Equivalent function is called, calculating net price equivalent now...")
    return listPrice * (1 - (discountRate / 100))

def calcDiscountRate(discount, listPrice):
    print("Calculate Discount Rate function is called, calculating discount rate now...")
    if listPrice == 0:
        return None
    return (discount / listPrice) * 100

def calcSeriesDiscount(discount1, discount2, listPrice):
    print("Calculate Series Discount function is called, calculating net price after series discounts now...")
    return listPrice * (1 - (discount1 / 100)) * (1 - (discount2 / 100))

def calcEquivalentDiscount(discount1, discount2):
    print("Calculate Equivalent Discount function is called, calculating equivalent discount now...")
    equivalent = 1 - (1 - (discount1 / 100)) * (1 - (discount2 / 100))
    return equivalent * 100

def calcProfit(sellingPrice, cost):
    print("Calculate Profit function is called, calculating profit now...")
    return max(sellingPrice - cost, 0)

def calcLoss(cost, sellingPrice):
    print("Calculate Loss function is called, calculating loss now...")
    return max(cost - sellingPrice, 0)

def calcProfitRateOnCost(profit, cost):
    print("Calculate Profit Rate on Cost function is called, calculating profit rate now...")
    if cost == 0:
        return None
    return (profit / cost) * 100

def calcProfitMargin(profit, sellingPrice):
    print("Calculate Profit Margin function is called, calculating profit margin now...")
    if sellingPrice == 0:
        return None
    return (profit / sellingPrice) * 100

def calcSellingPriceForDesiredProfit(cost, profitRate):
    print("Calculate Selling Price for Desired Profit function is called, calculating selling price now...")
    return cost * (1 + (profitRate / 100))

def calcCostFromSellingPrice(sellingPrice, profitRate):
    print("Calculate Cost from Selling Price function is called, calculating cost now...")
    divisor = 1 + (profitRate / 100)
    if divisor == 0:
        return None
    return sellingPrice / divisor

def calcLossRate(loss, cost):
    print("Calculate Loss Rate function is called, calculating loss rate now...")
    if cost == 0:
        return None
    return (loss / cost) * 100

def calcSimpleInterest(principal, rate, time):
    print("Calculate Simple Interest function is called, calculating interest now...")
    return principal * (rate / 100) * time

def calcPrincipal(simpleInterest, rate, time):
    print("Calculate Principal function is called, calculating principal now...")
    divisor = (rate / 100) * time
    if divisor == 0:
        return None
    return simpleInterest / divisor

def calcRateFromSimpleInterest(simpleInterest, principal, time):
    print("Calculate Rate from Simple Interest function is called, calculating rate now...")
    divisor = principal * time
    if divisor == 0:
        return None
    return (simpleInterest / divisor) * 100

def calcTimeFromSimpleInterest(simpleInterest, principal, rate):
    print("Calculate Time from Simple Interest function is called, calculating time now...")
    divisor = principal * (rate / 100)
    if divisor == 0:
        return None
    return simpleInterest / divisor

def calcSimpleMaturityValue(principal, simpleInterest):
    print("Calculate Simple Interest Maturity Value function is called, calculating maturity value now...")
    return principal + simpleInterest

def calcMaturityValueDirectly(principal, rate, time):
    print("Calculate Maturity Value Directly function is called, calculating maturity value now...")
    return principal * (1 + (rate / 100) * time)

def calcCompoundAmount(principal, rate, time, n):
    print("Calculate Compound Amount function is called, calculating amount now...")
    if n == 0:
        return None
    return principal * (1 + (rate / 100) / n) ** (n * time)

def calcCompoundInterest(compoundAmount, principal):
    print("Calculate Compound Interest function is called, calculating interest now...")
    return compoundAmount - principal

def calcPrincipalFromCompoundAmount(compoundAmount, rate, time, n):
    print("Calculate Principal from Compound Amount function is called, calculating principal now...")
    if n == 0:
        return None
    factor = (1 + (rate / 100) / n) ** (n * time)
    if factor == 0:
        return None
    return compoundAmount / factor

def calcFutureCompoundValue(presentValue, rate, time, n):
    print("Calculate Future Compound Value function is called, calculating future value now...")
    if n == 0:
        return None
    return presentValue * (1 + (rate / 100) / n) ** (n * time)

def calcPresentCompoundValue(futureValue, rate, time, n):
    print("Calculate Present Compound Value function is called, calculating present value now...")
    if n == 0:
        return None
    factor = (1 + (rate / 100) / n) ** (n * time)
    if factor == 0:
        return None
    return futureValue / factor

def calcEffectiveAnualRate(rate, n):
    print("Calculate Effective Annual Rate function is called, calculating effective annual rate now...")
    if n == 0:
        return None
    return ((1 + (rate / 100) / n) ** n - 1) * 100

def calcFutureValueOfOrdinaryAnnuity(payment, n, i):
    print("Calculate Future Value of Ordinary Annuity function is called...")
    rate = i / 100
    if rate == 0:
        return payment * n
    return payment * (((1 + rate) ** n - 1) / rate)

def calcPresentValueOfOrdinaryAnnuity(payment, n, i):
    print("Calculate Present Value of Ordinary Annuity function is called...")
    rate = i / 100
    if rate == 0:
        return payment * n
    return payment * ((1 - (1 + rate) ** (-n)) / rate)

def calcFutureValueOfAnnuityDue(payment, n, i):
    print("Calculate Future Value of Annuity Due function is called...")
    rate = i / 100
    return calcFutureValueOfOrdinaryAnnuity(payment, n, i) * (1 + rate)

def calcPresentValueOfAnnuityDue(payment, n, i):
    print("Calculate Present Value of Annuity Due function is called...")
    rate = i / 100
    return calcPresentValueOfOrdinaryAnnuity(payment, n, i) * (1 + rate)

def calcRegularPayment(futureValue, n, i):
    print("Calculate Regular Payment function is called...")
    rate = i / 100
    if n == 0:
        return None
    if rate == 0:
        return futureValue / n
    denominator = (1 + rate) ** n - 1
    if denominator == 0:
        return None
    return futureValue * rate / denominator

def calcPeriodicalLoanPayment(presentValue, n, i):
    print("Calculate Periodical Loan Payment function is called...")
    rate = i / 100
    if n == 0:
        return None
    if rate == 0:
        return presentValue / n
    denominator = 1 - (1 + rate) ** (-n)
    if denominator == 0:
        return None
    return presentValue * rate / denominator

def calcLoanPayment(presentValue, n, i):
    print("Calculate Loan Payment function is called...")
    return calcPeriodicalLoanPayment(presentValue, n, i)

def calcTotalPayment(loanPayment, n):
    print("Calculate Total Payment function is called...")
    return loanPayment * n

def calcTotalInterest(totalPayment, principal):
    print("Calculate Total Interest function is called...")
    return totalPayment - principal

def calcOutstandingBalance(principal, payment, k, i):
    print("Calculate Outstanding Balance function is called...")
    rate = i / 100
    if rate == 0:
        return max(principal - (payment * k), 0)
    return principal * (1 + rate) ** k - payment * (((1 + rate) ** k - 1) / rate)

def calcFutureValue(presentValue, i, n):
    print("Calculate Future Value function is called...")
    return presentValue * (1 + (i / 100)) ** n

def calcPresentValue(futureValue, i, n):
    print("Calculate Present Value function is called...")
    factor = (1 + (i / 100)) ** n
    if factor == 0:
        return None
    return futureValue / factor

def calcSimpleInterestValue(presentValue, rate, time):
    print("Calculate Simple-Interest Future Value function is called...")
    return presentValue * (1 + (rate / 100) * time)

def compoundInterestFutureValue(presentValue, rate, time, n):
    print("Calculate Compound-Interest Future Value function is called...")
    if n == 0:
        return None
    return presentValue * (1 + (rate / 100) / n) ** (n * time)

def calcStraightLineDepreciation(cost, salvageValue, usefulLife):
    print("Calculate Straight-Line Depreciation function is called...")
    if usefulLife == 0:
        return None
    return (cost - salvageValue) / usefulLife

def calcBookValue(cost, depreciation, time):
    print("Calculate Book Value function is called...")
    return max(cost - depreciation * time, 0)

def calcTotalDepreciation(cost, salvageValue):
    print("Calculate Total Depreciation function is called...")
    return cost - salvageValue

def calcDecliningBalanceDepreciation(bookValue, rate):
    print("Calculate Declining-Balance Depreciation function is called...")
    return bookValue * (rate / 100)

def calcDecliningBalanceBookValue(cost, rate, time):
    print("Calculate Declining-Balance Book Value function is called...")
    return cost * (1 - (rate / 100)) ** time

def calcCommision(sales, rate):
    print("Calculate Commission function is called...")
    return sales * (rate / 100)

def calcTotalEarnings(salary, commission):
    print("Calculate Total Earnings function is called...")
    return salary + commission

def calcCommissionRate(commission, sales):
    print("Calculate Commission Rate function is called...")
    if sales == 0:
        return None
    return (commission / sales) * 100

def calcSales(commission, commissionRate):
    print("Calculate Sales function is called...")
    rate = commissionRate / 100
    if rate == 0:
        return None
    return commission / rate

def calcGrossPay(regularPay, overtimePay, otherEarnings):
    print("Calculate Gross Pay function is called...")
    return regularPay + overtimePay + otherEarnings

def calcRegularPay(hourlyRate, regularHours):
    print("Calculate Regular Pay function is called...")
    return hourlyRate * regularHours

def calcOvertimePay(hourlyRate, overtimeRate, overtimeHours):
    print("Calculate Overtime Pay function is called...")
    return hourlyRate * overtimeRate * overtimeHours

def calcNetPay(grossPay, totalDeductions):
    print("Calculate Net Pay function is called...")
    return grossPay - totalDeductions

def calcTotalDeduction(taxes, contributions, otherDeduction):
    print("Calculate Total Deductions function is called...")
    return taxes + contributions + otherDeduction

def calcBasicTax(taxableIncome, taxRate):
    print("Calculate Basic Tax function is called...")
    return taxableIncome * (taxRate / 100)

def calcTaxableIncome(grossIncome, deductions):
    print("Calculate Taxable Income function is called...")
    return max(grossIncome - deductions, 0)

def calcNetIncome(grossIncome, basicTax, otherDeductions):
    print("Calculate Net Income function is called...")
    return grossIncome - basicTax - otherDeductions

def calcContributionMargin(sellingPrice, variableCost):
    print("Calculate Contribution Margin function is called...")
    return sellingPrice - variableCost

def calcContributionMarginRatio(contributionMargin, sellingPrice):
    print("Calculate Contribution Margin Ratio function is called...")
    if sellingPrice == 0:
        return None
    return (contributionMargin / sellingPrice) * 100

def calcBreakEvenUnits(fixedCost, sellingPrice, variableCost):
    print("Calculate Break-Even Units function is called...")
    contributionMargin = sellingPrice - variableCost
    if contributionMargin == 0:
        return None
    return fixedCost / contributionMargin

def calcBreakEvenSales(fixedCost, contributionMarginRatio):
    print("Calculate Break-Even Sales function is called...")
    if contributionMarginRatio in (0, None):
        return None
    return fixedCost / (contributionMarginRatio / 100)

def calcBreakEvenProfit(totalRevenue, totalCost):
    print("Calculate Break-Even Profit function is called...")
    return totalRevenue - totalCost

def calcTotalRevenue(sellingPrice, quantity):
    print("Calculate Total Revenue function is called...")
    return sellingPrice * quantity

def calcTotalCost(fixedCost, variableCost):
    print("Calculate Total Cost function is called...")
    return fixedCost + variableCost

def calcRevenue(price, quantity):
    print("Calculate Revenue function is called...")
    return price * quantity

def calcBusinessTotalCost(fixedCost, variableCostPerUnit, quantity):
    print("Calculate Business Total Cost function is called...")
    return fixedCost + (variableCostPerUnit * quantity)

def calcVariableCost(variableCostPerUnit, quantity):
    print("Calculate Variable Cost function is called...")
    return variableCostPerUnit * quantity

def calcBusinessProfit(revenue, totalCost):
    print("Calculate Business Profit function is called...")
    return revenue - totalCost

def calcAverageCost(totalCost, quantity):
    print("Calculate Average Cost function is called...")
    if quantity == 0:
        return None
    return totalCost / quantity

def calcAverageRevenue(revenue, quantity):
    print("Calculate Average Revenue function is called...")
    if quantity == 0:
        return None
    return revenue / quantity

def calcUnitProfit(profit, quantity):
    print("Calculate Unit Profit function is called...")
    if quantity == 0:
        return None
    return profit / quantity

def calcRatio(a, b):
    print("Calculate Ratio function is called...")
    if b == 0:
        return None
    return a / b

def calcProportion(a, b, c, d):
    print("Calculate Proportion function is called...")
    if b == 0 or d == 0:
        return None
    return a / b == c / d

def calcCrossMultiplication(a, b, c, d):
    print("Calculate Cross Multiplication function is called...")
    return a * d == b * c

def calcUnitRate(units, quantity):
    print("Calculate Unit Rate function is called...")
    if units == 0:
        return None
    return quantity / units

def calcDirectVariation(k, x):
    print("Calculate Direct Variation function is called...")
    return k * x

def calcInverseVariation(k, x):
    print("Calculate Inverse Variation function is called...")
    if x == 0:
        return None
    return k / x

def calcMean(values):
    print("Calculate Mean function is called...")
    if len(values) == 0:
        return None
    return sum(values) / len(values)

def calcWeightedMean(data):
    print("Calculate Weighted Mean function is called...")
    denominator = sum(w for w, x in data)
    if denominator == 0:
        return None
    return sum(w * x for w, x in data) / denominator

def calcRange(values):
    print("Calculate Range function is called...")
    if len(values) == 0:
        return None
    return max(values) - min(values)

def calcPopulationVariance(mean, values):
    print("Calculate Population Variance function is called...")
    if len(values) == 0:
        return None
    return sum((x - mean) ** 2 for x in values) / len(values)

def calcPopulationStandardDeviation(variance):
    print("Calculate Population Standard Deviation function is called...")
    if variance is None:
        return None
    return variance ** 0.5

def calcPopulationMean(values):
    print("Calculate Population Mean function is called...")
    return calcMean(values)

def calcSampleMean(sample):
    print("Calculate Sample Mean function is called...")
    return calcMean(sample)

def calcBasicProbability(favorable, total):
    print("Calculate Basic Probability function is called...")
    if total == 0:
        return None
    return favorable / total

def calcComplement(probability):
    print("Calculate Complement function is called...")
    return 1 - probability

def calcadditionRule(p_a, p_b, p_a_and_b):
    print("Calculate Addition Rule function is called...")
    return p_a + p_b - p_a_and_b

def calcMultiplicationRule(p_a, p_b):
    print("Calculate Multiplication Rule function is called...")
    return p_a * p_b

def calcConditionalProbability(p_a_and_b, p_b):
    print("Calculate Conditional Probability function is called...")
    if p_b == 0:
        return None
    return p_a_and_b / p_b

def calcDecimalToPercentage(decimal):
    print("Calculate Decimal to Percentage function is called...")
    return decimal * 100

def calcPercentageToDecimal(percentage):
    print("Calculate Percentage to Decimal function is called...")
    return percentage / 100

def calcPercentageToFraction(percentage):
    print("Calculate Percentage to Fraction function is called...")
    return percentage / 100

def calcFractionToPercentage(fraction):
    print("Calculate Fraction to Percentage function is called...")
    return fraction * 100

def calcMonthlyRate(annualRate):
    print("Calculate Monthly Rate function is called...")
    return annualRate / 12

def calcQuarterlyRate(annualRate):
    print("Calculate Quarterly Rate function is called...")
    return annualRate / 4

def calcSemiAnnualRate(annualRate):
    print("Calculate Semiannual Rate function is called...")
    return annualRate / 2

def calcCurrentRatio(currentAssets, currentLiabilities):
    print("Calculate Current Ratio function is called...")
    if currentLiabilities == 0:
        return None
    return currentAssets / currentLiabilities

def calcQuickRatio(currentAssets, inventory, currentLiabilities):
    print("Calculate Quick Ratio function is called...")
    if currentLiabilities == 0:
        return None
    return (currentAssets - inventory) / currentLiabilities

def calcReturnOnInvestment(netProfit, investment):
    print("Calculate Return on Investment function is called...")
    if investment == 0:
        return None
    return (netProfit / investment) * 100

def calcReturnOnAssets(netIncome, totalAssets):
    print("Calculate Return on Assets function is called...")
    if totalAssets == 0:
        return None
    return (netIncome / totalAssets) * 100

def calcReturnOnEquity(netIncome, shareholderEquity):
    print("Calculate Return on Equity function is called...")
    if shareholderEquity == 0:
        return None
    return (netIncome / shareholderEquity) * 100

def calcDebtoEquityRatio(totalDebt, totalEquity):
    print("Calculate Debt-to-Equity Ratio function is called...")
    if totalEquity == 0:
        return None
    return totalDebt / totalEquity

def calcNetProfitMargin(netIncome, revenue):
    print("Calculate Net Profit Margin function is called...")
    if revenue == 0:
        return None
    return (netIncome / revenue) * 100

def calcNetPresentValue(cashFlows, discountRate, initialInvestment):
    print("Calculate Net Present Value function is called...")
    rate = discountRate / 100
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashFlows, start=1)) - initialInvestment

def _npvAtRate(cashFlows, rate):
    total = 0
    for t, cashFlow in enumerate(cashFlows):
        total += cashFlow / ((1 + rate) ** t)
    return total

def calcInternalRateOfReturn(cashFlows):
    print("Calculate Internal Rate of Return function is called...")
    if len(cashFlows) < 2:
        return None
    if not any(value < 0 for value in cashFlows) or not any(value > 0 for value in cashFlows):
        return None
    low = -0.9999
    high = 1.0
    lowValue = _npvAtRate(cashFlows, low)
    highValue = _npvAtRate(cashFlows, high)
    attempts = 0
    while lowValue * highValue > 0 and high < 1000000 and attempts < 60:
        high = (high * 2) + 1
        highValue = _npvAtRate(cashFlows, high)
        attempts += 1
    if lowValue * highValue > 0:
        return None
    for _ in range(200):
        middle = (low + high) / 2
        middleValue = _npvAtRate(cashFlows, middle)
        if abs(middleValue) < 0.0000001:
            return middle * 100
        if lowValue * middleValue <= 0:
            high = middle
            highValue = middleValue
        else:
            low = middle
            lowValue = middleValue
    return ((low + high) / 2) * 100

def calcPaybackPeriod(initialInvestment, annualCashInflows):
    print("Calculate Payback Period function is called...")
    if annualCashInflows == 0:
        return None
    return initialInvestment / annualCashInflows

def calcDividendYield(annualDividends, sharePrice):
    print("Calculate Dividend Yield function is called...")
    if sharePrice == 0:
        return None
    return (annualDividends / sharePrice) * 100

def calcCurrentBondYield(annualCoupon, bondPrice):
    print("Calculate Current Bond Yield function is called...")
    if bondPrice == 0:
        return None
    return (annualCoupon / bondPrice) * 100

def calcInsurancePremium(faceValue, rate):
    print("Calculate Insurance Premium function is called...")
    return faceValue * (rate / 100)

def calcShortRatePremium(annualPremium, shortRate):
    print("Calculate Short-Rate Premium function is called...")
    return annualPremium * shortRate

def calcPromissoryMaturityValue(principal, rate, time):
    print("Calculate Promissory Note Maturity Value function is called...")
    return principal * (1 + (rate / 100) * time)

def calcBankDiscount(maturityValue, discountRate, time):
    print("Calculate Bank Discount function is called...")
    return maturityValue * (discountRate / 100) * time

def calcProceeds(maturityValue, discount):
    print("Calculate Proceeds function is called...")
    return maturityValue - discount

def calcMedian(values):
    print("Calculate Median function is called...")
    if len(values) == 0:
        return None
    return statistics.median(values)

def calcMode(values):
    print("Calculate Mode function is called...")
    if len(values) == 0:
        return None
    return statistics.mode(values)

def calcSampleVariance(values):
    print("Calculate Sample Variance function is called...")
    if len(values) < 2:
        return None
    return statistics.variance(values)

def calcSampleStandardDeviation(values):
    print("Calculate Sample Standard Deviation function is called...")
    if len(values) < 2:
        return None
    return statistics.stdev(values)
