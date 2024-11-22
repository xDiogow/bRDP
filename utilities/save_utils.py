import logging


def save_result(ip, port=3389):
    with open("Results.txt", "a") as file:
        file.write(f"{ip}:{port}\n")
    logging.info(f"Saved IP {ip}:{port} to results file.")
