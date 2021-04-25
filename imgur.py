import requests, configparser
config = configparser.ConfigParser()
config.read('./config.ini')
client_id = config['imgur']['client_id']
client_secret = config['imgur']['client_secret']

headers = {
'Authorization': 'Client-ID '+ client_id
}