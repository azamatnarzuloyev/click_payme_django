import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="payment-django",
    version="1.1",
    author="Azamat Narzulloyev",
    author_email="azamatdev@mail.ru",
    description="payment dango add click and payme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django'],
    url="https://github.com/azamat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)