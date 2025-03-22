from setuptools import setup

setup(
    name="hexacode",
    version="1.0",
    description="A simple programming language for automation and game cheats.",
    author="YourName",
    packages=["hexacode"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "hexa=hexacode.HexaCodeInterpreter:main",
        ],
    },
)
