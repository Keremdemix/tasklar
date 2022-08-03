import excel2json
import json
data=excel2json.convert_from_file('data.xlsx')
x={}
with open('Sayfa1.json') as json_file:

    data = json.load(json_file)

    for i in range (len(data)):
        
       key=data[i]["VendorID"]
       
       x[str(int(key))]={ 
        
            "Context": data[i]["EventMap.Context"],
            "SubType":  data[i]["EventMap.SubType"],
            "Type":  data[i]["EventMap.Type"] 
        
        }
    
    dest = dict(x) 
    jsonString = json.dumps(dest)
    jsonFile = open(("data.json"), "w")
    jsonFile.write(jsonString)
    jsonFile.close()
      
