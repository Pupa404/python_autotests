import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '414d085767aab60d57fc4b8a896b2d48'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_update_name = {
    "pokemon_id": "279486",
    "name": "generate",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "279486"
}
    
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())'''

response_update_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update_name)
print(response_update_name.json())

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json())





