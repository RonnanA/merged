FROM python:3.10-slim
COPY src/ /src/
WORKDIR /src
ENTRYPOINT ["python", "/src/entrypoint.py"]