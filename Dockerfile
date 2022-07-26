FROM python:3.9.7-alpine

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./sf23 /app
WORKDIR /app

RUN python manage.py migrate --no-input && python manage.py collectstatic --no-input

CMD [ "gunicorn","sf23.wsgi:application", "--bind", "0.0.0.0:8000" ]