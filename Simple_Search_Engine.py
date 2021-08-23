# ask for inputs
text = input("give a phrase.\n")
word = input("give a word of a phrase\n")
# create function to compare inputs
def search(text, word):
    if word in text:
        return("Word found.\n")
    else:
        return("Word not found.\n")
# print the returned variables
print(search(text,word))