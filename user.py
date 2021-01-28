# coding: utf-8

import json
import hashlib


# def sha256(s):
#     return hashlib.sha256(s.encode("utf-8")).hexdigest()
# not used

def login(user, pass_):
    data = []
    with open("./user.json") as f:
        data = json.load(f)
    ldata = {"username": user, "password": pass_}
    return ldata in data
