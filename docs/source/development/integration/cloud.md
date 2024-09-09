
# Amazon Web Services

After connecting to an Amazon Web Services (AWS) account, directly or via an identity service, the `AWS access portal` screen appears.  The details therein are critical to setting up programmatic access to AWS directly.

:::{dropdown} Table of Contents
```{contents}
:depth: 2
:local:
:backlinks: top
```
:::

<br>

## Programmatic Access

### Install AWS CLI

Foremost, install [AWS CLI (Command Line Interface)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions).  If using a machine that has Windows Subsystem for Linux, install `aws cli` within Windows, and relevant Linux Kernels, however all the steps below should be repeated within Windows; all outcomes propagate to Linux Kernels.

<br>

### Basic Configuration

Via key parameters and arguments.

<img src="../../_static/images/aws_access_portal.png" alt="Access Portal">

The key values of the `aws configure` parameters are set via the directives below.  Use the image above, and below, to determine most of the parameter values, i.e., the values in brackets. 

```shell
aws configure set sso_session {sso.session.string} --profile default
aws configure set sso_account_id {account id} --profile default
aws configure set sso_role_name {aws sso role name} --profile default
aws configure set region {region} --profile default

# Refer to the notes below
aws configure set output {output.string} --profile default
```

Notes: 
* The value of the `sso_session` parameter is user dependent.  It is a string that names a session, e.g., to name a session `alpha`
  > aws configure set sso_session **alpha** --profile default

* `aws configure` output [options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-config-output).  Example
  > aws configure set output **json** --profile default


<br>

### Single Sign On (SSO) Configuration

The image above has a link named `Access keys`; each account within a portal page will have its own `Access keys` link.  Within your AWS access portal, click on the Access keys link of the account of interest.  A pop-up, similar to   

<img src="../../_static/images/aws_access_credentials.png" alt="Access Credentials">


Type

```shell
aws configure sso
```

Subsequently, and aided by the image above, answer the questions below

```command
SSO session name [sso.session.string]: {sso.session.string}
SSO start URL [None]: {url}
SSO region [None]: {region}
SSO registration scopes [sso:account:access]: sso:account:access
```

<br>

### Hence, Programmatic Single Sign On (SSO)


```shell
aws sso login --profile {profile.name}
```


<br>
<br>

## Testing Programmatic Access

### Via Command Line

[Listing Amazon S3 objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html).

```shell
aws s3 ls
```

[Listing the images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html) of an Amazon ECR (Elastic Container Registry) repository of an account.

```shell
aws ecr list-images --registry-id {account.identifer} --repository-name {repository.name}
```

<br>

### Via Software Programs

:::{note} 
A link is upcoming.
:::


<br>
<br>

## References

* <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html"><abbr title="Amazon Web Services">AWS</abbr> <abbr title="Command Line Interface">CLI</abbr> with <abbr title="Identity & Access Management">IAM</abbr> Identity Centre</a>
* [IAM (Identity & Access Management) Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
* [Amazon Web Services Managed Policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html)
* [Changing or setting a region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
