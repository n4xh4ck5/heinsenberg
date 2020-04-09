#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from utils.send_request import send_request


def manage_response (data):
    ports = None
    ip = None
    try:
        ip = str(data['ip_str'])
        ports = str(data['ports']).replace("[","").replace("]","")
        print ("Ports:"+ str(ports))
    except:
        print ("Not found information of the IP")
        ports = "-"

    finally:
        return ports


def shodan (target,api):
    r = None
    ports = []
    try:
        print("[*] Starting Shodan...\n")
        for ip in target:
            print ("[*]Target: " + str(ip))
            url = ("https://api.shodan.io/shodan/host/"+ip+"?key="+api)
            #Sent request
            r = send_request(url)
            # Manage the response
            port = manage_response(r)
            ports.append(str(port))

    except Exception as e:
        print ("Error in shodan function" + str(e))
    finally:
        return ports