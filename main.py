import json

def read_sentence():
    sentence_input = input("Please type the word: ")
    language_input = input("Please specify the language: ") or "ger"
    return sentence_input, language_input


def write_phonetic_alphabet(sentence_input: str, language_input: str):
    with open(f'./alphabets/{language_input.lower()}.json') as f:
        data = json.load(f)
    words = sentence_input.split(" ")
    for word in words:
        print(f"{word}:\t", end=" ")
        for character in word:
            if character.upper() in data['alphabet'].keys():
                print(data['alphabet'][character.upper()], end=" ")
        print("\r")



if __name__ == '__main__':
    sentence, language = read_sentence()
    write_phonetic_alphabet(sentence, language)
