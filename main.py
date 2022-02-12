from flask import Flask, request, render_template
import image_gen
# import random
from random import randint
from pathlib import Path
from replit import db
import logging
    


app = Flask(__name__, template_folder='template')
count = int(db["gen_count"])


@app.route("/")
def index():
  global count
  message1 = request.args.get("message1", "")
  message2 = request.args.get("message2", "")
  if message1:
      link = image_gen.generate_image(message1=message1, message2=message2, prank='fly', color_scheme='dark')
      count += 1
      db["gen_count"] = str(count)
  else:
      link = ''
  return render_template('index.html', link=link, count=count)


if __name__ == "__main__":
  Path("./output/").mkdir(parents=True, exist_ok=True)
  logging.basicConfig(filename='info.log',level=logging.INFO)
  app.run(
		host='0.0.0.0',
		port=randint(2000, 9000),
    debug=False
	)
