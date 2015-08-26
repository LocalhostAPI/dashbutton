from scapy.all import *
import time

def record_press():
  print "Pushed button"
  data = {
    "Timestamp": time.strftime("%Y-%m-%d %H:%M"),
  }
  print data

def arp_display(pkt):
  timestamp = time.strftime("%Y-%m-%d %H:%M")
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'your_mac_here...':
        record_press()
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)
