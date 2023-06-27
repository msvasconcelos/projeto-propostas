FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Executar migrações do Django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Criar usuário administrador
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell


CMD celery -A proposta_projeto worker -l info
