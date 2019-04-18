FROM python:3.6.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /workfile
WORKDIR /workfile
COPY . /workfile/
RUN python --version
RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt
COPY . /workfile/
