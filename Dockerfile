FROM python:3.10-slim
COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]