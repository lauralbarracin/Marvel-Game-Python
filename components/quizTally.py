from components import vars
from PIL import Image


def total(value):
    if value == 300:
        vars.character = vars.characters[0]
        im = Image.open("img/Laura.jpg")
        im.show()
    elif value == 50:
        vars.character = vars.characters[1]
        im = Image.open("img/JessicaJones.jpg")
        im.show()
    elif value == 350:
        vars.character = vars.characters[2]
        im = Image.open("img/wolverine.jpg")
        im.show()
    elif value == 600:
        vars.character = vars.characters[3]
        im = Image.open("img/deadpool.jpg")
        im.show()
    print("It's" + vars.character)
    # add some emoji icons, or show the character image using the Pillow package
