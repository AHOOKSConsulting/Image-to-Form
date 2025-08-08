from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'OK', 'message': 'Deployment successful!'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'app': 'Image-to-Form'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)