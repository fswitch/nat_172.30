### NAT rules in Linux

There are 50 real IP addresses for NAT clients.  
Fake real IPs are 333.333.333.[1-50]
Clients network 172.30.0.0/16
```
iptables -t nat -A POSTROUTING -s 172.30.0.0/22 -o eth1 -j SNAT --to-source 333.333.333.1
iptables -t nat -A POSTROUTING -s 172.30.4.0/22 -o eth1 -j SNAT --to-source 333.333.333.2
iptables -t nat -A POSTROUTING -s 172.30.8.0/22 -o eth1 -j SNAT --to-source 333.333.333.3
iptables -t nat -A POSTROUTING -s 172.30.12.0/22 -o eth1 -j SNAT --to-source 333.333.333.4
iptables -t nat -A POSTROUTING -s 172.30.16.0/22 -o eth1 -j SNAT --to-source 333.333.333.5
iptables -t nat -A POSTROUTING -s 172.30.20.0/22 -o eth1 -j SNAT --to-source 333.333.333.6
iptables -t nat -A POSTROUTING -s 172.30.24.0/22 -o eth1 -j SNAT --to-source 333.333.333.7
iptables -t nat -A POSTROUTING -s 172.30.28.0/22 -o eth1 -j SNAT --to-source 333.333.333.8
iptables -t nat -A POSTROUTING -s 172.30.32.0/22 -o eth1 -j SNAT --to-source 333.333.333.9
iptables -t nat -A POSTROUTING -s 172.30.36.0/22 -o eth1 -j SNAT --to-source 333.333.333.10
iptables -t nat -A POSTROUTING -s 172.30.40.0/22 -o eth1 -j SNAT --to-source 333.333.333.11
iptables -t nat -A POSTROUTING -s 172.30.44.0/22 -o eth1 -j SNAT --to-source 333.333.333.12
iptables -t nat -A POSTROUTING -s 172.30.48.0/22 -o eth1 -j SNAT --to-source 333.333.333.13
iptables -t nat -A POSTROUTING -s 172.30.52.0/22 -o eth1 -j SNAT --to-source 333.333.333.14
iptables -t nat -A POSTROUTING -s 172.30.56.0/22 -o eth1 -j SNAT --to-source 333.333.333.15
iptables -t nat -A POSTROUTING -s 172.30.60.0/22 -o eth1 -j SNAT --to-source 333.333.333.16
iptables -t nat -A POSTROUTING -s 172.30.64.0/22 -o eth1 -j SNAT --to-source 333.333.333.17
iptables -t nat -A POSTROUTING -s 172.30.68.0/22 -o eth1 -j SNAT --to-source 333.333.333.18
iptables -t nat -A POSTROUTING -s 172.30.72.0/22 -o eth1 -j SNAT --to-source 333.333.333.19
iptables -t nat -A POSTROUTING -s 172.30.76.0/22 -o eth1 -j SNAT --to-source 333.333.333.20
iptables -t nat -A POSTROUTING -s 172.30.80.0/22 -o eth1 -j SNAT --to-source 333.333.333.21
iptables -t nat -A POSTROUTING -s 172.30.84.0/22 -o eth1 -j SNAT --to-source 333.333.333.22
iptables -t nat -A POSTROUTING -s 172.30.88.0/22 -o eth1 -j SNAT --to-source 333.333.333.23
iptables -t nat -A POSTROUTING -s 172.30.92.0/22 -o eth1 -j SNAT --to-source 333.333.333.24
iptables -t nat -A POSTROUTING -s 172.30.96.0/22 -o eth1 -j SNAT --to-source 333.333.333.25
iptables -t nat -A POSTROUTING -s 172.30.100.0/22 -o eth1 -j SNAT --to-source 333.333.333.26
iptables -t nat -A POSTROUTING -s 172.30.104.0/22 -o eth1 -j SNAT --to-source 333.333.333.27
iptables -t nat -A POSTROUTING -s 172.30.108.0/22 -o eth1 -j SNAT --to-source 333.333.333.28
iptables -t nat -A POSTROUTING -s 172.30.112.0/22 -o eth1 -j SNAT --to-source 333.333.333.29
iptables -t nat -A POSTROUTING -s 172.30.116.0/22 -o eth1 -j SNAT --to-source 333.333.333.30
iptables -t nat -A POSTROUTING -s 172.30.120.0/22 -o eth1 -j SNAT --to-source 333.333.333.31
iptables -t nat -A POSTROUTING -s 172.30.124.0/22 -o eth1 -j SNAT --to-source 333.333.333.32
iptables -t nat -A POSTROUTING -s 172.30.128.0/22 -o eth1 -j SNAT --to-source 333.333.333.33
iptables -t nat -A POSTROUTING -s 172.30.132.0/22 -o eth1 -j SNAT --to-source 333.333.333.34
iptables -t nat -A POSTROUTING -s 172.30.136.0/22 -o eth1 -j SNAT --to-source 333.333.333.35
iptables -t nat -A POSTROUTING -s 172.30.140.0/22 -o eth1 -j SNAT --to-source 333.333.333.36
iptables -t nat -A POSTROUTING -s 172.30.144.0/22 -o eth1 -j SNAT --to-source 333.333.333.37
iptables -t nat -A POSTROUTING -s 172.30.148.0/22 -o eth1 -j SNAT --to-source 333.333.333.38
iptables -t nat -A POSTROUTING -s 172.30.152.0/22 -o eth1 -j SNAT --to-source 333.333.333.39
iptables -t nat -A POSTROUTING -s 172.30.156.0/22 -o eth1 -j SNAT --to-source 333.333.333.40
iptables -t nat -A POSTROUTING -s 172.30.160.0/22 -o eth1 -j SNAT --to-source 333.333.333.41
iptables -t nat -A POSTROUTING -s 172.30.164.0/22 -o eth1 -j SNAT --to-source 333.333.333.42
iptables -t nat -A POSTROUTING -s 172.30.168.0/22 -o eth1 -j SNAT --to-source 333.333.333.43
iptables -t nat -A POSTROUTING -s 172.30.172.0/22 -o eth1 -j SNAT --to-source 333.333.333.44
iptables -t nat -A POSTROUTING -s 172.30.176.0/22 -o eth1 -j SNAT --to-source 333.333.333.45
iptables -t nat -A POSTROUTING -s 172.30.180.0/22 -o eth1 -j SNAT --to-source 333.333.333.46
iptables -t nat -A POSTROUTING -s 172.30.184.0/22 -o eth1 -j SNAT --to-source 333.333.333.47
iptables -t nat -A POSTROUTING -s 172.30.188.0/22 -o eth1 -j SNAT --to-source 333.333.333.48
iptables -t nat -A POSTROUTING -s 172.30.192.0/22 -o eth1 -j SNAT --to-source 333.333.333.49
iptables -t nat -A POSTROUTING -s 172.30.0.0/16 -o eth1 -j SNAT --to-source 333.333.333.50
```

During exploitation there should be unequal traffic allocation.  
`iptables -t nat -nvL POSTROUTING --line-numbers` will show this.  
  
I have empty NAT networks, so I need to split /22 network with maximum packets counter into two /23.  
Python script reads NAT rules and propose which one should be replaced.
