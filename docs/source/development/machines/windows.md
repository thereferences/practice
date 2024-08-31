<br>

# Fundamental Software: Windows

<br>

## Core

### Basic Tools

Foremost, install

* [Notepad++](https://notepad-plus-plus.org) / [Notepad++](https://github.com/notepad-plus-plus/notepad-plus-plus/releases)
* Java: [JDK & JRE](https://adoptium.net/en-GB/temurin)

<br>

### Open Office

Unload the core executable & language pack of [OpenOffice](https://www.openoffice.org/download/index.html).

<br>

### Git

Unload the executable at [git-scm](https://git-scm.com), and install.  During installation use the text slides below as a guide.

<br>

::::{card-carousel} 2

:::{card} Select Destination Location<br><br>
This installation directory.
:::
:::{card} Select Components<br><br>
Deselect            
  <ul class="deselect">
    <li class="deselect">Additional icons On the Desktop</li>
    <li class="deselect">Git LFS (Large File Support)</li>
    <li class="deselect">Add a Git Bash Profile to Windows Terminal</li>
  </ul>
:::
:::{card} Select Start Menu Folder<br><br>
Deselect
  <ul class="deselect">
    <li class="deselect">Don't create a Start Menu folder</li>
  </ul>
:::
:::{card} Choosing the default editor used by Git<br><br>
Select
  <ul class="select">
    <li class="select">Use Notepad++ as Git's default editor</li>
  </ul>
:::
:::{card} Adjusting the name of the initial branch in new repositories<br><br>
Select
  <ul class="point">
    <li class="point">Override the default branch name for new repositories [master]</li>
  </ul>
:::
:::{card} Adjusting your PATH environment<br><br>
Select          
  <ul class="point">
    <li class="point">Git from the command line and also from 3rd-party software</li>
  </ul>
:::
:::{card} Choosing the SSH executable<br><br>
Select          
  <ul class="point">
    <li class="point">Use bundled OpenSSH</li>
  </ul>
:::
:::{card} Choosing HTTPS Transport Backend<br><br>
Select          
  <ul class="point">
    <li class="point">Use the OpenSSL library</li>
  </ul>
:::
::::

<br>

Continuing $\ldots$


::::{card-carousel} 2

:::{card} Configuring the line ending conversions<br><br>
Select
  <ul class="point">
    <li class="point">Checkout Windows-style, commit Unix-style line endings</li>
  </ul>
:::
:::{card} Configuring the terminal emulator to use with Git Bash<br><br>
Select
  <ul class="point">
    <li class="point">Use MinTTY (the default terminal of MSYS2)</li>
  </ul>
:::
:::{card} Choose the default behaviour of `git pull`<br><br>
Select
  <ul class="point">
    <li class="point">Fast-forward or merge</li>
  </ul>
:::
:::{card} Choose a credential helper<br><br>
Select          
  <ul class="point">
    <li class="point">None</li>
  </ul>
:::
:::{card} Configuring extra options<br><br>
Select          
  <ul style="list-style-type: '\2611'; margin-left: 35px;">
    <li style="list-style-type: '\2611'; padding-left: 5px;">Enable file system caching</li>
  </ul>
:::
:::{card} Configuring experimental options<br><br>
  <ul class="deselect">
    <li class="deselect"><b>Deselect all</b></li>
  </ul>
  <br><br>
:::
::::

<br>
<br>

## Installations that Propagate to WSL Kernels

### Docker Desktop

Unload [Docker Desktop](https://www.docker.com/products/docker-desktop/), subsequently install.  During installation

- [x] Use WSL-2 instead of Hyper-V  [**Select**]
- [ ] Add shortcut to desktop [**Deselect**]


<br>


### IntelliJ IDEA Ultimate

Unload [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/?section=windows), subsequently install.  During the product's initial launch, a licence screen appears.  Activate your licence via one of the presented methods, e.g., via an **Activation Code**.

<br>

### VS Code

Study the [Visual Studio CODE](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) installation [notes](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode#install-vs-code-and-the-wsl-extension).  Whilst installing VS Code

<ul class="disc">
  <li class="disc">Select Destination Location (This is about the installation directory)</li>
  <li class="disc">Select Start Menu Folder (Leave default text)</li>
  <li class="disc">Select Additional Tasks (Ensure `Add to PATH (requires <i>shell</i> restart)` is selected.  Deselect everything else.)</li>
</ul>

Subsequently, and after launching VS Code, install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack via the extension button.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
