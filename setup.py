from setuptools import setup, find_packages

setup(
    name="replacer",
    version="0.1",
    py_modules=["replacer"],
    entry_points={
        "console_scripts": [
            "replacer=replacer:main",
        ],
    },
    author="Mishal",
    description="A Python CLI tool to organize files by extension",
    long_description=open("README.md").read() if open("README.md", "r", encoding="utf-8") else ""
)