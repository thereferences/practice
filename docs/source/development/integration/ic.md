<br>

# Images & Containers

:::{admonition} In Progress
<br>
:::

Designing & developing within containers.

## Python

### For Development

For Python projects, create:

* requirements.txt
* Dockerfile
* devcontainer.json

Within the `.devcontainer/` directory, which must be within the project's parent directory; <a href="https://github.com/enqueter/distributions/tree/master/.devcontainer" target="_blank">example</a>.  Always ascertain that the `requirements.txt` file lists the packages/libraries required for development.  Next, build the image:

```{code} bash
docker build . --file .devcontainer/Dockerfile --tag {tag.name}
```






<br>

Subsequently, run an instance of the image for development purposes, e.g.,

> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app \
> &nbsp; &nbsp; --mount type=bind,src="$(pwd)",target=/app {tag.name}

or

> docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app \
> &nbsp; &nbsp; --mount type=bind,src="$(pwd)",target=/app -v ~/.aws:/root/.aws {tag.name}

<br>

wherein `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  The second option is important for interactions with Amazon Web Services.  Get the name of the running instance of {tag.name} via:

```shell
docker ps --all
```

<br>

Next, attach the running an IDE (independent development environment) application to a running container.  If IntelliJ IDEA:

> Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** {operating.system}
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

Similarly, Visual Studio Code as its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).


<br>

### For Deployment

* **Never deploy root containers**; study [this production Dockerfile](https://github.com/enqueter/distributions/blob/master/Dockerfile), which blocks access to `root` by creating a standard user; cf. [the development Dockerfile](https://github.com/enqueter/distributions/blob/master/.devcontainer/Dockerfile).

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
