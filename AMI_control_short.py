# External Asterisk control via AMI

from calendar import c
from os import stat
import sys
import subprocess
import telnetlib
import time
import mysql.connector

def login (action_id, username = 'admin', password = 'huHFU2UG3Urt37JG932MVKLSkfdi2'):
    ami_resp = b'Asterisk Call Manager/'
    output = telnetObj.read_until(ami_resp)
    command_login = 'Login'
    action_id += 1
    ami_command_login_str = 'Action: {}\n' \
                            'ActionID: {}\n' \
                            'Username: {}\n' \
                            'Secret: {}\n\n'.format(command_login, action_id, username, password)
    ami_command_login = ami_command_login_str.encode('utf-8')
    telnetObj.write(ami_command_login)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    ami_resp = b'\r\n'
    output = telnetObj.read_until(ami_resp)
    return action_id

def new_channel_catch ():
    while True:
        ami_resp = b'\r\n'
        output = telnetObj.read_until(ami_resp)
        print(output)
        log = open(log_path, 'a')
        localtime = time.asctime( time.localtime(time.time()) )
        log.write(localtime + ' ')
        to_file = str(output, 'UTF-8')
        if len (to_file) > 2:
            splitted_row = to_file.split (": ")
            if splitted_row[0] == "Event":
                if splitted_row[1].strip() == "Newchannel":
                    log.write(to_file)
                    log.close()
                    currentchannel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    while True:
                        ami_resp = b'\r\n'
                        output = telnetObj.read_until(ami_resp)
                        print(output)
                        log = open(log_path, 'a')
                        localtime = time.asctime( time.localtime(time.time()) )
                        log.write(localtime + ' ')
                        to_file = str(output, 'UTF-8')
                        log.write(to_file)
                        log.close()
                        if len (to_file)<3:
                            channels[currentchannel[Uniqueid]] = currentchannel
                            print (channels[currentchannel[Uniqueid]])
                            print (channels)
                            break
                        splitted_row = to_file.split (": ")
                        if splitted_row[0] == "Privilege":
                            privilege = splitted_row[1].strip()
                        elif splitted_row[0] == "Channel":
                            currentchannel[Channel] = splitted_row[1].strip()
                        elif splitted_row[0] == "ChannelState":
                            currentchannel[ChannelState] = splitted_row[1].strip()
                        elif splitted_row[0] == "ChannelStateDesc":
                            currentchannel[ChannelStateDesc] = splitted_row[1].strip()
                        elif splitted_row[0] == "CallerIDNum":
                            currentchannel[CallerIDNum] = splitted_row[1].strip()
                        elif splitted_row[0] == "CallerIDName":
                            currentchannel[CallerIDName] = splitted_row[1].strip()
                        elif splitted_row[0] == "ConnectedLineNum":
                            currentchannel[ConnectedLineNum] = splitted_row[1].strip()
                        elif splitted_row[0] == "ConnectedLineName":
                            currentchannel[ConnectedLineName] = splitted_row[1].strip()
                        elif splitted_row[0] == "Language":
                            currentchannel[Language] = splitted_row[1].strip()
                        elif splitted_row[0] == "AccountCode":
                            currentchannel[AccountCode] = splitted_row[1].strip()
                        elif splitted_row[0] == "Context":
                            currentchannel[Context] = splitted_row[1].strip()
                        elif splitted_row[0] == "Exten":
                            currentchannel[Exten] = splitted_row[1].strip()
                        elif splitted_row[0] == "Priority":
                            currentchannel[Priority] = splitted_row[1].strip()
                        elif splitted_row[0] == "Uniqueid":
                            currentchannel[Uniqueid] = splitted_row[1].strip()
                            if currentchannel[Uniqueid] in channels:
                                print('=======================')
                        elif splitted_row[0] == "Linkedid":
                            currentchannel[Linkedid] = splitted_row[1].strip()
                            if currentchannel[Linkedid] in channels:
                                print('+++++++++++++++++++++++')
                            else:
                                thiscall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                thiscall[0] = localtime
                                thiscall[1] = currentchannel[Channel]
                                thiscall[2] = currentchannel[CallerIDNum]
                                thiscall[3] = currentchannel[CallerIDName]
                                thiscall[4] = currentchannel[Exten]
                                calls[currentchannel[Uniqueid]] = thiscall
                                print (calls)
                        else:
                            print ("Aaaaaaaaaaaaaaa, WTF!!!!!!!")
                else:
                    log.write(to_file)
                    log.close()
            else:
                log.write(to_file)
                log.close()
        else:
            log.write(to_file)
            log.close()
            break
    return (currentchannel)       

def check_status(CallerID):
    status = -1
    if CallerID == 677990:
        status = 0
    else:
        status - 1
return (status)



def channel_hangup(channelID):
    


# ****************** START ******************

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
action_id = 1
username = 'admin'
password = 'huHFU2UG3Urt37JG932MVKLSkfdi2'
telnetObj = telnetlib.Telnet("127.0.0.1", 5038)

Linkedid = 0
Uniqueid = 1
Priority = 2
Exten = 3
Context = 4
AccountCode = 5
Language = 6
ConnectedLineName = 7
ConnectedLineNum = 8
CallerIDName = 9
CallerIDNum = 10
ChannelStateDesc = 11
ChannelState = 12
Channel = 13
log_path = "/var/log/asterisk/AMI_005.log"
channels = {}
calls = {}

action_id = login (action_id, username, password)
new_channel = new_channel_catch()
CallerID = new_channel[CallerIDNum]
status = check_status(CallerID)
if status == 0:
