from main import run_collection, send_message_collections_finished

collections = ['collection_name_1.json', 'collection_name_2.json',
             'collection_name_3.json', 'collection_name_4.json']

environment = 'https://api.getpostman.com/environments/__YOUR_ENVIRONMENT_'
environment_name = 'QA Environment'
path = './postman_collections/'


for collection in collections:
    run_collection(path + collection, collection, environment, environment_name)

send_message_collections_finished()

# print(collections)