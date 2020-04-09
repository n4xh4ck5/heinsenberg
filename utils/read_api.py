#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def read_api(path):
    d = []
    try:
        with open(path) as json_data:
            d = json.loads(json_data.read())
    except Exception as exc:
        print ("Error in read_api " + str(exc))

    finally:
        return d
