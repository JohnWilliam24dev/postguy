from setuptools import setup, find_packages

setup(
    name="postguy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],  
    entry_points={
        "console_scripts": [
            "postguy = postguy.cli:PostguyCLI.run",
        ],
    },
    author="JohnWilliam24.dev",
    description="CLI para testar APIs rapidamente",
)