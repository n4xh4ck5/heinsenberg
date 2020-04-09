#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests


def manage_response(data):
    protocols = None
    try:
        for port in data['results']:
            protocols = port["protocols"]
        for k in protocols:
            print("Port: " + k.split("/")[0] + " Protocol:" + k.split("/")[1])

    except:
        print("Not found information of the IP")
        protocols = '[-]'
    finally:
        return protocols


def send_request(url, ip, secret, uid):

    response = None
    target = {'query': ip, 'flatten': True}
    try:

        response = requests.post(url + "/search/ipv4", json=target, auth=(uid, secret), timeout=20,
                                 allow_redirects=True)
        if response.status_code != 200:
            print("Error to connect Censys API")
    except Exception as exc:
        print("Error in send_request" + str(exc))
    finally:
        return response.json()


def censys (target, secret, uid):

    r = None
    ports =[]
    array_ports =[]
    try:
        print ("\n[*] Starting censys...\n")
        for ip in target:
            print ("[*]Target:" + str(ip))
            url ="https://censys.io/api/v1"
            #Sent request
            r = send_request(url,ip,secret,uid)
            # Manage the response
            ports = manage_response(r)
            array_ports.append(ports)

    except Exception as exc:
        print ("Error in censys function " + str(exc))
    finally:
        return array_ports
