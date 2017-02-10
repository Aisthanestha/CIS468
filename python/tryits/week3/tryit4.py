#!/usr/bin/env python3
import logging
import logging.handlers
import random
logging.basicConfig(filename='test.log',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger('test.log')
handler=logging.handlers.RotatingFileHandler('test.log', maxBytes=40,backupCount=5)
logger.addHandler(handler)
#logger.setLevel(logging.DEBUG)
#logging.disable(logging.CRITICAL)
for i in range(0,100):
        logging.info(random.randrange(1,100))        

print('test')
