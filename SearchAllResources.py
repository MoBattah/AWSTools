import boto3
import logging
import argparse


def main():
    getData()

def getData():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(instance.id, instance.state)
if __name__ == "__main__":
    main()