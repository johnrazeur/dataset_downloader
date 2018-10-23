import requests
import os
import pathlib
import sys

from multiprocessing.pool import Pool
from urllib.parse import urlparse
from dataset_downloader.urls import generateUrls


def getFilename(url):
    a = urlparse(url)
    return os.path.basename(a.path)


def downloadFile(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print('{} downloaded'.format(url))
            return r.content
    except requests.exceptions.ConnectionError:
        pass


def downloadClassFiles(className, trainFolder, testFolder, urls, ratio):
    trainFolder = os.path.join(trainFolder, className)
    testFolder = os.path.join(testFolder, className)
    pathlib.Path(trainFolder).mkdir(parents=True, exist_ok=True)
    pathlib.Path(testFolder).mkdir(parents=True, exist_ok=True)

    limitTrain = len(urls) * ratio

    for index, url in enumerate(urls):
        if limitTrain > index + 1:
            folder = trainFolder
        else:
            folder = testFolder
        filename = getFilename(url)
        content = downloadFile(url)
        if content:
            open(os.path.join(folder, filename), 'wb').write(content)


def run(config, processes):
    with Pool(processes=processes) as pool:
        try:
            for className in config['classes']:
                pool.apply_async(downloadClassFiles, (
                  className,
                  config['outputTrain'],
                  config['outputTest'],
                  generateUrls(config['classes'][className]),
                  config['ratio'])
                )

            pool.close()
            pool.join()
            print('All files downloaded')
        except (KeyboardInterrupt, SystemExit):
            pool.terminate()
            sys.exit(0)
