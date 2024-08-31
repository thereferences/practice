
# Fundamental Software: Linux

Apriori

```shell
sudo apt update
sudo apt upgrade
```

<br>

Additionally, often inspect the GNU Privacy Guard (<abbr title="GNU Privacy Guard">GPG</abbr>) keys via:

```shell
gpg --list-keys
gpg --list-secret-keys
```

<br>

:::{dropdown} Table of Contents
```{contents}
:depth: 1
:local:
:backlinks: top
```
:::



## WGET

The <a href="https://www.gnu.org/software/wget/manual/wget.html" target="_blank">wget</a> utility - check if `wget` exists

```shell
wget --version
```

<br>

Installing `wget`, `ca-certificates`

```shell
sudo apt install wget ca-certificates
```

<br>

`ca-certificates` allows applications that are secure sockets layer (SSL) dependent to verify the authenticity of SSL connections; SSL is a deprecated tool.

<br>

## Java

### Installing: Java

[Further details](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04)

```shell
# jdk & jre
sudo apt install openjdk-19-jdk-headless
java --version
javac --version
```

<br>

### Environment Variables: Java

The environment variable of interest is the `JAVA_HOME` variable, which depends on the installation directory string, i.e.,

```shell
sudo update-alternatives --config java
```
or

```shell
readlink -f `which java`
```

<br>

The `JAVA_HOME` environment variable is defined as

```shell
readlink -f `which java` | sed "s:/bin/java::"
```

<br>

i.e., the `/bin/java` suffix of the penultimate command's output is excluded/removed. If the resulting string is `/usr/lib/jvm/java-19-openjdk-amd64`, then

```shell
export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```


<br>

Or rather, edit `/etc/environment` by appending the definition of `JAVA_HOME` at the end of the file.  An edit mode option is

```shell
sudo vi /etc/environment
```

<br>

Subsequently, append

```shell
JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```

<br>

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).

<br>

## GIT

Update `git` via the `git-core/ppa` <abbr title="Personal Package Archive">PPA</abbr> (Personal Package Archive).

```shell
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt list --upgradable
sudo apt install git-all
```

<br>

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

<br>

Next, SSH key

```shell
ssh-keygen -t ed25519 -C "...@users.noreply.github.com"
$ Enter file in which to save the key ... [Default $\rightarrow$ ENTER.]
```

<br>

Beware, a key [re-write might be requested](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#:~:text=When%20you%27re%20prompted) if a key file already exists.  The command

```
cat ~/.ssh/id_ed25519.pub
```

prints the text for setting-up SSH key pair within a version control service.  For instances whereby multiple accounts have to be managed per git client, e.g., study [GitHub Multiple Accounts](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts).

<br>

## CONDA [Optional]

This is for readers that sometimes need to develop outwith a container, i.e., within a virtual environment of the host machine instead.  Installation is via `miniconda`.  Foremost, check the python version

```shell
python --version
```

<br>

### The Installer

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell
# if python 3.10.*
sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_24.4.0-0-Linux-x86_64.sh
cd Downloads
sudo chmod +x Miniconda3-py310_24.4.0-0-Linux-x86_64.sh
```

<br>

### Install

Install in the specified directory

```shell
# Include <-b> for automatic acceptance of the terms & conditions
sudo bash Miniconda3-py310_24.4.0-0-Linux-x86_64.sh -p /opt/miniconda3

$ Do you wish the installer to initialize Miniconda3 by running conda init?
>>> no
```

<br>

### Set the Path Variable

Open `/etc/profile`, i.e.,

```shell
sudo vi profile
```

and append

```shell
if ! [[ $PATH =~ "/opt/miniconda3/bin" ]]; then
	PATH="/opt/miniconda3/bin:$PATH"
fi
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).  **Exit** the terminal.

<br>

### Set-up

Next, within a new terminal

```shell
conda init bash
conda config --set auto_activate_base false
sudo chown -R $USER:$USER /opt/miniconda3
```

<br>

### Upkeep

Update [conda](https://docs.conda.io/projects/conda/en/4.14.x/index.html) via

```shell
conda update -n base -c anaconda conda
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
