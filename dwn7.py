import pygal
worldmap =  pygal.maps.world.World()
import json

filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

x=input('Enter the year here:')
y=input('Enter the country name:')
for pop_dict in pop_data:
    if pop_dict['Year']==x and pop_dict['Country Name']==y :
        po=pop_dict['Value']
        break
print('The population was :',po)
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None

print(get_country_code(y))