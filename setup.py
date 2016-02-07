from setuptools import setup, find_packages

setup(
    name='parker',
    version='0.0.1',
    author='Chris Gilemr',
    author_email='chris.gilmer@gmail.com',
    maintainer='Chris Gilmer',
    maintainer_email='chris.gilmer@gmail.com',
    description='Music Theory',
    url='https://github.com/chrisgilmerproj/silliness/tree/master/music',
    packages=find_packages(exclude=["*.tests",
                                    "*.tests.*",
                                    "tests.*",
                                    "tests"]),
    include_package_data=True,
    zip_safe=False,
    test_requires=[
        'mock==1.0.1',
        'nose==1.3.1',
    ],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ),
)
