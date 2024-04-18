#random phone number generator

import random
print("#AVS Random Phone Number Generator!")

randomcharacters = "1234567890"
randomfirstdigit = "6789"
number_of_phonenumbers = int(input("How Many Phone Numbers are You wanted to generated : "))
characters_of_phonenumbers = 10

print("Here are Your Random Phone Numbers :-")
for x in range(number_of_phonenumbers):
    phonenumbers = ""
    for characters in range(characters_of_phonenumbers):
        if characters == 0:
            print(random.choice(randomfirstdigit),end="")
        else:
            phonenumbers = phonenumbers + random.choice(randomcharacters)
    print(phonenumbers)
