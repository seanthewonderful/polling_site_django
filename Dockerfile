FROM python:3.12-slim-bullseye

ENV PYTHONBUFFERED=1
# Ensures that Python output is sent to container logs

WORKDIR /django-polls
# Set the working directory to `/django-polls`

COPY requirements.txt requirements.txt
# Copies your code file from your action repository to the filesystem path `/` of the container.

RUN pip install -r requirements.txt

COPY . .
# Copies your code file from your action repository to the filesystem path `/` of the container.

CMD python manage.py runserver 0.0.0.0:8000
# Command to run when the container starts. 0.0.0.0 makes it available outside the container


