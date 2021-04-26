from PIL import Image, ImageDraw, ImageFont, ImageColor
from imgbb import post_image
import os

# Constants
dark_bg = ImageColor.getrgb("#36393f")
dark_text = ImageColor.getrgb("#dcddde")
whitney = ImageFont.truetype('./whitney/whitneymedium.otf', 40) #16

fly = Image.open('./pranks/fly.png')
fly.thumbnail((100, 100),Image.ANTIALIAS)

dark_fly = Image.open('./pranks/dark_fly.jpg')
width, height = dark_fly.size
dark_fly.resize((width*2, height*2))

def generate_image(message1='Hello world!', message2='Hello from mars!', prank=fly, color_scheme='dark'):
    try:
        # Create new background
        background = Image.new('RGB', (1000, 110), color=dark_bg)
        d = ImageDraw.Draw(background)
        # Overlay the text
        d.text((0, 0), message1, font=whitney, fill=dark_text)
        d.text((0, 65), message2, font=whitney, fill=dark_text)

        # Set offset and paste
        # third param used to indicate transparency mask
        offset = (800, 0)
        background.paste(dark_fly.resize((width*2, height*2)), offset)
        background.save('./output/output.png')
        try:
            url = post_image('./output/output.png')
            os.remove('./output/output.png')
            
            return url
        except Exception as e:
          return ("An error occured while uploading your image" + str(e))
    except Exception as e:
        return ("An error occured while generating your image\n" + str(e))
