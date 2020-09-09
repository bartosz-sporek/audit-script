## Table of content
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [To-Do](#to-do)
* [Images](#images)

## General info
Simple script which gathers a few informations (Windows version, host name, IP and MAC adress) and saves into the .xlsx file (Excel format).

## Technologies
```
Everything in "requirements.txt": DOWNLOAD -> RUN "pip install -r requirements.txt" -> PROFIT
```
- Python (of course),
- pandas,
- openpyxl,
- xlrd,
- re,
- subprocess,
- getmac.

## Setup
Everything you need to do is download the newest version of the <a href="https://github.com/bartosz-sporek/audit-script/releases">audit.rar</a>, extract it and open audit.exe file! The result will be saved in audit.xlsx file.

## To-Do
- [x] Add MAC gathering with adapters menu choose
- [x] Shrink setup - python and dependencies to .exe file
- [x] Before gather info generate Excel file with headers (Windows Version, Host Name, IP Adress, MAC Adress)
- [ ] Add Windows and Office (if exists) key gathering
- [ ] Add auto-adjusting cell width

## Images
![cmd](https://i.imgur.com/emkb52p.jpeg)
![Excel](https://i.imgur.com/zpRBZSc.jpeg)
