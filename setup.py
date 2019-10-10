from setuptools import setup, find_packages


setup(
    name="py_utils",
    author="Winter",
    author_email="785576549@qq.com",
    packages=find_packages(),
    description="Utils collector for python.",
    include_package_data=True,
    platforms="any",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords=["utils", "tools"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
)
