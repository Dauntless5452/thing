states = {
    'oregon': 'OR',
    'florida': 'FL',
    'Californai': "CA",
    'new york': "NY",
    'michigan': "MI"
}

cities = {
    'CA': 'san francisco',
    "MI": 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'new york'
cities['OR'] = 'portland'

print("-" * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbrevoation is: ", states['michigan'])
print("Florida's abbreviation is: ", states['florida'])

print("Michigan has: ", cities[states['michigan']])
print("Florida has: ", cities[states['michigan']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))
 
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('texas', None)

if not state:
    print("sorry, no texas")

city = cities.get('TX', 'Does NOt Exist')
print("The city for the state 'TX' is: %s" % city)