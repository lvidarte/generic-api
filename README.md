# Generic API Docker Image - Alpine Linux based


## Run with docker

    docker run -d --name generic-api -v `pwd`/db:/app/db -p 5000:5000 lvidarte/generic-api:latest


## Usage


### POST

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


### GET

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


### DELETE

	$ curl -XDELETE localhost:5000/points/1
	{
	  "_id": "1", 
	  "x": 1, 
	  "y": 2
	}



