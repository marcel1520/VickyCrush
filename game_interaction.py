import json
import re #find_birth_year
import random #random pick of famous people for the player

def get_countries(path):
    ''' Returns a list of all countries from world-countries.json'''
    with open(path, 'r') as fileobj:
        countries_data = json.load(fileobj)

    countries = []
    for feature in countries_data['features']:
        name = feature['properties']['name']
        countries.append(name)
    return countries

def get_us_states(path):
    ''' Returns a list of all us-states from world-countries.json '''
    with open(path, 'r') as fileobj:
        data = json.load(fileobj)

        us_states = []
        for state in data:
            us_states.append(state['name'])
        return us_states

def get_professions(path):
    with open(path, 'r') as fileobj:
        data = json.load(fileobj)

        professions = []
        for profession in list(data.values()):
            professions.append(profession)
    return professions[0]


def get_random_person(data):
    """ Pick a person at random from a list of celebrities """
    while True:
        data = candidate_list_full
        random_person = random.choice(data)

        name = random_person[0]
        if len(name) < 2:
            continue
        else:
            return random_person

def find_birth_year(text):
    """ finds the birth year in the birth_info string in results. """
    match = re.search(r'\b\d{4}\b', text) # Use regex to find 4-digit integers in the string
    if match:
        birth_year = int(match.group())
        return birth_year
    else:
        print('No integer found in wikipedia. Skipping that Question!!')
        return False


def get_answer_1(points, random_person):
    """ gets the answer for birth date from the user and compares with random_person
        returns the points gained in Q1. The closer the guess, the more points """

    print(f"Current Points: {points}\n")
    # Find birth year in random_person:
    name = random_person[0]
    birth_info = random_person[1]
    birth_year_result = find_birth_year(birth_info)

    # get user input, compare and give points:
    birth_year_answer = int(input(f"\nQUESTION 1: What year was {name} born?\n"))
    if birth_year_answer == birth_year_result: #correct answer
        print(f"{birth_year_result} is correct! You get 20 points!\n")
        points += 30
    elif birth_year_answer in range(birth_year_result - 10, birth_year_result + 10): # range 10 years
        print(f"{birth_year_answer} is in 10 year range! You get 15 points! Correct Answer: {birth_year_result}")
        points += 15
    elif birth_year_answer in range(birth_year_result - 50, birth_year_result + 50): # 50 year range
        print(f"{birth_year_answer} is in 50 year range! You get 10 points! Correct Answer: {birth_year_result}")
        points += 10
    elif birth_year_answer in range(birth_year_result - 100, birth_year_result + 100): # 100 year range
        print(f"{birth_year_answer} is in 100 year range! You get 5 points! Correct Answer: {birth_year_result}")
        points += 5
    else:
        print(f"{birth_year_answer} is more than 100 years apart! Correct Answer: {birth_year_result}. You get 0 points!")

    return points


def get_answer_2(points, random_person, countries, us_states):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""

    print(f"Current Points: {points}")
    # Find birth location in random_person:
    name = random_person[0]
    birth_info = random_person[1]
    location_data = birth_info.split(",")[-1].strip().lower()
    country = None
    state = None

    # Extract country/state from location_data
    for word in location_data.split():
        if word in countries:
            country = word
        elif word in us_states:
            country = "usa"
            state = word

    if not country:
        print(f"Could not find a valid country/state in the data: {location_data}")
        print("Skipping this question!")
        return points

    # Ask user for country input and check:
    location_answer = input(f"\nQUESTION 2: Where was {name} born? ").strip().lower()
    if location_answer == country or (state and location_answer == state):
        print(f"Correct! {name} was born in {location_answer}. You get 10 points!")
        points += 10
    else:
        print(f"False! {name} was born in {state if state else country}.")

    # Optional Guess if a city was extracted:
    birth_city = random_person[1].split(",")[0].split()[-1]
    if len(birth_city) > 4:
        guess_city = input(f"Get 10 Bonus Points if you know the City {name} was born.\nGuess the city: ")

        if guess_city.lower() == birth_city.lower():
            points += 10
            print(f"Great Job, {birth_city} is correct!")
        else:
            print(f"False, {name} was born in {birth_city}.")

    return points


def get_answer_3(points, random_person, profession_keywords):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""
    print(f"Current Points: {points}")
    name = random_person[0]
    profession_info = random_person[2].split()

    # find professions of the random person
    professions = [word for word in profession_info if word in profession_keywords]

    # make a guess:
    profession_guess = input(f"\nWhat is the profession of {name}, why are they famous? (Seperate with ',')\n")
    guesses = [guess.strip().lower() for guess in profession_guess.split(',')]

    for guess in guesses:
        if guess in professions:
            print(f"Correct! {guess.upper()} is a profession of {name}! You get 10 Points!")
            points += 10
        else:
            print(f"{guess} is no profession. Sorry!")

    return points


def main():

    # get all countries, us_states and professions:
    countries = get_countries('world-countries.json')
    us_states = get_us_states('us-states.json')
    profession_keywords = get_professions('professions.json')

    #Game Start: Print Welcome Text, Rules, etc...
    # get_random_person():
    random_person = get_random_person(candidate_list_full)

    print(f"\nWelcome to VickyCrush! Your Random Person is: {random_person[0].upper()}")

    points = 0
    #Q1: Birth Date
    points = get_answer_1(points, random_person)

    #Q2: Birth Location
    points = get_answer_2(points, random_person, countries, us_states)

    #Q3: Profession/Fame
    points = get_answer_3(points, random_person, profession_keywords)
    print(f"Your Total Score is: {points}\n")


if __name__ =="__main__":
    main()

# switch language to english?
# limited to 4-digit birth year
# limited to the use of lists to find birth location.
