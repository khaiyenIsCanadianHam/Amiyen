from flask import Flask, render_template, request

app = Flask(__name__)
percentage = None,
rate = None,
base = None,
percentageChange = None,
percentIncrease = None,
percentDecrease = None,

@app.route('/', methods=['POST', 'GET'])
def index():
    
    return render_template('index.html')        
if __name__ == '__main__':
    app.run(debug=True)
