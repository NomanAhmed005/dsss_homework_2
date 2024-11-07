from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # List any dependencies here if needed
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # This points to the function you want to run in the command line
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
