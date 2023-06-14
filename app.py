from flask import Flask, jsonify, render_template
import psutil
import subprocess

app = Flask(__name__)

def get_gpu_usage():
    result = subprocess.check_output("nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits", shell=True)
    gpu_usage = float(result.strip())
    return gpu_usage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/system_info')
def system_info():
    info = {
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "network_info": psutil.net_io_counters(pernic=True),
        "gpu_usage": get_gpu_usage()
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
