FROM --platform=linux/amd64 python:3.11.1-alpine

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt
RUN mkdir /templates
RUN mkdir /static

COPY main.py /app/
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/

EXPOSE 5050

CMD ["python3", "main.py"]