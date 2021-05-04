phone_num = input("Enter your Phone Number : ")
# output = ""
digits_in_words = {

    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Seven",
    "0": "Zero"
}

output = ""


for character in phone_num:
    output += digits_in_words.get(character, "!") + " "
print(output)
