**Documentação da API**
----

OBS.:
	Através do software Postman, o arquivo `FINXI - DEMANDAS.postman_collection.json` pode ser importado e o ambiente
	para testes estará configurado, de forma que todas as rotas da API estarão disponíveis.


**Login**
----
  Gera o token de acesso à api

* **URL**

  /api/v1/oauth/token/

* **Method:**

  `POST`

* **Headers**
  ``` console
  {
    "Contet-Type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache"
  }
  
* **Data Params**

  ``` console
  {
    "grant_type": "password",
    "client_id": "<client id gerado em applications no admin>"
    "client_secret": "<client secret gerado em applications no admin>"
    "username": "test@test.com",
    "password": "123$#45"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** 
    ``` console
    {
      "access_token": "<access_token>",
      "expires_in": 36000,
      "token_type": "Bearer",
      "scope": "read write",
      "refresh_token": "<refresh_token>"
    }
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** 
    ``` console
    {
      "error": "invalid_client"
    }
    
  **Causa: Client id ou client secret diferentes do que foram gerados no admin**

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    ``` console
    {
      "error": "invalid_grant",
      "error_description": "Invalid credentials given."
    }
  
  **Causa: Dados de usuário (username ou password) incorretos**
   


**Criar Demandante**
----
  Cria usuário para fazer uso da API

* **URL**

  /api/v1/accounts/

* **Method:**

  `POST`

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json"
  }

* **Data Params**

  ``` console
  {
    "name": "Test",
    "email": "test@test.com",
    "phone": "(99)99999-9999",
    "password1": "#pass123",
    "password2": "#pass123"
  }

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:**
    ```console
    {
    "id": "<hash uuid>",
    "name": "Test",
    "email": "test@test.com",
    "is_active": true,
    "phone": "(99)99999-9999",
    "created_at": "<datetime da criação>"
    }
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    ``` console
      { 
        error: {
          email: [
              "Usuário com este e-mail já existe."
            ]
          },
       }
  
  OU
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:** ``` console
      { 
        error: {
          phone: [
              "Usuário com este telefone já existe."
            ]
          },
       }

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    ``` console
      {
        error: {<field>:
            [
              "Este campo é obrigatório"
            ]
         },
       }


**Listar demandantes**
----
  Lista os demandantes

* **URL**

  127.0.0.1:8001/api/v1/accounts/

* **Method:**

  `GET`

* **Data Params**

  None
* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `
    ``` console
    [
      {
        "id": "<hash uuid>",
        "name": "Test",
        "email": "test@test.com",
        "is_active": true,
        "phone": "(99)99999-9999",
        "created_at": "<datetime da criação>"
      }
    ]
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**


**Detalhar demandante**
----
  Detalha o demandante

* **URL**

  127.0.0.1:8001/api/v1/accounts/<id>/

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  None
* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `
    ``` console
      {
        "id": "<hash uuid>",
        "name": "Test",
        "email": "test@test.com",
        "is_active": true,
        "phone": "(99)99999-9999",
        "created_at": "<datetime da criação>"
      }


 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
  
  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID do demandante está incorreto ou não pertence ao usuário**
   

**Editar demandante**
----
  Edita o demandante

* **URL**

  127.0.0.1:8001/api/v1/accounts/<id>/

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  ``` console
      {
        "name": "Test",
        "email": "test@test.com",
        "phone": "(99)99999-9999",
      }

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ``` console
      {
        "id": "<hash uuid>",
        "name": "Test",
        "email": "test@test.com",
        "is_active": true,
        "phone": "(99)99999-9999",
        "created_at": "<datetime da criação>"
      }


 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      {
        "<field>": [
            "Este campo é obrigatório."
        ]
      }
     
   **Os campos no detalhe não foram informados**
    
  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID do demandante está incorreto ou não pertence ao usuário**

   

**Editar senha do demandante**
----
  Edita a senha do demandante

* **URL**

  127.0.0.1:8001/api/v1/accounts/<id>/

* **Method:**

  `PATCH`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  ``` console
      {
        "last_pass": "#pass123",
        "password": "#pass123",
        "password2": "#pass123"
      }

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** 
    ``` console
      {
        "id": "<hash uuid>",
        "name": "Test",
        "email": "test@test.com",
        "is_active": true,
        "phone": "(99)99999-9999",
        "created_at": "<datetime da criaçãofor>"
      }


 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      {
        "<field>": [
            "Este campo é obrigatório."
        ]
      }
     
   **Os campos no detalhe não foram informados**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
        [
            "Antiga senha inválida"
        ]

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
        [
            "As senhas não conferem"
        ]  

  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID do demandante está incorreto ou não pertence ao usuário**


**Criar Demanda**
----
  Cria uma demanda

* **URL**

  /api/v1/demand/

* **Method:**

  `POST`

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json"
  }

