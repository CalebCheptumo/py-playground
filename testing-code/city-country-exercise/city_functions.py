#function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile.


#def get_formatted_name(city, country, population):
 #   """Generate a neatly formatted city and country"""
  #  formatted_name = f"{city}, {country} - population {population}"
   # return formatted_name.title()


def get_formatted_name(city, country, population=0):
    """Generate a neatly formatted city and country"""
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()