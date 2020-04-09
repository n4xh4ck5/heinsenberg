# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" LIBRARIES"""
import argparse
import sys
import json

from modules.binaryegde.binaryegde import binaryegede
from modules.censys.censys import censys
from modules.onyphe.onyphe import onyphe
from modules.sh0d4n.sh0d4n import shodan
from utils.export_results import export_results
from utils.read_api import read_api
from utils.read_input import read_input
from utils.visu_results import visu_results

""" IMPORT MODULES """

def banner ():

    """ FUNCTION BANNER"""

    print ("""   
                                                                                                                                             
     __              _                                  __                              
    [  |            (_)                                [  |                             
     | |--.  .---.  __   _ .--.   .--.  .---.  _ .--.   | |.--.   .---.  _ .--.  .--./) 
     | .-. |/ /__\\[  | [ `.-. | ( (`\]/ /__\\[ `.-. |  | '/'`\ \/ /__\\[ `/'`\]/ /'`\; 
     | | | || \__., | |  | | | |  `'.'.| \__., | | | |  |  \__/ || \__., | |    \ \._// 
    [___]|__]'.__.'[___][___||__][\__) )'.__.'[___||__][__;.__.'  '.__.'[___]   .',__`  
                                                                               ( ( __)) """)
    print (" \n")
    print ( """ *** Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge
        ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
        ** Version 1.0
        ** DISCLAMER: This tool was developed for educational goals. 
        ** Github: https://github.com/n4xh4ck5/
        ** The author is not responsible for using to others goals.
        ** A high power, carries a high responsibility!""" )

def help ():
    """FUNCTION HELP"""
    print (""" \nTool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge

        			Example of usage: python heisenberg.py -i input.txt""")

def main (argv):
    """ FUNCTION MAIN"""
    parser = argparse.ArgumentParser(
        description="Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-e', '--export',
                        help="File in xlsx format which contains the ports opened (y/n)",
                        required=False)
    parser.add_argument('-i', '--input', help="Input in txt with the IP's which it wants to analyze",
                        required=True)
    parser.add_argument('-a', '--api', help="Input in json with the API key of the services. Please, read the example file",
                        required=True)
    args = parser.parse_args()

    """ local var"""
    path = args.input # Get input file
    output = args.export #Get output
    api = args.api # Get API key
    target =[] # list to save the input IP
    api_keys = []
    shodan_ports = []
    censys_ports = []
    onyphe_ports = []
    binaryedge_ports = []

    # functions banner and help
    banner()
    help()

    #Validate input parameters
    if output is None:
        output ='n'
    output = output.lower()
    if (output != 'y' and output != 'n'):
        print ("Incorrect output format selected")
        exit (1)
    try:
        #Read input parameters
        target = read_input (path)
        #Read API keys
        api_keys = read_api(api)
        api_shodan = api_keys['api_shodan']
        api_censys_secret = api_keys ['censys_secret']
        api_censys_uid = api_keys['censys_uid']
        api_onyphe = api_keys ['onyphe_api']
        api_binaryegde = api_keys ['binaryedge_api']

        #call The different API's
        #Shodan
        shodan_ports = shodan(target,api_shodan)
        #censys
        censys_ports = censys(target, api_censys_secret, api_censys_uid)
        #onyphe
        onyphe_ports = onyphe(target, api_onyphe)
        #BinaryEgede
        binaryedge_ports = binaryegede(target,api_binaryegde)

        # Print results
        #Shodan
        print ("\n[*] Print results Shodan: \n")
        visu_results(target, shodan_ports)
        #censys
        print ("\n[*] Print results Censys: \n")
        visu_results(target, censys_ports)
        #onyphe
        print ("\n[*] Print results onyphe: \n")
        visu_results(target, onyphe_ports)
        #binaryegede
        print ("\n[*] Print results BinaryEdge: \n")
        visu_results (target, binaryedge_ports)

        #Export results
        if output =='y':
            export_results (target,shodan_ports,censys_ports, onyphe_ports,binaryedge_ports)


    except Exception as exc:
        print ("Error in main funcion" + str(exc))

# CALL MAIN
if __name__ == "__main__":
   main(sys.argv[1:])