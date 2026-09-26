import sqlite3

def inputPercentage(rate, base):
    if rate == None:
        if base == None:
            return "Can't calculate without rate and base."
        else:
            return "Can't calculate without rate."
    else:
        if base == None:
            return "Can't calculate without base."
        else:
            return "Calculate"

def inputRate(percentage, base):
    if percentage == None:
        if base == None:
            return "Can't calculate without percentage and base."
        else:
            return "Can't calculate without percentage."
    else:
        if base == None:
            return "Can't calculate without base."
        else:
            return "Calculate"

def inputBase(percentage, rate):
    if percentage == None:
        if rate == None:
            return "Can't calculate without percentage and rate."
        else:
            return "Can't calculate without percentage."
    else:
        if rate == None:
            return "Can't calculate without rate."
        else:
            return "Calculate"       

def inputPercentageChange(dbPath, new):
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
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

def inputPercentIncrease(percentage, dbPath):
    if percentage == None:
        return "Can't calculate without percentage"
    else:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT percentage
            FROM bbm_db
            ORDER BY id DESC
            LIMIT 1
            """)
        row = cursor.fetchone()
        if row is None:
            return "Can't calculate without the old percentage."
        else:
            original = row["percentage"]
        if percentage > original:
            increase = percentage
            if original == None:
                if increase == None:
                    return "Can't calculate without the old percentage and the new percentage."
                else:
                    return "Can't calculate without the old percentage."
            else:
                if increase == None:
                    return "Can't calculate without the new percentage."
                else:
                    return "Calculate"  
        else:
            return "Calculate"

def inputPercentDecrease(percentage, dbPath):
    if percentage == None:
        return "Can't calculate without percentage"
    else:
        conn = sqlite3.connect(dbPath)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT percentage
            FROM bbm_db
            ORDER BY id DESC
            LIMIT 1
            """)
        row = cursor.fetchone()
        if row is None:
            return "Can't calculate without the old percentage."
        else:
            original = row["percentage"]
        if original > percentage:
            decrease = percentage
            if decrease == None:
                if original == None:
                    return "Can't calculate without the old percentage and the new percentage."
                else:
                    return "Can't calculate without the old percentage."
            else:
                if decrease == None:
                    return "Can't calculate without the new percentage."
                else:
                    return "Calculate" 
        else:
            return "Calculate"