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
1. Clone o repositório ou faça o download dos arquivos.
2. Execute o arquivo "minha_api.py" em algum terminal com o comando: `!python minha_api.py` <br> (Para melhor visualização de como foi criada a api, foi disponibilizado um notebook que contém todo o processo de sua criação utilizando pycaret)
Você pode acessar a API em http://127.0.0.1:8000 após executar o código. <br>
Você pode usar uma ferramenta como o Postman para fazer solicitações POST para esta URL com os dados dos clientes e obter previsões.<br>
A API aceita solicitações JSON no seguinte formato: <br>
{ <br>
    "Gender": 1, <br>
    "Age": 30 <br>
}
## Escolha do Modelo de Machine Learning
O modelo de regressão foi escolhido para este projeto com base na tarefa de previsão da renda anual de um cliente. A escolha justifica-se pela natureza de seu problema, a previsão de uma variável contínua.
