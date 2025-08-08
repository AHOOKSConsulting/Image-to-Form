import os
import sys
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__, 
    static_folder='dist',  # Vite builds to 'dist' by default
    static_url_path=''
)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'asdf#FGSgvasgf$5$WGT')

# Database configuration
database_path = os.path.join(os.path.dirname(__file__), 'database', 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{database_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# CORS configuration for production
CORS(app, 
    origins=["*"],  # In production, specify your Railway domain
    supports_credentials=True,
    resources={r"/api/*": {"origins": "*"}}
)

# Import routes after app initialization
try:
    from src.routes.user import user_bp
    from src.routes.ocr import ocr_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(ocr_bp, url_prefix='/api/ocr')
except ImportError as e:
    print(f"Warning: Could not import routes: {e}")
    # Continue running without routes for basic deployment

# Create database tables
with app.app_context():
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    try:
        db.create_all()
    except Exception as e:
        print(f"Database initialization warning: {e}")

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'OCR API is running',
        'version': '1.0.0',
        'environment': 'production' if os.environ.get('RAILWAY_ENVIRONMENT') else 'development'
    })

# API root endpoint
@app.route('/api')
def api_root():
    return jsonify({
        'message': 'OCR Scanner API',
        'endpoints': {
            'health': '/health',
            'ocr': '/api/ocr/scan',
            'user': '/api/user'
        }
    })

# Serve React app - MUST be last route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    # Check if path is an API route
    if path.startswith('api/'):
        return jsonify({'error': 'API endpoint not found'}), 404
    
    # Check if requesting a static file
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Serve index.html for all other routes (React routing)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"Starting OCR Scanner API on port {port}")
    print(f"Static folder: {app.static_folder}")
    print(f"Database: {database_path}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)