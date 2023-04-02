import csv


def fetch_words():
    with open('words.csv', newline='') as file:
        data = [row[0] for row in csv.reader(file)]

    return data

