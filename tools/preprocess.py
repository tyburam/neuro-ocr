from scipy import misc
import numpy as np

CHAR_VECTOR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789 "
letters = [letter for letter in CHAR_VECTOR]


def process_images(file_paths):
    images = [misc.imread(path).transpose((1, 0, 2)) for path in file_paths]
    images = np.asarray(images)
    return images / 255


def process_labels(labels):
    new_labels = []
    for lab in labels:
        new_one = make_label(lab)
        while len(new_one) < 11:
            new_one.append(letters.index(' '))
        new_labels.append(new_one)
    return new_labels


def make_label(text):
    return list(map(lambda x: letters.index(x), text))
