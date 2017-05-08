import os
import sys
import time

from bhive_client import BhiveClient

if __name__ == '__main__':
	while True:
		if os.environ['BHIVE_API_TOKEN']=='':
			print 'Please set BHIVE_API_TOKEN in docker-compose.yml'
			sys.exit()			
		if os.environ['BEEHIVEAI_CHECK_INTERVAL']==-1:
			print 'Please set BEEHIVEAI_CHECK_INTERVAL in docker-compose.yml'
			sys.exit()
		b = BhiveClient(os.environ['BHIVE_API_TOKEN'])
		b.run()
		time.sleep(int(os.environ['BEEHIVEAI_CHECK_INTERVAL']))