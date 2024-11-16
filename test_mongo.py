from pymongo import MongoClient

# Conectare la MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['produse']

# Adaugare document de test
collection = db['produse_colectie']
document = {"nume": "produs1", "pret": 100}
collection.insert_one(document)

# Verifica daca functioneaza
print("Conectare reusita la MongoDB!")
