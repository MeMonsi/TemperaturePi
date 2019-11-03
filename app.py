from flask import Flask, render_template, Response
from time import sleep, strftime, time
from datetime import datetime
import src.database_tools
from src.entities.Temperature import Temperature
from src.TemperatureSlave import TemperatureSlave
from src.database_tools.TemperatureDataService import TemperatureDataService
import json
import random

app = Flask(__name__)
slave = TemperatureSlave()
dataService = TemperatureDataService()
random.seed()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/DummyTemperatureSlave')
def DummyTemperatureSlave(): 
    temperature = slave.ReadTemperature()
    return str(temperature.Value)

@app.route('/chart-data')
def chart_data():
    def generate_random_data():        
        while True:
            temperature = slave.ReadTemperature()
            json_data = json.dumps(
                {'time': temperature.TimeStamp.strftime('%H:%M:%S'), 'value': temperature.Value})
            yield f"data:{json_data}\n\n" 
            dataService.Save(temperature)
            sleep(10)

    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
