import json
import requests
from parse import *


def getRequirements(name_package):
    response = requests.get('https://pypi.org/pypi/' + name_package + '/json')
    pckg_json = json.loads(response.text)
    list = []
    try:
        for pack in pckg_json.get('info').get('requires_dist'):
            if pack.find("extra") == -1:
                temp_list = pack.split(' ')
                list.append(temp_list[0])
        for pack in list:
            print(name_package + ' -> ' + pack)
        try:
            for pack in list:
                getRequirements(pack)
        except TypeError: pass
    except TypeError:
        return


def main():
    name_package = input()
    getRequirements(name_package)


main()
