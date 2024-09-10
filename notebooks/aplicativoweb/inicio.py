from gtts import gTTS
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    audio_path=None
    texto=request.form['texto']
    pass


