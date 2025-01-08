# Use a Python image to build the app
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install openai

CMD ["python", "app.py"]
