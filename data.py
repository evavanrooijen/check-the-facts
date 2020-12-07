import urllib.request as ur
import pandas as pd
import ast
import json

url = 'https://onderwijsdata.duo.nl/api/3/action/datastore_search?resource_id=445e53f4-b293-4c4c-85c2-8f4843d24a1f&limit=5&q=title:jones'  
fileobj = ur.urlopen(url)
print(fileobj.read())
output = fileobj.read()
print(type(output))
#dataset = pd.DataFrame(data= fileobj.read().result)
#print(dataset.head())
#dict_str = fileobj.read().decode("UTF-8")
#mydata = ast.literal_eval(dict_str)
#print(repr(mydata))

json.loads(fileobj.read().decode('utf-8'))
