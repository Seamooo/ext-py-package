import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numbers_for_entropy_12421",
    version="0.0.1",
    author="seamus mulholland-patterson",
    author_email="seamus.mulholland-patterson@artrya.com",
    description="test package to use external dependency not on pypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_dir={'numbers_for_entropy_12421':'numbers_for_entropy_12421'},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
)
