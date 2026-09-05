import statistics
import numpy_financial

def calcPercentage(rate, base):
    percentage = rate*base
    return percentage

def calcRate(percentage, base):
    rate = percentage/base
    return rate

def calcBase(percentage, rate):
    base = percentage / rate
    return base

def calcPercentageChange(new, old):
    change = (new - old) / old * 100
    return change

def calcPercentIncrease(increase, original):
    increaseRate = increase / original * 100
    return increaseRate

def calcPercentDecrease(decrease, original):
    decreaseRate = decrease / original * 100
    return decreaseRate

def calcMarkup(sellingPrice, cost):
    markup = sellingPrice - cost
    return markup

def calcMarkupRateOnCost(markup, cost):
    markupRate = markup / cost * 100
    return markupRate

def calcMarkupRateOnSellingPrice(markup, sellingPrice):
    markupRateOnSellingPrice = markup / sellingPrice * 100
    return markupRateOnSellingPrice

def calcSellingPrice(cost, markup):
    sellingPrice = cost + markup
    return sellingPrice

def calcSellingPriceFromMarkupRate(cost, markupRate):
    sellingPrice = cost * (1 + markupRate)
    return sellingPrice

def calcCost(sellingPrice, markup):
    cost = sellingPrice - markup
    return cost

def calcMarkdown(originalPrice, salePrice):
    markdown = originalPrice - salePrice
    return markdown

def calcMarkdownRate(markdown,originalPrice):
    markdownRate = markdown / originalPrice * 100
    return markdownRate

def calcSalePrice(originalPrice, markdown):
    salePrice = originalPrice - markdown
    return salePrice

def calcSalePriceFromMarkdownRate(originalPrice, markdownRate):
    salePrice = originalPrice * (1 - markdownRate)
    return salePrice

def calcTradeDiscount(listPrice, discountRate):
    discount = listPrice * discountRate
    return discount

def calcNetPrice(listPrice, discount):
    netPrice = listPrice - discount
    return netPrice

def calcNetPriceEquivalent(listPrice, discountRate):
    netPriceEquivalent = listPrice * (1 - discountRate)
    return netPriceEquivalent

def calcDiscountRate(discount, listPrice):
    discountRate = discount / listPrice * 100
    return discountRate

def calcSeriesDiscount(discount1, discount2, listPrice):
    netPrice = listPrice * (1 - discount1) * (1 - discount2)    
    return netPrice

def calcEquivalentDiscount(discount1, discount2):
    equivalent = 1 - (1-discount1) * (1-discount2)
    return equivalent

def calcProfit(sellingPrice, cost):
    profit = sellingPrice - cost
    return profit

def calcLoss(cost, sellingPrice):
    loss = cost - sellingPrice
    return loss

def calcProfitRateOnCost(profit, cost):
    profitRate = profit / cost * 100
    return profitRate

def calcProfitMargin(profit, sellingPrice):
    profitMargin = profit / sellingPrice * 100
    return profitMargin

def calcSellingPriceForDesiredProfit(cost, profitRate):
    sellingPriceForDesiredProfit = cost * (1 + profitRate)
    return sellingPriceForDesiredProfit

def calcCostFromSellingPrice(sellingPriceForDesiredProfit, profitRate):
    costFromSellingPrice = sellingPriceForDesiredProfit / (1 + profitRate)
    return costFromSellingPrice

def calcLossRate(loss, cost):
    lossRate = loss / cost * 100
    return lossRate

def calcSimpleInterest(principal, rate, time):
    simpleInterest = principal * rate * time
    return simpleInterest

def calcPrincipal(simpleInterest, rate, time):
    principal = simpleInterest / (rate * time)
    return principal

def calcRateFromSimpleInterest(simpleInterest, principal, time):
    rateFromSimpleInterest = simpleInterest / (principal * time)
    return rateFromSimpleInterest

def calcTimeFromSimpleInterest(simpleInterest, principal, rate):
    timeFromSimpleInterest = simpleInterest / (principal * rate)
    return timeFromSimpleInterest

def calcMaturityValue(principal, simpleInterest):
    maturityValue = principal + simpleInterest
    return maturityValue

