import functions
import input

def calcVal_bbm(percentage, rate, base, dbPath):
    percentageChange = None
    percentIncrease = None
    percentDecrease = None
    calcValAttempt = 0
    while calcValAttempt <= 6:
        inputPercentage = input.inputPercentage(rate, base)
        if inputPercentage == "Calculate":
            percentage = functions.calcPercentage(rate, base)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        inputRate = input.inputRate(percentage, base)
        if inputRate == "Calculate":
            rate = functions.calcRate(percentage, base)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        inputBase = input.inputBase(percentage, rate)
        if inputBase == "Calculate":
            base = functions.calcBase(percentage, rate)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        inputPercentageChange = input.inputPercentageChange(dbPath, percentage)
        if inputPercentageChange == "Calculate":
            percentageChange = functions.calcPercentageChange(dbPath, percentage)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        inputPercentIncrease = input.inputPercentIncrease(percentage, dbPath)
        if inputPercentIncrease == "Calculate":
            percentIncrease = functions.calcPercentIncrease(percentage, dbPath)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        inputPercentDecrease = input.inputPercentDecrease(percentage, dbPath)
        if inputPercentDecrease == "Calculate":
            percentDecrease = functions.calcPercentDecrease(percentage, dbPath)
            calcValAttempt += 1
        else:
            calcValAttempt -= 1
        calcValAttempt += 1
    return percentage, rate, base, percentageChange, percentIncrease, percentDecrease








