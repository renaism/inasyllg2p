from setuptools import setup

from codecs import open
from os import path

# This file's directory
HERE = path.abspath(path.dirname(__file__))

setup(
    name="syllg2p",
    version="0.1.0",
    description="Tagger for syllabification and grapheme-to-phoneme (G2P)",
    author="Rezza Nafi",
    author_email="zafitract@gmail.com",
    license="MIT",
    packages=["syllg2p"],
    include_package_data=True,
    install_requires=["numpy"]
)