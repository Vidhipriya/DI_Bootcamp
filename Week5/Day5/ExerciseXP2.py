import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
json_file = "my_file.json"
sampleJson['company']['employee']['birth_date']="01.02.03"
with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj, indent=2)
    