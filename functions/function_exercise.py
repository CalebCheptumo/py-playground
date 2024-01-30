#message

def display_message():
    """Display a simple message"""
    print("I am learning about functions in python")

display_message()


#favorite book

def favorite_book(title):
    """Display a message about someone's favorite book"""
    print(f"My favorite book is {title.title()}")

favorite_book('alice in wonderland')



#t-shirt
def make_shirt(size, message):
    """Display a message about the size of the shirt and the message printed on it"""
    print(f"The size of the shirt is {size} and the message printed on it is {message}")

make_shirt('large', 'hello world') #positional arguments
make_shirt(size='large', message='hello world') #keyword arguments


#large shirts
def make_shirt(size='large', message='I love Python'):
    """Display a message about the size of the shirt and the message printed on it"""
    print(f"The size of the shirt is {size} and the message printed on it is {message}")

make_shirt()



#cities

def describe_city(city, country='Kenya'):
    """Display a message about a city and the country it is in"""
    print(f"{city.title()} is in {country.title()}")


describe_city('nairobi')
describe_city('mombasa')
describe_city('kampala', 'uganda')


#city name
def city_country(city, country):
    """Return a string like 'Santiago, Chile'"""
    return f"{city.title()}, {country.title()}"

city = city_country('nairobi', 'kenya')
print(city)


#three city-country pairs
def city_country(city, country):
    """Return a string like 'Santiago, Chile'"""
    return f"{city.title()}, {country.title()}"

city1 = city_country('nairobi', 'kenya')
city2 = city_country('mombasa', 'kenya')
city3 = city_country('kampala', 'uganda')

print(city1)
print(city2)
print(city3)



#album
def make_album(artist, title, tracks='None'):
    """Return a dictionary of information about an album"""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album('khaligraph', 'testimony')
album2 = make_album('sauti sol', 'midnight train')
album3 = make_album('beyonce', 'lemonade')
album4 = make_album('beyonce', 'lemonade', tracks=12)

print(album1)
print(album2)
print(album3)
print(album4)


#user albums
def make_album(artist, title, tracks='None'):
    """Return a dictionary of information about an album"""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease enter the artist and album name:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)


#messages
text_messages = ['hello', 'how are you?', 'what are you doing?']

def show_messages(messages):
    """Print all messages in a list"""
    for message in messages:
        print(message)

show_messages(text_messages)



#sending messages
text_messages = ['hello', 'how are you?', 'what are you doing?']
sent_messages = []

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(text_messages, sent_messages)

print("\nFinal lists:")
print(text_messages)
print(sent_messages)



#archived messages
text_messages = ['hello', 'how are you?', 'what are you doing?']
sent_messages = []

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_messages(messages):
    """Print all messages in a list"""
    for message in messages:
        print(message)

send_messages(text_messages[:], sent_messages)
print("\nFinal lists:")
print(text_messages)
print(sent_messages)



#sandwiches
def make_sandwich(*items):
    """Make a sandwich with the given items"""
    print(items)

make_sandwich('cheese')
make_sandwich('cheese', 'ham')
make_sandwich('cheese', 'ham', 'lettuce')


def make_sandwich(*items):
    """Make a sandwich with the given items"""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('cheese')
make_sandwich('cheese', 'ham')
make_sandwich('cheese', 'ham', 'lettuce')


#user profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


    
