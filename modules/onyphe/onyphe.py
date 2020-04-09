#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.send_request import send_request


""" FUNCTION TO MANAGE THE RESPONSE"""
def manage_response (data):
    ports = []
    try:
        for port in data['results']:
            print ("Ports:" + str(port['port']))
            ports.append(str(port['port']))

    except Exception as exc:
        print ("Not found information of the IP" + str(exc))
        ports = "-"

    finally:
        return ports

def onyphe(target, api):

    r = None
    port=None
    ports = []
    try:
        print("\n[*] Starting Onpyhe...\n")
        for ip in target:
            print ("[*]Target: " + str(ip))
            url ="https://www.onyphe.io/api/synscan/{0}?apikey={1}".format(ip, api)
            #Sent request
            r = send_request(url)
            # Manage the response
            port = manage_response(r)
            ports.append(port)

    except Exception as exc:
        print ("Error in main function " + str(exc))
    finally:
        return ports
