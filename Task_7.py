import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

conn = sqlite3.connect('sales_data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS sales
             (sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
              product TEXT,
              quantity INTEGER,
              price REAL)''')

conn.execute("DELETE FROM sales")

conn.execute("INSERT INTO sales (product, quantity, price) VALUES ('A', 10, 5.0)")
conn.execute("INSERT INTO sales (product, quantity, price) VALUES ('A', 15, 5.0)")
conn.execute("INSERT INTO sales (product, quantity, price) VALUES ('B', 20, 10.0)")
conn.execute("INSERT INTO sales (product, quantity, price) VALUES ('C', 5, 15.0)")
conn.execute("INSERT INTO sales (product, quantity, price) VALUES ('C', 10, 15.0)")
conn.commit()

query = """
SELECT product,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
print(df)

df.plot(kind='bar', x='product', y='revenue')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.show()

conn.close()