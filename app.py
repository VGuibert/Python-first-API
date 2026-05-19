from flask import Flask, request
from flask import jsonify

tableauPokemon = [{'name': 'pikachu', 'power': 20, 'life': 50},{'name': 'bulbizare', 'power': 30, 'life': 60}]

app= Flask(__name__)

# Route "Welcome" de l'api
@app.route('/')
def home():
    return '<p> Welcome Home ! </p>' \
    ' <p> route - </p>' \
    ' <p> /data => vers les données des pokemons (GET) </p>'\
    ' <p> /data/new/pokemon => Enregistrer un nouveau pokemon (POST) : Format {\'name\': \'Nom du pokemon', 'power\': Sa puissance, \'life\': Sa vie} </p>'


# Route pour récupérer les info d'un pokemon
@app.route('/data/<pokemon_name>')
def dataNamePokemon(pokemon_name):
    pokemonToDisplay = ''
    for pokemon in tableauPokemon :
        if(pokemon_name == pokemon['name']):
            pokemonToDisplay = pokemon

    if(pokemonToDisplay != ''):
        return pokemonToDisplay
    else :
        return 'No pokemon with this name'

# Route pour ajouter un pokemon
@app.route('/data/new/pokemon', methods=['POST'])
def savePokemon():
    data = request.get_json()
    
    newPokemon = {
        "name" : data.get("name"),
        "power" : data.get("power"),
        "life" : data.get("life")
    }

    tableauPokemon.append(newPokemon)
    return jsonify(newPokemon), 201