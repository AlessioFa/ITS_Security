from scapy.all import sniff, Ether, get_if_hwaddr


# Nome dell'interfaccia di rete da monitorare. In questo caso è una VPN privata (interfaccia virtuale)
IFACE = "tap0"

# Otteniamo il MAC address dell'interfaccia specificata con la funzione get_if_hwaddr
MY_MAC = get_if_hwaddr(IFACE).lower()  # MAC locale


def handle(pkt):
    """
    Funzione chiamata ogni volta che sniff() cattura un pacchetto.
    'pkt' è l'oggetto pacchetto catturato da Scapy.
    """
    # Controlliamo che il pacchetto abbia un livello Ethernet e che sia destinato al nostro MAC
    if Ether in pkt and pkt[Ether].dst.lower() == MY_MAC:
        # Stampa una breve descrizione del pacchetto
        print("Pacchetto ricevuto per me:", pkt.summary())
        # Mostra tutti i dettagli del pacchetto: header Ethernet, IP, TCP/UDP e payload
        pkt.show()

# sniff() cattura pacchetti dall'interfaccia IFACE
# prn=handle -> chiama la funzione handle() per ogni pacchetto catturato
# lfilter=... -> filtro in Python applicato prima di chiamare handle()
# count=1 -> ferma lo sniffing dopo aver catturato 1 pacchetto


sniff(iface=IFACE, prn=handle, lfilter=lambda p: Ether in p and p[Ether].dst.lower() == MY_MAC, count=1)
