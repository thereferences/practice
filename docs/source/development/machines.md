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

The <a href="https://www.gnu.org/software/wget/manual/wget.html" target="_blank">wget</a> utility - check if `wget` exists

```shell
wget --version
```

Installing `wget`, `ca-certificates`

```shell
sudo apt install wget ca-certificates
```

`ca-certificates` allows applications that are secure sockets layer (SSL) dependent to verify the authenticity of SSL connections; SSL is a deprecated tool.

<br>

### Java

References
* [Installing JAVA](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04)

#### Installing: Java

```shell
# jdk & jre
sudo apt install openjdk-19-jdk-headless
java --version
javac --version
```

#### Environment Variables: Java

The environment variable of interest is the `JAVA_HOME` variable, which depends on the installation directory string, i.e.,

```shell
sudo update-alternatives --config java
```
or

```shell
readlink -f `which java`
```

The `JAVA_HOME` environment variable is defined as

```shell
readlink -f `which java` | sed "s:/bin/java::"
```

i.e., the `/bin/java` suffix of the penultimate command's output is excluded/removed. If the resulting string is `/usr/lib/jvm/java-19-openjdk-amd64`, then

```shell
export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```

Or rather, edit `/etc/environment` by appending the definition of `JAVA_HOME` at the end of the file.  An edit mode option is

```shell
sudo vi /etc/environment
```

Subsequently, append

```shell
JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).

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

# Navigate to Settings -> Emails ... within the *Primary email address* section 
# you will find a ...@users.noreply.github.com address that can be used for Git operations.
# Additionally, consider enabling - Keep my email addresses private 
git config --global user.email "...@users.noreply.github.com"

git config --global core.editor "vim --nofork"
git config --global init.defaultBranch master
```

Next, SSH key

```shell
ssh-keygen -t ed25519 -C "...@users.noreply.github.com"
$ Enter file in which to save the key ... [Default $\rightarrow$ ENTER.]
```

Beware, a key [re-write might be requested](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#:~:text=When%20you%27re%20prompted) if a key file already exists.  The command


```shell
cat ~/.ssh/id_ed25519.pub
```

prints the text for setting-up SSH key pair within a version control service.


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

* [Notepad++](https://notepad-plus-plus.org) / [Notepad++](https://github.com/notepad-plus-plus/notepad-plus-plus/releases)
* [Git for Windows](https://git-scm.com)
    * Editor: Select Notepad++
    * Default Branch Name: *master*
* Java: [JDK & JRE](https://adoptium.net/en-GB/temurin)
* [OpenOffice](https://www.openoffice.org/download/index.html)

<br>

### Windows Installations that Propagate to WSL Kernels


#### Docker Desktop

[Docker Desktop](https://www.docker.com/products/docker-desktop/)

Select
- [ ] Use WSL-2 instead of Hyper-V

Deselect
- [ ] Add shortcut to desktop


<br>


#### IntelliJ IDEA

* [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/?section=windows)


<br>


#### VS Code

Study the [Visual Studio CODE](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) installation [notes](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode#install-vs-code-and-the-wsl-extension).  Whilst installing VS Code

* Select Destination Location (This is about the installation directory)
* Select Start Menu Folder (Leave default text)
* Select Additional Tasks (Ensure `Add to PATH (requires shell restart)` is selected.  Deselect everything else.)

Subsequently, and after launching VS Code, install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack via the extension button.

<br>
<br>
<br>


## Addendum

### Git


#### Select Destination Location

<br>


#### Select Components

Deselect
- [ ] Additional icons 
  - [ ] On the Desktop
- [ ] Git LFS (Large File Support)
- [ ] Add a Git Bash Profile to Windows Terminal 

<br>


#### Select Start Menu Folder

Deselect
- [ ] Don't create a Start Menu folder

<br>


#### Choosing the default editor used by Git

Select
- Use Notepad++ as Git's default editor

<br>

#### Adjusting the name of the initial branch in new repositories

Select
- Override the default branch name for new repositories
  {master}

<br>

#### Adjusting your PATH environment

Select
- Git from the command line and also from 3rd-party software

<br>

#### Choosing the SSH executable

Select
- Use bundled OpenSSH

<br>

#### Choosing HTTPS transport backend

Select
- Use the OpenSSL library

<br>


#### Configuring the line ending conversions

Select
- Checkout Windows-style, commit Unix-style line endings

<br>

#### Configuring the terminal emulator to use with Git Bash

Select
- Use MinTTY (the default terminal of MSYS2)

<br>

#### Choose the default behaviour of `git pull`

Select
- Fast-forward or merge

<br>

#### Choose a credential helper

Select
- None

<br>

#### Configuring extra options

Select
- Enable file system caching

<br>

#### Configuring experimental options
 
- *Deselect all*

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>