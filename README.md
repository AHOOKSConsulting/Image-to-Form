# OCR Mobile Document Scanner

## 🚀 Quick Deploy to Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → Sign in with GitHub
3. "New Project" → "Deploy from GitHub" → Select this repo
4. Railway automatically deploys both Flask backend and React frontend!
5. Your app will be live at: https://your-app-name.railway.app

## 📱 Features

- ✅ Real-time camera document scanning
- ✅ AI-powered OCR with PaddleOCR
- ✅ Structured data extraction (names, dates, IDs)
- ✅ Mobile-optimized PWA
- ✅ "Add to Home Screen" capability
- ✅ Offline functionality
- ✅ Auto-detects API connection
- ✅ Demo mode fallback

## 🏗️ Architecture

- **Backend**: Flask + PaddleOCR + OpenCV
- **Frontend**: React + Vite + Tailwind CSS
- **Deployment**: Railway (full-stack)
- **Database**: SQLite
- **Mobile**: Progressive Web App (PWA)

## 📁 Project Structure

```
ocr-scanner/
├── requirements.txt          # Python dependencies
├── railway.json             # Railway deployment config
├── main.py                  # Flask application
├── package.json             # React dependencies
├── index.html               # React entry point
├── public/
│   ├── manifest.json        # PWA configuration
│   └── sw.js               # Service worker
├── src/
│   ├── main.jsx            # React entry
│   ├── App.jsx             # Main React component
│   ├── App.css             # Styles
│   ├── routes/             # Flask routes
│   └── models/             # Flask models
└── README.md               # This file
```

## 🔧 Development

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies  
npm install

# Run Flask backend
python main.py

# Run React frontend (in another terminal)
npm run dev
```

## 📱 Mobile Usage

1. Open the Railway URL on your phone
2. Allow camera permissions
3. Start scanning documents
4. View extracted data in real-time
5. Add to home screen for app-like experience

That's it! Your OCR scanner is ready to go! 🎉