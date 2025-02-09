import logging


def setup_request_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/requests.log', mode='w'),
            logging.StreamHandler()
        ]
    )
    logging.getLogger('faker.factory').setLevel(logging.ERROR)
    logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
