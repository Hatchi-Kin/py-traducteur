FROM python:3.10-slim-buster

WORKDIR /api

ADD . /api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "src/api.py"]  