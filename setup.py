import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VK",
    url="https://github.com/vaibhavkumar779/FinalDevOpsKUP",
    project_urls={
        "Bug Tracker": "https://github.com/vaibhavkumar779/FinalDevOpsKUP/issues",
        "Source": "https://github.com/pypa/sampleproject/",
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
       # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `init` which
    # executes the function `create_app` from this package when invoked:
    entry_points={  # Optional
        "console_scripts": [
            "init=app:create_app",
        ],
    },
)