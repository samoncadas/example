from setuptools import setup, find_packages

setup(
    name:"milib-ejemplo",
    version="0.0.1",
    author="Samuel",
    author_email="samumoncada225@gmail.com",
    description="Una libreria de prueba para subir a Nexus",
    package = find_packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License,
    ],
    python_requires='>=3.6'
)
