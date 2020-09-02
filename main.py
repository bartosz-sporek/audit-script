import subprocess


def cmdResult(command, first, second):

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tmp = proc.stdout.read()

    systeminfo = str(tmp, 'utf-8', errors='ignore')

    strippedCmd = ((systeminfo[(systeminfo.find(first)):(systeminfo.find(second))]).replace(first, "")).strip()

    return strippedCmd

def winVer():

    winVersion = cmdResult('systeminfo', "OS Name:", "OS Version:")
    winNum = cmdResult('systeminfo', "Build", "OS Manufacturer:")

    return [winVersion + " " + winNum]


def hostName():

    hostName = cmdResult('systeminfo', "Host Name:", "OS Name")

    return [hostName]

def ipAdress():
    
    ip = cmdResult('ipconfig /all', "IPv4 Address. . . . . . . . . . . :", "Subnet Mask")

    ipFinal = ip.replace("(Preferred)", "")

    return [ipFinal]

print("Gathering info...")