#def get_formatted_name(first, last): # the function get_formatted_name() combines the first and last name
def get_formatted_name(first, middle, last): # should work for people with middle names
    """Generate a neatly formatted full name"""
    #full_name = f"{first} {last}"
    full_name = f"{first} {middle} {last}"
    return full_name.title()