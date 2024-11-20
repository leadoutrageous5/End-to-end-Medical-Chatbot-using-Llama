from setuptools import setup, find_packages

setup(
    name="MedicalChatBot",
    version="0.0.0",
    author="Ramakrishna Paritala",
    author_email="ramakrishnaparitala@gmail.com",
    description="A medical chatbot using Llama2.",
    packages=find_packages(),
    install_requires=["setuptools", "wheel"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
