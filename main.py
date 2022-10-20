

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd
import numpy as np
import pyspark as ps

def load_pokemon():
    df_final = pd.DataFrame()
    for index in range(1,905): # Assigning index for each pokemon
        print(index)

        # Loading pokemon data
        url = f'https://pokeapi.co/api/v2/pokemon/{index}'
        response = requests.get(url)
        read_json = response.json()

        # Note which games the pokemon has been
        games = read_json["game_indices"]
        list_of_games = [games[k]["version"]["name"] for k in range(0,len(games))]
        pokemon_in_game = np.isin(['red', 'blue', 'leafgreen', 'white'],list_of_games)
        if sum(pokemon_in_game )>0: # Will only save the pokemon if it is one of the designated games

            # Makes a dict with the following 6 variables
            poke_dict = {k: read_json[k] for k in ('name', 'id','base_experience','weight','height','order')}

            # Saves the types of the pokemon
            pokemon_types = read_json['types']
            poke_dict['type1'] = pokemon_types[0]['type']['name']
            if len(pokemon_types) == 1:
                poke_dict['type2'] = None
            else:
                poke_dict['type2'] = pokemon_types[1]['type']['name']

            # Calculates the BMI of the pokemon
            BMI = poke_dict['weight']/(0.1 * poke_dict['height'] * poke_dict['height'])
            poke_dict['BMI'] = round(BMI, 2)
            poke_dict['name'] = poke_dict['name'].capitalize() # We ensure the pokemons name is capitalized

            # Saves the url to the front sprite
            poke_dict['front_default sprite'] = read_json['sprites']['front_default']

            # save which game the pokemon is in
            poke_dict['Red'] = pokemon_in_game[0]
            poke_dict['Blue'] = pokemon_in_game[1]
            poke_dict['Leafgreen'] = pokemon_in_game[2]
            poke_dict['White'] = pokemon_in_game[3]

            # We convert the dict to a dataframe and add the data to the main dataframe
            df = pd.DataFrame([poke_dict])
            df_final = pd.concat([df_final,df])
    return df_final


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testP = load_pokemon()
    print(testP)
    # We save the data as a csv
    testP.to_csv("C:/Users/simon/Desktop/Jobsøgning/Lwgo/Lego Case/Data/Pokedat.csv", encoding='utf-8', index=False)
    # We also create a spark Dataframe from the pandas Dataframe
    spark = ps.sql.SparkSession.builder.getOrCreate()
    spark_df = spark.createDataFrame(testP)
    print(spark_df)
