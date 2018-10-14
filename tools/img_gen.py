from PIL import Image, ImageDraw, ImageFont


class ImageGenerator:
    def __init__(self):
        self.fonts_path = ''
        self.img = None

    def set_font_path(self, path):
        self.fonts_path = path

    def generate(self, size, bg_color=(255, 255, 255)):
        self.img = Image.new('RGB', size, color=bg_color)

    def draw_text(self, position, text, fnt_name, fnt_size, fnt_color):
        fnt = ImageFont.truetype(self.fonts_path + '/' + fnt_name, fnt_size)
        d = ImageDraw.Draw(self.img)
        d.text(position, text, font=fnt, fill=fnt_color)

    def save(self, path):
        self.img.save(path)
