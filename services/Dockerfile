FROM python:3.11.7

WORKDIR /services

RUN apt-get install make
COPY Makefile .
COPY pyproject.toml .
RUN make deps

COPY . .
CMD make run