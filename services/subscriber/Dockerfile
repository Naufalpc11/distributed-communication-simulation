FROM python:3.9
WORKDIR /app
COPY subscriber.py .
RUN pip install paho-mqtt
CMD ["python", "subscriber.py"]