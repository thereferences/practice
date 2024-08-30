# Impact Assessment

The team does not have a standard workload.  Solutions that it designs, develops, tests, etc., will be delivered to 
clients/colleagues. This brief assessment considers a hypothetical, but partially representative, scenario.

```{contents} Table of Contents
:depth: 1
:local:
```

## SCENARIO

### Project in focus

The design, development, and delivery of a machine learning product that will forecast particulate matter levels for a small geographic area. The client will use it to dynamically control traffic flow into the area.

<br>

### Assets stored within the cloud platform

In this case, the assets are **(a)** raw data, **(b)** processed data, **\(c\)** engineered features, **(d)** image 
containers, and **(e)** developed models & artefacts.

<br>

### Design, development, and resources zones

These are:

<ul class="disc">
<li class="disc"><b>Local mobile workstations</b><br>
  For developing programs <b>for</b> data acquisition, programmatic data delivery to Amazon S3, data processing, features engineering, modelling, infrastructure as code (IAC), etc.</li>
<li class="disc"><b>GitHub & GitHub Actions</b><br>
  For version control, code analysis, dependencies vulnerability analysis, building & storing container images, and
  trackable delivery of code assets to Amazon Web Services.</li>
<li class="disc"><b>Amazon Web Services</b><br>
  For <b>(a)</b> secure storage of data, container images, models, and artefacts of models, <b>(b)</b> computing resources, and
  <b>(c)</b> designing, developing and testing machine learning systems solution architectures based on infrastructure-as-code programs.</li>
</ul>


<iframe style="overflow:hidden; width:100%; height:330px; border:none;" src="../../../../../assets/beforehand.html"></iframe>
<figure>
  <figcaption>An illustration of a team member's interaction with cloud services</figcaption>
</figure>

<br>

### Plausible Disruptions

The plausible disruptions are:

<ul class="disc">
  <li class="disc">Data loss</li>
  <li class="disc">Data breach</li>
  <li class="disc">Data corruption; loss of integrity.</li>
  <li class="disc">Unavailable services/data due to platform malfunction</li>
</ul>



<br>
<br>


## CONSIDERATION & CONTINGENCIES VIS-À-VIS DISRUPTIONS

Overall, disruptions will impact project delivery times, and will cost money.  In future, and depending on the context, the 
team will have to consider a mix of financial, operational, legal, and/or regulatory impacts of disruptions.

<br>

### Data Loss / Data Breach

Steps:

<ul class="disc">
  <li class="disc"><b>Confidentiality:</b> The team will only store open data, and their derivatives, within the cloud platform.  Therefore, 
  confidentiality issues vis-à-vis sensitive or personal data are inapplicable.</li>
  <li class="disc"><b>Recovery:</b> The back-up routes are <b>(a)</b> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html" target="_blank">AWS Back-up for Amazon S3 (Simple Storage Service)</a>, and <b>(b)</b> re-running the project's container images.</li>
</ul>

<br>

### Data Corruption

**Recovery:** The back-up routes are **(a)** [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html), and **(b)** re-running the data acquisition, data processing, features engineering, modelling, etc., images.

<br>

### Unavailable Cloud Platform

**Contingency**: Use a different computing hub to **(a)** retrieve the back-up container images from GitHub Container Registry, and **(b)** run the containers. [Each container image registration is via GitHub Container Registry (GCR) and Amazon Elastic Container Registry (ECR).]


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
