FROM python:latest

WORKDIR /django

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

ENV DJANGO_SETTINGS_MODULE=nomash.settings
ENV POSTGRES_USER=nomashadmin
ENV POSTGRES_PASSWORD=nomash123
ENV POSTGRES_DB=nomash

EXPOSE 8000

CMD ["uvicorn", "nomash.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

