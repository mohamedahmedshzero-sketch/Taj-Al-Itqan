#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف إعداد التثبيت
Setup installation file
"""

from setuptools import setup, find_packages
from pathlib import Path

# قراءة README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="taj-al-itqan",
    version="1.0.0",
    author="Taj Al-Itqan Team",
    author_email="support@taj-al-itqan.com",
    description="نظام إدارة حلقات تحفيظ القرآن الكريم",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/taj-al-itqan",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/taj-al-itqan/issues",
        "Documentation": "https://github.com/yourusername/taj-al-itqan#readme",
        "Source Code": "https://github.com/yourusername/taj-al-itqan",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "kivy>=2.2.0,<3.0.0",
        "kivymd>=0.104.2,<0.105.0",
        "qrcode>=7.4.0",
        "Pillow>=9.0.0,<10.0.0",
        "arabic-reshaper>=0.4.0",
        "python-bidi>=0.4.2",
        "python-dotenv>=1.0.0",
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pylint>=2.0",
            "flake8>=4.0",
            "black>=22.0",
        ],
        "android": [
            "buildozer>=1.3.0",
            "Cython>=0.29.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Natural Language :: Arabic",
        "Environment :: X11 Applications",
        "Environment :: No Input/Output (Daemon)",
    ],
    entry_points={
        "console_scripts": [
            "taj-al-itqan=src.main:main",
        ],
    },
    zip_safe=False,
)

