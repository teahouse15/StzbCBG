from urllib.parse import urlparse

def get_account_ordersn(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    return path_parts[5]