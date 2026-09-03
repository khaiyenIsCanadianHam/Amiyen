from cmath import cos
from operator import eq
import re
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
