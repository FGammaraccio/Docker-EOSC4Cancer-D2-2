FROM python:3.13.2

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python","./main.py"]