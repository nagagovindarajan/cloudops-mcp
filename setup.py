from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="cloudops-mcp",
    version="1.0.0",
    author="CloudOps-MCP Contributors",
    author_email="nagagovindarajan@gmail.com",
    description="A Model Context Protocol server for AWS cloud operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cloudops-mcp",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/cloudops-mcp/issues",
        "Documentation": "https://github.com/yourusername/cloudops-mcp#readme",
        "Source Code": "https://github.com/yourusername/cloudops-mcp",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: System :: Systems Administration",
    ],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cloudops-mcp=run:main",
        ],
    },
)
