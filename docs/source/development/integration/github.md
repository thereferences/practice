
# The GitHub Route

Automatically delivering assets to Amazon Web Services (AWS) via GitHub, hence enabling continuous integration, delivery, and deployments.

## Identity Provider

Foremost, add the requisite identity provider

* Adding the [GitHub OIDC (Open Identifier Connect) identity provider to Amazon Web Services](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#adding-the-identity-provider-to-aws)

<br>

## Identity & Asset Management Role

Subsequently, create an AWS IAM (Identity & Asset Management) role for GitHub OIDC connections.

* [create](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create)
* [ascertain configuration](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create_GitHub)

During the policy step, select a policy, or policies, in relation to the purpose of this role, e.g., for delivering images to Amazon ECR (Elastic Container Registry) ([REF: Point 8](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create))

> ... IAM includes a list of the AWS managed and customer managed policies in your account. Select the policy to use for the permissions policy ...


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
