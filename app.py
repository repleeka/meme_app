from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    top_text = request.form['top_text']
    bottom_text = request.form['bottom_text']

    img = Image.open('static/meme.jpg')
    draw = ImageDraw.Draw(img)
    font_path = "arial.ttf"  # Change this path to your font file
    font = ImageFont.truetype(font_path, size=40)

    draw.text((10, 10), top_text, fill='white', font=font)
    draw.text((10, img.height - 60), bottom_text, fill='white', font=font)

    meme_path = f'static/{top_text[:5]}_{bottom_text[:5]}.jpg'
    img.save(meme_path)

    return render_template('result.html', meme_path=meme_path)


if __name__ == '__main__':
    app.run(debug=True)
