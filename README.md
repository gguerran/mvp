# Gerêcia de Demandas da Federação de Comércio
Repositório para o software que gerencia as demadas da Federação de Comércio.

## Para utilizar a aplicação em seu computador:
Para fazer uso da aplicação, uma sequência de passos devem ser executadas. A seguir, elas serão enumeradas e abaixo poderá ver os comandos utilizados no terminal.\
(Feito baseado no sistema operacional Linux. Se você usa outro sistema operacional, veja os comandos equivalentes para o mesmo. Pressupõe-se também que o usuário possua em sua máquina já instalados os softwares Docker e Docker-Compose, estes já com permissão de execução. Caso não os possua, o tutorial a seguir ajuda a instalar o docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt e o docker-compose: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-pt)


1.: Clone o repositório;\
```git clone https://github.com/gguerran/mvp.git```


2.: Entre na pasta baixada;\
```cd mvp```


3.: Copie o arquivo env_sample como .env;\
```cp env_sample .env```\
(deve alterar a SECRET_KEY para uma chave mais segura, utilizando um editor de texto)


4.: Inicie o container da aplicação;\
```docker-compose up --build -d```


5.: Execute o terminal dentro do container;\
```docker exec -it <container_name> /bin/bash```\
(a princípio, o container_name é mvp_app_1, mas caso tenha mudado, utilize o comando ``` docker ps```, veja o nome do container e aplique no comando)


6.: Dentro do terminal do container, o banco de dados da aplicação deve ser gerado. Esse comando rodará as migrations;\
```python manage.py migrate```


7.: Ainda dentro do container, o super usuário (administrador) deve ser criado, através do comando;\
```python manage.py createsuperuser```


Se tudo correr bem, a aplicação deverá estar em pleno funcionamento. Para testar isso, abra o navegador e digite na url: ```http://127.0.0.1:8001/admin```.


Utilize os dados de superusuário, criado anteriormente e terá acesso ao painel adminitrativo, que gerencia toda a aplicação.\
Para continuar e poder utilizar as requisições da API, deverá seguir os seguintes passos:

1.: No menu DJANGO OAUTH TOOLKIT clique em Application -> Adicionar;\
(Percebe-se que os campos Client id e Client Secret já estão preenchidos. Guarde-os, pois precisaremos mais tarde)


2.: No campo Client Type, selecione a opção 'Confidential' e no campo Autorization Grant Type, selecione a opção 'Resource owner password-based';

A partir disso, podemos abrir o software Postman e importar a coleção do arquivo 'FINXI - DEMANDAS.postman_collection.json'. Nele contém alguns endpoints para o consumo  da API.
A documentação mais detalhada da API se encontra no arquivo DOC.md, poderá consulta-la para o melhor uso da API.
Dentro da coleção, na requisição 'Login', deve-se configurar alguns campos do body:\
Lembra da Application que criamos? vá até a listagem e abra a que foi criada segundo as intruções acima.\
**OBS.: Não deve-se alterar nada na mesma, apenas consultar os dados**


1.: No campo 'client_id' da requisição, no Postman,vc deverá copiar o que está na application, no campo 'Client id';

2.: No campo 'client_secret' da requisição, no Postman, vc deverá copia o que está na application, no campo 'Client secret';

A partir disso, a API poderá ser utilizada.
É importante ressaltar que a requisição 'Criação de demandante' não necessita de autenticação, poderá criar o demandante através da API, na requisição e utilizar os dados da
 mesma para o login (em username usar o email).
 
 
 Agora sim, você deve consultar a documentação no arquivo 'DOC.md' e utilizar a API.
 
 Obrigado :)
