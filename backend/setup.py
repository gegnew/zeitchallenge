from setuptools import find_packages, setup

setup(
    name="zeitchallenge",
    packages=find_packages(),
    version="0.1.0",
    description="Sr SWE Take Home Challenge",
    author="Gerrit Egnew",
    author_email="g.egnew@gmail.com",
    license="",
    install_requires=[
        "fastapi~=0.75",
        "uvicorn~=0.17",
        "requests~=2.27",
        "python-multipart~=0.0",
        "jinja2-time~=0.2",
        "python-jose~=3.3",
        "python-dotenv~=0.20",
    ],
    tests_require=["pytest~=7.1"],
    python_requires=">=3.7",
)
