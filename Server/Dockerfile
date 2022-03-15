FROM python:3.9-alpine
WORKDIR /Server
COPY requirements.txt /Server
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /Server
ENTRYPOINT ["python3"]
CMD ["Api.py"]


