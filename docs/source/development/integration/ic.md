<br>

# Images & Containers

<br>

:::{note}
In Progress
:::

<br>

A key practice is designing & developing within containers.  Foremost, create the scripts

* requirements.txt
* Dockerfile
* .devcontainer/devcontainer.json

within the project directory.  Always ascertain that the `requirements.txt` file lists the packages/libraries required for 
development.  Next, and after ensuring that the project directory is the active directory, build the image

```shell
docker build . --file .devcontainer/Dockerfile --tag {tag-name}
```

Subsequently, run an instance of the image for development purposes, e.g.,

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app {tag-name}
```

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
