# Icinga2/Nagios check for Asterisk Contacts

This script checks if any of contact not Available are.


## Installation

Run following on remote server:
```bash
cd /usr/lib/nagios/plugins
wget https://raw.githubusercontent.com/Branrir/check_proxmox_backup/master/check_proxmox_backup.py
chmod +x check_proxmox_backup.py
```

## Parameter

| Parameter | Description |
| --- | --- |
| -h, --help | Shows help |
| -x, --exclude | Exclude specific contact (can be used multiple times) |

## Example usage

```bash
check_asterisk_contact.py -x astproxy/sip:dmc@123.123.123.123:5060
```

## Output

```bash
CRITICAL - Contact astproxy/sip:dmc@123.123.123.123:5060 - Unknown 
```