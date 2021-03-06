import setuptools

from io import open


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setuptools.setup(
    name="pyaiodl",
    version="0.0.5",
    author="Aryan Vikash",
    author_email="followvikash8@gmail.com",
    description="A Python Asynchronous Downloader - pyaiodl",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/aryanvikash/pyaiodl",
    packages=setuptools.find_packages(),
    install_requires=['aiohttp', 'fake-useragent', 'aiofiles'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
