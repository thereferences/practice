# Amazon Web Services & Solution Architectures

Hover over an illustration's symbols for more details; some have links to further details.  Images only have captions.  Over 
time, more Amazon Web Services (AWS) details will be added.

<br>

:::{dropdown} Table of Contents
```{contents}
:depth: 1
:local:
:backlinks: top
```
:::

<br>

## DELIVERING ASSETS

<iframe style="overflow:hidden; width:100%; height:330px; border:none; margin-left:65px" 
        src="../../../../../assets/beforehand.html"></iframe>
<figure>
<figcaption>For more details hover over the icons; a few icons have links to more details.  Assets, e.g., 
container images, will be automatically & securely delivered to Amazon Web Services (AWS) via GitHub.  The illustration highlights security tools along transfer paths.    [Independent code analysis via <a 
href="https://github.com/enqueter/pollutants/actions/runs/8443640990/job/23127661393" target="_blank">CodeQL</a>, and continuous integration and delivery via GitHub Actions &rarr;  <a href="https://github.com/enqueter/pollutants/actions/runs/8443640949" target="_blank">Actions</a>/<a href="https://github.com/enqueter/pollutants/actions/runs/8443640949/workflow" target="_blank">Actions Code</a>] 
</figcaption>
</figure>

<br>
<br>

## INTERACTING

### Elastic Compute Cloud

<br>

#### With a public subnet

<iframe style="overflow:hidden; width:100%; height:430px; border:none; margin-left:65px"
        src="../../../../../assets/ec2.html"></iframe>
<figure>
<figcaption>In general, containers will be run via the <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html" target="_blank">Fargate</a> option of Amazon's <abbr title="Elastic Container Service">ECS</abbr>. Sometimes, containers will be tested via an EC2 (Elastic Cloud Compute) using a set-up such as this; launched via a launch template.  Within each team member's machine AWS CLI (Command Line Interface) will be configured to use the <a href="https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso" target="_blank">AWS Identity & Access Management's identity centre for authentication.
</a></figcaption>
</figure>

<br>

:::{dropdown} A launch template example: redacted.
```json
{
    "EbsOptimized": false,
    "IamInstanceProfile": {
        "Arn": "{amazon.resource.name}"
    },
    "BlockDeviceMappings": [
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "Encrypted": false,
                "DeleteOnTermination": true,
                "Iops": 3000,
                "VolumeSize": 29,
                "VolumeType": "gp3",
                "Throughput": 125
            }
        }
    ],
    "NetworkInterfaces": [
        {
            "AssociatePublicIpAddress": true,
            "DeleteOnTermination": true,
            "Description": "",
            "DeviceIndex": 0,
            "Groups": [
                "{security.group.identifier}"
            ],
            "InterfaceType": "interface",
            "Ipv6Addresses": [],
            "SubnetId": "{subnet.identifier}",
            "NetworkCardIndex": 0
        }
    ],
    "ImageId": "{amazon.machine.image.identifier}",
    "InstanceType": "{instance.type.code}",
    "KeyName": "{key.pair.name}",
    "Monitoring": {
        "Enabled": false
    },
    "Placement": {
        "AvailabilityZone": "{availability.zone}",
        "GroupName": "",
        "Tenancy": "default"
    },
    "DisableApiTermination": false,
    "InstanceInitiatedShutdownBehavior": "terminate",
    "TagSpecifications": [
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "cost",
                    "Value": "free tier"
                }
            ]
        }
    ],
    "CreditSpecification": {
        "CpuCredits": "standard"
    },
    "CapacityReservationSpecification": {
        "CapacityReservationPreference": "open"
    },
    "HibernationOptions": {
        "Configured": false
    },
    "MetadataOptions": {
        "HttpTokens": "required",
        "HttpPutResponseHopLimit": 2,
        "HttpEndpoint": "enabled",
        "HttpProtocolIpv6": "disabled",
        "InstanceMetadataTags": "disabled"
    },
    "EnclaveOptions": {
        "Enabled": false
    },
    "PrivateDnsNameOptions": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    },
    "MaintenanceOptions": {
        "AutoRecovery": "default"
    },
    "DisableApiStop": false
}
```
:::

<br>
<br>

#### With a private subnet

<iframe style="overflow:hidden; width:100%; height:485px; border:none; margin-left:65px" 
        src="../../../../../assets/endpoint-connect.html"></iframe>
<figure>
<figcaption>Similar to the previous illustration, using a private subnet requires a slightly different design.  Click on the 
Private Subnet symbol link to read more.  Within each team member's machine AWS CLI (Command Line Interface) will be configured to use <a 
href="https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso" title="Amazon Web Services (AWS) Identity & Access Management (IAM) Identity Centre (IC)">AWS IAM IC</a> for authentication.</figcaption>
</figure>

