import json

book = {                # Definició del contingut del JSON
    "book": [
        {
            "title": "Va puntxar al seu colega",
            "cover": "Dura",
            "year": "2004",
            "pages": "1312"
        },
        {
            "title": "En teo va al supermercat",
            "cover": "Tova",
            "year": "2001",
            "pages": "4"
        },
        {
            "title": "Virtual Hero 2",
            "cover": "Durisima",
            "year": "2012",
            "pages": "No suficients"
        },
        {
            "title": "Soy un gnomo",
            "cover": "toveta",
            "year": "1966",
            "pages": "0"
        }
    ]
}
def imprimeix():                #Funció que imprimeix el contingut del JSON en el seu format
    print(json.dumps(book, indent=2))

def crea():                     #Funció que transfereix el contingut del JSON del Python al fitxer jason.json
    with open("jason.json", "w") as file:
        json.dump(book, file)


