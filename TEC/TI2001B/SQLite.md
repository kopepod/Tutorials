# SQL + Python

```bash
wget https://raw.githubusercontent.com/kopepod/Tutorials/refs/heads/main/FisherIris/fisher_iris.csv
```


```python
import sqlite3
import pandas

conn = sqlite3.connect("fisher_iris.db");
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepal_length FLOAT,
    sepal_width FLOAT,
    petal_length FLOAT,
    petal_width FLOAT,
    variety TEXT
)
""") # SQL query

DF = pandas.read_csv("fisher_iris.csv");

for _, row in DF.iterrows():
  flower_data = ( row.sepal_length, row.sepal_width, row.petal_length, row.petal_width, row.variety )
  cursor.execute("""
INSERT OR IGNORE INTO flowers (sepal_length, sepal_width, petal_length, petal_width, variety)
VALUES (?, ?, ?, ?, ?)
""", flower_data)

conn.commit() # cierra conexion

```
