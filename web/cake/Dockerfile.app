FROM python:latest

WORKDIR /app
COPY ./code/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./code /app
CMD ["python", "app.py"]
