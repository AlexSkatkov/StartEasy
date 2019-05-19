import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="star-easy",
    version="0.0.1",
    author="olga L",
    author_email="olgala1@ac.sce.ac.il",
    description="web site",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexSkatkov/StartEasy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)