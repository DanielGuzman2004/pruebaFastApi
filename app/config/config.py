from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Vanidosa:ADSO2022@cluster0.v5drsdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crea un nuevo cliente para conectarse al servidor
client = MongoClient(uri)

db = client.bank
blogsCollection = db['user']  # Asegúrate de que el nombre de la colección sea correcto

# Si la conexión es exitosa te enviará un mensaje
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
