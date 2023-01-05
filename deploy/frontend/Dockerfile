FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
WORKDIR /code
COPY ./app /code/app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 5000
ENV PORT=5000
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app