from setuptools import setup, find_packages

setup(
    name="TimeMasterX",
    version="0.1.0",
    author="Henoc N'GASAMA",
    author_email="ngasamah@gmail.com",
    description="Un package avancé pour manipuler le temps, les dates et fuseaux horaires.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/henoc/TimeMasterX",
    packages=find_packages(),
    install_requires=["pytz"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "timemasterx=cli:main",
        ],
    },
)
