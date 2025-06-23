from setuptools import setup, find_packages

setup(
    name="vecz",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "vecz=vecz.cli:main",
        ],
    },
    install_requires=["numpy"],
    author="Omkar Zende",
    author_email="expertomkar@gmail.com",
    description="Block-level vector compressor for ML embeddings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zomkarm/vecz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
