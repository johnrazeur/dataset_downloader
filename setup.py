import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="dataset_downloader",
    version="1.0.0",
    author="Clément Lafont",
    author_email="lafont.clem@gmail.com",
    description="Tool to download large dataset from a list of url",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnrazeur/dataset_downloader",
    install_requires=requirements,
    entry_points='''
      [console_scripts]
      dataset_downloader=dataset_downloader.cli:cli
    ''',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)