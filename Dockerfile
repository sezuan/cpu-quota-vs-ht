FROM debian:jessie-slim

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install python3 python3-pbkdf2 python3-psutil

COPY main_cont.py /main_cont.py

ENTRYPOINT ["/main_cont.py"]

