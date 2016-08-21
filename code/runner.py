# Import the driver.
import psycopg2
import uuid

def runApp():
    conn = psycopg2.connect(database='teststuff', user='testuser', host='roach1', port=26257)
    createTable(conn)
    putStuff(conn)
    conn.close()

def createTable(conn):
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fakedata(id string primary key, data1 string not null, data2 string, data3 string, data4 string, data5 string, data6 string)")
    cur.close()

def putStuff(conn):
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Insert two rows into the "accounts" table.
    for i in xrange(10000):
        cur.execute("INSERT INTO fakedata (id, data1, data2, data3, data4, data5) VALUES ('"+str(i)+"-"+str(uuid.uuid4())+","+str(uuid.uuid4())+"','"+str(uuid.uuid4())+"','"+str(uuid.uuid4())+"','"+str(uuid.uuid4())+"','"+str(uuid.uuid4())+"')")

    # Close the database connection.
    cur.close()
