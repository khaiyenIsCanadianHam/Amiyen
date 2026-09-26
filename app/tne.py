import input
import functions

def calcVal_bbm(percentage, rate, base, dbPath):
    print("Calculate Values of Basic Business Math function is called, calculating values now... ")
    percentageChange = None
    percentIncrease = None
    percentDecrease = None
    calcValAttempt = 0
    while calcValAttempt <= 6:
        if percentage == None:
            print("Calling the function for validating inputs...")
            inputPercentage = input.inputPercentage(rate, base)
            if inputPercentage == "Calculate":
                print("Calling the function for calculating the percentage...")
                percentage = functions.calcPercentage(rate, base)
                calcValAttempt += 1
                print("Calculated percentage.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputPercentage + " Trying to calculate the missing values...")
        else:
            print("Percentage already has a value, calculating other missing values...")
        if rate == None:
            print("Calling the function for validating inputs...")
            inputRate = input.inputRate(percentage, base)
            if inputRate == "Calculate":
                print("Calculating rate...")
                rate = functions.calcRate(percentage, base)
                calcValAttempt += 1
                print("Calculated rate.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputRate + " Trying to calculate the missing values...")
        else:
            print("Rate already has a value, calculating other missing values...")
        if base == None:
            print("Calling the function for validating inputs...")
            inputBase = input.inputBase(percentage, rate)
            if inputBase == "Calculate":
                print("Calling the function for calculating the percentage...")
                base = functions.calcBase(percentage, rate)
                calcValAttempt += 1
                print("Calculated base.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputBase + " Trying to calculate the missing values...")
        else:
            print("Base already has a value, calculating other missing values...")
        if percentageChange == None:
            print("Calling the function for validationg inputs...")
            inputPercentageChange = input.inputPercentageChange(dbPath, percentage)
            if inputPercentageChange == "Calculate":
                print("Calling the function for calculating the percentage change...")
                percentageChange = functions.calcPercentageChange(dbPath, percentage)
                calcValAttempt += 1
                print("Calculated percentage change.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputPercentageChange + " Trying to calculate the missing values...")
        else:
            print("Percentage change already has a value, calculating other missing values...")
        if percentIncrease == None:
            print("Calling the function for validating inputs...")
            inputPercentIncrease = input.inputPercentIncrease(percentage, dbPath)
            if inputPercentIncrease == "Calculate":
                print("Calling the function for calculating the percentage increase...")
                percentIncrease = functions.calcPercentIncrease(percentage, dbPath)
                calcValAttempt += 1
                print("Calculated percentage increase.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputPercentIncrease + " Trying to calculate the missing values...")
        else:
            print("Percentage increase already has a value, calculating other missing values...")
        if percentDecrease == None:
            print("Calling the function for validating inputs...")
            inputPercentDecrease = input.inputPercentDecrease(percentage, dbPath)
            if inputPercentDecrease == "Calculate":
                print("Calling the function for calculating the percentage decrease...")
                percentDecrease = functions.calcPercentDecrease(percentage, dbPath)
                calcValAttempt += 1
                print("Calculated percentage decrease.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputPercentDecrease + " Trying to calculate the missing values...")
        calcValAttempt += 1
    return percentage, rate, base, percentageChange, percentIncrease, percentDecrease









def calcVal_mam(sellingPrice, markup, cost, dbPath):
    print("Calculate Values of Markup and Markdown function is called, calculating values now... ")
    markupRateOnCost = None
    markupRateOnSellingPrice = None
    sellingPriceFromMarkupRate = None
    markdown = None
    markdownRate = None
    salePrice = None
    salePriceFromMarkdownRate = None
    calcValAttempt = 0
    while calcValAttempt <= 10:
        if cost == None:
            print("Calling the function for validating inputs...")
            inputCost = input.inputCost(sellingPrice, markup)
            if inputCost == "Calculate":
                print("Calling the function for calculating the cost...")
                cost = functions.calcCost(sellingPrice, markup)
                calcValAttempt += 1
                print("Calculated cost.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputCost + " Trying to calculate the missing values...")
        else:
            print("Cost already has a value, calculating other missing values...")

        if markup == None:
            print("Calling the function for validating inputs...")
            inputMarkup = input.inputMarkup(sellingPrice, cost)
            if inputMarkup == "Calculate":
                print("Calling the function for calculating the markup...")
                markup = functions.calcMarkup(sellingPrice, cost)
                calcValAttempt += 1
                print("Calculated markup.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputMarkup + " Trying to calculate the missing values...")
        else:
            print("Markup already has a value, calculating other missing values...")

        if sellingPrice == None:
            print("Calling the function for validating inputs...")
            inputSellingPrice = input.inputSellingPrice(cost, markup)
            if inputSellingPrice == "Calculate":
                print("Calling the function for calculating the selling price...")
                sellingPrice = functions.calcSellingPrice(cost, markup)
                calcValAttempt += 1
                print("Calculated selling price.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputSellingPrice + " Trying to calculate the missing values...")
        else:
            print("Selling price already has a value, calculating other missing values...")

        if markupRateOnCost == None:
            print("Calling the function for validating inputs...")
            inputMarkupRateOnCost = input.inputMarkupRateOnCost(markup, cost)
            if inputMarkupRateOnCost == "Calculate":
                print("Calling the function for calculating the markup rate on cost...")
                if cost == 0:
                    markupRateOnCost = None
                    print("Can't calculate markup rate on cost because cost is zero.")
                else:
                    markupRateOnCost = functions.calcMarkupRateOnCost(markup, cost)
                    calcValAttempt += 1
                    print("Calculated markup rate on cost.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputMarkupRateOnCost + " Trying to calculate the missing values...")
        else:
            print("Markup rate on cost already has a value, calculating other missing values...")

        if markupRateOnSellingPrice == None:
            print("Calling the function for validating inputs...")
            inputMarkupRateOnSellingPrice = input.inputMarkupRateOnSellingPrice(markup, sellingPrice)
            if inputMarkupRateOnSellingPrice == "Calculate":
                print("Calling the function for calculating the markup rate on selling price...")
                if sellingPrice == 0:
                    markupRateOnSellingPrice = None
                    print("Can't calculate markup rate on selling price because selling price is zero.")
                else:
                    markupRateOnSellingPrice = functions.calcMarkupRateOnSellingPrice(markup, sellingPrice)
                    calcValAttempt += 1
                    print("Calculated markup rate on selling price.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputMarkupRateOnSellingPrice + " Trying to calculate the missing values...")
        else:
            print("Markup rate on selling price already has a value, calculating other missing values...")

        if sellingPriceFromMarkupRate == None:
            print("Calling the function for validating inputs...")
            inputSellingPriceFromMarkupRate = input.inputSellingPriceFromMarkupRate(cost, markupRateOnCost)
            if inputSellingPriceFromMarkupRate == "Calculate":
                print("Calling the function for calculating the selling price from markup rate...")
                sellingPriceFromMarkupRate = functions.calcSellingPriceFromMarkupRate(cost, markupRateOnCost)
                calcValAttempt += 1
                print("Calculated selling price from markup rate.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputSellingPriceFromMarkupRate + " Trying to calculate the missing values...")
        else:
            print("Selling price from markup rate already has a value, calculating other missing values...")

        if markdown == None:
            print("Calling the function for validating inputs...")
            inputMarkdown = input.inputMarkdown(sellingPrice, dbPath)
            if inputMarkdown == "Calculate":
                print("Calling the function for calculating the markdown...")
                markdown = functions.calcMarkdown(sellingPrice, dbPath)
                calcValAttempt += 1
                print("Calculated markdown.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputMarkdown + " Trying to calculate the missing values...")
        else:
            print("Markdown already has a value, calculating other missing values...")

        if markdownRate == None:
            print("Calling the function for validating inputs...")
            inputMarkdownRate = input.inputMarkdownRate(markdown, dbPath)
            if inputMarkdownRate == "Calculate":
                print("Calling the function for calculating the markdown rate...")
                markdownRate = functions.calcMarkdownRate(markdown, dbPath)
                calcValAttempt += 1
                print("Calculated markdown rate.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputMarkdownRate + " Trying to calculate the missing values...")
        else:
            print("Markdown rate already has a value, calculating other missing values...")

        if salePrice == None:
            print("Calling the function for validating inputs...")
            inputSalePrice = input.inputSalePrice(sellingPrice, markdown, dbPath)
            if inputSalePrice == "Calculate":
                print("Calling the function for calculating the sale price...")
                salePrice = functions.calcSalePrice(sellingPrice, dbPath)
                calcValAttempt += 1
                print("Calculated sale price.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputSalePrice + " Trying to calculate the missing values...")
        else:
            print("Sale price already has a value, calculating other missing values...")

        if salePriceFromMarkdownRate == None:
            print("Calling the function for validating inputs...")
            inputSalePriceFromMarkdownRate = input.inputSalePriceFromMarkdownRate(markdownRate, markdown, dbPath)
            if inputSalePriceFromMarkdownRate == "Calculate":
                print("Calling the function for calculating the sale price from markdown rate...")
                salePriceFromMarkdownRate = functions.calcSalePriceFromMarkdownRate(markdownRate, dbPath)
                calcValAttempt += 1
                print("Calculated sale price from markdown rate.\nCalculation attempt: " + str(calcValAttempt))
            else:
                print(inputSalePriceFromMarkdownRate + " Trying to calculate the missing values...")
        else:
            print("Sale price from markdown rate already has a value, calculating other missing values...")

        calcValAttempt += 1

    return markup, markupRateOnCost, markupRateOnSellingPrice, sellingPrice, sellingPriceFromMarkupRate, cost, markdown, markdownRate, salePrice, salePriceFromMarkdownRate


def _validateInputs(validationResult):
    if validationResult != "Calculate":
        print(validationResult)
        raise ValueError(validationResult)

def calcVal_dis(listPrice, discountRate, secondDiscountRate):
    print("Calculate Values of Discounts function is called, calculating values now...")
    _validateInputs(input.inputDiscounts(listPrice, discountRate, secondDiscountRate))
    tradeDiscount = functions.calcTradeDiscount(listPrice, discountRate)
    netPrice = functions.calcNetPrice(listPrice, tradeDiscount)
    netPriceEquivalent = functions.calcNetPriceEquivalent(listPrice, discountRate)
    calculatedDiscountRate = functions.calcDiscountRate(tradeDiscount, listPrice)
    seriesDiscount = functions.calcSeriesDiscount(discountRate, secondDiscountRate, listPrice)
    equivalentDiscount = functions.calcEquivalentDiscount(discountRate, secondDiscountRate)
    return listPrice, discountRate, secondDiscountRate, tradeDiscount, netPrice, netPriceEquivalent, calculatedDiscountRate, seriesDiscount, equivalentDiscount

def calcVal_pnl(cost, sellingPrice, desiredProfitRate):
    print("Calculate Values of Profit and Loss function is called, calculating values now...")
    _validateInputs(input.inputProfitAndLoss(cost, sellingPrice, desiredProfitRate))
    profit = functions.calcProfit(sellingPrice, cost)
    loss = functions.calcLoss(cost, sellingPrice)
    profitRateOnCost = functions.calcProfitRateOnCost(profit, cost)
    profitMargin = functions.calcProfitMargin(profit, sellingPrice)
    sellingPriceForDesiredProfit = functions.calcSellingPriceForDesiredProfit(cost, desiredProfitRate)
    costFromSellingPrice = functions.calcCostFromSellingPrice(sellingPrice, desiredProfitRate)
    lossRate = functions.calcLossRate(loss, cost)
    return cost, sellingPrice, desiredProfitRate, profit, loss, profitRateOnCost, profitMargin, sellingPriceForDesiredProfit, costFromSellingPrice, lossRate

def calcVal_sin(principal, rate, time):
    print("Calculate Values of Simple Interest function is called, calculating values now...")
    _validateInputs(input.inputSimpleInterest(principal, rate, time))
    simpleInterest = functions.calcSimpleInterest(principal, rate, time)
    calculatedPrincipal = functions.calcPrincipal(simpleInterest, rate, time)
    calculatedRate = functions.calcRateFromSimpleInterest(simpleInterest, principal, time)
    calculatedTime = functions.calcTimeFromSimpleInterest(simpleInterest, principal, rate)
    maturityValue = functions.calcSimpleMaturityValue(principal, simpleInterest)
    maturityValueDirect = functions.calcMaturityValueDirectly(principal, rate, time)
    return simpleInterest, calculatedPrincipal, calculatedRate, calculatedTime, maturityValue, maturityValueDirect

def calcVal_cin(principal, rate, time, compoundsPerYear):
    print("Calculate Values of Compound Interest function is called, calculating values now...")
    _validateInputs(input.inputCompoundInterest(principal, rate, time, compoundsPerYear))
    compoundAmount = functions.calcCompoundAmount(principal, rate, time, compoundsPerYear)
    compoundInterest = functions.calcCompoundInterest(compoundAmount, principal)
    calculatedPrincipal = functions.calcPrincipalFromCompoundAmount(compoundAmount, rate, time, compoundsPerYear)
    futureValue = functions.calcFutureCompoundValue(principal, rate, time, compoundsPerYear)
    presentValue = functions.calcPresentCompoundValue(futureValue, rate, time, compoundsPerYear)
    effectiveAnnualRate = functions.calcEffectiveAnualRate(rate, compoundsPerYear)
    return principal, rate, time, compoundsPerYear, compoundAmount, compoundInterest, calculatedPrincipal, futureValue, presentValue, effectiveAnnualRate

def calcVal_ann(payment, periodicRate, periods):
    print("Calculate Values of Annuities function is called, calculating values now...")
    _validateInputs(input.inputAnnuities(payment, periodicRate, periods))
    futureValueOfOrdinaryAnnuity = functions.calcFutureValueOfOrdinaryAnnuity(payment, periods, periodicRate)
    presentValueOfOrdinaryAnnuity = functions.calcPresentValueOfOrdinaryAnnuity(payment, periods, periodicRate)
    futureValueOfAnnuityDue = functions.calcFutureValueOfAnnuityDue(payment, periods, periodicRate)
    presentValueOfAnnuityDue = functions.calcPresentValueOfAnnuityDue(payment, periods, periodicRate)
    regularPayment = functions.calcRegularPayment(futureValueOfOrdinaryAnnuity, periods, periodicRate)
    return payment, periodicRate, periods, futureValueOfOrdinaryAnnuity, presentValueOfOrdinaryAnnuity, futureValueOfAnnuityDue, presentValueOfAnnuityDue, regularPayment

def calcVal_loa(principal, periodicRate, periods, paymentsMade):
    print("Calculate Values of Loans function is called, calculating values now...")
    _validateInputs(input.inputLoans(principal, periodicRate, periods, paymentsMade))
    periodicalLoanPayment = functions.calcPeriodicalLoanPayment(principal, periods, periodicRate)
    loanPayment = functions.calcLoanPayment(principal, periods, periodicRate)
    totalPayment = functions.calcTotalPayment(loanPayment, periods)
    totalInterest = functions.calcTotalInterest(totalPayment, principal)
    outstandingBalance = functions.calcOutstandingBalance(principal, loanPayment, paymentsMade, periodicRate)
    return principal, periodicRate, periods, paymentsMade, periodicalLoanPayment, loanPayment, totalPayment, totalInterest, outstandingBalance

def calcVal_pfv(presentValue, rate, periods, time, compoundsPerYear):
    print("Calculate Values of Present and Future Value function is called, calculating values now...")
    _validateInputs(input.inputPresentAndFutureValue(presentValue, rate, periods, time, compoundsPerYear))
    futureValue = functions.calcFutureValue(presentValue, rate, periods)
    calculatedPresentValue = functions.calcPresentValue(futureValue, rate, periods)
    simpleInterestFutureValue = functions.calcSimpleInterestValue(presentValue, rate, time)
    compoundInterestFutureValue = functions.compoundInterestFutureValue(presentValue, rate, time, compoundsPerYear)
    return presentValue, rate, periods, time, compoundsPerYear, futureValue, calculatedPresentValue, simpleInterestFutureValue, compoundInterestFutureValue

def calcVal_dep(cost, salvageValue, usefulLife, time, decliningRate):
    print("Calculate Values of Depreciation function is called, calculating values now...")
    _validateInputs(input.inputDepreciation(cost, salvageValue, usefulLife, time, decliningRate))
    straightLineDepreciation = functions.calcStraightLineDepreciation(cost, salvageValue, usefulLife)
    bookValue = functions.calcBookValue(cost, straightLineDepreciation, time)
    totalDepreciation = functions.calcTotalDepreciation(cost, salvageValue)
    decliningBalanceBookValue = functions.calcDecliningBalanceBookValue(cost, decliningRate, time)
    decliningBalanceDepreciation = functions.calcDecliningBalanceDepreciation(decliningBalanceBookValue, decliningRate)
    return cost, salvageValue, usefulLife, time, decliningRate, straightLineDepreciation, bookValue, totalDepreciation, decliningBalanceDepreciation, decliningBalanceBookValue

def calcVal_com(sales, commissionRate, salary):
    print("Calculate Values of Commission function is called, calculating values now...")
    _validateInputs(input.inputCommission(sales, commissionRate, salary))
    commission = functions.calcCommision(sales, commissionRate)
    totalEarnings = functions.calcTotalEarnings(salary, commission)
    calculatedCommissionRate = functions.calcCommissionRate(commission, sales)
    calculatedSales = functions.calcSales(commission, commissionRate)
    return sales, commissionRate, salary, commission, totalEarnings, calculatedCommissionRate, calculatedSales

def calcVal_paw(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings):
    print("Calculate Values of Payroll and Wages function is called, calculating values now...")
    _validateInputs(input.inputPayrollAndWages(hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings))
    regularPay = functions.calcRegularPay(hourlyRate, regularHours)
    overtimePay = functions.calcOvertimePay(hourlyRate, overtimeRate, overtimeHours)
    grossPay = functions.calcGrossPay(regularPay, overtimePay, otherEarnings)
    totalDeductions = functions.calcTotalDeduction(taxes, contributions, otherDeductions)
    netPay = functions.calcNetPay(grossPay, totalDeductions)
    return hourlyRate, regularHours, overtimeRate, overtimeHours, taxes, contributions, otherDeductions, otherEarnings, grossPay, regularPay, overtimePay, netPay, totalDeductions

def calcVal_tax(grossIncome, allowableDeductions, taxRate, otherDeductions):
    print("Calculate Values of Taxes function is called, calculating values now...")
    _validateInputs(input.inputTaxes(grossIncome, allowableDeductions, taxRate, otherDeductions))
    taxableIncome = functions.calcTaxableIncome(grossIncome, allowableDeductions)
    basicTax = functions.calcBasicTax(taxableIncome, taxRate)
    netIncome = functions.calcNetIncome(grossIncome, basicTax, otherDeductions)
    return grossIncome, allowableDeductions, taxRate, otherDeductions, basicTax, taxableIncome, netIncome

def calcVal_bea(sellingPrice, variableCostPerUnit, fixedCost, quantity):
    print("Calculate Values of Break-Even Analysis function is called, calculating values now...")
    _validateInputs(input.inputBreakEvenAnalysis(sellingPrice, variableCostPerUnit, fixedCost, quantity))
    contributionMargin = functions.calcContributionMargin(sellingPrice, variableCostPerUnit)
    contributionMarginRatio = functions.calcContributionMarginRatio(contributionMargin, sellingPrice)
    breakEvenUnits = functions.calcBreakEvenUnits(fixedCost, sellingPrice, variableCostPerUnit)
    breakEvenSales = functions.calcBreakEvenSales(fixedCost, contributionMarginRatio)
    totalRevenue = functions.calcTotalRevenue(sellingPrice, quantity)
    totalVariableCost = variableCostPerUnit * quantity
    totalCost = functions.calcTotalCost(fixedCost, totalVariableCost)
    profit = functions.calcBreakEvenProfit(totalRevenue, totalCost)
    return sellingPrice, variableCostPerUnit, fixedCost, quantity, contributionMargin, contributionMarginRatio, breakEvenUnits, breakEvenSales, profit, totalRevenue, totalCost

def calcVal_brc(price, quantity, fixedCost, variableCostPerUnit):
    print("Calculate Values of Business Revenue and Cost function is called, calculating values now...")
    _validateInputs(input.inputBusinessRevenueAndCost(price, quantity, fixedCost, variableCostPerUnit))
    revenue = functions.calcRevenue(price, quantity)
    variableCost = functions.calcVariableCost(variableCostPerUnit, quantity)
    totalCost = functions.calcBusinessTotalCost(fixedCost, variableCostPerUnit, quantity)
    profit = functions.calcBusinessProfit(revenue, totalCost)
    averageCost = functions.calcAverageCost(totalCost, quantity)
    averageRevenue = functions.calcAverageRevenue(revenue, quantity)
    unitProfit = functions.calcUnitProfit(profit, quantity)
    return price, quantity, fixedCost, variableCostPerUnit, revenue, totalCost, variableCost, profit, averageCost, averageRevenue, unitProfit

def calcVal_rnp(a, b, c, d, quantity, units, k, x):
    print("Calculate Values of Ratios and Proportions function is called, calculating values now...")
    _validateInputs(input.inputRatiosAndProportions(a, b, c, d, quantity, units, k, x))
    ratio = functions.calcRatio(a, b)
    proportion = functions.calcProportion(a, b, c, d)
    crossMultiplication = functions.calcCrossMultiplication(a, b, c, d)
    unitRate = functions.calcUnitRate(units, quantity)
    directVariation = functions.calcDirectVariation(k, x)
    inverseVariation = functions.calcInverseVariation(k, x)
    return a, b, c, d, quantity, units, k, x, ratio, proportion, crossMultiplication, unitRate, directVariation, inverseVariation

def calcVal_sta(values, weights):
    print("Calculate Values of Statistics function is called, calculating values now...")
    _validateInputs(input.inputStatistics(values, weights))
    if weights == None or len(weights) == 0:
        weights = [1 for value in values]
    mean = functions.calcMean(values)
    weightedMean = functions.calcWeightedMean(list(zip(weights, values)))
    rangeValue = functions.calcRange(values)
    populationVariance = functions.calcPopulationVariance(mean, values)
    populationStandardDeviation = functions.calcPopulationStandardDeviation(populationVariance)
    populationMean = functions.calcPopulationMean(values)
    sampleMean = functions.calcSampleMean(values)
    median = functions.calcMedian(values)
    mode = functions.calcMode(values)
    sampleVariance = functions.calcSampleVariance(values)
    sampleStandardDeviation = functions.calcSampleStandardDeviation(values)
    return ", ".join(str(value) for value in values), ", ".join(str(value) for value in weights), mean, weightedMean, rangeValue, populationVariance, populationStandardDeviation, populationMean, sampleMean, median, mode, sampleVariance, sampleStandardDeviation

def calcVal_pro(favorable, total, pA, pB, pAandB):
    print("Calculate Values of Probability function is called, calculating values now...")
    _validateInputs(input.inputProbability(favorable, total, pA, pB, pAandB))
    basicProbability = functions.calcBasicProbability(favorable, total)
    complement = functions.calcComplement(basicProbability)
    additionRule = functions.calcadditionRule(pA, pB, pAandB)
    multiplicationRule = functions.calcMultiplicationRule(pA, pB)
    conditionalProbability = functions.calcConditionalProbability(pAandB, pB)
    return favorable, total, pA, pB, pAandB, basicProbability, complement, additionRule, multiplicationRule, conditionalProbability

def calcVal_prc(decimal, percentage, fraction, annualRate):
    print("Calculate Values of Percentage and Rate Conversions function is called, calculating values now...")
    _validateInputs(input.inputPercentageAndRateConversions(decimal, percentage, fraction, annualRate))
    decimalToPercentage = functions.calcDecimalToPercentage(decimal)
    percentageToDecimal = functions.calcPercentageToDecimal(percentage)
    percentageToFraction = functions.calcPercentageToFraction(percentage)
    fractionToPercentage = functions.calcFractionToPercentage(fraction)
    monthlyRate = functions.calcMonthlyRate(annualRate)
    quarterlyRate = functions.calcQuarterlyRate(annualRate)
    semiannualRate = functions.calcSemiAnnualRate(annualRate)
    return decimal, percentage, fraction, annualRate, decimalToPercentage, percentageToDecimal, percentageToFraction, fractionToPercentage, monthlyRate, quarterlyRate, semiannualRate

def calcVal_fra(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue):
    print("Calculate Values of Financial Ratios function is called, calculating values now...")
    _validateInputs(input.inputFinancialRatios(currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue))
    currentRatio = functions.calcCurrentRatio(currentAssets, currentLiabilities)
    quickRatio = functions.calcQuickRatio(currentAssets, inventory, currentLiabilities)
    returnOnInvestment = functions.calcReturnOnInvestment(netProfit, investment)
    returnOnAssets = functions.calcReturnOnAssets(netIncome, totalAssets)
    returnOnEquity = functions.calcReturnOnEquity(netIncome, shareholderEquity)
    debtToEquityRatio = functions.calcDebtoEquityRatio(totalDebt, totalEquity)
    netProfitMargin = functions.calcNetProfitMargin(netIncome, revenue)
    return currentAssets, currentLiabilities, inventory, netProfit, investment, netIncome, totalAssets, shareholderEquity, totalDebt, totalEquity, revenue, currentRatio, quickRatio, returnOnInvestment, returnOnAssets, returnOnEquity, debtToEquityRatio, netProfitMargin

def calcVal_cbu(initialInvestment, annualCashFlow, discountRate, cashFlows):
    print("Calculate Values of Capital Budgeting function is called, calculating values now...")
    _validateInputs(input.inputCapitalBudgeting(initialInvestment, annualCashFlow, discountRate, cashFlows))
    netPresentValue = functions.calcNetPresentValue(cashFlows, discountRate, initialInvestment)
    internalRateOfReturn = functions.calcInternalRateOfReturn([-initialInvestment] + cashFlows)
    paybackPeriod = functions.calcPaybackPeriod(initialInvestment, annualCashFlow)
    return initialInvestment, annualCashFlow, discountRate, ", ".join(str(value) for value in cashFlows), netPresentValue, internalRateOfReturn, paybackPeriod

def calcVal_sbo(annualDividend, sharePrice, annualCoupon, bondPrice):
    print("Calculate Values of Stocks and Bonds function is called, calculating values now...")
    _validateInputs(input.inputStocksAndBonds(annualDividend, sharePrice, annualCoupon, bondPrice))
    dividendYield = functions.calcDividendYield(annualDividend, sharePrice)
    currentBondYield = functions.calcCurrentBondYield(annualCoupon, bondPrice)
    return annualDividend, sharePrice, annualCoupon, bondPrice, dividendYield, currentBondYield

def calcVal_inc(faceValue, rate, annualPremium, shortRateFactor):
    print("Calculate Values of Insurance function is called, calculating values now...")
    _validateInputs(input.inputInsurance(faceValue, rate, annualPremium, shortRateFactor))
    insurancePremium = functions.calcInsurancePremium(faceValue, rate)
    shortRatePremium = functions.calcShortRatePremium(annualPremium, shortRateFactor)
    return faceValue, rate, annualPremium, shortRateFactor, insurancePremium, shortRatePremium

def calcVal_pno(principal, rate, time, discountRate):
    print("Calculate Values of Promissory Notes function is called, calculating values now...")
    _validateInputs(input.inputPromissoryNotes(principal, rate, time, discountRate))
    maturityValue = functions.calcPromissoryMaturityValue(principal, rate, time)
    bankDiscount = functions.calcBankDiscount(maturityValue, discountRate, time)
    proceeds = functions.calcProceeds(maturityValue, bankDiscount)
    return principal, rate, time, discountRate, maturityValue, bankDiscount, proceeds
