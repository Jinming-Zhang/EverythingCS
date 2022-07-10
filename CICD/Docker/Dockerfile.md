A Dockerfile is simply a text-based script of instructions that is used to create a container image.
# Dockerfile Commands
- From
```
FROM <image_tag>
```
Use the existing image and build on top of it.

- WORKDIR
```
WORKDIR <dir_path>
```
Create <dir_path> and use it as working directory for all subsequent commands

- ENV
```
ENV <var_name> <var_value>
ENV PORT 80
```
Define environment variables that can be accessed by other processes that running inside the image

- COPY
```
COPY <src> <dst>
```
Copy content of working directory into the image's target directory

- RUN
```
RUN <cmd>
```

- CMD
```
CMD ["node", "src/server.js"]
```
Commands to run when starting the container
