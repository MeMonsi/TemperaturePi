from flask import Flask, render_template
from time import sleep, strftime, time
from src.TemperatureSlave import TemperatureSlave

app = Flask(__name__)
tempeatureSlave = TemperatureSlave()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/DummyTemperatureSlave')
def DummyTemperatureSlave(): 
    return str(tempeatureSlave.ReadTemperature())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    