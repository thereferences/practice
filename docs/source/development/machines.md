<br>

# Machines

<br>

:::{admonition} In Progress
<br>
:::

All the organisation's computer usage rules apply; remember, Universal Serial Bus (USB) sticks are disallowed.

<br>
<br>
<br>

## Initial Set-up

Foremost:

* Do not select Microsoft Account.  Instead, select the **School/Business** option, thereafter select **other domains** option.
* Set-up security software.
* Hard Drive Partitioning: Consider partitioning the C drive into two drives; such that the second drive is for development purposes.

<br>

### Basic Tools

Install

* [firefox](https://www.mozilla.org/en-GB/firefox/)
* [opera](https://www.opera.com)
* [KeePassXC](https://keepassxc.org/)

Ensure that the privacy & security settings of the browsers are strict; additionally, set the default search engine to _duckduckgo_.

<br>
<br>
<br>

## Linux & Windows Subsystem for Linux (WSL)

Using a Linux requires (a) activating WSL, and (b) installing a Linux distribution.  The auto-script approach sometimes
fails.  This section outlines the semi-manual approach.  For reference purposes:

* [Auto](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-2---check-requirements-for-running-wsl-2)

<br>

### Activate Windows Subsystem for Linux

The activation steps are

> Control Panel $\rightarrow$ Uninstall a program $\rightarrow$ Turn Windows features on or off $\rightarrow$ Windows Subsystem for Linux.

Subsequently, re-start the machine.

<br>

### Enable the virtual machine feature via PowerShell; administrator mode.

For details visit [enable virtual machine feature](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature).

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

<br>

### Linux Kernel Update Package

>[Download and install](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) the package.

<br>

### Download & Install a Linux Distribution

* [Download](https://learn.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions)
* To install, run `Add-AppxPackage .\app_name.appx`
* Double-click on the installed app, which will exists within the applications' menu, to activate it.  You will be asked to set up credentials.

<br>

### Commands

* [Basic Commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)

<br>
<br>
<br>

## Fundamental Software: Linux

Apriori

```shell
sudo apt update
sudo apt upgrade
```

Additionally, often inspect the GNU Privacy Guard (<abbr title="GNU Privacy Guard">GPG</abbr>) keys via:

```shell
gpg --list-keys
gpg --list-secret-keys
```

Print environment variables via

```shell
printenv
```

<br>

### WGET

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

For instances whereby multiple accounts have to be managed per git client, e.g., study [GitHub Multiple Accounts](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts).

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
sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_24.4.0-0-Linux-x86_64.sh
cd Downloads
sudo chmod +x Miniconda3-py310_24.4.0-0-Linux-x86_64.sh
```

#### Install

Install in the specified directory

```shell
# Include <-b> for automatic acceptance of the terms & conditions
sudo bash Miniconda3-py310_24.4.0-0-Linux-x86_64.sh -p /opt/miniconda3

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

### Core

* [Notepad++](https://notepad-plus-plus.org)
* [Git for Windows](https://git-scm.com)
    * Editor: Select Notepad++
    * Default Branch Name: *master*
* Java: [JDK & JRE](https://adoptium.net/en-GB/temurin)
* [OpenOffice](https://www.openoffice.org/download/index.html)

<br>

### Windows Installations that Propagate to WSL Kernels

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/?section=windows)
* [Visual Studio CODE](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>