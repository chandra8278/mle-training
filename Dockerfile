FROM python:3.11

WORKDIR /docker-practice

COPY requirements.txt .
COPY ./src ./src
COPY ./datasets ./datasets

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python","./src/nonstandardcode.py"]