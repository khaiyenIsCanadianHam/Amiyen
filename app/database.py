from pathlib import Path
import sqlite3

def initialize_database():
    base_dir = Path(__file__).resolve().parent
    db_dir = base_dir / "data"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "amiyenDB.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bbm_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            percentage NUMERIC,
            rate NUMERIC,
            base NUMERIC,
            percentageChange NUMERIC,
            percentIncrease NUMERIC,
            percentDecrease NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mam_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            markup NUMERIC,
            markupRateOnCost NUMERIC,
            markupRateOnSellingPrice NUMERIC,
            sellingPrice NUMERIC,
            sellingPriceFromMarkupRate NUMERIC,
            cost NUMERIC,
            markdown NUMERIC,
            markdownRate NUMERIC,
            salePrice NUMERIC,
            salePriceFromMarkdownRate NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dis_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tradeDiscount NUMERIC,
            netPrice NUMERIC,
            netPriceEquivalent NUMERIC,
            discountRate NUMERIC,
            seriesDiscount NUMERIC,
            equivalentDiscount NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pnl_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            profit NUMERIC,
            loss NUMERIC,
            profitRateOnCost NUMERIC,
            profitMargin NUMERIC,
            SellingPriceForDesiredProfit NUMERIC,
            costFromSellingPrice NUMERIC,
            lossrate NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sin_ (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            simpleInterest NUMERIC,
            principal NUMERIC,
            rate NUMERIC,
            time NUMERIC,
            maturityValue NUMERIC,
            maturityValueDirect NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            compoundAmount NUMERIC,
            compoundInterest NUMERIC,
            principal NUMERIC,
            futureValue NUMERIC
            presentValue NUMERIC,
            effectiveAnnualRate NUMERIC
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ann_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            futureValueOfOrdinaryAnnuity NUMERIC,
            presentValueofOrdinaryAnnuity NUMERIC,
            futureValueOfAnnuityDue NUMERIC,
            presentValueOfAnnuityDue NUMERIC,
            regularPayment NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loa_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            periodaclLoanPayment NUMERIC,
            loanPayment NUMERIC,
            totalPayment NUMERIC,
            totalInterest NUMERIC,
            outstandingBalance NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pfv_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            futureValue NUMERIC,
            presentValue NUMERIC,
            simpleInterestFutureValue NUMERIC,
            compoundInterestFutureValue NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dep_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            straightLineDepreciation NUMERIC,
            bookValue NUMERIC,
            totalDepreciation NUMERIC,
            decliningBalanceDepreciation NUMERIC,
            decliningBalanceBookValue NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS com_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commission NUMERIC,
            totalEarnings NUMERIC,
            commissionRate NUMERIC,
            sales NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paw_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grossPay NUMERIC,
            regularPay NUMERIC,
            overtimePay NUMERIC,
            netPay NUMERIC,
            totalDeductions NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tax_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            basicTax NUMERIC,
            taxableIncome NUMERIC,
            netIncome NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bea_db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contributionMargin NUMERIC,
            contributionMarginRatio NUMERIC,
            breakEvenSales NUMERIC,
            breakEvenUnits NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS brc_db (
            businessRevenueProfit NUMERIC,
            totalRevenue NUMERIC,
            totalCost NUMERIC,
            revenue NUMERIC,
            totalCost1 NUMERIC,
            variableCost NUMERIC,
            averageCost NUMERIC,
            averageRevenue NUMERIC,
            unitProfit NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rnp_db (
            ratio NUMERIC,
            proportion NUMERIC,
            crossMultiplication NUMERIC,
            unitRate NUMERIC,
            directVariation NUMERIC,
            inverseVariation NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sta_db (
            mean NUMERIC,
            weightedMean NUMERIC,
            range NUMERIC,
            populationVariance NUMERIC,
            populationStandardDeviation NUMERIC,
            populationMean NUMERIC,
            sampleMEAN,
            median NUMERIC,
            mode NUMERIC,
            sampleVariace NUMERIC,
            sampleStandardDeviation NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pro_db (
            basicProbability NUMERIC,
            complement NUMERIC,
            additionRule NUMERIC,
            multiplicationRule NUMERIC,
            conditionalProbability NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prc_db (
            decimalToPercentage NUMERIC,
            percentageToDecimal NUMERIC,
            percentageToFraction NUMERIC,
            fractionToPercentage NUMERIC,
            monthlyRate NUMERIC,
            quarterlyRate NUMERIC,
            semiannualRate NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fra_db (
            currentRatio NUMERIC,
            quickRatio NUMERIC,
            returnToInvestment NUMERIC,
            returnToAssets NUMERIC,
            returnOnEquity NUMERIC,
            debtToEquityRatio NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cbu_db (
            netProfitMargin NUMERIC,
            netPresentValue NUMERIC,
            internalRateOfReturn NUMERIC,
            paybackPeriod NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sbo_db (
            dividendYield NUMERIC,
            currentBondYield NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inc_db (
            insurancePremium NUMERIC,
            shortRatePremium NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pno_db (
            maturityValue NUMERIC,
            bankDiscount NUMERIC,
            proceeds NUMERIC
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
""")
    conn.commit()
    conn.close()    
    print(f"Database initialized: {db_path}")
    return db_path

def updateBbm_db(percentage, rate, base, percentChange, percentIncrease, percentDecrease, dbPath):
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bbm_db (percentage, rate, base, percentageChange, percentIncrease, percentDecrease)
            VALUES (?, ?, ?, ?, ?, ?) 
        """, (percentage, rate, base, percentChange, percentIncrease, percentDecrease)) 
        conn.commit()
        conn.close()
        return 0
