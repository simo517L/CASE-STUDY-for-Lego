
import requests
import pandas as pd
import numpy as np


def load_pokemon_number():
    # The function will find the numbers of pokemon in the different games which also appear in the other versions
    # We make a list for each of the four pokemon games
    poke_red = []
    poke_blue = []
    poke_leafgreen = []
    poke_white = []
    for index in range(1,905): # Assigning index for each pokemon
        print(index)

        # Loading pokemon data
        url = f'https://pokeapi.co/api/v2/pokemon/{index}'
        response = requests.get(url)
        read_json = response.json()

        # Note which games the pokemon has been
        games = read_json["game_indices"]
        list_of_games = [games[k]["version"]["name"] for k in range(0,len(games))]
        if len(set(list_of_games) & set(['red', 'blue', 'leafgreen', 'white']))>0: # Will only save the pokemon if it is one of the designated games
            # We save the pokemons name in the list game where it appeared
            if 'red' in set(list_of_games):
                poke_red.append(read_json['name'])
            if 'blue' in set(list_of_games):
                poke_blue.append(read_json['name'])
            if 'leafgreen' in set(list_of_games):
                poke_leafgreen.append(read_json['name'])
            if 'white' in set(list_of_games):
                poke_white.append(read_json['name'])

    # using a numpy function, we find the number of pokemons that appear in two games
    poke_red_in_blue  = sum(np.isin(poke_red,poke_blue))
    poke_red_in_leafgreen = sum(np.isin(poke_red, poke_leafgreen))
    poke_red_in_white = sum(np.isin(poke_red, poke_white))
    poke_leafgreen_in_white = sum(np.isin(poke_leafgreen, poke_white))
    return {'poke_red' : len(poke_red), 'poke_red_in_blue':poke_red_in_blue, 'poke_red_in_leafgreen ':poke_red_in_leafgreen, 'poke_red_in_white':poke_red_in_white, 'poke_leafgreen_in_white ':poke_leafgreen_in_white   }


# Press the green button in the gutter to run the script.
if __name__ == '__Number of pokemon__':
    Number_pokemon = load_pokemon_number()
    print(Number_pokemon)

