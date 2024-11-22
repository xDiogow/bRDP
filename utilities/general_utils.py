import socket
import logging
from random import randint

def check_rdp(host, port=3389) -> bool:
    """
    Check if an RDP connection is available on the specified host and port.

    Args:
        host (str): The target hostname or IP address.
        port (int): The port to check for RDP (default: 3389).

    Returns:
        bool: True if RDP is available, False otherwise.
    """
    logging.info(f"Attempting to connect to {host}:{port}")
    try:
        with socket.create_connection((host, port), timeout=2):
            logging.info(f"A RDP connection has been found on {host}:{port}")
            return True
    except socket.timeout:
        logging.warning(f"Connection attempt to {host}:{port} timed out.")
    except socket.error:
        logging.error(f"RDP is not enabled on {host}:{port}")
    return False


def generate_random_ip():
    """Generate a single random public IP."""
    while True:
        ip = ".".join(str(randint(1, 254)) for _ in range(4))  # Avoid 0 and 255
        if not is_private(ip):
            return ip


def is_private(ip):
    """Check if an IP address is in a private range."""
    first_octet = int(ip.split('.')[0])
    second_octet = int(ip.split('.')[1])

    # Private ranges
    if first_octet == 10:  # 10.0.0.0/8
        return True
    if first_octet == 172 and 16 <= second_octet <= 31:  # 172.16.0.0/12
        return True
    if first_octet == 192 and second_octet == 168:  # 192.168.0.0/16
        return True

    # Other non-routable ranges
    if first_octet == 127:  # Loopback
        return True
    if first_octet == 169 and second_octet == 254:  # Link-local
        return True
    return False