def calcMaturityValueDirectly(principal, rate, time):
    maturityValueDirectly = principal * (1 + rate * time)
    return maturityValueDirectly

def calcCompoundAmount(principal, rate, time):
    compoundAmount = principal * (1 + rate) ** time
    return compoundAmount

def calcCompoundInterest(compoundAmount, principal):
    compoundInterest = compoundAmount - principal
    return compoundInterest

def calcPrincipalFromCompoundAmount(compoundAmount, rate, time, n):
    principalFromCompoundAmount = compoundAmount / (1 + rate/n) ** (n*time)
    return principalFromCompoundAmount

def calcFutureCompoundValue(presentValue, rate, time, n):
    futureCompoundValue = presentValue * (1 + rate/n) ** (n*time)
    return futureCompoundValue

def calcPresentCompoundValue(futureValue, rate, time, n):
    presentCompoundValue = futureValue / (1 + rate/n) ** (n*time)
    return presentCompoundValue

def calcEffectiveAnualRate(rate, n):
    effectiveAnualRate = (1 + rate/n) ** n - 1
    return effectiveAnualRate

def calcFutureValueOfOrdinaryAnnuity(payment, rate, time, n, i):
    futureValueOfOrdinaryAnnuity = payment * ((1 + i) ** n - 1) / i
    return futureValueOfOrdinaryAnnuity

def calcPresentValueOfOrdinaryAnnuity(payment,n, i):
    presentValueOfOrdinaryAnnuity = payment * (1 - (1 + i) ** -n) / i
    return presentValueOfOrdinaryAnnuity

def calcFutureValueOfAnnuityDue(payment, n, i):
    futureValueOfAnnuityDue = payment * ((1 + i) ** n - 1) / i * (1 + i)
    return futureValueOfAnnuityDue

def calcPresentValueOfAnnuityDue(payment, n, i):
    presentValueOfAnnuityDue = payment * (1 - (1 + i) ** -n) / i * (1 + i)
    return presentValueOfAnnuityDue 

def calcRegularPayment(futureValues, n, i):
    regularPayment = futureValues * i / ((1 + i) ** n - 1)
    return regularPayment

def calcPeriodicalLoanPayment(presentvalue, n, i):
    periodicalLoanPayment = presentvalue * i / (1 - (1 + i) ** -n)
    return periodicalLoanPayment

def calcLoanPayment(presentvalue, n, i):
    loanPayment = presentvalue * i / (1 - (1 + i) ** -n)
    return loanPayment

def calcTotalPayment(loanPayment, n):
    totalPayment = loanPayment * n
    return totalPayment

def calcTotalInterest(totalPayment, principal):
    totalInterest = totalPayment - principal
    return totalInterest

def calcOutstandingBalance(principal, payment, k, i):
    outstandingBalance = principal * (1 + i) ** k - payment * ((1 + i) ** k - 1) / i
    return outstandingBalance

def calcFutureValue(presentValue, i, n):
    futureValue = presentValue * (1 + i) ** n
    return futureValue

def calcPresentValue(futureValue, i, n):
    presentValue = futureValue / (1 + i) ** n
    return presentValue

def calcSimpleInterestValue(presentValue, rate, time):
    simpleInterestValue = presentValue * (1 + rate * time)
    return simpleInterestValue

def compoundInterestFutureValue(presentValue, rate, time, n):
    compoundInterestValue = presentValue * (1 + rate/n) ** (n*time)
    return compoundInterestValue

def calcStraightLineDepreciation(cost, salvageValue, usefulLife):
    straightLineDepreciation = (cost - salvageValue) / usefulLife
    return straightLineDepreciation

def calcBookValue(cost, depreciation, time):
    bookValue = cost - depreciation * time
    return bookValue

def calcTotalDepreciation(cost, salvageValue):
    totalDepreciation = cost - salvageValue
    return totalDepreciation

def calcDecliningBalanceDepreciation(bookValue, rate):
    decliningBalanceDepreciation = bookValue * rate
    return decliningBalanceDepreciation     

def calcDecliningBalanceBookValue(cost, rate, time):
    decliningBalanceBookValue = cost * (1 - rate) ** time
    return decliningBalanceBookValue

def calcCommision(sales, rate):
    commission = sales * rate
    return commission

