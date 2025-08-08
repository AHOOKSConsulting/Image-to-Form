FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

CMD ["sh", "-c", "gunicorn main:app --bind 0.0.0.0:${PORT:-5000}"]