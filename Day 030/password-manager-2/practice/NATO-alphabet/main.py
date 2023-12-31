import pandas

nato_df = pandas.read_csv("Day 030/password-manager-2/practice/NATO-alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()