# Introduction
To stream small content in a low weight webserver frame work is an interesting topic. There is a very good - but unfortunately not up to date - tutorial at https://runnable.com/docker/python/dockerize-your-flask-application
According to this tutorial the linux environment is the biggest change. Compared to the (in this case old ) ubutnu version, alpine leads to a very much faster build process and is taking very more less disk storage.
Important to say is, that the commands in the Dockerfile for the updating and package adding have to change as well. In general the following project is based on the previos shown tutorial but with a lower weighted and faster linux distribution and with an up to date version of python and all dependencies.


# Usage
## Bild the Image
To build the image just start in the root directory of the project (where the DockerFile-File is stored) the following command:

```console
docker build -t flask-tutorial:latest .
```

## Start the Container
Flask is using Port 5000 by default. So internally the port can be changed in the python app.py file. The external port can be changed in the docker run section.
```console
docker run -d --name flask_webserver -p 5000:5000 flask-tutorial
```

# Further Information and Trouble shooting
## Troubleshooting
In some cases the Requirements are not up to date. So a look in 
```console
docker container logs flask_webserver
```

could be usefull

## Helpfull links
https://runnable.com/docker/python/dockerize-your-flask-application
https://blog.miguelgrinberg.com/post/video-streaming-with-flask
https://hub.docker.com/_/alpine
https://wiki.alpinelinux.org/wiki/Package_management
