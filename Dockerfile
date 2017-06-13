FROM alpine:latest

MAINTAINER Leo Vidarte "lvidarte@gmail.com"

RUN apk add --update python3 && rm -rf /var/cache/apk/*

COPY . /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
