from pygal import maps.world
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None
y=input('Enter the country name:')
print(get_country_code(y))

