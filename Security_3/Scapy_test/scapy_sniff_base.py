from scapy.all import sniff


def handle(pkt):
    print(pkt.summary())


sniff(count=1, prn=handle)