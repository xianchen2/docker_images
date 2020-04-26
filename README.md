# Docker_images

A python command line interface that can connect to the OPCV API. 
Script is able to run within docker and take parameters from the command line.

**To Run**
```
docker pull xianc410/bigdata1:1.0
docker tag xianc410/bigdata1:1.0 bigdata1:1.0
```
```
docker run -e APP_KEY=app_token -t bigdata1:1.0 python main.py 1000 4 resul2
```

page_size: 1000  
num_pages(optional): 4  
output_filename(optional): resul2

https://hub.docker.com/repository/docker/xianc410/bigdata1
