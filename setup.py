import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diagrams",
    version="0.0.1",
    author="Simon Pfreundschuh",
    author_email="simon.pfreundschuh@chalmers.se",
    description="Drawing diagrams with tkinter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonpf/diagrams",
    packages=setuptools.find_packages(), # Searches modules in current directory.
    python_requires='>=3.6',
    install_requires=[
        "numpy"
    ],
)
