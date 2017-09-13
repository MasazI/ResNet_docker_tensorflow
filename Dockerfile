FROM tensorflow/tensorflow:latest-py3

ENV HOME_PATH=/home/deep
ENV APP_PATH=/home/deep/resnet

COPY . ${APP_PATH}

WORKDIR ${APP_PATH}

RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential git python-pip wget
RUN /bin/bash -c 'pip3 install -r requirements.txt'
RUN /bin/bash -c 'cd /home/deep/resnet/data ; ./preprocess.sh'
