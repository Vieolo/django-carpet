import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_foundation",  # Replace with your own username
    version="0.1.0",
    author="Vieolo OÜ",
    author_email="info@vieolo.com",
    description="Foundational functionalities for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vieolo/django-foundation.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
