import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


required = [
    'amazon-kclpy~=2.0.1']

setup(name='Kinesis consumer',
      version=read('VERSION'),
      author="Francisco Huertas",
      author_email="pacohuertas@gmail.com",
      license="Apache2",
      packages=find_packages(include=['src', 'src.*']),
      description="Example of kinesis consumer",
      long_description=read('README.md'),
      url='https://github.com/fhuertas/python_base',
      download_url="https://github.com/fhuertas/python_base/tarball/{}".format(read('VERSION')),
      install_requires=required,
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          'Programming Language :: Python :: 3.6',
      ])
