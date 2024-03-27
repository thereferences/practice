<br>

Python
======

<br>

:::{note}
:class: margin
In progress.  A brief introduction to the code of practice for Python programming
:::

Please use the <a href="https://peps.python.org/pep-0008/">PEP (Python Enhancement Proposal) 8 Style Guide for 
Python</a>.  Always refer to the naming conventions guide, for example:

<br>

<table style="width: 85%; border: 0; border-spacing: 5px; margin-left: 35px">
    <colgroup>
        <col span="1" style="width: 26.5%;">
        <col span="1" style="width: 63.5%;">
    </colgroup>
    <thead><tr style="text-align: left"><th>Object</th><th>Note</th></tr></thead>
        <tr><td>Type Variable Name</td><td>Always pascal case, e.g., HyperParameter.</td></tr>
        <tr><td>Class Name</td><td>Always pascal case.</td></tr>
        <tr><td>Variable Name</td><td>A lower case or snake case string, e.g., <i>length</i>, `number_of_cities` Use two leading underscores for private variables.</td></tr>
        <tr><td>Constants</td><td>The PEP pages note that <a href="https://peps.python.org/pep-0008/#constants" target="_blank">constants</a> <q><i>... are usually defined on a 
module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.</i></q></td></tr>
</table>

<br>

## Importing

In line with the HitchHiker's Guide to Python, best practice & readability override all else.  Hence, please use the import format  ...

```shell
import math
```

Subsequently, use a method as required, e.g.,

```shell
math.cos(...)
```

**Not**

```shell
from math import cos
```

**Not**

```shell
from math import *
```

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
