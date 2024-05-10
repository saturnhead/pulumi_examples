import pulumi
from pulumi_aws import ec2

# Create a new security group
security_group = ec2.SecurityGroup('my-security-group',
    description='Enable SSH access',
    ingress=[
        {'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0']},
    ])

# Create a new EC2 instance
instance = ec2.Instance('my-instance',
    instance_type='t2.micro',
    ami='ami-0905a3c97561e0b69',
    security_groups=[security_group.name])

pulumi.export('instance_id', instance.id)
pulumi.export('public_ip', instance.public_ip)




