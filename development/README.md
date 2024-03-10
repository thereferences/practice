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
conda remove --prefix J:\programs\anaconda3\envs\transcribe --all
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

* [Furo](https://pradyunsg.me/furo/)
  * [Sample](https://sphinx-themes.org/sample-sites/furo/)
* [Sphinx Design: Furo](https://sphinx-design.readthedocs.io/en/furo-theme/)


* [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/index.html)
* [Sphinx Design: Sphinx Book Theme](https://sphinx-design.readthedocs.io/en/sbt-theme/)


* [MyST](https://myst-parser.readthedocs.io/en/latest/index.html)
  * [Organising Content](https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#using-toctree-to-include-other-documents-as-children)
* [Sphinx Directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
* [mermaid](https://mermaid.js.org/intro/)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
