import re
import random
import cowsay
from colorama import Fore, Back, Style, init
# Initialize colorama
init()
# # Print colored text
# print(Fore.RED + "This is red text.")
# print(Fore.GREEN + "This is green text.")
# print(Back.YELLOW + "This text has a yellow background.")
# print(Style.BRIGHT + "This is bright text.")
# print(Style.RESET_ALL + "This resets all styles.")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT)
# ----- above for colors --------------------

import requests
from bs4 import BeautifulSoup
import wikipedia
import warnings
import re
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")



def get_x_amount_wiki_people():

    # Define the URL
    # url = "https://de.wikipedia.org/w/index.php?limit=500&offset=0&profile=default&search=famous+people&title=Spezial:Suche&ns0=1"
    url = "https://de.wikipedia.org/w/index.php?limit=500&offset=500&profile=default&search=famous+people&title=Spezial:Suche&ns0=1"
    # Send a GET request to the URL
    response = requests.get(url)

    potential_wiki_cadidate = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for all search result links
        links = soup.find_all('a', href=True)

        # Loop through each link and check if it contains a valid Wikipedia article
        for link in links:
            href = link['href']

            # Filter out non-article links
            if href.startswith('/wiki/') and not href.startswith('/wiki/Spezial:'):
                # Build the full URL
                full_link = "https://de.wikipedia.org" + href
                title = link.get_text(strip=True)  # Get the link text (title)

                # Print the title and link
                # print(f"Title: {title}, Link: {full_link}")

                print(f"{title}_______{href[6:]}")
                name_surname = title.split(" ")
                href_name_surname = href[6:].split("_")
                try:
                    if len(name_surname) < 4 and name_surname[0] == href_name_surname[0] and name_surname[1] == \
                            href_name_surname[1]:
                        potential_wiki_cadidate.append(title)
                except IndexError:
                    pass



    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    # print(potential_wiki_cadidate)

    return potential_wiki_cadidate

def get_all_answers_keywords(candidate_list_full):
    """
    The function creates a KEYWORD_List for the Answers
    :param summary
    :return:
    answer_3_keywords
    """
    person_count = 0
    for x in range(len(candidate_list_full)):
        person = candidate_list_full[x][0]
        birth_data = candidate_list_full[x][1].split("in ")

        birth_date = birth_data[0]
        try:
            birth_town = birth_data[1]
        except IndexError:
            birth_town = "t.b.a"

        profession_info = candidate_list_full[x][2]

        person_count += 1
        if person_count == 250:
            break

        print(f"\n--> {person_count}. {person} <--")



        # QUESTION 1
        print(f"QUESTION 1:\n(correct YEAR: 100 points / correct CENTURY:  50 points)\nWhen was {person} born?\nAnswer (keywords): {birth_date}")

        # # QUESTION 2
        print(f"\nQUESTION 2:\n(correct TOWN: 100 points / correct COUNTRY:  50 points)\nWhat was {person} birth Town?\nAnswer (keywords): {birth_town}")

        # # QUESTION 3
        splitted_profession_info = profession_info.split(" ")
        professions = []
        for word in splitted_profession_info:
            if len(word) > 4:
                professions.append(word)

        print(f"\nQUESTION 3:\n(2 correct KEYWORDS: 100 points / 1 correct KEYWORD:  50 points)\nWhat was {person} known for ?\nAnswer (keywords): {professions}")


def get_birth_info_and_sentence(url_list):
    candidate_list_full = []
    candidate_birth_town_profession = []

    for url in url_list:

        # Define the URL for German Wikipedia
        # url = "https://de.wikipedia.org/wiki/Melchior_Ndadaye"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for paragraphs that might contain the birth info and the name
            paragraphs = soup.find_all('p')

            birth_info = None
            full_sentence_after_birth = None
            person_name = None

            for paragraph in paragraphs:
                text = paragraph.get_text()

                # Look for the birth info pattern and name before the bracket (e.g., Kate Garry Hudson (* 19. April 1979 in Los Angeles, Kalifornien))
                birth_info_match = re.search(r'([A-Za-zäöüß]+(?: [A-Za-zäöüß]+)*) \(\* (.*?)\)', text)
                if birth_info_match:
                    person_name = birth_info_match.group(1)  # Capture the name before the bracket
                    birth_info = birth_info_match.group(2)  # Capture the birth info in the bracket

                    # Extract the full sentence after the birth info (after the closing parenthesis)
                    remaining_text = text.split(')', 1)[1].strip()
                    if remaining_text:
                        full_sentence_after_birth = remaining_text.split('.')[0].strip()  # Extract full sentence until the first period

                    break  # Stop searching after finding the birth info and the sentence


            # Print the extracted information
            if person_name:
                # print(f"Name: {person_name}")
                candidate_birth_town_profession.append(person_name)
            else:
                # print("Name not found.")
                a = 1
            if birth_info:
                # print(f"Birth Info: {birth_info}")
                candidate_birth_town_profession.append(birth_info)
            else:
                # print("Birth Info not found.")
                a = 0
            if full_sentence_after_birth:
                # print(f"Full Sentence after birth info: {full_sentence_after_birth}")
                candidate_birth_town_profession.append(full_sentence_after_birth)
            else:
                # print("Follow-up sentence not found.")
                a = 2

        else :
            a = 5
            # print(f"Failed to retrieve the page. Status code: {response.status_code}")

        if len(candidate_birth_town_profession) == 3:
            candidate_list_full.append(candidate_birth_town_profession)

        candidate_birth_town_profession = []

    return candidate_list_full

