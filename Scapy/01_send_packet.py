from scapy.all import Ether, Raw, sendp


def send_with_scapy(iface, dst_mac, src_mac, ethertype, payload, count=1):
    """
    Crea e invia un pacchetto Ethernet usando Scapy.

    Parametri:
    - iface: interfaccia di rete da cui inviare il pacchetto (es. tap0)
    - dst_mac: MAC address di destinazione
    - src_mac: MAC address sorgente
    - ethertype: tipo del frame Ethernet (es. 0x0800 per IP)
    - payload: dati da inserire nel pacchetto (Raw)
    - count: numero di pacchetti da inviare
    """

    # Costruzione del pacchetto
    # - Ether(): crea l'header Ethernet
    #   - dst: MAC di destinazione
    #   - src: MAC sorgente
    #   - type: tipo di protocollo (EtherType)
    # - Raw(load=payload): aggiunge i dati grezzi (payload) al pacchetto
    pkt = Ether(dst=dst_mac, src=src_mac, type=ethertype) / Raw(load=payload)
    # Invia il pacchetto tramite l'interfaccia specificata
    # sendp(): invia pacchetti a livello 2 (Ethernet)
    # iface: interfaccia di rete da cui inviare
    # count: numero di copie del pacchetto da inviare
    # verbose=True: mostra informazioni sul processo di invio
    sendp(pkt, iface=iface, count=count, verbose=True)


if __name__ == "__main__":
    iface = "tap0"
    dst_mac = "00:11:22:33:44:29"
    src_mac = "00:11:22:33:44:28"
    ethertype = 0x88B5
    payload = b"Hello from Scapy"
    send_with_scapy(iface, dst_mac, src_mac, ethertype, payload)
