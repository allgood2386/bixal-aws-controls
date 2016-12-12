"""This module turns off AWS instances."""
# !/usr/bin/python

import argparse
import boto3

parser = argparse.ArgumentParser(description='Stop AWS EC2 AMI instances.')
parser.add_argument('AWS-EC2-IDS',
                    type=str,
                    nargs='+',
                    help='A list of AMI Id\'s.')

parser.add_argument('--region',
                    '-r',
                    default='us-east-1',
                    help='The region where your instances are located. ' +
                    'Typically us-east-1, NOT us-east-1a.')

args = parser.parse_args()
argsdict = vars(args)

ec2 = boto3.resource('ec2',
                     region_name=argsdict['region'])

response = dict()
for arg in argsdict['AWS-EC2-IDS']:
    instance = ec2.Instance(arg)
    instance.stop()
