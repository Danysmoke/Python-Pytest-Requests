import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b75bb169bea47d155158649cc668dd1d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_pokemons = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemons)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_update_pokemons = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update_pokemons)
print(response_update.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

respons_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(respons_add_pokeball.text)