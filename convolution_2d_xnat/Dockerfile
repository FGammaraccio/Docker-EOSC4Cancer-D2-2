FROM python:3.13.2

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get clean 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY envxnat.py .
COPY main.py .

CMD ["python","./main.py"]




