FROM python:3-alpine
MAINTAINER Sahand Zeinali
COPY web-app /web-app
WORKDIR /web-app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python","web-app.py"]