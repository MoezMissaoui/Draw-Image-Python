
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import random

class OpenGraphImage:
	# PATH where images will saved
	PATH_imgs = os.path.join('assets', 'tmp')
	# List of colors for background images
	colors = ['#18BC9C', '#2C3E50', '#873600', '#4A235A', '#17202A', '#6C3483', '#B7950B', '#C0392B', '#186A3B', '#FFCC00', '#FF99CC', '#CC6699', '#FF0000', '#66CC99', '#33FF00', '#006699', '#669966']
	

	# Constructor
	def __init__(self, image_title, image_text):

		# Take the image name
		image_name = self.get_image_name()

		# save the image location in instance variable 'location'
		self.location = self._location(image_name)

		# Create a background image
		background = self.base()

		# Print the title on the background
		self.print_on_img(background, image_title.capitalize(), 70, 50)

		# Cut the text to sentences
		sentences = textwrap.wrap(image_text, width=60)
		# Print the sentences on the background
		current_h, pad = 180, 10
		for sentence in sentences:
			w, h = self.print_on_img(background, sentence, 40, current_h)
			current_h += h + pad

		# Save the image to PATH where images will saved 
		background.save(self._path(image_name), quality=90)


	# The base() function create image with size w,h=1500,1400 and take color of background randomly from the list of colors
	def base(self):
		img = Image.new('RGB', (1350, 1150), random.choice(self.colors))
		img = img.resize((1350, 1150), Image.ANTIALIAS)
		return img


	# The print_on_img() function print text & title on the image with Arcon-Regular font and white color of text and fixe the position to middle of image
	def print_on_img(self, img, text, size, height):
		font = ImageFont.truetype(os.path.join( 'assets', 'fonts', 'Arcon-Regular.otf'), size)
		draw = ImageDraw.Draw(img)
		w,h = draw.textsize(text,font)
		position = ((img.width - w) / 2 , height)
		draw.text(position, text, (255,255,255), font=font)
		#return the position of text (width, height)
		return (w, h)


	# The _path() function return the PATH where image will saved
	def _path(self, image_name):
		return os.path.join(self.PATH_imgs, '{}.jpg'.format(image_name))


	# The _location() function return the PATH where image saved
	def _location(self, image_name):
		return self.PATH_imgs+'\\{}.jpg'.format(image_name)


	# The get_image_name() function check the existance of random name (sequence of 15 digits) in the directory of saving. If existe take an other random name
	def get_image_name(self):

		# existfiles = list(filter(lambda file : os.path.isfile(os.path.join(self.PATH_imgs, file)) , os.listdir(self.PATH_imgs) ))
		existfiles = [file for file in os.listdir(self.PATH_imgs) if os.path.isfile(os.path.join(self.PATH_imgs, file)) ]
		
		# existfiles = list(map(lambda file : os.path.splitext(file)[0] , existfiles ))
		existfiles = [os.path.splitext(file)[0] for file in existfiles]

		image_name = str(random.randrange(100000000000000,999999999999999))
		while image_name in existfiles  :
			image_name = str(random.randrange(100000000000000,999999999999999))

		return image_name





# Exemple:
image_title = "Lorem Ipsum"
image_text = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker."
image = OpenGraphImage(image_title, image_text)
print(image.location)

