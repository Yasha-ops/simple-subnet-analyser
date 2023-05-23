import sys
from ping3 import ping, verbose_ping

def ip_to_int(ip):
    # Convertir une adresse IP en entier
    parts = ip.split('.')
    return int(parts[0]) * 256**3 + int(parts[1]) * 256**2 + int(parts[2]) * 256 + int(parts[3])

def int_to_ip(num):
    # Convertir un entier en adresse IP
    octet_1 = num // (256**3)
    octet_2 = (num % (256**3)) // (256**2)
    octet_3 = (num % (256**2)) // 256
    octet_4 = num % 256
    return f'{octet_1}.{octet_2}.{octet_3}.{octet_4}'

def list_possible_ips(start_ip, end_ip):
    # Convertir les adresses IP en entiers
    start_ip = ip_to_int(start_ip)
    end_ip = ip_to_int(end_ip)

    # Vérifier si l'adresse de fin est supérieure à l'adresse de départ
    if end_ip < start_ip:
        start_ip, end_ip = end_ip, start_ip

    # Liste pour stocker les adresses IP
    ips = []

    # Boucle pour générer les adresses IP
    while start_ip <= end_ip:
        # Test l'addresse IP 
        ip = int_to_ip(start_ip)
        response = ping(ip)
        if response is not None and response:
            print(f"IP address {ip} found.")
        else:
            print(f"No {ip}.")
        # Incrémenter l'adresse IP
        start_ip += 1

    return ips
# Vérifier si les arguments de ligne de commande sont fournis
if len(sys.argv) != 3:
    print("Utilisation : python analyse.py <adresse IP de départ> <adresse IP de fin>")
else:
    start_ip = sys.argv[1]
    end_ip = sys.argv[2]
    print(list_possible_ips(start_ip, end_ip))
