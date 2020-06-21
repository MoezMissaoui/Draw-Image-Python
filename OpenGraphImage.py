
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import random

class OpenGraphImage:
	PATH_imgs = os.path.join('assets', 'tmp')
	colors = ['#18BC9C', '#2C3E50', '#873600', '#4A235A', '#17202A', '#6C3483', '#B7950B', '#C0392B', '#186A3B', '#FFCC00', '#FF99CC', '#CC6699', '#FF0000', '#66CC99', '#33FF00', '#006699', '#669966']
	def __init__(self, image_title, image_text):
		image_name = self.get_image_name()
		self.location = self._location(image_name)
		background = self.base()
		self.print_on_img(background, image_title.capitalize(), 70, 50)
		sentences = textwrap.wrap(image_text, width=60)
		current_h, pad = 180, 10
		for sentence in sentences:
			w, h = self.print_on_img(background, sentence, 40, current_h)
			current_h += h + pad
		background.save(self._path(image_name), quality=90)

	def base(self):
		img = Image.new('RGB', (1500,1400), random.choice(self.colors))
		img = img.resize((1500,1400), Image.ANTIALIAS)
		return img


	def print_on_img(self, img, text, size, height):
		font = ImageFont.truetype(os.path.join( 'assets', 'fonts', 'Arcon-Regular.otf'), size)
		draw = ImageDraw.Draw(img)
		w,h = draw.textsize(text,font)
		position = ((img.width - w) / 2 , height)
		draw.text(position, text, (255,255,255), font=font)
		return (w, h)

	def _path(self, image_name):
		return os.path.join(self.PATH_imgs, '{}.jpg'.format(image_name))

	def _location(self, image_name):
		return self.PATH_imgs+'\\{}.jpg'.format(image_name)

	def get_image_name(self):
		existfiles = list(filter(lambda file : os.path.isfile(os.path.join(self.PATH_imgs, file)) , os.listdir(self.PATH_imgs) ))
		existfiles = list(map(lambda file : os.path.splitext(file)[0] , existfiles ))
		image_name = str(random.randrange(100000000000000,999999999999999))
		while image_name in existfiles  :
			image_name = str(random.randrange(100000000000000,999999999999999))
		return image_name



image_title = "Lorem Ipsum"
image_text = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker."
image = OpenGraphImage(image_title, image_text)
print(image.location)