def get_xxxx_amount_wiki_people():

    # Define the URL
    url = "https://de.wikipedia.org/w/index.php?limit=50&offset=0&profile=default&search=famous+people&title=Spezial:Suche&ns0=1"

    url_list = []
    # Send a GET request to the URL
    response = requests.get(url)

    potential_wiki_cadidate = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for all search result links
        links = soup.find_all('a', href=True)

        # Loop through each link and check if it contains a valid Wikipedia article
        for link in links:
            href = link['href']

            # Filter out non-article links
            if href.startswith('/wiki/') and not href.startswith('/wiki/Spezial:'):
                # Build the full URL
                full_link = "https://de.wikipedia.org" + href
                title = link.get_text(strip=True)  # Get the link text (title)

                # Print the title and link
                # print(f"Title: {title}, Link: {full_link}")
                url_list.append(full_link)

                # print(f"{title}_______{href[6:]}")
                name_surname = title.split(" ")
                href_name_surname = href[6:].split("_")
                try:
                    if len(name_surname) < 4 and name_surname[0] == href_name_surname[0] and name_surname[1] == \
                            href_name_surname[1]:
                        potential_wiki_cadidate.append(title)
                except IndexError:
                    pass



    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    # print(potential_wiki_cadidate)

    return url_list


def main():
    head_line = f"\t\t\t{'*' * 10} WELCOME TO THE VICKY CRUSHES GAME {'*' * 10}"
    length_head_line = len(head_line)
    print(f"\t\t\t{'*' * length_head_line}\n{head_line}\n\t\t\t{'*' * length_head_line}")
    user_input = input("\t\t\t   Pass your name and hit Enter to enter the game mode \n").upper()
    cowsay.ghostbusters(f"HELLO {user_input}\nPlease read\ninstructions\ncarefully!!!")
    print()
    print_note_ghost = ("\n\t\t\t\t\tTHE GAME WILL RANDOMLY PICK A CELEBRITY."
                  "\n\t\t\t  YOU HAVE TO ANSWER 3 QUESTIONS ABOUT THE CELEBRITY."
                  "\n\t\tYOU GET POINTS FOR EACH RIGHT ANSWER WHICH WILL SHOW AT THE END."
                  "\n\t\t  EACH QUESTION HAS A SLIGHTLY DIFFERENT POINTING SYSTEM."
                )
    print(print_note_ghost)
    input(f"\n\t\t\t\t\tPress Enter if you are good to go\n")
    cowsay.kitty(f"{user_input}\nget ready\nto answer the\nfirst question")
    print_note_cat_1 = ("\n\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH YEAR\n"
                  "\n\t\t\t  If you get the correct year you get 20 points."
                  "\n\t\tIf you guess within a range of 25 years + /- you get 10 points."
                  "\n\t\tIf you guess within a range of 50 years + / - you get 5 points."
                  )
    print(print_note_cat_1)
    input("\n\t\t\t\t\tPress Enter for the next question\n")

    cowsay.stegosaurus(f"{user_input}\nget ready\nto answer the\nsecond question")
    print_note_steg_2 = ("\n\t\t\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH PLACE\n"
                      "\n\t\t\t\t\t  If you get the correct city you get 20 points."
                      "\n\t\t\t\t\tIf you guess correct country you get 10 points."
                      )

    print(print_note_steg_2)
    input("\n\t\t\t\t\t\t\tPress Enter for the next question\n")
    cowsay.turtle(f"{user_input}\nget ready\nto answer the\nthird question")
    print_note_turtle_3 = ("\n\t\t\t\t\t\t\t\t\tGUESS THE CELEBRETY'S OCCUPATION\n"
                      "\n\t\t\t\t\t\t\t  If you get the correct occupation you get 20 points."
                      )

    print(print_note_turtle_3)
    input("\n\t\t\t\t\t\t\t\t\tPress Enter to see the final score\n")


    url_list = get_xxxx_amount_wiki_people()
    candidate_list_full = get_birth_info_and_sentence(url_list)

    # below a file to work with ...50 entries... takes too long to load , so saved as constante
    # candidate_list_full = [['Mary Kathleen Turner', '19. Juni 1954 in Springfield, Missouri', 'ist eine US-amerikanische Schauspielerin, die ihre größten Filmerfolge in den 1980er-Jahren hatte'], ['Mary Kathleen Turner', '19. Juni 1954 in Springfield, Missouri', 'ist eine US-amerikanische Schauspielerin, die ihre größten Filmerfolge in den 1980er-Jahren hatte'], ['Tamara Taylor', '27. September 1970 in Toronto, Ontario', 'ist eine kanadische Schauspielerin'], ['Tamara Taylor', '27. September 1970 in Toronto, Ontario', 'ist eine kanadische Schauspielerin'], ['OBE', '7. Juni 1974 in Donaghadee,[1][2] Nordirland', 'ist ein britischer Dokumentarfilmer, Abenteurer, TV-Moderator, Survival-Ausbilder, Pfadfinderleiter, Autor und ehemaliger SAS-Soldat'], ['OBE', '7. Juni 1974 in Donaghadee,[1][2] Nordirland', 'ist ein britischer Dokumentarfilmer, Abenteurer, TV-Moderator, Survival-Ausbilder, Pfadfinderleiter, Autor und ehemaliger SAS-Soldat'], ['Cariba Heine', '1. Oktober 1988 in Johannesburg, Südafrika', 'ist eine australische Schauspielerin und Tänzerin'], ['Cariba Heine', '1. Oktober 1988 in Johannesburg, Südafrika', 'ist eine australische Schauspielerin und Tänzerin'], ['Daniels', '19. Februar 1955 in Athens, Georgia', 'ist ein US-amerikanischer Schauspieler'], ['Daniels', '19. Februar 1955 in Athens, Georgia', 'ist ein US-amerikanischer Schauspieler'], ['Lola Van Wagenen', '19. Dezember 1938 in Provo, Utah, Vereinigte Staaten', 'ist eine US-amerikanische Historikerin und Aktivistin'], ['Jeffrey Edward Epstein', '20. Januar 1953 in New York City; † 10. August 2019 ebenda', 'war ein US-amerikanischer Investmentbanker und verurteilter Sexualstraftäter'], ['Jeffrey Edward Epstein', '20. Januar 1953 in New York City; † 10. August 2019 ebenda', 'war ein US-amerikanischer Investmentbanker und verurteilter Sexualstraftäter'], ['Cynthia Ann Parker', 'zwischen 1825 und 1827 wohl im Crawford County,[1] Illinois; † 1870 ebenda', '[2] war die älteste Tochter der Siedler Silas Mercer Parker und Lucy (Duty) Parker'], ['Cynthia Ann Parker', 'zwischen 1825 und 1827 wohl im Crawford County,[1] Illinois; † 1870 ebenda', '[2] war die älteste Tochter der Siedler Silas Mercer Parker und Lucy (Duty) Parker'], ['Künstlername von Danielle Schoovaerts', '1. Januar 1953[2][3] in Brüssel[4]', 'ist eine belgische Sängerin'], ['Künstlername von Danielle Schoovaerts', '1. Januar 1953[2][3] in Brüssel[4]', 'ist eine belgische Sängerin'], ['Jon Stewart', '28. November 1962 in New York City als Jonathan Stuart Leibowitz', 'ist ein US-amerikanischer Komiker, Schauspieler, Schriftsteller, Produzent und Regisseur'], ['Jon Stewart', '28. November 1962 in New York City als Jonathan Stuart Leibowitz', 'ist ein US-amerikanischer Komiker, Schauspieler, Schriftsteller, Produzent und Regisseur'], ['geborene Donner', '26. Dezember 1855', 'und dessen späterer Ehefrau Agnes, geborene Donner (* 26'], ['geborene Donner', '26. Dezember 1855', 'und dessen späterer Ehefrau Agnes, geborene Donner (* 26'], ['Lucy Elizabeth Fry', '13. März 1992 in Brisbane, Queensland', 'ist eine australische Schauspielerin'], ['Lucy Elizabeth Fry', '13. März 1992 in Brisbane, Queensland', 'ist eine australische Schauspielerin'], ['Rodney Alcala', '23. August 1943 in San Antonio, Texas; † 24. Juli 2021 in Corcoran, Kalifornien[1]; gebürtig: Rodrigo Jacques Alcala-Buquor', 'war ein US-amerikanischer verurteilter Serienmörder'], ['Rodney Alcala', '23. August 1943 in San Antonio, Texas; † 24. Juli 2021 in Corcoran, Kalifornien[1]; gebürtig: Rodrigo Jacques Alcala-Buquor', 'war ein US-amerikanischer verurteilter Serienmörder'], ['Ruby Rose Turner', '16. Oktober 2005 in Los Angeles, Kalifornien, USA', 'ist eine US-amerikanische Schauspielerin, Sängerin und Tänzerin'], ['Kate Garry Hudson', '19. April 1979 in Los Angeles, Kalifornien', 'ist eine US-amerikanische Schauspielerin'], ['Kate Garry Hudson', '19. April 1979 in Los Angeles, Kalifornien', 'ist eine US-amerikanische Schauspielerin'], ['Andreas Apergis', 'vor 1988 in Kanada', 'ist ein kanadischer Schauspieler'], ['Snowden', '21. Juni 1983 in Elizabeth City, North Carolina', '[1] ist ein US-amerikanisch-russischer Whistleblower'], ['Snowden', '21. Juni 1983 in Elizabeth City, North Carolina', '[1] ist ein US-amerikanisch-russischer Whistleblower'], ['Pino Palladino', '17. Oktober 1957 in Cardiff, Wales', 'ist ein walisischer Bassist italienischer Abstammung'], ['Pino Palladino', '17. Oktober 1957 in Cardiff, Wales', 'ist ein walisischer Bassist italienischer Abstammung'], ['Gareth L John Forwood', '14. Oktober 1945; † 16. Oktober 2007', '[1] war ein britischer Schauspieler'], ['Allen Payne', '7. Juli 1968 in New York City als Allen Roberts', 'ist ein US-amerikanischer Schauspieler'], ['Jacqueline Erika Tham', '15. Dezember 1999 in Singapur', '[1] ist eine singapurisch-kanadische[2][3] Schauspielerin'], ['Jacqueline Erika Tham', '15. Dezember 1999 in Singapur', '[1] ist eine singapurisch-kanadische[2][3] Schauspielerin'], ['Baron Jean Baptiste Joseph Fourier', '21. März 1768 bei Auxerre; † 16. Mai 1830 in Paris', 'war ein französischer Mathematiker und Physiker'], ['Baron Jean Baptiste Joseph Fourier', '21. März 1768 bei Auxerre; † 16. Mai 1830 in Paris', 'war ein französischer Mathematiker und Physiker'], ['Gould', '27. Mai 1836 in Roxbury, New York; † 2. Dezember 1892 in New York City', 'war ein US-amerikanischer Anleger und Unternehmer'], ['Gould', '27. Mai 1836 in Roxbury, New York; † 2. Dezember 1892 in New York City', 'war ein US-amerikanischer Anleger und Unternehmer'], ['Frances Louise McDormand', '23. Juni 1957 in Chicago, Illinois als Cynthia Ann Smith', 'ist eine US-amerikanische Schauspielerin'], ['Frances Louise McDormand', '23. Juni 1957 in Chicago, Illinois als Cynthia Ann Smith', 'ist eine US-amerikanische Schauspielerin'], ['Melchior Ndadaye', '28. März 1953 in Mwaro; † 21. Oktober 1993 in Bujumbura', 'war der erste gewählte Präsident Burundis'], ['Melchior Ndadaye', '28. März 1953 in Mwaro; † 21. Oktober 1993 in Bujumbura', 'war der erste gewählte Präsident Burundis'], ['Ying Fusu', '3. Jahrhundert v. Chr.; † 210 v. Chr.', 'war der älteste Sohn des chinesischen Kaisers Qin Shihuangdi und dessen designierter Erbe'], ['Lauren Hays', '21. Mai 1968 in Fairfax, Virginia als Laura Lynn Thorsen', 'ist eine US-amerikanische Schauspielerin und Moderatorin'], ['Luciana Zogbi', '27. Oktober 1994 in São Paulo, Brasilien', 'ist eine brasilianisch-libanesische Sängerin, Songwriterin und Musikerin']]

    get_all_answers_keywords(candidate_list_full)
    print(candidate_list_full)

if __name__ == "__main__":
    main()
