from setuptools import find_packages
from setuptools import setup

setup(
    name='parker',
    version='0.0.1',
    author='Chris Gilemr',
    author_email='chris.gilmer@gmail.com',
    maintainer='Chris Gilmer',
    maintainer_email='chris.gilmer@gmail.com',
    description='Music Theory',
    url='https://github.com/chrisgilmerproj/parker',
    packages=find_packages(exclude=["*.tests",
                                    "*.tests.*",
                                    "tests.*",
                                    "tests"]),
    include_package_data=True,
    zip_safe=False,
    test_requires=[
        'nose==1.3.1',
        'pluggy==0.3.1',
        'py==1.4.31',
        'tox==2.3.1',
    ],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ),
)
