#!/usr/bin/env python
import boto3
import logging
import argparse


def main():
    getdata()
    searchdata()


def getdata():
    ec2 = boto3.resource('ec2')
    file = open("datalake.txt", "w")
    for instance in ec2.instances.all():
        print(instance.id, instance.state, instance.ami_launch_index, instance.architecture, instance.block_device_mappings, instance.instance_type, instance.kernel_id, instance.launch_time, instance.state_reason, instance.state_transition_reason, instance.subnet_id, instance.tags, instance.vpc_id, instance.security_groups, instance.public_ip_address, instance.private_ip_address, file=open("datalake.txt","a"))


def searchdata():
    for line in open("datalake.txt"):
        if "INTSA" in line:
            print(line)


if __name__ == "__main__":
    main()
