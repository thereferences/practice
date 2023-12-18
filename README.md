<br>

Experiment: Code of Practice

<br>

### Prepare

A key practice is designing & developing within containers.  Foremost, create the scripts

* requirements.txt
* Dockerfile
* .devcontainer/devcontainer.json

within the project directory.  Always ascertain that the requirements file lists the packages/libraries required for development.  Next, and after ensuring that the project directory is the active directory, build the image

```shell
docker build -t practice .
```

Subsequently, run an instance of the image for development purposes

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src=...,target=/app practice
```

Substitute the ellipses for project directory.

<br>

### Sphinx

Initialise Sphinx

```shell
mkdir docs && cd docs && sphinx-quickstart && cd ..
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>