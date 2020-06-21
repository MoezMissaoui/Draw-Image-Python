# Draw-Image-Python

Draw Image with *Python* using **Pillow**

## how it works

*OpenGraphImage* class get two parameters: *image_title* and *image_text*.
* The **size** is fixed to: w,h = 1500,1400.
* The **color** taken at random from the list of colors declared in the class.
* The **name of the image file** generated by the *get_image_name* function, the function takes a sequence of 15 digits randomly and verified if this name already taken by another file in the directory for saving images (assets \ tmp).
* There are an instance variable: **location**, to verify the path of saving.

The **image file** generated with **.jpg** extension.

**Note:** *get_image_name()* function use *list comprehensions*. Also can use *filter & map* functions to get the existing files in the directory of saving.

### Exemple

```
image_title = "Lorem Ipsum"

image_text = "Le Lorem Ipsum est simplement du faux texte employé dans 
la composition et la mise en page avant impression. 
Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, 
quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser 
un livre spécimen de polices de texte. 
Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique 
informatique, sans que son contenu n'en soit modifié. 
Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant 
des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications 
de mise en page de texte, comme Aldus PageMaker."

image = OpenGraphImage(image_title, image_text)
print(image.location)
```


## Authors
* **Moez Missaoui** - *Initial work* - [MoezMissaoui](https://github.com/MoezMissaoui)