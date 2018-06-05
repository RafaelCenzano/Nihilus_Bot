#Imports
import json
import os
import logging

#logging config and start script log
logging.basicConfig(filename='clear_data.log', level=logging.INFO)
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info('script started')

#path to json file to update
player_data_path = os.path.join('/Users/savagecoder/Desktop/Programming/Enchanter77_Discord_Bot/Json_files/User_data.json')

#open file to read
with open(player_data_path, 'r') as profile_data:
    daily_data1 = json.load(profile_data)
logging.debug('read json file')

#open file to write
with open(player_data_path, 'w') as outfile:
    for user in daily_data1['userdata']:
        daily_data1['userdata'][user]['daily'] = 0
        daily_data1['userdata'][user]['repped'] = 0
    json.dump(daily_data1, outfile)
logging.debug('overwrite daily and repped')

#log end of file
logging.info('script end')