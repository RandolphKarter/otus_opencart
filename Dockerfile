FROM python:3.11.5-bookworm
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]