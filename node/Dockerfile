FROM node:15.14.0


RUN apt-get update && apt-get install -y \
    sudo \
    rsync

WORKDIR /app
COPY ./gulpfile.js /app

RUN npm init -y
RUN sudo npm install --unsafe-perm --save \
    gulp gulp-load-plugins gulp-plumber gulp-sass gulp-pleeease
RUN sudo npm link gulp

CMD gulp compile
