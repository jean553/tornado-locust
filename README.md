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
```

Start the service:

```
python -m "tornado-locust"
```
