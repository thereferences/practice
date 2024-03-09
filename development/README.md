<br>

The repository's development notes.

<br>

# Remote & Local Environments

## Remote

Foremost, the scripts for building a docker image

* requirements.txt
* Dockerfile
* .devcontainer/devcontainer.json

The requirements file lists the packages/libraries required for development.  Next, an image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile --tag transcribe
```

Subsequently, an instance of the image, i.e., a container,

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app transcribe
```

is run for development purposes.

<br>

## Local

If developing outwith a container, try

````commandline
conda remove --prefix J:\programs\anaconda3\envs\practice --all
environment.bat
````

or

```shell
source environment.sh
```

Each script depends on the `environment.yml`, which uses the same *requirements.txt* as Dockerfile.

<br>
<br>

# Sphinx

Initialise Sphinx

```shell
mkdir docs && cd docs && sphinx-quickstart && cd ..
```

Build

```shell
sphinx-build -E -b html docs/source docs/build/html
```

<br>

### References

* [Sphinx Design](https://sphinx-design.readthedocs.io/en/rtd-theme/index.html)
* https://sphinx-themes.org/sample-sites/furo/
* https://pradyunsg.me/furo/
* https://sphinx-design.readthedocs.io/en/furo-theme/
* https://myst-parser.readthedocs.io/en/latest/index.html
    * https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#using-toctree-to-include-other-documents-as-children

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
