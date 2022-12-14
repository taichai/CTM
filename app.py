from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, myDocker!<br>This is version3.2'

if __name__== '__main__':
    app.run(host="0.0.0.0", port=7070, threaded=True, debug=True)


