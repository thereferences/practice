<br>

# Machines

<br>

:::{admonition} In Progress
<br>
:::

All the organisation's computer usage rules apply; remember, Universal Serial Bus (USB) sticks are disallowed.

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


```{toctree}
:caption: Content
:glob:

machines/*
```

<br>
<br>

## Addendum

<br>
<br>

<div class="carousel-page-container">
  <div class="carousel-container">
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Select Destination Location</h2>
          <p style="color: black;">This installation directory.</p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #cccccc;">
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
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Select Start Menu Folder</h2>
          Deselect
          <ul style="list-style-type: '\2610';">
            <li>Don't create a Start Menu folder</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choosing the default editor used by Git</h2>
          Select
          <ul style="list-style-type: '\268A';">
            <li>Use Notepad++ as Git's default editor</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Adjusting the name of the initial branch in new repositories</h2>
          Select
          <ul style="list-style-type: '\268A';">
            <li>Override the default branch name for new repositories [master]</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Adjusting your PATH environment</h2>
          Select          
          <ul style="list-style-type: '\2609';">
            <li>Git from the command line and also from 3rd-party software</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choosing the SSH executable</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use bundled OpenSSH</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choosing HTTPS transport backend</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use the OpenSSL library</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring the line ending conversions</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Checkout Windows-style, commit Unix-style line endings</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring the terminal emulator to use with Git Bash</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Use MinTTY (the default terminal of MSYS2)</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choose the default behaviour of `git pull`</h2>
          Select
          <ul style="list-style-type: '\2609';">
            <li>Fast-forward or merge</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choose a credential helper</h2>
          Select          
          <ul style="list-style-type: '\2609';">
            <li>None</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring extra options</h2>
          Select          
          <ul style="list-style-type: '\268A';">
            <li>Enable file system caching</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring experimental options</h2>
          <ul style="list-style-type: '\2610';">
            <li>*Deselect all*</li>
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
