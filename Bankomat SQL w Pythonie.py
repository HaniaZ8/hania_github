import sqlite3
#cos

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

def get_customer_data(x):
    try:
        with sqlite3.connect('customers.db') as conn:
            cursor = conn.cursor()
            user=(x,)
            cursor.execute('''SELECT * FROM customers_data WHERE customer_id=(?)''', user)
            data = cursor.fetchall()
            cursor.close()
            g = data
            w = list(g[0])
            categories = ['customer_id', 'customer_name', 'address', 'balance', 'pin']
            res={}
            for i in range(len(categories)):
                res[categories[i]] = w[i]
            return res
    except:
        print("problem z data")
    
    
class Customer:
    def __init__(self, customer_id="nonne", customer_name="nope", address="nowhere", balance=0, pin=0):
        self.customer_id = customer_id
        self.customer_name = customer_name 
        self.address = address
        self.balance = balance 
        self.pin = pin
        
    def withdraw_money(self, customer, amount):
        try:
            with sqlite3.connect('customers.db') as conn:
                cursor = conn.cursor()
                user=(self.customer,)
                cursor.execute('''SELECT * FROM customers_data WHERE customer_id=(?)''', user)
                data = cursor.fetchall()
                cursor.close()
                g = data
                w = list(g[0])
                categories = ['customer_id', 'customer_name', 'address', 'balance', 'pin']
                res={}
                for i in range(len(categories)):
                    res[categories[i]] = w[i]
                moneyout = res['balance'] - self.amount
                customer = Customer(customer,res['customer_name'],res['address'],moneyout,res['pin'])
                return customer
        
        except:
            print('error occured')
            
    def deposit_money(self, customer, amount):
        try:
            with sqlite3.connect('customers.db') as conn:
                cursor = conn.cursor()
                user=(self.customer,)
                cursor.execute('''SELECT * FROM customers_data WHERE customer_id=(?)''', user)
                data = cursor.fetchall()
                cursor.close()
                g = data
                w = list(g[0])
                categories = ['customer_id', 'customer_name', 'address', 'balance', 'pin']
                res={}
                for i in range(len(categories)):
                    res[categories[i]] = w[i]
                moneyin = res['balance'] + self.amount
                customer = Customer(customer,res['customer_name'],res['address'],moneyin,res['pin'])
                return customer
        except:
            print('error occured')

        
def get_customer_object(x):
    
    try:
        dane = get_customer_data(x)
        klient = Customer(x,dane['customer_name'],dane['address'],dane['balance'],dane['pin'])
        return klient
    except:
        print("Error with creating customer")
