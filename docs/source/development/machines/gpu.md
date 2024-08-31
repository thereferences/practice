
# Graphics Processing Unit, etc.

**Before proceeding**, install Docker Desktop: ref. Fundamental Software: Windows.

<br>

:::{dropdown} Table of Contents
```{contents}
:depth: 2
:local:
:backlinks: top
```
:::

<br>

## Key Windows Settings

<br>

The references herein outline the fundamental NVIDIA installations **required within Windows 11** that ensure the ability **to run CUDA dependent programs/containers within Windows 11 or a WSL (Windows Subsystem for Linux) kernel**. 

<br>
 
### NVIDIA Driver

Beware of the mappings between [CUDA Toolkit Version & CUDA Driver Version](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5:~:text=Windows%2C%20WSL-,CUDA%20Driver,-Running%20a%20CUDA).  Before installing unloading an NVIDIA driver, determine the machine's CUDA GPU (Graphics Processing Unit) type.  Within the Windows desktop

<ul class="disc">
  <li class="disc">Right Click</li>
  <li class="disc"><b>SELECT</b> <i>Show more options</i></li>
  <li class="disc"><b>SELECT</b> <i>NVIDIA Control Panel</i></li>
</ul>


The NVIDIA Control Panel's landing page will display the name of the machine's Graphics Processing Unit, e.g.,

```markdown
NVIDIA RTX 2000 Ada Generation Laptop GPU 
```

Hence, [download the appropriate NVIDIA Driver](https://www.nvidia.com/en-gb/drivers/).  In relation to the above example

<ul class="disc">
  <li class="disc">Product Category: NVIDIA RTX/Quadro</li>
  <li class="disc">Product Series: NVIDIA RTX Series (Notebooks)</li>
  <li class="disc">Product: NVIDIA RTX 2000 Ada Generation Laptop GPU</li>
  <li class="disc">Operating System [If uncertain, check Settings &rarr System &rarr About]</li>
</ul>

Install.  During installation

<ul class="disc">
  <li class="disc">AGREE AND CONTINUE</li>
  <li class="disc">Custom (Advanced)</li>
  <li class="disc">Perform clean installation</li>
  <li class="disc">
    <ul class="circle">
      <li class="circle"><abbr title="High Definition">HD</abbr> Audio Driver</li>
      <li class="circle"><abbr title="Ray Tracing eXtreme">RTX</abbr> Desktop Manager</li>
      <li class="circle">Graphics Driver</li>
      <li class="circle"><abbr title="Universal Serial Bus Type <b>C</b>">USB-C</abbr> Driver</li>
    </ul>
  </li>
</ul> 

NVIDIA will request a machine restart: restart.

<br>
<br>


### NVIDIA CUDA Toolkit

Install [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
* [Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)

<br>

Installation Steps:
* NVIDIA software licence agreement: AGREE AND CONTINUE
* Custom installation options: deselect visual studio integration
* Leave the default installation location $\rightarrow$ C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v{version.number}


<br>
<br>

### cuDNN

**Defunct/Skip**

Install [cuDNN](https://developer.nvidia.com/cudnn)
* [Windows](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows)


<br>
<br>

## Within Linux Kernels

### NVIDIA Container Toolkit

#### Installing

A key tool for building and running GPU accelerated containers is the NVIDIA Container Toolkit.  This section outlines the installation of the toolkit via APT (Advanced Package Tool); NVIDIA outlines [a few options](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit).  Set-up, configure, the production repository via commands:

```shell
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | 
  sudo gpg --dearmour -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
```

and

```shell
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | 
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | 
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

<br>

Next, update the repository's packages list:

```shell
sudo apt update
```

<br>

Finally, install the NVIDIA Container Toolkit packages:

```shell
sudo apt install -y nvidia-container-toolkit
```

<br>
<br>

#### Configuring

Initially, configure the container runtime for docker; NVIDIA's pages detail extra component dependent [configurations](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuration).  

```shell
sudo nvidia-ctk runtime configure --runtime=docker
```

<br>

Subsequently, restart docker via docker desktop.

<img src="../../../../assets/engine.png" alt="Docker Engine">

<br>
<br>

#### Testing

Foremost, determine the machines CUDA version, i.e.,  {major}.{minor}.{build}, via

```bash
nvidia-smi
```

and Ubuntu version, i.e., {major}.{minor}, via

```bash
cat /etc/os-release
```

<br>

Subsequently, use

> docker run --rm --gpus all nvidia/cuda:{cuda_version}-base-ubuntu{ubuntu_version} nvidia-smi

to create and run a CUDA test command, e.g.,

```bash
docker run --rm --gpus all nvidia/cuda:12.5.0-base-ubuntu22.04 nvidia-smi
```

<br>
<br>

#### Downgrading

* Uninstall 12.5 / All NVIDIA Components<br>
  Restart machine as many times as necessary

* Downgrade to 12.2<br>
  [Download](https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11)

* Install<br>
  Opt for custom installation: deselect visual studio integration

* Check environment variable paths

* Re-start

* Re-configure linux container toolkit settings<br>
  https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker

* Re-start docker


Version Matrix
https://docs.nvidia.com/cuda/archive/12.2.2/cuda-toolkit-release-notes/index.html


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
