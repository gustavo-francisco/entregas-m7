# Projeto Entrega 4
Este é um projeto que consiste em um sistema de autenticação construído com Flask e Werkzeug Security, que posteriormente consome uma API de um modelo preditivo de regressão desenvolvido com o PyCaret. O objetivo principal deste projeto é prever a renda anual de um consumidor com base em seu gênero e idade. Além disso, o front-end da aplicação foi desenvolvido usando HTML e CSS. Posteriormente, o projeto foi dockerizado e implantado em um servidor EC2 na AWS, conforme vídeo de demonstração.

# Funcionalidades Principais
Autenticação de Usuários: O sistema possui autenticação de usuários para garantir que apenas usuários autorizados possam acessar as funcionalidades do aplicativo. <br>

Modelo de Regressão de Renda: O projeto inclui um modelo preditivo de regressão treinado com base no gênero e idade do consumidor para prever sua renda anual. <br>

Front-End Interativo: A interface de usuário foi criada usando HTML e CSS para fornecer uma experiência amigável e intuitiva para os usuários. <br>

Dockerização: O aplicativo foi dockerizado para garantir a portabilidade e facilidade de implantação. <br>

Implantação na AWS: O aplicativo foi implantado em um servidor EC2 da AWS para torná-lo acessível na web. <br>

# Requisitos de Instalação
Para executar este projeto localmente, você precisará das seguintes dependências instaladas:<br>
Python (versão 3.7 ou superior)<br>
Flask<br>
Werkzeug Security<br>
PyCaret<br>
Docker<br>
Ou, utilize o comando `pip install requirements.txt` na pasta backend.


# Execução local para testes
Para executar o projeto localmente, primeiro, crie um clone deste repositório. <br>
Após isso, acesse a pasta raiz (entrega4) <br>
Execute o comando `docker compose up` <br>
Então, acesse o localhost na porta definida (80) na rota signup, ou seja, localhost:80/signup. <br>
Depois dessa etapa o fluxo de telas é bem fluído, você cria uma conta, loga e realiza os inputs para a predição. <br>
