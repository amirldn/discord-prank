from flask import Flask, request, escape

import image_gen
from image_gen import *

app = Flask(__name__)

@app.route("/")
def index():
    message1 = request.args.get("message1", "")
    message2 = request.args.get("message2", "")
    if message1:
        link = image_gen.generate_image(message1=message1, message2=message2, prank='fly', color_scheme='dark')
        html = ("<a href=%s>%s</a>" % (link, link))
    else:
        html = ''
    return ("""<form action="" method="get">
                    <p>Message 1</p>
                    <input type="text" name="message1">
                    <p>Message 2</p>
                    <input type="text" name="message2">
                    <input type="submit" value="Generate">
                  </form>"""
    + html)

# @app.route("/<string:message1>,<string:message2>")
# def generate(message1='message1', message2='message2!'):
#     # message2 = request.args.get('message2', None)
#     # prank = request.args.get('prank', None)
#     # color_scheme = request.args.get('color_scheme', None)
#     # link = image_gen.generate_image(message1=message1, message2=message2, prank='fly', color_scheme='dark')
#     link = image_gen.generate_image(message1=message1, message2=message2)
#     html = ("<a href=%s>%s</a>" % (link,link))
#     # print(html)
#     return html


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
