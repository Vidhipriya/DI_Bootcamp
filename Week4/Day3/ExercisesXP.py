# ExerciseXP1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# for item in zip(keys, values): 
#     print(item)
    
  
  
  
  
  
  
  
  
  
  
    
# ExerciseXP2

# family = {"baby": 2,"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for name,age in family.items():

#     age = int(age)
#     if age < 3:
#        price=''

#     elif age < 12:
#        price="$10"
        
#     else:
#        price="$15"
#     print(f"{name} aged {age} has to pay {price} ")


#ExerciseXP3

brand_dict={
     "name": "Zara" ,
     "creation_date": 1975,
     "creator_name": "Amancio Ortega Gaona" ,
     "type_of_clothes": ["men", "women", "children", "home"] ,
     "international_competitors": ["Gap", "H&M", "Benetton"] ,
     "number_stores": 7000 ,
     "major_color": 
       { "France": "blue", 
        "Spain": "red", 
        "US": "pink, green"}}

brand_dict['number_stores']=2
print(brand_dict)
print(f"zara has as clients {brand_dict['type_of_clothes']}")
brand_dict.update({'country_creation':'Spain'})
print(brand_dict)
if "international_competitors" in  brand_dict:
    brand_dict.get('international_competitors').append('Desigual')
print(brand_dict)
del brand_dict['creation_date']
print(brand_dict)
print("The last competitor is",brand_dict['international_competitors'][-1])
print(brand_dict['major_color']['US'])
print(len (brand_dict))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
    
}
brand_dict.update(more_on_zara)
print(brand_dict['number_stores'])


# ExerciseXP4
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]