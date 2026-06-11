FROM python:3.12-slim
WORKDIR /app
COPY .
RUN python backup.py
EXPOSE 8000
