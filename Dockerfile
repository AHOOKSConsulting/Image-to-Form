FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Railway will set PORT automatically
EXPOSE $PORT

# Use gunicorn with proper port binding
CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 main:app