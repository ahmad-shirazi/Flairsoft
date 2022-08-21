FROM python:3.8-slim-buster

WORKDIR /src

COPY ./src /src
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "/src/gateway.py"]

