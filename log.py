import logging


logging.basicConfig(filename='log-msg.log', filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')
