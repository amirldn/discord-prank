from PIL import Image, ImageDraw, ImageFont, ImageColor

dark_bg = ImageColor.getrgb("#36393f")
dark_text = ImageColor.getrgb("#dcddde")
whitney = ImageFont.truetype('./whitney-2-cufonfonts/whitneymedium.otf', 40) #16

img = Image.new('RGB', (1000, 100), color=dark_bg)
d = ImageDraw.Draw(img)
d.text((0, 10), "Hello world", font=whitney, fill=dark_text)

img.save('pil_text_font.png')