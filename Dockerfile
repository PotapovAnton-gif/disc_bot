FROM python:3.9.13-slim-bullseye
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD python dic_bot.py
