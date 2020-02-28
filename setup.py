from setuptools import setup, find_packages


PACKAGENAME = "pkg_template"
VERSION = "0.0.dev"


setup(
    name=PACKAGENAME,
    version=VERSION,
    author="Duncan Campbell",
    author_email="duncanc@andrew.cmu.edu",
    description="Some package",
    long_description="Just some package",
    install_requires=["numpy"],
    packages=find_packages(),
    url="https://github.com/duncanc/pkg_template"
)
