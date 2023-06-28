FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

CMD celery -A proposta_projeto worker -l info
