A docker network allows multiple containers to communicate.

# Create a network
```sh
docker network create <network_name>
```

# Attach to Network

```sh
docker run -d\
--network <network_name>\
--network-alias <alias>
<image_name>
```
`--network-alias` will use the given name as the network name that the current container is in. It can be used as host-names for other containers to connect.
