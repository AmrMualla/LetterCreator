#AmrMuallaLetterMailMergeLetterCreator
invitelist = []
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f:
    namelist = f.readlines()

for name in namelist:
    invitelist.append(name.replace("\n", ""))

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in invitelist:
        specific_letter = letter_contents.replace(PLACEHOLDER, name)

        with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as finished_letter:
            finished_letter.write(specific_letter)
