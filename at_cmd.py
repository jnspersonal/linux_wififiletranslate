#!/usr/bin/python

import re
import serial
import os

'''
def dealDataToSerial(stringATCmd, serialFd):
    if(None == re.match(stringATCmd, 'AT').span()):
        serialFd.port.write('AT+CIPSEND=4'.encode(gb2312))
        serialFd.port.write(stringATCmd)
        return
    serialFd.port.write(stringATCmd)
    response = serialFd.port()
    return response
'''
'''
def main():
    #打开串口
    serialFd =  serial.Serial('com5', 115200)

    listATCmd = ['AT', 'AT+CWJAP="301","15857108766"', 'AT+CIFSR', 'AT+CIPSTART="TCP","192.168.0.109",8888']
    for atcmd in listATCmd:
        #if(None == re.match(atcmd, 'AT').span()):
        serialFd.write(atcmd)
        response = serialFd.read()
        printf(response)

    while(1):
        stringSendMsg = raw_input(":")
        stringSendMsg.encode = 'gb2312'
        serialFd.write('AT+CIPSEND=4'.encode(gb2312))
        serialFd.write(stringSendMsg)
        response = serialFd.read()
        printf(response)


    serialFd.close()
    #关闭串口
main()
'''

serialFd =  serial.Serial('com5', 115200)
listATCmd = ['AT', 'AT+CWJAP="301","15857108766"', 'AT+CIFSR', 'AT+CIPSTART="TCP","192.168.0.109",8888']
for atcmd in listATCmd:
    #if(None == re.match(atcmd, 'AT').span()):
    atcmd = atcmd.encode('utf-8')
    serialFd.write(atcmd)
    response = serialFd.read()
    response = response.encode('gb2312')
    print(response)
while(1):
    stringSendMsg = input(":")
    stringSendMsg = stringSendMsg.encode('utf-8')
    serialFd.write('AT+CIPSEND=4'.encode('utf-8'))
    serialFd.write(stringSendMsg)
    response = response.encode('gb2312')
    print(response)
    if(response.encode('gb2312') == 'quit'.encode('gb2312')):
        break