* **Data Params**

  ``` console
  {
      "description": "Teste",
      "state": "PI",
      "city": "XXXX",
      "district": "XXXXX",
      "street": "Rua XXX",
      "number": 222,
      "status": "Aberta"
   }

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:**
    ```console
    {
      "id": "<hash uuid>",
      "description": "Teste",
      "state": "PI",
      "city": "XXXX",
      "district": "XXXXX",
      "street": "Rua XX",
      "number": 222,
      "email": "test@test.com",
      "phone": "(99)99999-9999",
      "status": "Aberta",
      "advertiser": "<hash uuid de quem fez a requisição>",
      "created_at": "<datetime da criação>"
    }
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    ´´´ console
      {
        "error": {
          "<field>": [
            "Este campo é obrigatório"
            ]
        }
      }

  OU
  
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }


**Listar demandas**
----
  Lista as demandas

* **URL**

  127.0.0.1:8001/api/v1/demand/

* **Method:**

  `GET`

* **Data Params**

  None
* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ``` console
    [
      {
        "id": "<hash uuid>",
        "description": "Teste",
        "state": "PI",
        "city": "XXXX",
        "district": "XXXXX",
        "street": "Rua XX",
        "number": 222,
        "email": "test@test.com",
        "phone": "(99)99999-9999",
        "status": "Aberta",
        "advertiser": "<hash uuid de quem fez a requisição>",
        "created_at": "<datetime da criação>"
      }
    ]
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**


**Detalhar demanda**
----
  Detalha a demanda

* **URL**

  127.0.0.1:8001/api/v1/demand/<id>

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`
 
* **Data Params**

  None
* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ``` console
    {
      "id": "<hash uuid>",
      "description": "Teste",
      "state": "PI",
      "city": "XXXX",
      "district": "XXXXX",
      "street": "Rua XX",
      "number": 222,
      "email": "test@test.com",
      "phone": "(99)99999-9999",
      "status": "Aberta",
      "advertiser": "<hash uuid de quem fez a requisição>",
      "created_at": "<datetime da criação>"
     }
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
 
  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID da demanda está incorreto ou não pertence ao usuário**
 

**Editar demanda**
----
  Edita a demanda

* **URL**

  127.0.0.1:8001/api/v1/demand/<id>/

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  ``` console
      {
        "description": "Teste",
        "state": "PI",
        "city": "XXXX",
        "district": "XXXXX",
        "street": "Rua XXX",
        "number": 222,
        "status": "Aberta"
      }

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ``` console
      {
        "id": "<hash uuid>",
        "description": "Teste",
        "state": "PI",
        "city": "XXXX",
        "district": "XXXXX",
        "street": "Rua XX",
        "number": 222,
        "email": "test@test.com",
        "phone": "(99)99999-9999",
        "status": "Aberta",
        "advertiser": "<hash uuid de quem fez a requisição>",
        "created_at": "<datetime da criação>"
      }

* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      {
        "<field>": [
            "Este campo é obrigatório."
        ]
      }
     
   **Os campos no detalhe não foram informados**
    
  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID da demanda está incorreto ou não pertence ao usuário**
 
 
 **Finalizar demanda**
----
  Finaliza a demanda

* **URL**

  127.0.0.1:8001/api/v1/demand/<id>/

* **Method:**

  `PATCH`

*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  ``` console
      {
        "status": "Finalizada"
      }

* **Headers**
  ``` console
  {
    "Contet-Type": "application/json",
    "Authorization": "Bearer <access_token gerado no login>"
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ``` console
      {
        "id": "<hash uuid>",
        "description": "Teste",
        "state": "PI",
        "city": "XXXX",
        "district": "XXXXX",
        "street": "Rua XX",
        "number": 222,
        "email": "test@test.com",
        "phone": "(99)99999-9999",
        "status": "Finalizada",
        "advertiser": "<hash uuid de quem fez a requisição>",
        "created_at": "<datetime da criação>"
      }

* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      {
        "<field>": [
            "Este campo é obrigatório."
        ]
      }
     
   **Os campos no detalhe não foram informados**
    
  OU
  
  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID da demanda está incorreto ou não pertence ao usuário**
  
  OU
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      [
           "A demanda já estava finalizada."
       ]
     
   **Acontece quando a demanda já havia sido finalizada antes**
   
   
  OU
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**
      ``` console
      [
           "A demanda já estava aberta."
       ]
     
   **Acontece quando a demanda estava aberta e tenta-se abri-la**


**Excluir demanda**
----
  Exclui uma demanda.

* **URL**

  127.0.0.1:8001/api/v1/demand/<id>/

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `id=[<uuid>]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 NO CONTENT<br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:**
      ``` console
      {
        "detail": "Not found."
      }
     
   **Causa: ID da demanda está incorreto ou não pertence ao usuário**
  

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**
      ``` console
      {
        "detail": "Authentication credentials were not provided."
      }
     
   **Causa: Token informado está expirado ou inválido**
