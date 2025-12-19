FROM python:3.13-slim
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y awscli ffmpeg libsm6 libxext6 unzip && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["python3", "app.py"]
