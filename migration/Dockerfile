FROM node:10.19
ARG NODE_ENV
RUN echo "Environment: ${NODE_ENV}"

COPY ./migration/package.json /cura/package.json

WORKDIR /cura
#RUN git clone https://gitlab.com/amin.karimi1/geohai-backend-libs.git
RUN git clone https://gitlab.com/osucura/geohai-backend-libs.git
RUN cp -r geohai-backend-libs/* .

WORKDIR /cura
RUN npm install
RUN npm install -g knex@0.14.6
#RUN yarn install && yarn cache clean

COPY ./services /cura/backend
COPY ./migration/migrate.sh /cura/migrate.sh
WORKDIR /cura


ENTRYPOINT ["/bin/bash", "/cura/migrate.sh"]
CMD ["/cura/migrate.sh"]
