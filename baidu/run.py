import subprocess
import schedule
import time
from scrapy import cmdline


if __name__=='__main__':
   cmdline.execute(['scray', 'crawl', 'baidu_spider'])