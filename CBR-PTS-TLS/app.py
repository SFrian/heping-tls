from flask import Flask, request, jsonify, render_template
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_ab', methods=['POST'])
def run_ab():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    command = f"ab -n 10000 -c 500 {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Extract relevant data for graphing (adjust regex as needed)
    requests_per_second = re.search(r"Requests per second:\s+(\d+\.\d+)", result.stdout)
    if requests_per_second:
        requests_per_second = float(requests_per_second.group(1))
    
    return jsonify({"requests_per_second": requests_per_second})

@app.route('/run_hping', methods=['POST'])
def run_hping():
    target = request.json.get('target')
    if not target:
        return jsonify({"error": "Target is required"}), 400

    command = f"hping3 -S -p 443 --flood {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Parse or extract results (e.g., number of packets sent)
    packets_sent = len(result.stdout.splitlines())
    
    return jsonify({"packets_sent": packets_sent})

# Add more routes for Siege, Wrk, etc.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
