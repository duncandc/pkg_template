from setuptools import setup, find_packages


PACKAGENAME = "pkg_template"
VERSION = "0.0.dev"


setup(
    name=PACKAGENAME,
    version=VERSION,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Some package",
    long_description="Some package, yo",
    install_requires=["numpy"],
    packages=find_packages(),
    url="https://github.com/path/to/pkg/repo"
)
