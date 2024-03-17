
# My Django App

Este é um projeto Django que utiliza Docker Compose para gerenciar um ambiente
de desenvolvimento e integração contínua (CI/CD) para automatizar o teste e
a implantação do código.

## Instruções de Instalação

Para executar este projeto localmente, siga as instruções abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/Dhrds/appmed.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd appmed
   ```
3. crie o .env.dev
   '''bash
   sudo nano .env
   '''
   exemplo na pasta 'exemplos'

5. Intale e inicie o ambiente Docker Compose:

   ```bash
   docker-compose up
   ```

6. Acesse a aplicação em seu navegador em
[http://localhost:8000](http://localhost:8000).

## Instruções de Uso

Após iniciar o ambiente Docker Compose, você pode interagir com a aplicação
normalmente. Qualquer alteração feita nos arquivos será automaticamente
refletida no servidor de desenvolvimento.

## Testes

Este projeto utiliza pytest para testes automatizados.
Para executar os testes, utilize o seguinte comando:

```bash
pytest
```

        
