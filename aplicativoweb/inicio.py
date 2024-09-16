from gtts import gTTS
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/senia', methods=['GET', 'POST'])
def abrir_assistente():
    audio_path = None
    if request.method == 'POST':
        texto = request.form['texto']
        lingua = 'pt-br'
        tts = gTTS(text=texto, lang=lingua)
        audio_path = "static/audio_exemplo.mp3"
        tts.save(audio_path)
    return render_template('senia.html', audio_path=audio_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def logar():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    # mock de autenticação
    usuario = request.form['usuario']
    senha = request.form['senha']

    # Verificando credenciais
    if senha == '123' and usuario.lower() in ['joao', 'joão']:
        return render_template('senia.html')
    else:
        msg = 'Erro na autenticação'
        return render_template('login.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
