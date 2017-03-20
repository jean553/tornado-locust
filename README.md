# tornado-locust

Simple example of Locust usage with Tornado.

## Requirements

 * Vagrant (tested with version 1.9.2)
 * Docker (tested with version 17.03)

## Start the service

Create the environment:

```bash
vagrant up
```

Log into the environment:

```bash
vagrant ssh
source /tmp/virtual_env35/bin/activate
```

Start the service:

```
python -m "tornado-locust"
```

## Run loading test

Log into the environment:

```bash
vagrant ssh
source /tmp/virtual_env27/bin/activate
```

Note that Locust is not running in the same virtualenv as Tornado,
Locust is not yet complient with Python 3.x.

Execute locustio:

```
locust --host=http://localhost:8080
```

Connect to the following URL in your host browser:

```
http://localhost:8089
```
