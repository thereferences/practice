
# Python

## Fundamentals

Please use the <a href="https://peps.python.org/pep-0008/">PEP (Python Enhancement Proposal) 8 Style Guide for 
Python</a>.  Always refer to the naming conventions guide, for example:

<br>

<table style="width: 85%;">
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

## Importing Modules

Abide by the HitchHiker's Guide to Python's best practice & readability advice vis-à-vis [importing modules](https://docs.python-guide.org/writing/structure/#modules).  Hence, please use the import format `import math`, and use a method of the module via pattern

```python
import math

math.cos(...)
```

<br>

**Not**

```shell
from math import cos
```

<br>

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
