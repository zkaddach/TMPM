FROM python:3.8
WORKDIR /.



RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

ADD . ./
EXPOSE 8888
CMD ["--port", "8888"]
ENTRYPOINT ["python3", "run.py"]
