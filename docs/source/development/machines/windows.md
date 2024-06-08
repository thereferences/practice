<br>

# Fundamental Software: Windows

## Core

Foremost, install

* [Notepad++](https://notepad-plus-plus.org) / [Notepad++](https://github.com/notepad-plus-plus/notepad-plus-plus/releases)
* Java: [JDK & JRE](https://adoptium.net/en-GB/temurin)

<br>

### Open Office

Unload the core executable & language pack of [OpenOffice](https://www.openoffice.org/download/index.html).

<br>

### Git

Unload the executable at [git-scm](https://git-scm.com)

<br>

<div class="carousel-page-container">
  <div class="carousel-container">
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Select Destination Location</h2>
          <p style="color: black;">This installation directory.</p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2>Select Components</h2>
          Deselect            
            <ul style="list-style-type: '\2610';">
              <li>Additional icons<br>On the Desktop</li>
              <li>Git LFS (Large File Support)</li>
              <li>Add a Git Bash Profile to Windows Terminal</li>
            </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Select Start Menu Folder</h2>
          Deselect
          <ul style="list-style-type: '\2610';">
            <li>Don't create a Start Menu folder</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Choosing the default editor used by Git</h2>
          Select
          <ul style="list-style-type: '\268A';">
            <li>Use Notepad++ as Git's default editor</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Adjusting the name of the initial branch in new repositories</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Override the default branch name for new repositories [master]</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Adjusting your PATH environment</h2>
          Select          
          <ul style="list-style-type: '\2609';">
            <li>Git from the command line and also from 3rd-party software</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Choosing the SSH executable</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use bundled OpenSSH</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Choosing HTTPS transport backend</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use the OpenSSL library</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Configuring the line ending conversions</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Checkout Windows-style, commit Unix-style line endings</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Configuring the terminal emulator to use with Git Bash</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use MinTTY (the default terminal of MSYS2)</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Choose the default behaviour of `git pull`</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Fast-forward or merge</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Choose a credential helper</h2>
          Select          
          <ul style="list-style-type: '\2609';">
            <li>None</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Configuring extra options</h2>
          Select          
          <ul style="list-style-type: '\2610';">
            <li>Enable file system caching</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide">
        <div class="carousel-slide-copy">
          <h2 style="color: black;">Configuring experimental options</h2>
          <ul style="list-style-type: '\2610';">
            <li><b>Deselect all</b></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
<script>
let elem = document.querySelector(".carousel-container");
new Flickity(elem, {
    cellAlign: "right",
    contain: true,
    initialIndex: 2,
    pageDots: false,
    wrapAround: true,
    draggable: true,
    prevNextButtons: true,
    pauseAutoPlayOnHover: false
});
</script>

<br>
<br>

## Windows Installations that Propagate to WSL Kernels

### Docker Desktop

Unload [Docker Desktop](https://www.docker.com/products/docker-desktop/), subsequently install.  During installation

**Select**
- [x] Use WSL-2 instead of Hyper-V

**Deselect**
- [ ] Add shortcut to desktop


<br>


### IntelliJ IDEA Ultimate

Unload [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/?section=windows), subsequently install.  During the product's initial launch, a licence screen appears.  Activate your licence via one of the presented methods, e.g., via an **Activation Code**.


<br>


### VS Code

Study the [Visual Studio CODE](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) installation [notes](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode#install-vs-code-and-the-wsl-extension).  Whilst installing VS Code

* Select Destination Location (This is about the installation directory)
* Select Start Menu Folder (Leave default text)
* Select Additional Tasks (Ensure `Add to PATH (requires shell restart)` is selected.  Deselect everything else.)

Subsequently, and after launching VS Code, install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack via the extension button.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
