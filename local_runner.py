import main.py

while client.access_token == None:
    username = input('Username: ')
    password = getpass()
    try:
        client = DocumentCloud(username, password)
    except:
        print("Something went wrong, try your credentials again or exit program.")

documents = []

while doc_picker != "none":
    doc_picker = input('Put in another document ID or type "none": ')
        if doc_picker != none:
            documents.append(doc_picker)

print("We're working on these documents " + str(documents))

data = input('Data option: ')
params = json.dump(params, p)

main(client, documents, data)