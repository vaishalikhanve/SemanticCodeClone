import json
import io
f=io.open('pdg_data.json','r',encoding="utf-8")
data=json.load(f)
print(data)
