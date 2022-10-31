from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
VERSION = "0.0.1"

setup(
    name="tgpd",
    version=VERSION,
    description="download or preview telegram graph in iTerm2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="telegraph download preview",
    author="RhythmLian",
    url="https://github.com/Rhythmicc/tgpd",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["Qpro", "QuickStart-Rhy"],
    entry_points={
        "console_scripts": [
            "tgpd = tgpd.main:main",
        ]
    },
)
