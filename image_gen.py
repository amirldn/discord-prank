# Imports
from PIL import Image, ImageDraw, ImageFont, ImageColor
from image_hosts.imgur import post_image
import os
from datetime import datetime

# Constants
dark_bg = ImageColor.getrgb("#36393f")
dark_text = ImageColor.getrgb("#dcddde")
whitney = ImageFont.truetype('./assets/fonts/whitney/whitneymedium.otf', 40) #16

fly = Image.open('./assets/pranks/fly.png')
fly.thumbnail((100, 100),Image.ANTIALIAS)

dark_fly = Image.open('./assets/pranks/dark_fly.jpg')
width, height = dark_fly.size
dark_fly.resize((width*2, height*2))

# Functions
def generate_image(message1='Hello world!', message2='Hello from mars!', prank=fly, color_scheme='dark'):
    try:
        # Create new background
        background = Image.new('RGB', (1000, 115), color=dark_bg)
        d = ImageDraw.Draw(background)
        # Overlay the text
        d.text((0, 0), message1, font=whitney, fill=dark_text)
        d.text((0, 65), message2, font=whitney, fill=dark_text)

        # Set offset and paste
        # third param used to indicate transparency mask
        offset = (800, 0)
        background.paste(dark_fly.resize((width*2, height*2)), offset)
        filename = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        background.save("./output/{}.png".format(filename))
        try:
            url = post_image("./output/{}.png".format(filename))
            os.remove("./output/{}.png".format(filename))
            return url
        except Exception as e:
          return ("An error occured while uploading your image" + str(e))
    except Exception as e:
        return ("An error occured while generating your image\n" + str(e))
