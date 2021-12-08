from setuptools import setup, find_packages


setup(
    name='drfexts',
    version='0.1.1',
    author='aiden lu',
    author_email='allaher@icloud.com',
    description='Django drf extension package',
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
        "django>=3.1.7",
        "django-storages>=1.11.1",
        "django-filter>=2.4.0",
        "djangorestframework>=3.12.4",
        "openpyxl~=3.0.9",
    ],
    classifiers=[
        'Development Status :: 1 - Pre-Production',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
