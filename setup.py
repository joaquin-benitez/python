from setuptools import setup, find_packages

setup(
    name="paquete_clientes",
    version="1.0",    
    description="Paquete para modelar clientes en una página de compras",
    author="Joaquín Benitez",
    author_email="joaquin@example.com",
    
    packages=find_packages(where='entregas'),
    package_dir={'': 'entregas'}
)
