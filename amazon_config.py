from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '$'
MIN_PRICE = '200'
MAX_PRICE = '600'
FILTERS = {
    'min':MIN_PRICE,
    'max':MAX_PRICE
} 
BASE_URL='http://www.amazon.com'

def get_edge_driver(options):
    return webdriver.Edge('./edgedriver',edge_options=options)

print('all done')