from setuptools import setup, find_packages

setup(
    name="loot-cli",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["rich>=13.0"],
    entry_points={
        "console_scripts": [
            "loot=loot_cli.cli:main",
        ],
    },
)
