import k2sc_tools
import setuptools
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="k2sc_tools",
    version=soyspacing.__version__,
    author=soyspacing.__author__,
    author_email='soy.lovit@gmail.com',
    description="kb_ftc_team_k2sc_tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dbsgh3344',
    packages=setuptools.find_packages(),
    install_requires=["numpy>=1.12.0", "pandas>=0.25.3"],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: Beerware license",
        "Operating System :: OS Independent",
    ),
    keywords = [
        'Natural-Language-Processing',
        'team-k2sc-tools',
    ],
)
