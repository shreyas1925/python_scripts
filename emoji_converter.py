message = input(
    "> Enter the statement with :) and :( it will converted to emojis\n")
words = message.split(" ")
output = ""

emojis = {
    ":)": "😁",
    ":(": "😔"
}

for word in words:
    output += emojis.get(word, word)+" "
print(output)
