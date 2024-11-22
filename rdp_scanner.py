import logging
from concurrent.futures.thread import ThreadPoolExecutor

from utilities.save_utils import save_result
from utilities.general_utils import check_rdp, generate_random_ip

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    logging.info("Scanning for RDP services...")
    cycle_limit = 1000  # Number of cycles to run = Limit
    max_threads = 5  # Number of concurrent threads

    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_ip) for _ in range(cycle_limit)]
        for future in futures:
            future.result()

    logging.info("Finished scanning for RDP services...")

def scan_ip():
    """Generate an IP, check RDP, and save the result if successful."""
    random_ip = generate_random_ip()
    if check_rdp(random_ip):
        save_result(random_ip)

if __name__ == "__main__":
    main()