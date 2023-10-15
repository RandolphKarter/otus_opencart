FROM python:3.11.5-alpine3.18
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apk add mariadb-connector-c mariadb-dev gcc musl-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]
