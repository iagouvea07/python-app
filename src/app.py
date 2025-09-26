from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def hello_world():
    return jsonify(
        {
            'app': 'python-app',
            'version': '1.0.0',
            'owner': 'igor',
            'date': datetime.datetime.now().strftime('%d-%m-%Y'),
            'hostname': socket.gethostname()
        }
    )

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')