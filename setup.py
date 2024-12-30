from setuptools import setup, find_packages

# Lendo o arquivo requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="meu_pacote",
    version="1.0.0",
    author="Bruno Alves Farrás",
    description="Pacote de interações com o usuário",
    packages=find_packages(),
    install_requires=requirements
)

