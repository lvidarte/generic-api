# Generic API Docker Image - Alpine Linux based

## Run with docker

    docker run -d --name generic-api -p 8080:8080 lvidarte/generic-api:latest

## Usage

POST

    $ curl -v http://127.0.0.1:8080/points -H 'application/json' -d '{"x":1, "y":2}'
    {
      "result": "ok"
    }


GET

    $ curl -v http://127.0.0.1:8080/points
    [
      {
        "x": 1, 
        "y": 2
      }
    ]


