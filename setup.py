from setuptools import setup, find_packages

setup(
    name="mirajev",
    version="1.0",
    author="MIRAJE Team",
    description="Advanced YouTube Video Downloader",
    long_description="MIRAJE | V - Powerful YouTube video downloading library with 4K support",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'typing-extensions>=3.7.4'
    ],
    python_requires=">=3.7",
    keywords="youtube download video 4k 1080p audio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'mirajev-cli=mirajev.cli:main',
        ],
    },
)