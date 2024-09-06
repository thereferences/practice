
# Local, GitHub, Amazon

After connecting to an Amazon Web Services (AWS) account directly or via an identity service, the `AWS access portal` screen appears.  The details herein are for ...


<img src="../../_static/images/aws_access_portal.png" alt="Access Portal">

Foremost, the key values of the `aws configure` parameters are set via the directives below.  Use the image above, and below, to determine most of the parameter values; the values enclosed in brackets. 

aws configure set sso_session {sso.session.string} --profile default
aws configure set sso_account_id {account id} --profile default
aws configure set sso_role_name {aws sso role name} --profile default
aws configure set region {region} --profile default
aws configure set output {output.string} --profile default

The


aws configure sso

SSO session name [sso.session.string]: {sso.session.string}
SSO start URL [None]: {url}
SSO region [None]: {region}
SSO registration scopes [sso:account:access]: sso:account:access



* <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html"><abbr title="Amazon Web Services">AWS</abbr> <abbr title="Command Line Interface">CLI</abbr> with <abbr title="Identity & Access Management">IAM</abbr> Identity Centre</a>
* [IAM (Identity & Access Management) Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
* [Amazon Web Services Managed Policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html)
* [Changing or setting a region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)
