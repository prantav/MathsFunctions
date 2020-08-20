import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MathsFunctions-programmer_pogav", # Replace with your own username
    version="0.0.1",
    author="Pranav Challa",
    author_email="pranav.moony.challa@gmail.com",
    description="Making maths in python easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prantav/MathsFunctions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
