# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hallo Ramblr.ai! Ich bin ein DevSecOps Beispiel.!"

if __main__ == '__main__':
    # Wichtig: degug=False für Produktion!
    # Ein Security-Scanner würde hier meckern, wenn hier True stünde.
    app.run(debug=False)