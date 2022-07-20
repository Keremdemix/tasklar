city_district_info = {}


## Use a function to match cities with their district as key-value pairs:
# define a function with a reasonable name# match these in function: Istanbul - Kadıkoy, Ankara - Sincan, Izmir - Alsancak
def matcher():
    city_district_info["Istanbul"]="Kadikoy"
    city_district_info["Ankara"]="Sincan"
    city_district_info["Izmir"]="Alsancak"




# print city_district_info in the global scope
matcher()
print(city_district_info)

