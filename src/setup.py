import setuptools


setuptools.setup(
    name="persistance_helper",
    version="0.0.2",
    author="Bence Szinyéri",
    author_email="szinyeribence@edu.bme.hu",
    description="Helpers to persist objects",
    long_description="Some python functions to persist Python objects",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.8',
)