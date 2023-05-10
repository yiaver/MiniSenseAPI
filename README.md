# # API_de_monitoramento_de_dispositivos_IOT
Nesse repositorio se encontra a API de monitoramento de sistemas IOT que foi feita para o MiniSense

# Instalation :
-Instale o Python 3.11.2
- Link oficial do python de como instalar no Windows <a>https://python.org.br/instalacao-windows/</a> .
- Link oficial do python de como instalar no Linux <a>https://python.org.br/instalacao-linux/</a> .
- (OPICIONAL):
  - Caso queira voce pode criar um ambiente virtual para armazenar as bibliotecas.
  - Link oficial do python de como criar um ambiente virtual <a>https://docs.python.org/pt-br/3/library/venv.html</a>
  - apos criar o ambiente emtre nele com os comandos do seu Sistema operacional.
- Apos ter instalado o python3 corretamente instale as bibliotecas necessarias com:
`pip3 install -r requirements.txt`
- Instale um servidor MySQL Server Version = 8.0.33 , caso queira instale tambem a MySQL Workbench para configurar a database com o script a baixo.
- Necessario a instalação da iot_server database em seu server para o funcionamento da api, o arquivo sql que configura a database esta em `/App/MySQL Server Config` e um script sql so e necessario rodar ele no seu server e a database ja vai estar configurada.
- Conecte-se ao banco de dados preenchendo as informações do .env:
```
PASSWORD = MySqlserverPassWord(aqui vai a senha do servidor)
USER = MySqlUser ( aqui o ususario)
HOST = Your host here ( aqui o host , se for localhost no windows o default e 127.0.0.1 )
DATABASE = your database here (aqui vai a database que você vai usar que no caso e a iot_server )
```
- Caso tudo ocora bem a conexão com o banco de dados sera feita , sem nenhum problema e você podera usufruir de tudo que a api tem.

# Usage:
- A documentação de como usar a api esta na pasta `/App/docs` usando swagger ou Redoc voce pode visualizar de forma detalhada todas as funcionalidades e os requerimentos para usar todos os endpoints dessa API.
- A baxo um breve resumo de cada endpoint:
  - GET:<br>
    /MensurementUnits : Retorna todos os  mensurament units (Unidades de medida)<br>
    /UserDevices/user: Retornas um json com todos os sensor devices de um usuario ( necessario o nome do usuario)<br>
    /UserDevice/SensorDeviceKey : Retorna um json com informações de um device especifico ( necessario ter a SensorDeviceKey)<br>
    /UserDevice/Stream/StreamKey : Retorna um json com as informações de uma stream de um sensor especifico ( necessario ter a StreamKey)<br>
  - POST:<br>
    
  
