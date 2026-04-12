FROM python:3.9
WORKDIR /app
COPY server.py .
RUN pip install flask paho-mqtt
CMD ["python", "server.py"]