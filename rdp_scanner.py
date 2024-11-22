import logging

from utilities.save_utils import save_result
from utilities.general_utils import check_rdp, generate_random_ip

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    logging.info("Scanning for RDP services...")
    cycle_limit = 10  # Number of cycles to run = Limit

    for cycle in range(cycle_limit):
        logging.info(f"Cycle {cycle + 1}/{cycle_limit}: Generating and checking an IP...")
        random_ip = generate_random_ip()
        #logging.info(f"Generated IP: {random_ip}")
        if check_rdp(random_ip):
            save_result(random_ip)
    logging.info("Finished scanning for RDP services...")

if __name__ == "__main__":
    main()