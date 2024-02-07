#test to verify that the function returns values such s 'santiago' and 'chile' correctly.
from city_functions import get_formatted_name



def test_city_country():
    """Do cities like 'santiago' and countries like 'chile' work?"""
    formatted_name = get_formatted_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'


def test_city_country_population():
    """Do cities like 'santiago' and countries like 'chile' work?"""
    formatted_name = get_formatted_name('santiago', 'chile', 5000000)
    assert formatted_name == 'Santiago, Chile - Population 5000000'