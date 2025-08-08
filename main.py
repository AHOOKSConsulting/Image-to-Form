import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'status': 'OK', 
        'message': 'OCR Document Scanner API is running!',
        'app': 'Image-to-Form'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Health check passed',
        'app': 'Image-to-Form'
    })

@app.route('/api/test')
def api_test():
    return jsonify({
        'message': 'API endpoint working',
        'status': 'success'
    })

if __name__ == '__main__':
    # Railway sets PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)