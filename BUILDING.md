# Building
##

Our application is built intended to run as container.\
So to build its image, is as easy as:\
<sup>Note: "tux/tux.tools" is an example, choose whatever project name you are using</sup>
```
$ cd <app_root_dir>
$ docker build tux/tux.tools .
### And run: ###
$ docker run -d -p 8000:8000 tux.tools
```
Now you're able to access it using: "http://localhost:8000".\
This is for local-testing only. Production environments should use a proxy in front (NGINX recommended)\ 