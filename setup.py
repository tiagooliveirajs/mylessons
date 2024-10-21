from setuptools import setup, find_packages

setup(
    name='mylessons',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot==20.0',  # Dependência do Telegram
        'langchain',                  # Langchain para LLM e agentes
        'requests',                   # Para comunicação com o LM Studio API
        'python-dotenv',              # Para carregar variáveis de ambiente
    ],
    entry_points={
        'console_scripts': [
            'mylessons-run = run:main',
        ],
    },
    description='A chatbot for Telegram using LM Studio API and word list validation.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/mylessons',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)