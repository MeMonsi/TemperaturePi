from flask import Flask, render_template, Response
from time import sleep, strftime, time
from datetime import datetime
from src.TemperatureSlave import TemperatureSlave
import json
import random

app = Flask(__name__)
slave = TemperatureSlave()
random.seed()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/DummyTemperatureSlave')
def DummyTemperatureSlave(): 
    return str(slave.ReadTemperature())

@app.route('/chart-data')
def chart_data():
    def generate_random_data():        
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': slave.ReadTemperature()})
            yield f"data:{json_data}\n\n"
            sleep(10)

    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
