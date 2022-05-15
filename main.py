alphabets = {
    "ger": {
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
}


def read_sentence():
    sentence_input = input("Please type the word: ")
    language_input = input("Please specify the language: ") or "ger"
    return sentence_input, language_input


def generate_phonetic_alphabet(sentence_input: str, language_input: str):
    result = ""
    data = alphabets[language_input]
    words = sentence_input.split(" ")
    for word in words:
        result += f"{word}:\t "
        for character in word:
            if character.upper() in data.keys():
                result += data[character.upper()] + " "
        result += "\n"
    return result


if __name__ == '__main__':
    sentence, language = read_sentence()
    generate_phonetic_alphabet(sentence, language)
