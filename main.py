#!/usr/bin/env python3
import numpy as np
import pandas as pd
from scipy import misc
from networks.ocr1 import OcrNetwork1
from tools.data_gen import DataGenerator
from tools.preprocess import process_labels

print('Start')
generator = DataGenerator()
generator.generate()

net = OcrNetwork1()

df = pd.read_csv('selfmade.csv')
labels = process_labels(list(df['message'].values))
print(len(labels))
print(len(labels[0]))

images = [misc.imread(path).transpose((1, 0, 2)) for path in list(df['filepath'].values)]
images = np.asarray(images)
images = images / 255

net.train(images, labels)
print(net.evaluate(images, labels))
