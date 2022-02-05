import main.py

while client.access_token == None:
    username = input('Username: ')
    password = getpass()
    try:
        client = DocumentCloud(username, password)
    except:
        print("Something went wrong, try your credentials again or exit program.")

params =  { 
    "token": client.access_token, 
    "base_uri": base_uri,
    "documents": documents,
    "data": data
    }

params_json = json.dump(params, p)

