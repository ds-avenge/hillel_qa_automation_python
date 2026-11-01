FROM python:3.14

WORKDIR /app

COPY requirements-29.txt .

RUN pip install --no-cache-dir -r requirements-29.txt

COPY . .

CMD ["pytest", "-v", "homework_29.py"]
