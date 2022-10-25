import json
import pygal
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None

cc_pop={}
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict['Country Name']
        populatio=int(float(pop_dict['Value']))
        code=get_country_code(country)
        if code:
            cc_pop[code]=populatio


wm=pygal.maps.world.World()
wm.title='World Population 2010'
wm.add('2010',cc_pop)

wm.render_to_file('Americas1.svg')
