from data import CONVERSION_TABLE


def converter(phrase):
    output = ""
    phrase = phrase + "SK"  # signals end with SK "end of work"

    for letter in phrase.upper():
        if letter in CONVERSION_TABLE:
            output = output + CONVERSION_TABLE[letter] + "   "

    return output


while True:
    input_phrase = input("Please enter the phrase you wish to convert: ")
    print(converter(input_phrase))
