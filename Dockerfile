FROM python:3.7
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python manage.py makemigrations && python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000 