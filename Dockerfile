FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get update && apt-get install -y python3-pip
COPY . /app
WORKDIR /app
#ENV BOT_TOKEN=
#    FLASK_CONFIG=ProductionConfig
#    SECRET_KEY=
#    FLASK_IP=
#    FLASK_PORT=
COPY requirements.txt /app/requirements.txt
COPY run.sh /app/run.sh
RUN pip3 install -r /app/requirements.txt
RUN chmod +x /app/run.sh
ENTRYPOINT ["/bin/bash", "/app/run.sh"]
EXPOSE 8000