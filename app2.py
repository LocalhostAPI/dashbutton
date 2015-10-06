import socket
import struct
import binascii
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
while True:
  packet = rawSocket.recvfrom(2048)
  ethernet_header = packet[0][0:14]
  ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
  arp_header = packet[0][14:42]
  arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
  ethertype = ethernet_detailed[2] 
  # skip non-ARP packets
  if ethertype != '\x08\x06':
    continue
  source_mac = binascii.hexlify(arp_detailed[5])
  dest_ip = socket.inet_ntoa(arp_detailed[8])
  if source_mac == '74c24671971c':
    print "Tide button pressed!, IP = " + dest_ip + " and mac = " + source_mac
  else:
    print "Other arp request, IP = " + dest_ip + " and mac = " + source_mac


