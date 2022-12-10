from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, myDocker3!\nThis is version3.1'

if __name__== '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)


