from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ckanext-curvelotheme",
    version="1.0.0",
    description="CKAN extension for Curvelo's city theme",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="",
    author="Edgar Zanella Alvarenha",
    author_email="e@vaz.i0",
    url="https://github.com/prefeitura-curvelo/ckanext-curvelotheme/",
    license="Public Domain",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    namespace_packages=["ckanext"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    setup_requires=["wheel"],
    entry_points="""
        [ckan.plugins]
        curvelotheme=ckanext.curvelo_theme.plugin:CurveloThemePlugin
    """,
)
