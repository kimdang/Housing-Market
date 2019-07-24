FROM alirom93/django:master-1

RUN mkdir /backend

WORKDIR /backend

COPY . /

EXPOSE 8000
RUN pip3 install -r requirements.txt
