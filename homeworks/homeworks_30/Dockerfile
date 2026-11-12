FROM python:3.14

WORKDIR /app

COPY requirements-30.txt .

RUN pip install --no-cache-dir -r requirements-30.txt

COPY . .

CMD ["pytest", "-v", "homework_30.py", "--alluredir=allure-results", "--clean-alluredir"]
