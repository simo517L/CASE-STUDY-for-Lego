

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
#import os
#import numpy as np
import pandas as pd
import json

def load_pokemon():
    df_final = pd.DataFrame()
    for index in range(1,905):
        print(index)
        url = f'https://pokeapi.co/api/v2/pokemon/{index}'
        response = requests.get(url)
        read_json = response.json()
        games = read_json["game_indices"]
        list_of_games = [games[k]["version"]["name"] for k in range(0,len(games))]
        if len(set(list_of_games) & set(['red', 'blue', 'leafgreen', 'white']))>0:
            poke_dict = {k: read_json[k] for k in ('name', 'id','base_experience','weight','height','order')}
            pokemon_types = read_json['types']
            poke_dict['type1'] = pokemon_types[0]['type']['name']
            if len(pokemon_types) == 1:
                poke_dict['type2'] = None
            else:
                poke_dict['type2'] = pokemon_types[1]['type']['name']
            poke_dict['BMI'] = poke_dict['weight']/(0.1 * poke_dict['height']* poke_dict['height'])
            poke_dict['name'] = poke_dict['name'].capitalize()
            poke_dict['front_default sprite'] = read_json['sprites']['front_default']
            df = pd.DataFrame([poke_dict])
            df_final = pd.concat([df_final,df])
    return df_final


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testP = load_pokemon()
    print(testP)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
