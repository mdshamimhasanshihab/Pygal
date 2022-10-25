import json
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

y=input('Enter the country name:')
x=input('Enter the year here:')

for pop_dict in pop_data:
    if pop_dict['Year']==x and pop_dict['Country Name']==y :
        population=pop_dict['Value']
        break
print('The population was :',population)