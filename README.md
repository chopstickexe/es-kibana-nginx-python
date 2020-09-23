# es-kibana-nginx-python
Docker compose example for Elasticsearch, kibana, nginx, and python

# How to set up

## 1. (Optional) Set user ID and password for nginx

Create a passwd file for basic authentication:

```
$ cd /path/to/this/directory
$ sudo apt -y install apache2-utils
$ mkdir htpasswd
$ htpasswd -c localhost admin  # Note that the name of the passwd file must be identical with the value of VIRTUAL_HOST variable in docker-compose.yml
# Type the password here
```

See https://github.com/nginx-proxy/nginx-proxy#basic-authentication-support for details.

## 2. Up containers

```
$ cd /path/to/this/directory
$ docker-compose up
```

Wait until all the four containers up and open `http://localhost` with your browser.  

Login with ID=`admin` and PW=`(The password you set)`.

## 3. Index data

`index.py` is an example script to index data to the Elasticsearch container.

``` 
$ docker exec -it python bash
# python -m venv .venv
# source .venv/bin/activate
(.venv) # pip install -r requirements.txt
(.venv) # python index.py
Finished indexing
```
