import subprocess
import re
from getmac import get_mac_address

def getCmdResult(command, first, second):

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tmp = proc.stdout.read()

    systeminfo = str(tmp, 'utf-8', errors='ignore')

    strippedCmd = ((systeminfo[(systeminfo.find(first)):(systeminfo.find(second))]).replace(first, "")).strip()

    return strippedCmd

def getMac():
    proc = subprocess.run("netsh interface show interface", stdout=subprocess.PIPE)
    tmp = proc.stdout

    systeminfo = str(tmp, errors='ignore')

    adapters = re.findall('(Et.*|Wi.*).*\r\n', systeminfo)
    activeStatus = re.findall('Connected|Disconnected', systeminfo)


    i=1
    for adapter in adapters:

        print(f'{str(i)}. {adapter} ({activeStatus[i-1]})')
        i+=1

    choice = input("\nMAC adress of which adapter do you need? ")

    chosenAdapter = adapters[int(choice)-1]

    win_mac = get_mac_address(interface=chosenAdapter)

    return [win_mac]

def winVer():

    winVersion = getCmdResult('systeminfo', "OS Name:", "OS Version:")
    winNum = getCmdResult('systeminfo', "Build", "OS Manufacturer:")

    return [winVersion + " " + winNum]


def hostName():

    hostName = getCmdResult('systeminfo', "Host Name:", "OS Name")

    return [hostName]

def ipAdress():
    
    ip = getCmdResult('ipconfig /all', "IPv4 Address. . . . . . . . . . . :", "Subnet Mask")

    ipFinal = ip.replace("(Preferred)", "")

    return [ipFinal]

print("Gathering info...")