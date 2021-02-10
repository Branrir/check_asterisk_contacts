# Icinga2/Nagios check for Asterisk Contacts

This script checks if any of contact not Available are.


## Installation

Run following on remote server:
```bash
cd /usr/lib/nagios/plugins
wget https://raw.githubusercontent.com/Branrir/check_proxmox_backup/master/check_proxmox_backup.py
chmod +x check_proxmox_backup.py
```


## Output

```bash
CRITICAL - Contact astproxy/sip:dmc@217.114.68.43:5060 - Unknown 
```