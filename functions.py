from cmath import cos
from operator import eq
import re
import time
from turtle import st


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