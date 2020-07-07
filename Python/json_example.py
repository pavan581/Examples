import json 
  
# Data to be written 
dictionary ={ 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
} 
  
# Serializing json  
json_object = json.dumps(dictionary, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "a") as outfile: 
    outfile.write(json_object)

outfile.close()

fp = open("sample.json","r")
obj = json.load(fp)
fp.close()
print(obj)
print(obj.get("name"))

obj["name"] = "pavan"
print(obj)

fp = open("sample.json","w")
fp.write(json.dumps(obj,indent=4))
fp.close()
