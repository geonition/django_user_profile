from setuptools import setup
from setuptools import find_packages

setup(
    name='user_profile',
    version='1.0.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/django_user_profile',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "user_profile": [
            "templates/*.js"
        ],
    },
    zip_safe=False,
    install_requires=['django']
)