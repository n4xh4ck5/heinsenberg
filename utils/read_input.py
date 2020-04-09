#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input(path):

    """ FUNCTION READ DOMAIN """
    d = []
    try:
        #Open file to read the input
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            d.append(line.rstrip('\n'))
        f.close()

    except Exception as exc:
        print ("Error in read_input" + str(exc))

    finally:
        return d
