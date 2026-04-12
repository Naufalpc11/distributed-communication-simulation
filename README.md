# MQTT Temperature Demo

This project demonstrates a simple MQTT-based data flow using Docker Compose.

## What Each File Does

- `docker-compose.yml`: Defines the broker, publisher, subscriber, and API containers.
- `services/api/server.py`: Provides a Flask web form and HTTP endpoint, then publishes temperature data to MQTT.
- `services/publisher/publisher.py`: Generates random temperature values and publishes them periodically.
- `services/subscriber/subscriber.py`: Subscribes to temperature topic and prints received messages.
- `services/api/Dockerfile`: Builds the API container image.
- `services/publisher/Dockerfile`: Builds the publisher container image.
- `services/subscriber/Dockerfile`: Builds the subscriber container image.

## Data Flow Summary

1. API or publisher sends temperature data to topic `sensor/suhu`.
2. MQTT broker routes messages to subscribers of that topic.
3. Subscriber receives and prints the messages.
