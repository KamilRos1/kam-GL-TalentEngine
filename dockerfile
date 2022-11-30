FROM python:3.11-buster

WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /code/
ENV PYTHONPATH /code
ENTRYPOINT [ "pytest" ]
CMD [ "-s", "-m loginPage" ]