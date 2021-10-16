import ipaddress
import subprocess
import sys
import os
from prettyprinter import pprint
import re

iptables = '/sbin/iptables'
grep = '/bin/grep'

if not os.getuid() == 0:
    print("You must be root to change IPTables.")
    sys.exit(2)

"""
# for test purposes
first_line = ""
with open('nat.txt','r') as nats:
    for line in nats:
        first_line = line
        break
"""

bashCmd = [ iptables, '-t', 'nat', '-nvL', 'POSTROUTING', '--line' ];
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
first_line, error = process.communicate()

first_line = str(first_line)

lines = first_line.split('\\n')

rules = []
rules_null = []
for line in lines:
    stripped = line.strip()
    cols = re.sub('\s+',' ',stripped).split(' ')
    if len(cols) > 8:
        if re.findall("^172\.30\..+$", cols[8]) and re.findall("^SNAT$", cols[3]) and not re.findall("^172\.30\.0\.0/16$", cols[8]):
            mult = 1
            packets = cols[1]
            letter = cols[1][-1]
            if letter == "K":
                mult = 1000
                packets = int(packets.replace(letter,""))
            elif letter == "M":
                mult = 1000000
                packets = int(packets.replace(letter,""))
            elif letter == "G":
                mult = 1000000000
                packets = int(packets.replace(letter,""))
            elif letter == "T":
                mult = 1000000000000
                packets = int(packets.replace(letter,""))
            else:
                packets = int(packets)
            packets = packets*mult

            tup = (
                cols[0],
                packets,
                cols[7],
                cols[8],
                cols[9],
                re.sub("^to:","",cols[10])
            )

            if packets > 0:
                rules.append(tup)
            else:
                rules_null.append(tup)

rules_sorted = sorted(rules, key=lambda rule: rule[1], reverse=True)




if len(rules_null) > 0:
    rule_replace = ()
    rule_null_replace = rules_null[0]
    for rule_sorted in rules_sorted:
        net_prefix = ipaddress.ip_network(rule_sorted[3]).prefixlen
        if net_prefix == 22:
            rule_replace = rule_sorted
            break

    # if we have some rule for replacement
    if len(rule_replace) > 0:

        net_net_old = ipaddress.ip_network(rule_replace[3]).network_address
        net_broadcast_old = ipaddress.ip_network(rule_replace[3]).broadcast_address
        net_prefix_old = ipaddress.ip_network(rule_replace[3]).prefixlen

        if net_prefix_old == 22:
            net_prefix_new = 23
        elif net_prefix_old == 23:
            net_prefix_new = 24

        net1_net = net_net_old
        net1_prefix = net_prefix_new
        net1_broadcast = ipaddress.ip_network(str(net1_net)+"/"+str(net1_prefix)).broadcast_address
        net2_net = ipaddress.ip_network(net1_broadcast+1).network_address
        net2_prefix = net_prefix_new
        net2_broadcast = ipaddress.ip_network(str(net2_net)+"/"+str(net2_prefix)).broadcast_address

        

        print(
            iptables+" -t nat -R POSTROUTING "+rule_replace[0]+" -s "+str(net1_net)+"/"+str(net1_prefix)+" -d "+rule_replace[4]+" -o "+rule_replace[2]+" -j SNAT --to-source "+rule_replace[5]
        )

        print(
            iptables+" -t nat -R POSTROUTING "+rule_null_replace[0]+" -s "+str(net2_net)+"/"+str(net2_prefix)+" -d "+rule_null_replace[4]+" -o "+rule_null_replace[2]+" -j SNAT --to-source "+rule_null_replace[5]
        )


