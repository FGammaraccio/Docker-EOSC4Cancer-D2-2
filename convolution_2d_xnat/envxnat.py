#!/usr/bin/env python
import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



versionNumber='1.0.0'
dateString='20240618'
author='Feriel'
progName=sys.argv[0].split('/')[-1]
idstring = '$Id: %s,v %s %s %s Exp $'%(progName,versionNumber,dateString,author)

# nsdict = {'xnat':'http://nrg.wustl.edu/xnat',
#            'xsi':'http://www.w3.org/2001/XMLSchema-instance'}

# def ns(namespace, tag):
#     return "{%s}%s" % (nsdict[namespace], tag)

# def schemaLoc(namespace):
#     return "{0} https://www.xnat.org/schemas/{1}/{1}.xsd".format(nsdict[namespace], namespace)

# def randstring(length):
#     return ''.join(random.choice(string.lowercase) for i in range(length))

def envvar():

    parser = argparse.ArgumentParser(description='Generate QC Manual Assessor XML file')
    parser.add_argument('-v', '--version',
                        help='Print version number and exit',
                        action='version',
                        version=versionNumber)
    parser.add_argument('--idstring',
                        help='Print id string and exit',
                        action='version',
                        version=idstring)
    parser.add_argument('subjectLabel', help='Subject label')
    parser.add_argument('sessionId', help='Session id')
    parser.add_argument('project', help='Project')
    parser.add_argument('xnat_host', help='XNAT Host')
    parser.add_argument('xnat_user', help='XNAT Username')
    parser.add_argument('xnat_pass', help='XNAT Password')
    args=parser.parse_args()


    subjectLabel = args.subjectLabel
    sessionId = args.sessionId
    project = args.project
    

    xnat_host = args.xnat_host
    xnat_user = args.xnat_user
    xnat_pass = args.xnat_pass
    
    return project, subjectLabel, sessionId, xnat_host, xnat_user, xnat_pass
