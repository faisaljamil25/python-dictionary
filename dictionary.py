import json

from difflib import get_close_matches  # for close matches

data = json.load(open("data.json"))

print('DICTIONARY USING PYTHON')


def translate(word):
    word = word.lower()
    if word in data:
        print(word.capitalize())
        return data[word]

    # if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:
        print(word.capitalize())
        return data[word.title()]

    # if user entered "texas" this will check for "TEXAS" as well.
    elif word.upper() in data:
        print(word.upper())
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())):         # does not execute for empty list
        match = get_close_matches(word, data.keys())[0]
        reply = input(
            f"Do you mean '{match}' instead? Enter Y if yes, or N if no: ")
        if reply == 'Y':
            print(match.upper())
            return data[match]
        else:
            return 'We didn\'t understand your entry.'

    else:
        return 'The word doesn\'t exist. Please double check it.'


word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
