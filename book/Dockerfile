FROM python:3.11
WORKDIR app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNDUFFERED 1
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .