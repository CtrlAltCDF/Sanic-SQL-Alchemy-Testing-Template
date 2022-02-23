from setuptools import setup

setup(
    name="myapi",
    version="0.1",
    description="Super simple API example with Sanic, testing and SQL Alchemy",
    author="cdf",
    package_dir={"myapi": "myapi"},
    install_requires=[
        "sanic",
        "pytest",
        "sanic_testing",
        "alembic",
        "sqlalchemy",
        "aiomysql",
        "aiosqlite"
    ],
    scripts=[
        "scripts/clear_temp",
        "scripts/devapp",
        "scripts/prodapp",
    ]
)