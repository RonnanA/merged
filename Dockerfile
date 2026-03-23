FROM python:3.10-slim
COPY /src/entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]