<br>
<br>
<br>

### Simple Storage Service (S3)

<iframe style="overflow:hidden; width:100%; height:430px; margin-left:65px; border:none;" src="../../../../../assets/endpoint-interface.html"></iframe>
<figure>
<figcaption>Interacting with Amazon S3 (Simple Storage Service) via <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html" target="_blank">AWS CLI (Command Line Interface)</a> and a private subnet. Within each team member's machine AWS CLI will be configured to use <a href="https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso" title="Amazon Web Services (AWS) Identity & Access Management (IAM) Identity Centre (IC)">AWS IAM IC</a> for authentication.</figcaption>
</figure>


<br>
<br>
<br>
<br>


## AUTO

### Via Step Functions

```{image} ../../../../assets/step-functions.png
:alt: Step Functions
:width: 65%
```
<figure>
<figcaption>Deploying an end-to-end solution via <a href="https://docs.aws.amazon.com/step-functions/latest/dg/welcome.
html" target="_blank">step functions</a>, an orchestration service. The underlying infrastructure code outlines (a) 
executions via Amazon's Elastic Container Service [Fargate], (b) virtual private cloud settings per case, alongside 
securty group and subnet settings, (c) notification settings, (d) time-boxing/auto-termination, (e) and much more.
</figcaption>
</figure>

<br>

:::{dropdown} The underlying infrastructure code of the above; redacted.
```json
{
  "Comment": "An example",
  "StartAt": "daily task",
  "TimeoutSeconds": 3600,
  "States": {
    "daily task": {
      "Type": "Task",
      "Resource": "arn:aws:states:::ecs:runTask.sync",
      "Parameters": {
        "LaunchType": "FARGATE",
        "Cluster": "arn:aws:ecs:{region.name}:{identifier}:cluster/{cluster.name}",
        "TaskDefinition": "arn:aws:ecs:{region.name}:{identifier}:task-definition/{task.definition}",
        "NetworkConfiguration": {
          "AwsvpcConfiguration": {
            "Subnets": [
              "{subnet.identifier}",
              "{subnet.identifier}",
              "{subnet.identifier}"
            ],
            "SecurityGroups": [
              "{security.group.identifier}"
            ],
            "AssignPublicIp": "..."
          }
        }
      },
      "Next": "distributions task",
      "Catch": [
        {
          "ErrorEquals": [
            "States.ALL"
          ],
          "Next": "Notify Failure",
          "Comment": "The daily task"
        }
      ],
      "Comment": "The daily task succeeded.  Next, the distributions task."
    },
    "distributions task": {
      "Type": "Task",
      "Resource": "arn:aws:states:::ecs:runTask.sync",
      "Parameters": {
        "LaunchType": "FARGATE",
        "Cluster": "arn:aws:ecs:{region.name}:{identifier}:cluster/{cluster.name}",
        "TaskDefinition": "arn:aws:ecs:{region.name}:{identifier}:task-definition/{task.definition}",
        "NetworkConfiguration": {
          "AwsvpcConfiguration": {
            "Subnets": [
              "{subnet.identifier}",
              "{subnet.identifier}",
              "{subnet.identifier}"
            ],
            "SecurityGroups": [
              "{security.group.identifier}"
            ],
            "AssignPublicIp": "..."
          }
        }
      },
      "Next": "Notify Success",
      "Catch": [
        {
          "ErrorEquals": [
            "States.ALL"
          ],
          "Comment": "The distributions task",
          "Next": "Notify Failure"
        }
      ],
      "Comment": "The distributions task succeeded."
    },
    "Notify Success": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:{region.name}:{identifier}:{topic}",
        "Message.$": "$"
      },
      "End": true
    },
    "Notify Failure": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:{region.name}:{identifier}:{topic}",
        "Message.$": "$"
      },
      "End": true
    }
  }
}
```
:::

<br>

:::{dropdown} Afterwards
```{image} ../../../../assets/step-functions-afterwards.png
:alt: Step Functions
:width: 85%
```
:::

<br>
<br>
<br>

### Elastic MapReduce (EMR)

<iframe
style="overflow:hidden; width:100%; height:375px; border:none; margin-left:65px"
src="../../../../../assets/emr.html"></iframe>
<figure>
<figcaption>An illustration of an EMR (Elastic MapReduce) cluster set-up.  The set-up includes virtual private cloud 
settings, security groups, auto-termination settings, and much more.  The team's launch templates repository, i.e., 
infrastructure code templates repository, will be visible during the upcoming weeks.
</figcaption>
</figure>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
