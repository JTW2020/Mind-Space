FROM python:3.8-alpine

WORKDIR /app

RUN apk --update add bash nano vim build-base
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run"]