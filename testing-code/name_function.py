#def get_formatted_name(first, last): # the function get_formatted_name() combines the first and last name
#def get_formatted_name(first, middle, last): # should work for people with middle names
  #  """Generate a neatly formatted full name"""
    #full_name = f"{first} {last}"
   # full_name = f"{first} {middle} {last}"
    #return full_name.title()


#make the middle name optional by giving it an empty default value
def get_formatted_name(first, last, middle=''): # make the middle name optional
    """Generate a neatly formatted full name"""
    if middle: # if middle name is given
        full_name = f"{first} {middle} {last}" # combine the first, middle, and last name
    else: # if middle name is not given
        full_name = f"{first} {last}" # combine the first and last name
    return full_name.title() # return the full name in title case