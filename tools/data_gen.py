import numpy as np
import pandas as pd
from pathlib import Path
from tools.img_gen import ImageGenerator
from tools.rgb import RgbColors

np.random.seed(2018)


def random_text_pos():
    return np.random.randint(10, 200), np.random.randint(10, 150)


def random_font_size():
    return np.random.randint(10, 20)


def file_name(i, msg):
    return './img/' + str(i) + '-' + msg + '.png'


class DataGenerator:
    def __init__(self):
        self.bg_colors = RgbColors.Basic
        self.font_colors = RgbColors.Basic
        self.font_colors.reverse()
        self.texts = ['Abracadabra', 'Bingo', 'Demeter', 'Fluent', 'Hello world']

    def make_images(self):
        gen = ImageGenerator()
        gen.set_font_path('/Library/Fonts')

        i = 1
        for msg in self.texts:
            for bc in self.bg_colors:
                for fc in self.font_colors:
                    if bc == fc:
                        continue
                    gen.generate((320, 240), bc)
                    gen.draw_text(random_text_pos(), msg, 'Arial.ttf', random_font_size(), fc)
                    gen.save(file_name(i, msg))
                    i += 1

    def make_csv(self):
        data = []
        i = 1
        for msg in self.texts:
            for bc in self.bg_colors:
                for fc in self.font_colors:
                    if bc == fc:
                        continue
                    ascii_msg = "-".join([str(ord(c)) for c in msg])
                    data.append((file_name(i, msg), msg, ascii_msg))
                    i += 1
        df = pd.DataFrame.from_records(data, columns=['filepath', 'message', 'ascii_msg'])
        df.to_csv('selfmade.csv')

    def generate(self):
        last_img_file = Path('./img/1200-Hello world.png')
        if not last_img_file.is_file():
            self.make_images()

        csv_file = Path('selfmade.csv')
        if not csv_file.is_file():
            self.make_csv()
