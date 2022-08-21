FROM python:3.8-slim-buster

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./migration/migrate.sh /Flairsoft/migrate.sh
WORKDIR /Flairsoft


ENTRYPOINT ["/bin/bash", "/Flairsoft/migrate.sh"]
CMD ["/Flairsoft/migrate.sh"]
