FROM python:3.6.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN python --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt
COPY . /code/
