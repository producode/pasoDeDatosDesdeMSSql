import pymssql
import pymongo
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Conexión a la base de datos SQL Server

#root:proyecto1234@tcp(localhost:3306)/PruebaBejerman
conn_sql = pymssql.connect(server=os.getenv('SQL_SERVER'), port=os.getenv('SQL_PORT'), user=os.getenv('SQL_USER'), password=os.getenv('SQL_PASSWORD'), database=os.getenv('SQL_DATABASE'))
cursor = conn_sql.cursor()

# Consulta SQL con la opción FOR JSON AUTO
query = "SELECT * FROM Recursos FOR JSON AUTO"
cursor.execute(query)
result = cursor.fetchall()

# Convertir los datos de SQL Server a objetos JSON
json_data = json.loads(result[0][0])

# Conexión a la base de datos MongoDB
if os.getenv('MONGO_SERVER') != "":
    conn_mongo = pymongo.MongoClient(os.getenv('MONGO_SERVER'), username=os.getenv('MONGO_USER'), password=os.getenv('MONGO_PASSWORD'))
    db = conn_mongo[os.getenv('MONGO_DATABASE')]
    collection = db[os.getenv('MONGO_COLLECTION')]

# Insertar los datos en MongoDB
print(json_data)
