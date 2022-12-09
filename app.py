from flask import Flask
from threading import Thread
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def temp():
    while True:
        print("hi")
        time.sleep(10)

if __name__ == "__main__":
    t1 = Thread(target=temp)
    t1.start()
    app.run()
