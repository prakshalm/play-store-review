FROM python:3.8-alpine
WORKDIR /workspace

RUN apt-get -y update

RUN apt-get install -y debconf-utils
ENV TZ=Asia/Kolkata
RUN echo $TZ > /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get clean

RUN apt-get update && \
    apt-get -y autoclean && \
    rm -rf /var/cache/apk/*
RUN cd /workspace
COPY . /workspace
RUN pip install -r requirements.txt

CMD ["python","main"]