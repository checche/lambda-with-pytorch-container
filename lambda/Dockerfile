FROM public.ecr.aws/lambda/python:3.8
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt
RUN python3.8 -m pip install -r requirements.txt
COPY app.py ./
COPY lib ./lib
CMD ["app.handler"]
