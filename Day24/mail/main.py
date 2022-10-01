# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# get names
with open("Input/Names/invited_names.txt") as name_file:
    names = list(map(lambda s: s.strip(), name_file.readlines()))

# make letter
NAME_FORMAT = "[name]"
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    for name in names:
        new_letter = letter.replace(NAME_FORMAT, name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(new_letter)
