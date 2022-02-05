base_uri = "http://api.www.documentcloud.org/api/"

documents = []

while doc_picker != "none":
    doc_picker = input('Put in another document ID or type "none": ')
        if doc_picker != none:
            documents.append(doc_picker)

print("We're working on these documents " + str(documents))

data = input('Data option: ')

params_dict =  { 
    "token": client.access_token, 
    "base_uri": base_uri,
    "documents": documents,
    "data": data
    }
