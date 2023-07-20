import socket

def check_domain_status(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return True, f"{domain} está en línea. IP: {ip_address}"
    except socket.gaierror:
        return False, f"No se puede resolver la IP de {domain}"

def main():
    domains = [
        "www.example.com",
        "www.google.com",
        "invalid-domain.com"  # Un dominio inválido para probar el manejo de errores
    ]

    for domain in domains:
        status, message = check_domain_status(domain)
        print(message)

if __name__ == "__main__":
    main()

