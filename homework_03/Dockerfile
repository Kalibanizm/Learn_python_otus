FROM python:3.9-buster

WORKDIR /APP

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./demo-app/pyproject.toml

COPY ./demo-app/poetry.lock

RUN poetry install

COPY demo-app ./

EXPOSE 8000

CMD ["uvicorn", "demo-app:app", "--host=0.0.0.0"]