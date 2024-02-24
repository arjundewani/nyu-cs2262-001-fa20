from flask import Flask
from datetime import datetime

app = Flask(__name__)  # Corrected from _name_ to __name__

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    # Returns the current time in a string format
    return datetime.now().strftime("%H:%M:%S")
    
if __name__ == '__main__':  # Corrected from _name_ == '__main__'
    app.run(host='0.0.0.0', port=8080, debug=True)
