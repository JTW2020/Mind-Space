FROM python:3.8-alpine3.14

WORKDIR /app

RUN apk update && apk add libffi-dev musl-dev gcc g++ make python3-dev openssl-dev
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]