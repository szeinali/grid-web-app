FROM python:3.6

RUN pip install --upgrade pip

MAINTAINER Sahand Zeinali

WORKDIR /web-app

COPY . /web-app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python", "web-app.py"]
