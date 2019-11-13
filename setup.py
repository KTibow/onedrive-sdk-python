from __future__ import with_statement
from setuptools import setup
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = "1.1.12"


def main():
    package_list = ['onedrivesdk_fork',
                    'onedrivesdk_fork.request',
                    'onedrivesdk_fork.model',
                    'onedrivesdk_fork.extensions',
                    'onedrivesdk_fork.helpers']

    if sys.version_info >= (3, 4):
        base_dir = 'python3'
        package_list.append('onedrivesdk_fork.version_bridge')
    else:
        base_dir = 'python2'

    setup(
        name='onedrivesdk_fork',

        version=version,

        description='Official Python OneDrive SDK for interfacing with OneDrive APIs',
        long_description=long_description,

        url='http://dev.onedrive.com',

        author='Microsoft',
        author_email='',

        license='MIT',

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.4',
            'Operating System :: OS Independent',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
        ],

        keywords='onedrive sdk',

        packages=package_list,

        package_dir={'onedrivesdk_fork': 'src/onedrivesdk_fork',
                     'onedrivesdk_fork.request': 'src/' + base_dir + '/request'},

        install_requires=['requests>=2.6.1'],

        extras_require={
            "samples": ["Pillow"],
            "tests": ["Mock"]
        },

        test_suite='testonedrivesdk'
    )

if __name__ == '__main__':
    main()
