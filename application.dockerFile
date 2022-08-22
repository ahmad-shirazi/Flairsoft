FROM python:3.8-slim-buster


RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
#CMD ["ls"]

COPY . /backend
COPY google/sapient-climate-350213-3fb7c260e157.json /backend
ENV GOOGLE_APPLICATION_CREDENTIALS "/backend/google/sapient-climate-350213-3fb7c260e157.json"
WORKDIR /backend/src
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/src"
WORKDIR /backend
CMD ["python", "src/main.py"]
#CMD ["ls"]

