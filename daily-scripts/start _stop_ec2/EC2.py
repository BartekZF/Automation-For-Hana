###### TO DO ######
### Combine into one script
### Execute from OS level - Test how to pass credentials
### Create an template in AWX tower
### Pass credentials for AWS to AWX
### Execute Job and see what will happend
###################
### AWS LAMBDA FOR STOP EC2###
import boto3

ec2 = boto3.resource('ec2')

all_instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
print ('Running instances: ')
print (all_instances)
def lambda_handler(event, context):
    
    filter = [{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:Status', 'Values':['Test']}]

    instances = [i for i in ec2.instances.filter(Filters=filter)]

    instances_to_stop = [to_stop for to_stop in all_instances if to_stop.id  in [i.id for i in instances]]
 
    for instance in instances_to_stop:
        instance.stop()
        print(instance.id)
        
    return 'OK'

    ###AWS LAMBDA FOR START EC2###

import boto3

ec2 = boto3.resource('ec2')

all_instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])]
print ('Stopped instances: ')
print (all_instances)
def lambda_handler(event, context):
    
    filter = [{'Name': 'instance-state-name', 'Values': ['stopped']}, {'Name':'tag:Status', 'Values':['Test']}]

    instances = [i for i in ec2.instances.filter(Filters=filter)]

    instances_to_stop = [to_stop for to_stop in all_instances if to_stop.id  in [i.id for i in instances]]
 
    for instance in instances_to_stop:
        instance.start()
        print('Starting: ')
        print(instance.id)
        
    return 'OK'

