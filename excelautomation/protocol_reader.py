'''
Created on 01.08.2023

@author: neumann
'''

from pprint import pprint


def open_protocol(filename):
    result = []
    with open(filename) as protocol_file:
        protocol = protocol_file.readlines()

    for line in protocol:
        result.append(line.split(';'))
    
    return result.copy()
    
if __name__ == '__main__':
    pprint(open_protocol('protocol.txt'))

