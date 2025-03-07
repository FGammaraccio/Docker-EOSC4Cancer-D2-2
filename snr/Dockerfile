FROM python:3.7.9-buster 

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python","./main.py"]