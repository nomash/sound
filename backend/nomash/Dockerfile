FROM python:latest

WORKDIR /app

COPY . .
COPY Pipfile .
COPY Pipfile.lock .

RUN pip3 install -r requirements.txt && pip cache purge

EXPOSE 8000

CMD ["./startup.sh"]

