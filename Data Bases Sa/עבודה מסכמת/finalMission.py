#ניצן בר-אל 322450552
import psycopg2

def connect_to_db(dbname, user, password):
    # Connect to an existing database
    con = psycopg2.connect(f"dbname={dbname} user={user} password={password}")

    # Open a cursor to perform database operations
    cursor = con.cursor()
    return con, cursor


def close_communication(cur, conn):
    # Close communication with the database
    cur.close()
    conn.close()

#Check what product that is bought the most
def Check_most_used(cur):
    # get the count of the products that was bought
    cur.execute("SELECT Product_id, COUNT(Product_id) AS NumOrders FROM Orders GROUP BY Product_id;")
    # setting counters to each product
    count_4005 = 0
    count_4006 = 0
    count_4007 = 0
    count_4008 = 0
    # Fetch all
    all = cur.fetchall()
    for row in all:
        if row[0] == 4005:
            count_4005 = row[1]
        if row[0] == 4006:
            count_4006 = row[1]
        if row[0] == 4007:
            count_4007 = row[1]
        if row[0] == 4008:
            count_4008 = row[1]
    countLst = [count_4005,count_4006,count_4007,count_4008]
    most_common = 0
    item_code = 0
    for i in range(0,4):
        if countLst[i] > most_common:
            if i == 0:
                item_code = 4005
            if i == 1:
                item_code = 4006
            if i == 2:
                item_code = 4007
            if i == 3:
                item_code = 4008
            most_common = countLst[i]
    cur.execute("SELECT Description FROM Product WHERE product.Product_id = %s", (item_code, ))
    print("the most item been bought is the: " + cur.fetchall()[0][0])

def change_employee_lastname(cur,name,employee_id):
    for characters in name:
        if name[0].islower():
            raise Exception("name must start with a capital letter please type again")
            return
        if characters.isdigit():
            raise Exception("name can not have numbers in it please try again")
            return
    cur.execute("UPDATE Employee SET Last_name = %s WHERE Employee_id = %s;",(name, employee_id))





conn, cur = connect_to_db("endassaingnment", "postgres", "n22d21b07")
Check_most_used(cur)
close_communication(cur, conn)
print("Shelly the ceo got married so she wants to change her last name to her husband last name")
conn, cur = connect_to_db("endassaingnment", "postgres", "n22d21b07")
change_employee_lastname(cur,'Jorden',987654)
conn.commit()
close_communication(cur,conn)