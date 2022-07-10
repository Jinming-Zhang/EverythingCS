# docker build
taking in a directory with `Dockerfile`, build it into an image
```
docker build -f path_to_Dockerbuild -t name:tag
i.e.
docker build --tag portfolio:1.0 .
```
# docker images
shows the docker images on the machine 

```
docker images
```
# docker run
run the given image
```
docker run portfolio
```
Run image with a mapping port and detached mode (for long lasting containers)
```
docker run -p <srcPort>:<dstPort> --name <containerName> -d <image_path>
```
To keep ubuntu image running:
```
docker run -dit
```
map **srcPort** to **dstPort**
	
# docker rm
remove a stopped container, or force remove it if it's running
```
docker rm -f <container_name>
```
# docker ps -a
Show the running images 
# docker logs
show logs of a given container
```
docker logs -f <container_name>
```

# docker exec
Attach to a docker container with an interactive bash
```sh
docker exec -it <container_name>
```