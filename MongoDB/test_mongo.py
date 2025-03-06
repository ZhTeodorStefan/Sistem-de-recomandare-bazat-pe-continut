from pymongo import MongoClient

# Conectare la serverul local MongoDB
client = MongoClient('mongodb+srv://teodorstefanzaharia:OdTvBHwBaENZZiC0@main.g8ezz.mongodb.net/')
print("Conectare reusita la MongoDB!")

# Selectarea bazei de date
db = client['testare']
print("Baza de date selectata")

# Selectarea colectiei
collection = db['tutorial']
print("Colectia selectata")

# CRUD
# CREATE
def adauga_produs(nume, pret):
    document = {"nume": nume, "pret": pret}
    result = collection.insert_one(document)
    print(f"Produsul {nume} adaugat cu pretul: {pret}.")

# READ
def citeste_toate_produsele():
    produse = collection.find()
    for produs in produse:
        print(produs)

def citeste_produs(nume):
    produs = collection.find_one({"nume": nume})
    if produs:
        print(f"Produs gasit: {produs}")
    else:
        print(f"Produsul '{nume}' nu a fost gasit.")

# UPDATE
def actualizeaza_produs(nume, pret_nou):
    result = collection.update_one(
        {"nume": nume},
        {"$set": {"pret": pret_nou}}
    )
    if result.matched_count > 0:
        print(f"Produsul '{nume}' a fost actualizat.")
    else:
        print(f"Produsul '{nume}' nu a fost gasit.")

# DELETE
def sterge_produs(nume):
    result = collection.delete_one({"nume": nume})
    if result.deleted_count > 0:
        print(f"Produsul '{nume}' a fost sters.")
    else:
        print(f"Produsul '{nume}' nu a fost gasit.")

# Verificare functionalitati
adauga_produs("Samsung A30", 600)
adauga_produs("Samsung A50", 850)
citeste_produs("Samsung")
print("\nProduse existente:")
citeste_toate_produsele()
actualizeaza_produs("Samsung A50", 600)
sterge_produs("Samsung A50")
print("\nProduse după modificare:")
citeste_toate_produsele()