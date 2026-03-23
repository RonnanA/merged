FROM python:3.10-slim
COPY requirements.txt /requirements.txt
COPY src/ /src/
RUN pip install -r /requirements.txt
WORKDIR /src
ENTRYPOINT ["python", "/src/entrypoint.py"]