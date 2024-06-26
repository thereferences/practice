<br>

# Graphics Processing Unit, etc.

**Before proceeding**, install Docker Desktop: ref. Fundamental Software: Windows.

<br>

## Key Windows Settings

<br>

The references herein outline the fundamental NVIDIA installations **required within Windows 11** that ensure the ability **to run CUDA dependent programs/containers within Windows 11 or a WSL (Windows Subsystem for Linux) kernel**. 

<br>
 
### NVIDIA Driver

Beware of the mappings between [CUDA Toolkit Version & CUDA Driver Version](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5:~:text=Windows%2C%20WSL-,CUDA%20Driver,-Running%20a%20CUDA).  Before installing unloading an NVIDIA driver, determine the machine's CUDA GPU (Graphics Processing Unit) type.  Within the Windows desktop

* Right Click
* **SELECT** _Show more options_
* **SELECT** _NVIDIA Control Panel_

The NVIDIA Control Panel's landing page will display the name of the machine's Graphics Processing Unit, e.g.,

```markdown
NVIDIA RTX 2000 Ada Generation Laptop GPU 
```

<br>

Hence, [download the appropriate NVIDIA Driver](https://www.nvidia.com/en-gb/drivers/).  In relation to the above example

* Product Category: NVIDIA RTX/Quadro
* Product Series: NVIDIA RTX Series (Notebooks)
* Product: NVIDIA RTX 2000 Ada Generation Laptop GPU
* Operating System [If uncertain, check Settings -> System -> About]

<br>

Install.  During installation

* AGREE AND CONTINUE
* Custom (Advanced)
* Perform clean installation
  * HD Audio Driver
  * RTX Desktop Manager
  * Graphics Driver
  * USBC Driver

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

<br>
<br>

<br>
<br>

<br>
<br>
