from flask import Flask, render_template, Response, request, session
from time import sleep, strftime, time
from datetime import datetime
import src.database_tools
from src.entities.Temperature import Temperature
from src.TemperatureSlave import TemperatureSlave
from src.database_tools.TemperatureDataService import TemperatureDataService
from src.database_tools.GlobalSettingsAdapter import GlobalSettingsAdapter
import json
import random

app = Flask(__name__)
app.secret_key = 'key'

slave = TemperatureSlave()
globalSettingsAdapter = GlobalSettingsAdapter()
dataService = TemperatureDataService()
random.seed()

@app.route('/', methods= ['GET', 'POST'])
def index():    
    if request.method == "POST":
        req_data = request.get_json()
        globalSettingsAdapter.SetIsStoringEnabled(req_data['value'])              
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
            isStoringEnabled = globalSettingsAdapter.GetIsStoringEnabled()            
            if(isStoringEnabled):
                dataService.Save(temperature)
            sleep(10)

    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
