import sqlite3

with sqlite3.connect('customers.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print('SQLite version:', data)

with sqlite3.connect('customers.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers_data
                  (customer_id INT, customer_name TEXT, address TEXT, balance REAL, pin INT)''')
    conn.commit()

dct = {"customer_id":'c_100', 'customer_name': 'Adam Kowalski', 'address': 'Warsaw', 'balance': 1000, 'pin': 1234}
dct2 = {"customer_id":'c_101', 'customer_name': 'Maria Nowak', 'address': 'Krakow', 'balance': 490, 'pin': 1111}
dct3 = {"customer_id":'c_102', 'customer_name': 'Laura Kwiatkowska', 'address': 'Gdansk', 'balance': 0, 'pin': 2137}

tup= [(dct["customer_id"], dct['customer_name'], dct['address'], dct['balance'], dct['pin']),
      (dct2["customer_id"], dct2['customer_name'], dct2['address'], dct2['balance'], dct2['pin']),
      (dct3["customer_id"], dct3['customer_name'], dct3['address'], dct3['balance'], dct3['pin'])]
print(tup)

with sqlite3.connect('customers.db') as conn:
    cursor = conn.cursor()
    for row in tup:
        sql_statement = '''customers_data(customer_id, customer_name, address, balance, pin) VALUES (?,?,?,?,?)'''
        cursor.execute(sql_statement, row)
    conn.commit()
    cursor.close()