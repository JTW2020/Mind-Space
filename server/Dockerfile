FROM python:3.11.0a5-bullseye

WORKDIR /app

ENV FLASK_ENV=development

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# CMD ["python3", "-m", "flask", "run"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]