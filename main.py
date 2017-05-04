import os
import time

from bhive_client import BhiveClient

if __name__ == '__main__':
	while True:
		b = BhiveClient(os.environ['BHIVE_API_TOKEN'])
		b.run()
		time.sleep(int(os.environ['BEEHIVEAI_CHECK_INTERVAL']))