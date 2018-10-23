import re
import requests
import io

from pathlib import Path


regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def downloadFile(url):
    r = requests.get(url)
    if r.status_code == 200:
        data = io.BytesIO(r.content)
        return io.TextIOWrapper(data, encoding='utf-8')
    else:
        raise Exception('{} return status code {}'.format(url, r.status_code))


def generateUrls(field):
    # If the field is already a list, do noting
    if isinstance(field, list):
        return field

    # If field is an url
    if re.match(regex, field):
        return [line.rstrip() for line in downloadFile(field)]

    file_list = Path(field)
    if file_list.is_file():
        return [line.rstrip() for line in open(field, 'r', encoding="utf8")]

    raise Exception('Invalid class urls source')
