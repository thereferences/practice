<br>

# Cloud Platform Solutions Architectures

<br>

:::{note}
:class: margin
Ths page will be continuously updated.
:::

Hover over an illustration's symbols for more details; some have links to further details.  Images only have captions.  
With time, more details will be added.

<br>

## Delivering Assets

<iframe 
    style="overflow:hidden; width:100%; height:330px; border:none;" 
    src="../../../../../assets/beforehand.html"></iframe>
<figure>
<figcaption>Assets, e.g., container images, will be delivered to the cloud platform via a version controlled route, i.e., 
via GitHub.</figcaption>
</figure>

<br>
<br>

## Interacting

### Elastic Compute Cloud

<iframe
style="overflow:hidden; width:100%; height:450px; border:none;"
src="../../../../../assets/ec2.html"></iframe>
<figure>
<figcaption>In general, containers will be run via the Fargate option of Amazon's Elastic Container Service.  Sometimes, 
containers will be tested via an EC2 (Elastic Cloud Compute) using a set-up such as this; launched via a launch 
template.</figcaption>
</figure>

:::{dropdown} A launch template example
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

<iframe
style="overflow:hidden; width:100%; height:450px; border:none;"
src="../../../../../assets/endpoint-connect.html"></iframe>
<figure>
<figcaption>An illustration</figcaption>
</figure>

<br>

### Simple Storage Service (S3)

<iframe
style="overflow:hidden; width:100%; height:450px; border:none;"
src="../../../../../assets/endpoint-interface.html"></iframe>
<figure>
<figcaption>An illustration</figcaption>
</figure>


<br>
<br>


## Auto

### Via Step Functions

```{image} ../../../../assets/step-functions.png
:alt: Step Functions
:width: 65%
```
<figure>
<figcaption>Step functions; alternative pipelines, with all the appropriate security settings.
</figcaption>
</figure>

<br>

### A Schema for a Step Functions Solution

```{image} ../../../../assets/pattern-emr.png
:alt: Elastic MapReduce
:width: 65%
```

<br>

### Elastic MapReduce (EMR)

<iframe
style="overflow:hidden; width:100%; height:450px; border:none;"
src="../../../../../assets/emr.html"></iframe>
<figure>
<figcaption>An illustration of an infrastructure-as-code launch of an EMR (Elastic MapReduce) cluster.  The code includes,
virtual private cloud settings, security groups, auto-termination settings, and much more.  The team's launch templates 
repository will be visible during the upcoming weeks.
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
