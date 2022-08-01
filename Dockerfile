FROM python:3.10.5

RUN apt-get update
RUN apt-get install -yq build-essential gnupg2 curl
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get update

RUN apt install -y nodejs
RUN apt-get clean

RUN npm install -g yarn

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./Makefile /app
COPY ./frontend/ /app/frontend/
RUN make build-frontend

COPY ./app /app/app
COPY ./main.py /app

CMD [ "make", "run" ]

EXPOSE 8080
