FROM python:3.8-alpine

WORKDIR /app

RUN apk update && apk add libffi-dev musl-dev gcc python3-dev openssl-dev
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]