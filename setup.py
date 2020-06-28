import setuptools

with open("README.md") as ld:
    long_description = ld.read()

setuptools.setup(
    name = "pyproperty",
    version = "0.1",
    author = "raifpy",
    author_email = "mail.raifpy@gmail.com",
    description="Python Explore Modules Func Tool *",
    long_description=long_description,
    url = "https://github.com/raifpy/pyproperty",
    packages=setuptools.find_packages(),
    python_requires= ">=3.5",
    scripts = ["pyproperty/pyproperty"]
        )