def calcTotalEarnings(salary, commission):
    totalEarnings = salary + commission
    return totalEarnings

def calcCommissionRate(commission, sales):
    commissionRate = commission / sales * 100
    return commissionRate

def calcSales(commission, commissionRate):
    sales = commission / commissionRate
    return sales

def calcGrossPay(regularPay, overtimePay, otherEarnings):
    grossPay = regularPay + overtimePay + otherEarnings
    return grossPay

def calcRegularPay(hourlyRate, regularHours):
    regularPay = hourlyRate * regularHours
    return regularPay

def calcOvertimePay(hourlyRate, overtimeRate, overtimeHours):
    overtimePay = hourlyRate * overtimeRate * overtimeHours
    return overtimePay

def calcNetPay(grossPay, totalDeductions):
    netPay = grossPay - totalDeductions
    return netPay

def calcTotalDeduction(taxes, contributions, otherDeduction):
    totalDeduction = taxes, contributions, otherDeduction
    return totalDeduction

def calcBasicTax(taxableIncome, taxRate):
    basicTax = taxableIncome * taxRate
    return basicTax

def calcTaxableIncome(grossIncome, deductions):
    taxableIncome = grossIncome - deductions
    return taxableIncome

def calcNetIncome(grossIncome, basicTax, totalDeductions):
    netIncome = grossIncome - basicTax - totalDeductions
    return netIncome

def calcContributionMargin(sellingPrice, variableCost):
    contributionMargin = sellingPrice - variableCost
    return contributionMargin

def calcContributionMarginRatio(contributionMargin, sellingPrice):
    contributionMarginRatio = contributionMargin / sellingPrice
    return contributionMarginRatio

def calcBreakEvenUnits(fixedCost, sellingPrice, variableCost):
    breakEvenUnits = fixedCost / sellingPrice * variableCost
    return breakEvenUnits

def calcBreakEvenSales(fixedCost, contributionMarginRatio):
    breakEvenSales = fixedCost / contributionMarginRatio
    return breakEvenSales

def calcProfit(totalRevenue, totalCost):
    profit = totalRevenue - totalCost
    return profit

def calcTotalRevenue(sellingPrice, quantity):
    totalRevenue = sellingPrice * quantity
    return totalRevenue

def calcTotalCost(fixedCost, variableCost):
    totalCost = fixedCost + variableCost
    return totalCost

def calcRevenue(price, quantity):
    revenue = price * quantity
    return revenue

def calcTotalCost1(variableCostPerUnit, quantity):
    totalCost1 = variableCostPerUnit * quantity
    return totalCost1

def calcProfit1(revenue, totalCost1):
    profit1 = revenue - totalCost1
    return profit1

def calcAverageCost(totalCost1, quantity):
    averageCost = totalCost1 / quantity
    return averageCost

def calcAverageRevenue(revenue, quantity):
    averageRevenue = revenue / quantity
    return averageRevenue

def calcUnitProfit(profit, quantity):
    unitProfit = profit / quantity
    return unitProfit

def calcRatio(a,b):
    ratio = a / b
    return ratio

def calcProportion(a, b, c, d):
    proportion = a / b == c / d
    return proportion

def calcCrossMultiplication(a, b, c, d):
    crossMultiplication = a * b == c * d
    return crossMultiplication

def calcUnitRate(units, quantity):
    unitRate = quantity / units
    return unitRate

def calcDirectVariation(k, x):
    y = k * x
    return y

def calcInverseVariation(k, x):
    y = k / x
    return y

def calcMean(values):
    mean = sum(values) / len(values)
    return mean

def calcWeightedMean(data):
    weightedMean = sum(w*x for w,x in data) / sum(w for w,x in data)
    return weightedMean

def calcRange(values):
    rangeValue = max(values) - min(values)
    return rangeValue

def calcPopulationVariance(mean, values):
    variance = sum((x-mean)**2 for x in values) / len(values)
    return variance

def calcPopulationStandardDeviation(variance):
    populationStandardDeviation = variance ** 0.5
    return populationStandardDeviation

def calcPopulationMean(values):
    populationMean = sum(values) / len(values)
    return populationMean

def calcSampleMean(sample):
    sampleMean = sum(sample) / len(sample)
    return sampleMean

