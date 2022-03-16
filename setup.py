import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FlashFire",
    version="1.0.0",
    author="Matthew Seath",
    author_email="seath.dev@gmail.com",
    description="FlashFire is a web application that functions as a trading platfrom.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matt-Seath/FlashFire",
    project_urls={
        "Bug Tracker": "https://github.com/Matt-Seath/FlashFire/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-session',
        'flask-wtf',
        'requests',
        'python-dotenv', 
        'alpaca-trade-api',
        'email_validator',
        'datetime'
    ],
)