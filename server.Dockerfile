FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

RUN mkdir sockets

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "server.py" ]
