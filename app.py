from flask import Flask, render_template

app = Flask(__name__)

# Home page route — loads the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Map page route — loads the mysterious map
@app.route('/map')
def map():
    return render_template('map.html')

# Shadow Path route — loads the shadow path puzzle
@app.route('/path/shadow')
def shadow():
    return render_template('shadow.html')

# Whispering Trail route — loads the whispering trail puzzle
@app.route('/path/whisper')
def whisper():
    return render_template('whisper.html')

# Trail of Bones route — loads the trail of bones puzzle
@app.route('/path/bones')
def bones():
    return render_template('bones.html')

# Quest page — all three puzzles in one flow
@app.route('/quest')
def quest():
    return render_template('quest.html')

# Secret chamber — sliding tile puzzle
@app.route('/secret')
def secret():
    return render_template('secret.html')

# Codex page — secret code entry
@app.route('/codex')
def codex():
    return render_template('codex.html')

# Victory page — final coordinates
@app.route('/victory')
def victory():
    return render_template('victory.html')

if __name__ == '__main__':
    app.run(debug=True)
