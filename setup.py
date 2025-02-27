import pathlib
from setuptools import setup, find_packages

from simsity import __version__


base_packages = [
    "scikit-learn>=1.0.0",
    "pynndescent>=0.5",
    "numba>=0.54.1",
    "pandas>=1.3.3",
]

minhash_packages = ["datasketch>=1.5.3"]

serve_packages = ["uvicorn>=0.15.0", "fastapi>=0.70.0"]

docs_packages = [
    "mkdocs==1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings==0.8.0",
    "mktestdocs==0.1.2",
]

test_packages = [
    "interrogate>=1.5.0",
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "pre-commit>=2.2.0",
    "pyanalyze>=0.3.1",
    "requests>=2.26.0",
    "dirty_cat",
]

all_packages = base_packages + minhash_packages + serve_packages
dev_packages = all_packages + docs_packages + test_packages


setup(
    name="simsity",
    version=__version__,
    author="Vincent D. Warmerdam",
    packages=find_packages(exclude=["notebooks", "docs"]),
    description="Simple Similarity Service",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://koaning.github.io/simsity/",
    project_urls={
        "Documentation": "https://koaning.github.io/simsity/",
        "Source Code": "https://github.com/koaning/simsity/",
        "Issue Tracker": "https://github.com/koaning/simsity/issues",
    },
    install_requires=base_packages,
    extras_require={"dev": dev_packages, "minhash": minhash_packages},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
