# Projeto Entrega 3
### O projeto Entrega 3 é a construção de um modelo preditivo que nos retorna a renda anual de um cliente com base no seu gênero e idade.
## Neste presente arquivo, iremos detalhar o processo de execução do projeto Entrega 3.
### O primeiro passo, é atender todos os requisitos, sendo eles: 
Python 3.x <br>
Jupyter Notebook (opcional, mas útil para desenvolvimento) <br>
Bibliotecas Python: pandas, pycaret <br>
Google Colab (para executar o código no ambiente do Colab) <br>
Arquivo CSV do conjunto de dados escolhido para a análise dos dados e criação do modelo. O conjunto de dados escolhido para este projeto foi o "Customer Segmentation" que, em suma, nos mostra um sistema de pontuação com base em seus comportamentos e dados de compra.
## Como executar o projeto Entrega 3?
1. Clone o repositório ou faça o download dos arquivos. <br>
2. Utilizando a Imagem Docker <br>
Você pode utilizar a imagem Docker que criamos para executar a API em um contêiner Docker. Siga as etapas abaixo para baixar e executar o contêiner: <br>
2.1. Certifique-se de que você tenha o Docker instalado em sua máquina. Se você ainda não o tem instalado, siga as instruções em [Docker Installation Guide](https://docs.docker.com/get-docker/) para instalá-lo. <br>
2.2. Abra um terminal e execute o seguinte comando para baixar a imagem Docker do Docker Hub: <br>
`docker pull gustavvnp/entregas-m7:v3.0` <br>
2.3 Após o download, execute o seguinte comando no terminal: <br>
`docker run -d -p 8000:8000 seunomeusuario/minha_api:latest` <br>
Você pode acessar a API em http://127.0.0.1:8000 após buildar a imagem do docker. <br>
Você pode usar uma ferramenta como o Postman para fazer solicitações POST para esta URL com os dados dos clientes e obter previsões.<br>
A API aceita solicitações JSON no seguinte formato: <br>
```json
   {
    "Gender": 1,
    "Age": 30
   }
```
## Escolha do Modelo de Machine Learning
O modelo de regressão foi escolhido para este projeto com base na tarefa de previsão da renda anual de um cliente. A escolha justifica-se pela natureza de seu problema, a previsão de uma variável contínua.
