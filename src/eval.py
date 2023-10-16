from pathlib import Path
from nltk import word_tokenize
from textstat import textstat

import numpy as np
import os


START_TOKEN = '"comment": "'
END_TOKEN = '"'


def calc_word_length(text: str):
    """
    Calculates the word length of a text.
    """
    tokens = word_tokenize(text.lower())
    return len(tokens)


def calc_ttr(text: str):
    """
    Calculates the type-token ratio of a text.
    """
    tokens = word_tokenize(text.lower())
    types = set(tokens)
    return len(types) / len(tokens)


def eval(path: Path) -> None:
    commentaries = {k: list() for k in range(1, 5)}
    for file in os.listdir(path):
        count = 1
        with open(os.path.join(path, file), 'r') as file:
            data = file.read()

        while data.find(START_TOKEN) != -1:
            start = data.index(START_TOKEN) + len(START_TOKEN)
            end = data.index(END_TOKEN, start)
            word = data[start:end]
            data = data[end:]
            commentaries[count].append(word)
            count += 1
            if count > 4:
                count = 1

    print('Prompt', 'N', 'WL', 'FRES', 'TTR', sep='\t')
    for k in commentaries.keys():
        n = len(commentaries[k])
        word_length = np.mean([calc_word_length(x) for x in commentaries[k]])
        reading_ease = np.mean([textstat.flesch_reading_ease(x) for x in commentaries[k]])
        ttr = np.mean([calc_ttr(x) for x in commentaries[k]])
        print(k, n, np.round(word_length, 1), np.round(reading_ease, 2), np.round(ttr, 4), sep='\t')
