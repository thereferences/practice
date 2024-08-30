<br>

# Risks & Mitigation Policies

<br>

## Data Breach

An unauthorised data, or information, access.

<dl>
<dt>Risk</dt><dd>Threaten cloud systems via corruption of storage systems and their content.</dd>
<dt>Mitigation</dt><dd>Mandatory two-factor authentication via FIDO (Fast Identity Online) Keys.</dd>
</dl>

<br>
<br>


## Attack Surface

The known and unknown routes via which an entities cloud asset can be infiltrated.

<dl>
    <dt>Risk</dt><dd>The corruption of cloud assets and the underlying systems, unauthorised access and distribution of 
data, reputation damage, financial loss. Endangerment of lives, if personal or sensitive data is present.</dd>
    <dt>Mitigation</dt>
    <dd>    
        Data [Classify Data Sets: Open, Sensitive, Personal.]    
        <ul class="disc">
          <li class="disc">Do not store sensitive or personal data within the team's cloud account.</li>
          <li class="disc">Encrypt all data sets; Amazon S3 (Simple Storage Service) <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html">encrypts by default</a>.</li>
          <li>Authorise and withdraw access to data via IAM (Identity &amp; Management) roles.</li><li>Delete redundant data assets.</li>
        </ul>    
        Compute Services
        <ul class="disc">
          <li class="disc">Authorise and withdraw access to compute services via IAM (Identity &amp; Management) roles, and trust policies thereof.</li>
          <li class="disc">Delete redundant compute assets.</li>
        </ul>    
        Architectures
        <ul class="disc"><li class="disc">Defensive, limited privileges, compute solutions architectures; refer to the architectures pages.</li></ul>    
    </dd>
</dl>

<br>
<br>


## Malware Infections

Software that enables the unauthorised installer to take control of a system by disrupting it or causing strategic damage.

<dl>
    <dt>Risk</dt>
    <dd>Industrial Espionage<br>
    <ul class="disc">
        <li class="disc">The theft of confidential, sensitive, etc., data or information.</li>
        <li class="disc">The theft of intellectual property, processes, ideas, techniques, etc.</li></ul>
    </dd>
    <dt>Mitigation [<a href="https://www.ncsc.gov.uk/pdfs/guidance/mitigating-malware-and-ransomware-attacks.pdf" target="_blank">Mitigating malware 
and ransomware attacks</a>]</dt>
    <dd>
      Cloud
      <ul class="disc">
          <li class="disc">Enforce multi-factor authentication; the default of GitHub &amp; Amazon Web Services.</li>
          <li class="disc"><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html" target="_blank">Encrypt all data sets.</a></li>
          <li class="disc">Backup data sets; <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html" target="_blank">Amazon Web Services Backup for Amazon S3 (Simple Storage Service)</a>.</li>
          <li class="disc">Limit access to cloud assets via the <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html" target="_blank">inbound rules of security groups</a>.</li>
          <li class="disc">Authorise and withdraw access to assets via IAM (Identity &amp; Management) roles.</li>
          <li class="disc">Restricted data delivery: Programmatic data delivery via data science team members only.</li>
          <li class="disc">Termination of instances immediately after use.</li><li>Prepare an incident contingency.</li></ul>
      Client
      <ul class="disc"><li class="disc">Interaction with cloud services via virtual private networks.</li></ul>
    </dd>
</dl>


<br>
<br>


## Insider Threats

Threats due to employees not adhering to security rules.

<dl>
    <dt>Risk</dt>
    <dd>Infiltration risks, and all the damages thereof.</dd>
    <dt>Mitigation</dt>
    <dd>At least:
      <ul class="disc">
      <li class="disc">Always-on virtual private network.</li>
      <li class="disc">Using compute services via infrastructure-as-code templates that always feature
          <ul class="disc">
          <li class="disc"><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html" target="_blank">VPC</a>(Virtual Private Cloud)</li>
          <li class="disc"><a href="https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html" target="_blank">Subnet</a></li>
          <li class="disc"><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html" target="_blank">Security Groups</a>: For controlling inbound &amp; outbound rules</li></ul>
      </li>
      </ul>
    </dd>
</dl>


<br>
<br>


## Zero Day Vulnerability

An unknown software security flaw; the developers are unaware of its existence.

<dl>
    <dt>Risk</dt>
    <dd>Include:<ul class="disc">
        <li class="disc">Zero-day exploits.</li>
        <li class="disc">Zero-day attacks.</li></ul></dd>
    <dt>Mitigation</dt>
    <dd>Local<ul class="disc">
        <li class="disc">Continuous, automatic, software updates</li>
        <li class="disc">Limited pool of applications.</li>
        <li class="disc">Firewall</li>
        <li class="disc">Network interactions via virtual private network only.</li></ul>
        Cloud
        <ul class="disc">
        <li class="disc">Always use the latest compute services &amp; software.</li></ul></dd>
</dl>

<br>
<br>


## Data Loss

The loss of data due to a natural disaster, malfunction, etc.

<dl>
    <dt>Risk</dt><dd>The loss of all data intelligence, e.g., engineered features, developed models, model artefacts, exploratory &amp; trend analysis, etc.</dd>
    <dt>Mitigation</dt><dd>
    At least:
    <ul class="disc">
    <li class="disc">Backup data sets: <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html" target="_blank">Amazon Web Services Backup for Amazon S3 (Simple Storage Service)</a></li>
    <li class="disc">Programmatic production of all data intelligence/products, via version controlled software programs; hence the wherewithal to reproduce all lost items.  This is a mandatory team practice.</li>
    </ul>
</dd>
</dl>

<br>
<br>


## Deficient Access Controls

Deficient access controls to cloud, and complementary, assets.

<dl>
  <dt>Risk</dt>
  <dd>
    Include:
    <ul class="disc">
    <li class="disc">An unnecessarily wider attack surface via which threat actors can conduct malicious activities.</li>
    <li class="disc">Financial loss, e.g, by using unaffordable products that were not intended for use by the organisation/team.</li></ul></dd>
  <dt>Mitigation</dt>
  <dd>
    Amazon Web Services (AWS)
    <ul class="disc">
    <li class="disc">Programmatic access to Amazon Web Services products via limited privileges roles &amp; trust policies. [Automatic temporary credentials via AWS Command Line Interface Single Sign On]</li>
    <li class="disc">Limited, zero, privileges by default.<br></li>
    <li class="disc">The continuous development and availability of launch templates, with security settings and limited assets privileges, for launching computing products.</li>
    <li class="disc">The team's cloud leads must use multi-factor authentication to access AWS online.  [Multi-factor authentication by default.]</li></ul>
    GitHub
    <ul class="disc"><li>Mandatory multi-factor authentication.</li><li>SSH (Secure Shell) command line interactions.</li></ul>
  </dd>
</dl>

<br>
<br>

## Hijacking (Cloud)

The take-over of a cloud account by a threat actor.

<dl>
    <dt>Risk</dt><dd>Theft and disruption, hence reputation and financial losses.</dd>
    <dt>Mitigation</dt><dd>Protect the infiltration route, e.g., interact with cloud services via virtual private networks 
only.</dd>
</dl>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
