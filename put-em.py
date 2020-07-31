import csv
import sys
import boto3

def load(file_path):
    session = boto3.Session(profile_name=profile)
    SSM = session.client('ssm')
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['key', 'value'])
        for row in reader:
            print(SSM.put_parameter(
                Name=row['key'],
                Value=row['value'],
                Type='String',
                Overwrite=True,
            ))
            
if __name__ == '__main__':
    file_path = sys.argv[1]
    profile = sys.argv[2]
    load(file_path)