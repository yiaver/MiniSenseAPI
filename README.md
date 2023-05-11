# # API_de_monitoramento_de_dispositivos_IOT
Nesse repositorio se encontra a API de monitoramento de sistemas IOT que foi feita para o MiniSense

# Instalation :
-Instale o Python 3.0.0 ou superior
- Link oficial do python de como instalar no Windows <a>https://python.org.br/instalacao-windows/</a> .
- Link oficial do python de como instalar no Linux <a>https://python.org.br/instalacao-linux/</a> .
- (OPICIONAL):
  - Caso queira voce pode criar um ambiente virtual para armazenar as bibliotecas.
  - Link oficial do python de como criar um ambiente virtual <a>https://docs.python.org/pt-br/3/library/venv.html</a>
  - apos criar o ambiente emtre nele com os comandos do seu Sistema operacional.
- Apos ter instalado o python3 corretamente instale as bibliotecas necessarias com:
`pip3 install -r requirements.txt`

# Conexão ao banco de dados:
Para usar a API, é necessário se conectar a um banco de dados MySQL  versão 8.0.33 , caso queira instale o mySQL Workbench para rodar o script de configuração da database iot_server . Para se conectar, você precisará preencher as seguintes informações no arquivo .env:

- PASSWORD: a senha do servidor de banco de dados.
- USER: o nome de usuário do banco de dados.
- HOST: o endereço do servidor de banco de dados (por exemplo, localhost ou 127.0.0.1).
- DATABASE: o nome do banco de dados que você deseja usar (neste caso, iot_server).

Aqui está um exemplo de como preencher o arquivo .env:
``` 
PASSWORD=senha_do_servidor
USER=nome_de_usuario
HOST=endereco_do_servidor
DATABASE=iot_server
```

Certifique-se de preencher essas informações corretamente, para que a API possa se conectar ao banco de dados com sucesso , lembrando que o arquivo .env tem que estar na mesma pasta de `app.py`.
- Necessario a instalação da iot_server database em seu server para o funcionamento da api, o arquivo sql que configura a database esta em `/App/MySQL Server Config`  ele e um script sql , so e necessario rodar ele no seu server e a database ja vai estar configurada.
- Caso tudo ocora bem a conexão com o banco de dados sera feita , sem nenhum problema e você podera usufruir de tudo que a api tem.

# Usage:
- Para ligar a API e necessario que o banco de dados esteja ativo e configurado de acordo com as instruções acima , apos isso basta iniciar o app.py .
  - no Windows `python.exe .\app.py` estando na mesma pasta do arquivo app.py.
- A documentação de como usar a api esta na pasta `/App/docs` usando swagger ou Redoc voce pode visualizar de forma detalhada todas as funcionalidades e os requerimentos para usar todos os endpoints dessa API.
- Abaixo um breve resumo de cada endpoint:
  - GET:<br>
    `/MensurementUnits` : Retorna todos os  mensurament units (Unidades de medida)<br>
    `/UserDevices/user`: Retornas um json com todos os sensor devices de um usuario ( necessario o nome do usuario)<br>
    `/UserDevice/SensorDeviceKey` : Retorna um json com informações de um device especifico ( necessario ter a SensorDeviceKey)<br>
    `/UserDevice/Stream/StreamKey` : Retorna um json com as informações de uma stream de um sensor especifico ( necessario ter a StreamKey)<br>
  - POST:<br>
    `/NewDevice/user` : Cria um novo sensor device associado ao usuario .(necessario um usuario existente)<br>
    `/NewStream/SensorKey/SensorKey` : Cria uma nova stream para um sensor especifico . (necessario ter a SensorKey)<br>
    `/StreamData/StreamKey/StreamKey` : Cria um novo dado para uma Stream . (necessario ter a StreamKey)
    
    
  
