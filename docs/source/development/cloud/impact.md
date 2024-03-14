<br>

Impact Assessment
=================

<br>

:::{important}
The impact of inaccessible/unavailable cloud services on team operations and services.
:::

<br>

The team does not have a standard workload.  Solutions that it designs, develops, tests, etc., will be delivered to 
clients/colleagues. This brief assessment considers a hypothetical, but partially representative, scenario.


##


### Scenario


#### Project in focus

The design, development, and delivery of a machine learning product that will forecast particulate matter levels for a small geographic area. The client will use it to dynamically control traffic flow into the area.


#### Assets stored within the cloud platform

* Raw Data
* Processed Data
* Engineered Features
* Image Containers
* Developed Models & Artefacts


#### Design, development, and resources zones

<iframe
style="overflow:hidden; width:100%; height:500px; border:none;"
src="../../../../../assets/beforehand.html"></iframe>

<dl>
    <dt>Local mobile workstations</dt>
    <dd>For developing programs for data acquisition, programmatic data delivery to Amazon S3, data processing, features engineering, modelling, infrastructure as code (IAC), etc.</dd>
    <dt>GitHub & GitHub Actions</dt>
    <dd>For version control, code analysis, dependencies vulnerability analysis, building & storing container images, and trackable delivery of code assets to Amazon Web Services.</dd>
    <dt>Amazon Web Services</dt>
    <dd>For (a) secure storage of data, container images, models, and artefacts of models, (b) computing resources, and (c) designing, developing and testing machine learning systems solution architectures based on infrastructure-as-code programs</dd>
</dl>


#### Plausible Disruptions

* Inaccessible services due to platform malfunction

#### Financial, operational, legal, regulatory impacts of disruptions

* Project delivery times, which also impacts finances.

<br>

### Contingencies

#### Built-in redundancies.

* Container Images Registration: GitHub Container Registry & Amazon Elastic Container Registry.
* Raw Data: The back-up routes are (a) [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.amazon.  com/AmazonS3/latest/userguide/backup-for-s3.html), and (b) re-running the data acquisition image.


<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
