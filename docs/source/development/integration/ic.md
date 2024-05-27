<br>

# Images & Containers

:::{admonition} In Progress
<br>
:::

## Python

### For Development

A key practice is designing & developing within containers.  For Python projects, Foremost, create:

* requirements.txt
* Dockerfile
* devcontainer.json

Within the `.devcontainer/` directory, which must be within the project's parent directory.  Always ascertain that the 
`requirements.txt` file lists the packages/libraries required for development.  Next, build the image:

```shell
docker build . --file .devcontainer/Dockerfile --tag {tag.name}
```

Subsequently, run an instance of the image for development purposes, e.g.,

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app 
  --mount type=bind,src="$(pwd)",target=/app {tag.name}
```

An independent development environment can be attached to a running container.

<br>

### For Deployment

* Never deploy root containers; study [this production Dockerfile](https://github.com/enqueter/distributions/blob/master/Dockerfile), which blocks access to `root` by creating a standard user.

<br>
<br>

## Scala

### For Development

The template ...

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
