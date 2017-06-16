# Generic API Docker Image - Alpine Linux based

This is a generic api for development tests. You can create any endpoint and add json objects as you wish. The data is persisted on disk by [shelve](https://docs.python.org/3.5/library/shelve.html).


### Run with docker

    docker run -d --name generic-api -v `pwd`/db:/app/db -p 5000:5000 lvidarte/generic-api:latest


### POST method

    $ curl localhost:5000/points -d '{"x": 1, "y": 2}'
    {
      "_id": "1", 
      "x": 1, 
      "y": 2
    }

<!-- -->

    $ curl localhost:5000/points -d '{"x": 5, "y": 10}'
    {
      "_id": "2", 
      "x": 5, 
      "y": 10
    }


### GET method

    $ curl localhost:5000/points
    {
      "1": {
        "_id": "1", 
        "x": 1, 
        "y": 2
      }, 
      "2": {
        "_id": "2", 
        "x": 5, 
        "y": 10
      }
    }

<!-- -->

	$ curl localhost:5000/points/1
	{
	  "_id": "1", 
	  "x": 1, 
	  "y": 2
	}

<!-- -->

	$ curl localhost:5000/points/1/x
    1


### DELETE method

	$ curl -XDELETE localhost:5000/points/1
	{
	  "_id": "1", 
	  "x": 1, 
	  "y": 2
	}


### Logs

    $ docker logs -f generic-api 
    172.17.0.1 - - [16/Jun/2017 04:50:56] "GET /points HTTP/1.1" 200 -
    172.17.0.1 - - [16/Jun/2017 04:51:40] "POST /points HTTP/1.1" 201 -
    172.17.0.1 - - [16/Jun/2017 04:51:55] "DELETE /points/1 HTTP/1.1" 404 -
