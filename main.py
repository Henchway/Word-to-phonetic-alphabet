# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

alphabet = {
    "A": "Anton",
    "Ä": "Ärger",
    "B": "Berta",
    "C": "Cäsar",
    "D": "Dora",
    "E": "Emil",
    "F": "Friedrich",
    "G": "Gustav",
    "H": "Heinrich",
    "I": "Ida",
    "J": "Julius",
    "K": "Konrad",
    "L": "Ludwig",
    "M": "Martha",
    "N": "Nordpol",
    "O": "Otto",
    "Ö": "Österreich",
    "P": "Paula",
    "Q": "Quelle",
    "R": "Richard",
    "S": "Siegfried",
    "ß": "scharfes S",
    "T": "Theodor",
    "U": "Ulrich",
    "Ü": "Übel",
    "V": "Viktor",
    "W": "Wilhelm",
    "X": "Xanthippe / Xaver",
    "Y": "Ypsilon",
    "Z": "Zürich / Zeppelin"
}


def read_word():
    word = input("Please type the word: ")
    return word


def write_phonetic_alphabet(word: str):
    for character in word:
        if character in alphabet.keys():
            print(alphabet[character])
        else:
            print("\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word = read_word()
    write_phonetic_alphabet(word)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
