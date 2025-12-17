FROM python:3.13-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["python3", "app.py"]
