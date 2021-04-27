import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="irct-api",
    version="1.0.1",
    description="Unofficial API for irct.ir",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/L1xPy/irct-api",
    author="LixPy",
    author_email="LixPy@protonmail.ch",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=['irct_api'],
    include_package_data=True,
    install_requires=["bs4", "requests"],
)
