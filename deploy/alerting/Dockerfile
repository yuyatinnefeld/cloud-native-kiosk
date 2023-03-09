FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

# YOU CAN ACTIVATE THESE ENV FOR LOCAL DEBUG
# ENV ENV=LOCAL
# ENV GCP_PROJECT_ID=????

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
