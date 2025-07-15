import scapy.all as scapy
from scapy.contrib.gtp import GTP_U_Header
import os


def extract_inner_ip(pkt):
    """從 GTP payload 遞迴找出最內層 IP 封包"""
    layer = pkt
    while layer:
        if isinstance(layer, scapy.IP):
            return layer
        layer = layer.payload
    return None


def main():
    pcap_dir = "PATH_TO_PCAP_DIR"  # Replace with your pcap directory path
    output_dir = "PATH_TO_OUTPUT_DIR"  # Replace with your output directory path
    
    SRC_MAC = "00:11:22:33:44:55"
    DST_MAC = "66:77:88:99:aa:bb"
    
    targets = [f for f in os.listdir(pcap_dir) if os.path.isfile(os.path.join(pcap_dir, f))]
    print(f"Found {len(targets)} pcap file: {targets}")
    
    check = input("Start processing? (Y/n) ")
    if check.lower() == 'n':
        return
    
    for pcap_file in targets:
        print(f"Start processing {pcap_file}", end=" | ")
        pcap_file_path = os.path.join(pcap_dir, pcap_file)
        packets = scapy.rdpcap(pcap_file_path)
        new_packets = []
        
        for pkt in packets:
            if not pkt.payload:
                continue

            # 判斷封包類型，取得 payload 與對應 ethertype
            if pkt.haslayer(scapy.IP):
                ether_type = 0x0800
                payload = pkt[scapy.IP]
            elif pkt.haslayer(scapy.IPv6):
                ether_type = 0x86DD
                payload = pkt[scapy.IPv6]
            elif pkt.haslayer(scapy.ARP):
                ether_type = 0x0806
                payload = pkt[scapy.ARP]
            else:
                ether_type = 0x0000
                payload = pkt.payload

            ether = scapy.Ether(src=SRC_MAC, dst=DST_MAC, type=ether_type)

            # 如果是 GTP-U 封包，解析 inner IP
            if pkt.haslayer(GTP_U_Header):
                inner_ip = extract_inner_ip(pkt[GTP_U_Header])
                if inner_ip:
                    cooked = scapy.CookedLinuxV2() / inner_ip
                    new_pkt = ether / cooked[scapy.IP]
                    new_pkt.time = float(pkt.time)
                    new_packets.append(new_pkt)
                else:
                    new_pkt = ether / pkt[scapy.IP]
                    new_pkt.time = float(pkt.time)
                    new_packets.append(new_pkt)
            else:
                new_pkt = ether / payload
                new_pkt.time = float(pkt.time)
                new_packets.append(new_pkt)

        save_path = f"{output_dir}/{pcap_file.split('.')[0]}-stripped.pcap"
        scapy.wrpcap(save_path, new_packets)
        print(f"Saved: {save_path}")


if __name__ == "__main__":
    main()
