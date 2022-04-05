FROM python:3.8.10

COPY /src /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 80/tcp

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
