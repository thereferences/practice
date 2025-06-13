# Threat Actors

:::{dropdown} Table of Contents
```{contents}
:depth: 1
:local:
:backlinks: top
```
:::

<br>

## Background

Each team member must be cognizant of threat actors, i.e., entities or individuals that conduct malicious cyber activities, e.g.,

<ul class="disc">
<li class="disc">Exploit vulnerabilities, e.g., <a href="https://www.technologyreview.com/2021/09/23/1036140/2021-record-zero-day-hacks-reasons/" target="_blank">zero-day</a> vulnerabilities.</li>
<li class="disc">Data theft via unauthorised access to computing assets.</li>
<li class="disc">Intentional disabling or destruction of computing assets, or disruption of services.</li>
</ul>

The actors have varying <a href="https://www.sophos.com/en-us/cybersecurity-explained/threat-actors#:~:text=are%20Threat%20Actors%E2%80%99-,Motivations,-%3F" target="_blank">motivations</a>. Threat actors will exploit unprotected or insufficiently secured attack surfaces.

Potential threat actors are listed below. Presently, the most probable threat actor is an insider. However, as the team **(a)** grows, **(b)** starts delivering products & services, and **\(c\)** engages with a wider range of internal & external entities – the threat likelihood per actor increases. [Intellectual property theft, data theft, etc., by external entities will become much more probable.]

<ul class="disc">
<li class="disc">Insiders, i.e., employees or contractors.</li>
<li class="disc">Cyber criminals.</li>
<li class="disc">Hackers.</li>
<li class="disc">State actors.</li>
</ul>



<br>
<br>


## Protection

The [Cyber Security Body of Knowledge](https://www.cybok.org/knowledgebase1_1/) is a helpful cyber security reference text.  Practically, the team will be guided by the <a href="https://www.sophos.com/en-us/cybersecurity-explained/threat-actors#:~:text=Protection%20Methods%20and-,Strategies,-Maintaining%20strict%20cyber">SOPHOS</a> protection proposals, e.g.,

<dl>
    <dt>Risk Assessment</dt><dd>The risks & mitigation policies page addresses this.<br></dd>
    <dt>Security Policies & Procedures</dt><dd>The risks & mitigation policies page addresses this.<br></dd>
    <dt>Enforce Access Control</dt><dd>Zero privilege approach. Initially, each team member will have a zero privileges account, i.e., Amazon Web Services products will be inaccessible. Privileges will be set, and withdrawn, via IAM (Identity & Access Management) roles, and trust policies thereof. Mandatory multi-factor authentication for cloud tools, e.g., Amazon Web Services, GitHub, etc.<br></dd>
    <dt>Automatic Code Scanning, Code Vulnerability Alerts</dt>
    <dd>GitHub <a href="https://docs.github.com/en/code-security/dependabot" target="_blank">DEPENDEABOTS</a>, GitHub <a href="https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql" target="_blank">CodeQL</a><br></dd>
</dl>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