def calcBasicProbability(favorable, total):
    probability = favorable / total
    return probability

def calcComplement(probability):
    complement = 1 - probability
    return complement

def calcadditionRule(p_a, p_b, p_a_and_b):
    additionRule = p_a + p_b - p_a_and_b
    return additionRule

def calcMultiplicationRule(p_a, p_b):
    multiplicationRule = p_a * p_b
    return multiplicationRule

def calcConditionalProbability(p_a_and_b, p_b):
    ConditionalProbability = p_a_and_b / p_b
    return ConditionalProbability

def calcDecimalToPercentage(decimal):
    percentage = decimal * 100
    return percentage

def calcPercentageToDecimal(percentage):
    decimal = percentage / 100
    return decimal

def calcPercentageToFraction(percentage):
    fraction = percentage / 100
    return fraction

def calcFractionToPercentage(fraction):
    percentage = fraction * 100
    return percentage

def calcMonthlyRate(annualRate):
    monthlyRate = annualRate / 12
    return monthlyRate

def calcAnnualRate(monthlyRate):
    annualRate = monthlyRate * 12
    return annualRate

def calcWeeklyRate(annualRate):
    weeklyRate = annualRate / 52
    return weeklyRate

def calcQuarterlyRate(annualRate):
    quarterlyRate = annualRate / 4
    return quarterlyRate

def calcSemiAnnualRate(annualRate):
    semiAnnualRate = annualRate / 2
    return semiAnnualRate

def calcCurrentRatio(currentAssets, currentLiabilities):
    currentRatio = currentAssets / currentLiabilities
    return currentRatio

def calcQuickRatio(currentAssets, inventory, currentLiabilities):
    quickRatio = (currentAssets - inventory) / currentLiabilities
    return quickRatio

def calcReturnOnInvestment(netProfit, investment):
    returnOnInvestment = netProfit / investment * 100
    return returnOnInvestment

def calcReturnOnAssets(netIncome, totalAssets):
    returnOnAssets = netIncome / totalAssets * 100
    return returnOnAssets

def calcReturnOnEquity(netIncome, shareholderEquity):
    returnOnEquity = netIncome / shareholderEquity * 100
    return returnOnEquity

def calcDebtoEquityRatio(totalDebt, totalEquity):
    debtToEquityRatio = totalDebt / totalEquity
    return debtToEquityRatio

def calcNetProfitMargin(netIncome, revenue):
    netProfitMargin = netIncome / revenue * 100
    return netProfitMargin

def calcNetPresentValue(cashFlows, discountRate, initialInvestment):
    npv = sum(cf / (1 + discountRate) ** t for t, cf in enumerate(cashFlows, start=1)) - initialInvestment
    return npv

def calcInternalRateOfReturn(cashFlows, initialInvestment):
    irr = numpy_financial.irr(cashFlows)
    return irr

def calcPaybackPeriod(initialInvestment, annualCashInflows):
    paybackPeriod = initialInvestment / annualCashInflows
    return paybackPeriod

def calcDividendYield(annualDividends, sharePrice):
    dividendYield = annualDividends / sharePrice * 100
    return dividendYield

def calcCurrentBondYield(annualCoupon, bondPrice):
    bondYield = annualCoupon / bondPrice * 100
    return bondYield

def calcInsurancePremium(faceValue, rate):
    premium = faceValue * rate
    return premium

def calcShortRatePremium(annualPremium, shortRate):
    shortRatePremium = annualPremium * shortRate
    return shortRatePremium

def calcMaturityValue(principal, rate, time):
    maturityValue = principal * (1 + rate * time)
    return maturityValue

def calcBankDiscount(maturityValue, discountRate, time):
    bankDiscount = maturityValue * discountRate * time
    return bankDiscount

def calcProceeds(maturityValue, discount):
    proceeds = maturityValue - discount
    return proceeds

def calcMedian(values):
    median = statistics.median(values)
    return median

def calcMode(values):
    mode = statistics.mode(values)
    return mode

def calcSampleVariance(values):
    sampleVariance = statistics.variance(values)
    return sampleVariance

def calcSampleStandardDeviation(values):
    sampleStandardDeviation = statistics.stdev(values)
    return sampleStandardDeviation