from flask import Flask, request, render_template
import image_gen
import random
from pathlib import Path


app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    message1 = request.args.get("message1", "")
    message2 = request.args.get("message2", "")
    if message1:
        link = image_gen.generate_image(message1=message1, message2=message2, prank='fly', color_scheme='dark')
        # html = ("<a href=%s>%s</a>" % (link, link))
    else:
        # html = ''
        link = ''
    return render_template('index.html', link=link)
    # return ("""<form action="" method="get">
    #                 <p>Message 1</p>
    #                 <input type="text" name="message1">
    #                 <p>Message 2</p>
    #                 <input type="text" name="message2">
    #                 <input type="submit" value="Generate">
    #               </form>"""
    # + link)


if __name__ == "__main__":
  Path("./output/").mkdir(parents=True, exist_ok=True)
  app.run(
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)
