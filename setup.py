from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="examinerview",             # This name is used in: pip install examinerview
    version="1.0.1",
    author="5f0",
    url="https://github.com/5f0ne/examinerview",
    description="Create visual timelines for forensic investigations",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "examinerview.template": ["index.html"]
    },
    install_requires=[
        ""
    ],
     entry_points={
        "console_scripts": [
            "examinerview = examinerview.__main__:main"
        ]
    }
)
