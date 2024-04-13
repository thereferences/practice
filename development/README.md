<br>

The repository's development notes.

<br>

## Remote Development

The container image depends on

* requirements.txt
* Dockerfile

The requirements file lists the packages/libraries required for development.  Next, an image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile --tag transcribe
```

Subsequently, a development container is initialised via the command

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app transcribe
```

<br>
<br>

## Sphinx

## Usage Notes

Initialise Sphinx

```shell
mkdir docs && cd docs && sphinx-quickstart && cd ..
```

Build

```shell
sphinx-build -E -b html docs/source docs/build/html
```

<br>

## References

* [Furo](https://pradyunsg.me/furo/)
  * [Sample](https://sphinx-themes.org/sample-sites/furo/)
* [Sphinx Design: Furo](https://sphinx-design.readthedocs.io/en/furo-theme/)

* [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/index.html)
  * [Sample](https://sphinx-book-theme.readthedocs.io/en/stable/reference/kitchen-sink/index.html)
* [Sphinx Design: Sphinx Book Theme](https://sphinx-design.readthedocs.io/en/sbt-theme/)

* [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
  * [Sphinx Directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
* [reStructuredText](https://docutils.sourceforge.io/rst.html)
  * [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
  * [reStructuredText Card](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
* [MyST](https://myst-parser.readthedocs.io/en/latest/index.html)
  * [Organising Content](https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#using-toctree-to-include-other-documents-as-children)
* [Extensions](https://myst-parser.readthedocs.io/en/latest/intro.html#extending-sphinx)
  * [mermaid](https://mermaid.js.org/intro/)
  * [tippy](https://sphinx-tippy.readthedocs.io/en/latest/)

* Text
  * [Data Science Projects](https://pubsonline.informs.org/action/doSearch?&target=digital-object-search&content=digitalObjects&Keywords=Principles%20for%20Successful%20Analytics%20Projects)
  * [The Artificial Intelligence Playbook](https://www.machinelearningkeynote.com/the-ai-playbook)
  * [The feasibility, and economic viability, of projects](https://ppp.worldbank.org/public-private-partnership/assessing-project-feasibility-and-economic-viability)
  * [System Reliability, Availability, and Maintainability](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
