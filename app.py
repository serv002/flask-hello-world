from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def temp():
    print("hi")

if __name__ == "__main__":
    t1 = Thread(target=temp)
    t1.start()
    app.run()
