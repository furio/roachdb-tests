# Import the driver.
import psycopg2

# Connect to the "bank" database.
conn = psycopg2.connect(database='teststuff', user='testuser', host='roach1', port=26257)


def runApp():  
    print "Yoh"

def runTest():
    # Make each statement commit immediately.
    conn.set_session(autocommit=True)

    # Open a cursor to perform database operations.
    cur = conn.cursor()

    # Insert two rows into the "accounts" table.
    cur.execute("INSERT INTO accounts (id, balance) VALUES (1, 1000), (2, 250)")

    # Print out the balances.
    cur.execute("SELECT id, balance FROM accounts")
    rows = cur.fetchall()
    print('Initial balances:')
    for row in rows:
        print([str(cell) for cell in row])

    # Close the database connection.
    cur.close()
    conn.close()    