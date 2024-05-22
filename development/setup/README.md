<br>

# Machines

> [!NOTE]  
> In Progress


<br>

## Initial Set-up

Foremost:

* Do not select Microsoft Account.  Instead, select the School/Business option, thereafter select other domains.
* Set-up security software.
* Partition the hard drive?

<br>
<br>
<br>

## Linux & Windows Subsystem for Linux (WSL)

Using a Linux requires (a) activating WSL, and (b) installing a Linux distribution.  The auto-script approach sometimes 
fails.  This section outlines the semi-manual approach.  For reference purposes:

* [Auto](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-2---check-requirements-for-running-wsl-2)

<br>

**STEPS:**

#### Activate Windows Subsystem for Linux

> Control Panel $\rightarrow$ Uninstall a program $\rightarrow$ Turn Windows features on or off $\rightarrow$ Windows Subsystem for Linux.

<br>

#### [Enable](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature) the virtual machine feature via PowerShell; administrator mode.

> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

<br>

#### Linux Kernel Update Package

>[Download and install](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) the package.

<br>

#### Download & Install [a Linux Distribution](https://learn.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions)

* Download
* To install, run `Add-AppxPackage .\app_name.appx`
* Double-click on the installed app, which will exists within the applications' menu, to activate it.  You will be asked 
  to set up credentials.

<br>
<br>
<br>

## Fundamental Software: Linux

### wget

The <a href="https://www.gnu.org/software/wget/manual/wget.html" target="_blank">wget</a> utility:

```shell
sudo apt install wget ca-certificates
```

`ca-certificates` allows applications that are secure sockets layer (SSL) dependent to verify the authenticity of SSL connections; SSL is a deprecated tool.

<br>

### GIT

Update `git` via the `git-core/ppa` <abbr title="Personal Package Archive">PPA</abbr> (Personal Package Archive).

```shell
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt list --upgradable
sudo apt install git-all
```

Subsequently, [set up & configure](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config) `git` ...

```shell
git config --global user.name ""
git config --global user.email "...@users.noreply.github.com"
git config --global core.editor "vim --nofork"
git config --global init.defaultBranch master

ssh-keygen -t ed25519 -C "...@users.noreply.github.com"

cat ~/.ssh/id_ed25519.pub
```

For instances whereby multiple accounts have to be managed per git client, e.g., study [GitHub Multiple Accounts]
(https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts).

<br>

### CONDA

Via `miniconda`.  Foremost, check the python version

```shell
python --version
```

#### The Installer

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell
# if python 3.10.*
sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
cd Downloads
sudo chmod +x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
```

#### Install

Install in the specified directory

```shell
# Include <-b> for automatic acceptance of the terms & conditions
sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -p /opt/miniconda3

$ Do you wish the installer to initialize Miniconda3 by running conda init?
>>> no
```

#### Set the Path Variable

Open `/etc/profile`, i.e.,

```shell
sudo vi profile
```

and append

```bash
if ! [[ $PATH =~ "/opt/miniconda3/bin" ]]; then
	PATH="/opt/miniconda3/bin:$PATH"
fi
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).  **Exit** the terminal.

<br>

#### Set-up

Next, within a new terminal

```shell
conda init bash
conda config --set auto_activate_base false
sudo chown -R $USER:$USER /opt/miniconda3
```

#### Upkeep

Update [conda](https://docs.conda.io/projects/conda/en/4.14.x/index.html) via

```shell
conda update -n base -c anaconda conda
```

<br>
<br>
<br>


## Fundamental Software: Windows

Browsers:
* [firefox](https://www.mozilla.org/en-GB/firefox/)
* [opera](https://www.opera.com)

Fundamentals:
* [KeePassXC](https://keepassxc.org/)
* Java: [JDK & JRE](https://adoptium.net/en-GB/temurin)
* [OpenOffice](https://www.openoffice.org/download/index.html)
* [Docker Desktop]()
* IntelliJ IDEA Ultimate


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>