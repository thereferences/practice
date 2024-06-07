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
          <h2 style="color: black;">Destination</h2>
          <p style="color: black;">Installation directory</p>
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
          <p style="color: black;">
          Select
          - Use Notepad++ as Git's default editor
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Adjusting the name of the initial branch in new repositories</h2>
          <p style="color: black;">
          Select
          - Override the default branch name for new repositories
            [master]
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Adjusting your PATH environment</h2>
          <p style="color: black;">
          Select
          - Git from the command line and also from 3rd-party software
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choosing the SSH executable</h2>
          <p style="color: black;">
          Select
          - Use bundled OpenSSH
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choosing HTTPS transport backend</h2>
          <p style="color: black;">
          Select
          - Use the OpenSSL library
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring the line ending conversions</h2>
          <p style="color: black;">
          Select
          - Checkout Windows-style, commit Unix-style line endings
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring the terminal emulator to use with Git Bash</h2>
          <p style="color: black;">
          Select
          - Use MinTTY (the default terminal of MSYS2)
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choose the default behaviour of `git pull`</h2>
          <p style="color: black;">
          Select
          - Fast-forward or merge
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Choose a credential helper</h2>
          <p style="color: black;">
          Select
          - None
          </p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="carousel-slide" style="background: #ffffff;">
        <div class="carousel-slide-copy ">
          <h2 style="color: black;">Configuring extra options</h2>
          <p style="color: black;">
          Select
          - Enable file system caching
          </p>
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
var Flickity;
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
