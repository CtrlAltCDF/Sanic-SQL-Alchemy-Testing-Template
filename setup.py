from setuptools import setup

setup(
    name="go_fast",
    version="0.1",
    description="Super simple API example with Sanic, testing and SQL Alchemy",
    author="cdf",
    package_dir={"go_fast": "go_fast"},
    install_requires=["sanic", "pytest", "sanic_testing"],
    scripts=[
        "scripts/clear_temp",
    ]
)