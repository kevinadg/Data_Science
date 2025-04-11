import sqlite3
import pandas as pd

# Connexion à la base de données (création si elle n'existe pas)
conn = sqlite3.connect('database.db')

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exemple : Création d'une table et insertion de données (si nécessaire)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# Exemple : Insertion de quelques données
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25), ('Bob', 30), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35), ('Charlie', 35)")
conn.commit()

query = "SELECT * FROM users"
df = pd.read_sql_query(query, conn)

print(df.head())

# Fermeture de la connexion
conn.close()
