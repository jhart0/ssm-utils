import csv
import sys
import boto3

def load(file_path, prefix):
    session = boto3.Session(profile_name=profile)
    SSM = session.client('ssm')
    paginator = SSM.get_paginator('get_parameters_by_path')
    with open(file_path, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        params_iterator = paginator.paginate(Path=prefix, Recursive=True)
        for page in params_iterator:
            for item in page['Parameters']:
                writer.writerow([item['Name'], item['Value']])
                
if __name__ == '__main__':
    file_path = sys.argv[1]
    profile = sys.argv[2]
    prefix = sys.argv[3]
    load(file_path, prefix)