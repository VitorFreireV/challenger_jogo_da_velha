FROM python:3.8.10

WORKDIR /src

COPY /src /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --updage -r /src/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
