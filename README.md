# AutoFacePost
Automatize suas postagens no Facebook com este script Python usando Selenium.

# Automatização de Postagem no Facebook

Este é um script Python que usa a biblioteca Selenium para automatizar ações no Facebook, como fazer login e fazer uma postagem. O código foi desenvolvido com o objetivo de facilitar a publicação de mensagens no Facebook de forma automática.

## Pré-requisitos

Certifique-se de que você tenha instalado o Python e as seguintes bibliotecas:

- Selenium
- ChromeDriverManager
- Chrome (e o ChromeDriver correspondente)

Você pode instalar as bibliotecas necessárias usando o pip:

pip install selenium webdriver-manager

Além disso, você precisa ter o navegador Google Chrome instalado em seu sistema.

## Uso

1. Clone ou faça o download deste repositório em seu computador.

2. Abra o arquivo `main.py` em seu editor de código e edite as seguintes linhas para fornecer suas informações de login do Facebook:

```python
email.send_keys('seu_email')
password.send_keys('sua_senha')
