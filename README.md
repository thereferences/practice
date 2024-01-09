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

Build

```shell
sphinx-build -E -b html docs/source docs/build/html
```

References:
* [Sphinx Design](https://sphinx-design.readthedocs.io/en/rtd-theme/index.html)

<br>

### Extra

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

### References

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
