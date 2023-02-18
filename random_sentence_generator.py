import random


def random_choice(sequence):
    return random.choice(sequence)


names = ["Georgi", "Silvia", "Maria", "Dalia", "Tea", "Leon"]
places = ["Sofia", "Stara Zagora", "Münster", "Wolfsburg", "Hanover", "Manchester"]
verbs = ["plays", "cooks", "cleans", "reads", "sleeps", "drinks"]
nouns = ["a cat", "the baby of the girl next door", "flowers", "no bier", "Python", "a knife"]
adverbs = ["happily", "honestly", "somehow", "hardly", "slowly", "loudly"]
details = ["in the kitchen", "under the table", "in the cinema", "on the bike", "in a tent", "at the see"]
more_details = ["cries", "smiles", "speaks on the phone", "smokes", "watches TV", "washes the dishes"]
more_nouns = ["better person", "doctor", "Python Web Developer", "pilot", "child again", "wine taster"]

print("Hello, this is your first random sentence:")

while True:
    random_name = random_choice(names)
    random_place = random_choice(places)
    random_verb = random_choice(verbs)
    random_noun = random_choice(nouns)
    random_adverb = random_choice(adverbs)
    random_detail = random_choice(details)
    random_more_detail = random_choice(more_details)
    random_more_noun = random_choice(more_nouns)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} with {random_noun} {random_detail} and \
{random_more_detail}... and that person dreams to become a {random_more_noun}.")
    print("Enter [go] to generate a new one.")

    command = input()
    if command != "go":
        break

