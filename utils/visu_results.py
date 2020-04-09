#!/usr/bin/env python
# -*- coding: utf-8 -*-


def visu_results (targets,ports):
    # Start from the first cell. Rows and columns are zero indexed.
    i = 0
    try:
        for port in ports:
                print ("[*] Target: "+ str(targets[i]) + " Port: " + str(port))
                i+=1

    except Exception as exc:
        print ("Error in visu_results" + str(exc))