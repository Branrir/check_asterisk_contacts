#!/usr/bin/python3
import sys
import subprocess

try:
    import argparse
except Exception as e:
    print ("Missing module:{0}".format(e))
    sys.exit(255)

# Return Codes
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

class contact_state:
    state = None
    name = None
    latency = None

    def parse_line(self, line):
        self.state = line.split(' ')[1]
        self.name = line.split(' ')[0]
        self.latency = line.split(' ')[2]
    
    def get_state(self):
        return self.state

    def get_name(self):
        return self.name

    def get_latecy(self):
        return self.latency

def main():
    states = []
    cons = []
    tmp_str = []
    ok_str = []
    result = subprocess.check_output(["/usr/sbin/asterisk -rx 'pjsip show contacts'| awk '{print $2, $4, $5}'"], shell=True).decode("utf-8").splitlines()
    
    # populate exclude list
    exclude = args['exclude']
        
    # parse lines
    for line in result:
        if "@" in line:
            c = contact_state()
            c.parse_line(line)
            cons.append(c)

    # states
    for con in cons:
        state = con.get_state()
        name = con.get_name()
        latency = con.get_latecy()
        if state != "Avail" and state not in exclude:
            states.append(CRITICAL)
            tmp_str.append('Contact {0} - {1} \n'.format(name, state))
        else:
            ok_str.append('Contact {0} - {1} ms'.format(name, latency))

    tmp_str = '\n'.join(tmp_str)
    ok_str = '\n'.join(ok_str)

    # check states
    if CRITICAL in states:
        print('CRITICAL - ' + tmp_str)
        sys.exit(CRITICAL)
    if WARNING in states and CRITICAL not in states:
        print('WARNING - ' + tmp_str)
        sys.exit(WARNING)
    if (CRITICAL or WARNING) not in states:
        print('OK - ' + ok_str)
        sys.exit(OK)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--exclude', help='Exclude sip contact', action='append', default=[])
    args = vars(parser.parse_args())
    main()
