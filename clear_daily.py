#Imports
import json
import os

#path to json file to update
player_data_path = os.path.join('/Users/savagecoder/Desktop/Programming/Enchanter77_Discord_Bot/Json_files/User_data.json')
#open file to read
with open(player_data_path, 'r') as profile_data:
    daily_data1 = json.load(profile_data)
#open file to write
with open(player_data_path, 'w') as outfile:
    daily_data1['userdata'][]['daily'] = 0
    json.dump(daily_data1, outfile)