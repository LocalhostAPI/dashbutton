import socket
import struct
import binascii
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    arp_header = packet[0][14:42]
    try:
        print('header is', arp_header)
        arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    except Exception as e:
        print('crashed...', e)

    ethertype = ethernet_detailed[2]

    # skip non-ARP packets
    if ethertype != '\x08\x06':
        continue

    source_mac = binascii.hexlify(arp_detailed[5])
    dest_ip = socket.inet_ntoa(arp_detailed[8])

    # ac63be53a3d2      smartwater
    # 44650d407cc4      snuggle
    # ac63be63ae23      blank
    # 74c24682a64a      elements
    # f0272da4079f      angel soft

    if source_mac == 'ac63be53a3d2':
        print("smartwater")
    elif source_mac == '44650d407cc4':
        print("snuggle")
    elif source_mac == 'ac63be63ae23':
        print("blank")
    elif source_mac == '74c24682a64a':
        print("elements")
    elif source_mac == 'f0272da4079f':
        print("angel_soft")
    else:
        print "Other arp request, IP = " + dest_ip + " and mac = " + source_mac
