
import string

alphabet = list(string.ascii_lowercase)

leek_list = [
    4, "I3", "[", ")", 3, "|=", "&", "#", 1, ",_|", ">|", 1, "/\/\"", " ^ /", 0, " | *", "(_,)", "I2", 5, 7, "(_)", "\/ ", "\/\/", " > <", "j", 2,
]

leek_traduction = []

text_input = input("Write a text to traduce: ")

# print(text_input)

try:
    for text in text_input:
        index_alph = alphabet.index(text)
        letter_leek = leek_list[index_alph]
        leek_traduction.append(letter_leek)
except:
    print("Don't use spaces or special characters, try again")
else:
    print(leek_traduction)
finally:
    print("Finished")
