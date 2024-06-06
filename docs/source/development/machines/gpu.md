<br>

## Graphics Processing Unit, etc.

<br>

The references herein outline the fundamental NVIDIA installations **required within Windows 11** that ensure the ability **to run CUDA dependent programs within Windows 11 or a WSL (Windows Subsystem for Linux) kernel**. 


### NVIDIA Driver

Beware of the mappings between [CUDA Toolkit Version & CUDA Driver Version](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5:~:text=Windows%2C%20WSL-,CUDA%20Driver,-Running%20a%20CUDA).

Right Click [desktop]
SELECT Show more options
SELECT NVIDIA Control Panel

The landing page will display the name of the machine's Graphics Processing Unit, e.g.,

```markdown
NVIDIA RTX 2000 Ada Generation Laptop GPU 
```

Hence, [download the appropriate NVIDIA Driver](https://www.nvidia.com/en-gb/drivers/).  In relation to the above example

* Product Category: NVIDIA RTX/Quadro
* Product Series: NVIDIA RTX Series (Notebooks)
* Product: NVIDIA RTX 2000 Ada Generation Laptop GPU
* Operating System [If uncertain, check Settings -> System -> About]

Install:

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

Install [cuDNN](https://developer.nvidia.com/cudnn)
* [Windows](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
