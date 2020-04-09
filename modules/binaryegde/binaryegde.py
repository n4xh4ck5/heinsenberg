#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def manage_response(data, flag):
    ports = []
    try:

        if flag == 1:  # 404
            ports = "-"  # If result = NULL
        else:
            for port in data['events']:
                print("Ports: " + str(port['port']))
                ports.append(str(port['port']))

    except Exception as exc:
        print("Error in manage_response " + str(exc))
        ports = "-"

    finally:
        return ports

def send_request(url, api):
    response = ""
    api_key = {'X-Key': api}
    flag = 0  # 0 = 200, 1=404
    try:
        response = requests.get(url, timeout=15, allow_redirects=True, headers=api_key)
        if response.status_code == 404:
            print("Not found information of the IP, pass the next")
            flag = 1
    except Exception as exc:
        response = "-"
        print("Error in send_request" + str(exc))
    finally:
        return response.json(), flag


def binaryegede (target,api):

    flag = 0
    r = None
    ports = []
    ports_array =[]
    try:
        print("\n[*] Starting BinaryEgede...\n")
        for ip in target:
            print ("[*]Target: " + str(ip))
            url ="https://api.binaryedge.io/v2/query/ip/{0}".format(ip)
            #Sent request
            (r,flag) = send_request(url,api)
            # Manage the response
            ports = manage_response(r,flag)
            ports_array.append(ports)

    except Exception as exc:
        print ("Error in main function " + str(exc))

    finally:
        return ports_array
