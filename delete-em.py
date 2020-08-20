import csv
import sys
import boto3

def load(prefix):
    session = boto3.Session(profile_name=profile)
    SSM = session.client('ssm')
    paginator = SSM.get_paginator('describe_parameters')
    params_iterator = paginator.paginate(ParameterFilters=[{'Key':"Name",'Option':"Contains",'Values':[prefix]}])
    for page in params_iterator:
        for item in page['Parameters']:
            SSM.delete_parameter(Name=item['Name'])
                
if __name__ == '__main__':
    prefix = sys.argv[1]
    profile = sys.argv[2]
    load(prefix)