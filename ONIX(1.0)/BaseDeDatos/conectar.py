from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
url = "mongodb+srv://erikaosorio:EzPml5yeSV6qC1YR@cluster0.1ltwt8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def conexion():
    cliente = MongoClient(url, server_api = ServerApi('1'))

    try:
        cliente.admin.command('ping')
        db = cliente.Onix
        print("Conectado a MongoDB")
        return (db)
    except Exception as e:
        print(e)