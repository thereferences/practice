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
style="overflow:hidden; width:100%; height:330px; border:none;"
src="../../../../../assets/beforehand.html"></iframe>
<figure>
<figcaption>An illustration of a team member's interaction with cloud services</figcaption>
</figure>

<dl>
    <dt>Local mobile workstations</dt>
    <dd>For developing programs for data acquisition, programmatic data delivery to Amazon S3, data processing, features engineering, modelling, infrastructure as code (IAC), etc.</dd>
    <dt>GitHub & GitHub Actions</dt>
    <dd>For version control, code analysis, dependencies vulnerability analysis, building & storing container images, and trackable delivery of code assets to Amazon Web Services.</dd>
    <dt>Amazon Web Services</dt>
    <dd>For (a) secure storage of data, container images, models, and artefacts of models, (b) computing resources, and (c) designing, developing and testing machine learning systems solution architectures based on infrastructure-as-code programs</dd>
</dl>


#### Plausible Disruptions

* Data loss
* Data breach
* Data corruption; loss of integrity.
* Unavailable services/data due to platform malfunction


<br>
<br>

### Considerations & Contingencies vis-à-vis Disruptions

Overall, disruptions will impact project delivery times, and will cost money.  In future, and depending on the context, the 
team will have to consider a mix of financial, operational, legal, and/or regulatory impacts of disruptions.

<br>

#### Data Loss / Data Breach

**Confidentiality:** The team will only store open data, and their derivatives, within the cloud platform.  Therefore, 
confidentiality issues vis-à-vis sensitive or personal data are inapplicable.

**Recovery:** The back-up routes are (a) [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html), and (b) re-running the project's container images.

<br>

#### Data Corruption

* Raw Data: The back-up routes are (a) [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html), and (b) re-running the data acquisition image.
* Derived Data 

<br>

#### Unavailable Cloud Platform

Use a different computing hub to

* Retrieve the back-up container images from GitHub Container Registry [Container Images Registration: GitHub Container 
  Registry & Amazon Elastic Container Registry.]


<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
