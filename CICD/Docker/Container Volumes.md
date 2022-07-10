`Volumes` provides the ability to connect specific filesystem paths of the container back to the host machine, hence a way to persist data from a container.
# Named Volume
Let docker create a volume with a name that we can reference with
Named volumes are great if we simply want to store data, as we don’t have to worry about _where_ the data is stored.
```
docker volume create <volume_name>
```
to use a volume when starting a container
```
docker run -dp 3000:3000 -v <volume_name>:<path_to_persist> <image_name>
```
`path_to_persist` is the path in the container that will be persisted with the volume
> If <volume_name> doesn't exist and it's not a path format, docker will create the volume automatically.

To check where a volume is located on the host machine:
```
docker volume inspect <volume_name>
```
# Bind Mounts
With **bind mounts**, we control the exact mountpoint on the host, also can provide additional data into container.
```
docker run -v <host_path>:<container_path> <image_name>
```