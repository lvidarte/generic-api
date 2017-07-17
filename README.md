# Generic API

This is a shemaless and generic api for development tests. You can create any endpoint and add json objects as you wish. The data is persisted on disk by [shelve](https://docs.python.org/3.5/library/shelve.html).


### Run with docker (Alpine Linux based)

    docker run -d --name generic-api -v `pwd`/data:/app/data -p 5000:5000 lvidarte/generic-api:latest


### POST method

The header `Content-Type: application/json` is not necessary, the api assumes you are sending jsons.

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

### Nested example

Create authors and books

	$ curl localhost:5000/authors -d '{"name": "Asimov"}'
	{
	  "_id": "1", 
	  "name": "Asimov"
	}

	$ curl localhost:5000/authors/1/books -d '{"title": "Nemesis", "year": 1988}'
	{
	  "_id": "1", 
	  "title": "Nemesis", 
	  "year": 1988
	}

	$ curl localhost:5000/authors/1/books -d '{"title": "Foundation and Earth", "year": 1987}'
	{
	  "_id": "2", 
	  "title": "Foundation and Earth", 
	  "year": 1987
	}

Get the full data

	$ curl localhost:5000/authors/1
	{
	  "_id": "1", 
	  "books": {
		"1": {
		  "_id": "1", 
		  "title": "Nemesis", 
		  "year": 1988
		}, 
		"2": {
		  "_id": "2", 
		  "title": "Foundation and Earth", 
		  "year": 1987
		}
	  }, 
	  "name": "Asimov"
	}

You can get only some field

	$ curl localhost:5000/authors/1/books/2/title
	"Foundation and Earth"

	$ curl localhost:5000/authors/1/books/2/year
	1987

And change any field as you wish

	$ curl localhost:5000/authors/1/books/2/year -d '1986'
	1986


	$ curl localhost:5000/authors/1/books/2
	{
	  "_id": "2", 
	  "title": "Foundation and Earth", 
	  "year": 1986
	}

### PUT method

There is not PUT method, use POST instead.

### Logs

    $ docker logs -f generic-api 
    172.17.0.1 - - [16/Jun/2017 04:50:56] "GET /points HTTP/1.1" 200 -
    172.17.0.1 - - [16/Jun/2017 04:51:40] "POST /points HTTP/1.1" 201 -
    172.17.0.1 - - [16/Jun/2017 04:51:55] "DELETE /points/1 HTTP/1.1" 404 -
