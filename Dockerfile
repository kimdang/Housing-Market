FROM python:3

RUN mkdir /backend

WORKDIR /backend

COPY . /

EXPOSE 8000
RUN pip3 install -r requirements.txt
