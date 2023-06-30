# Projeto de Adoção de Bens

Este é um projeto de adoção de bens, que visa facilitar a doação de objetos, pertences e recursos materiais de pessoas ou organizações para aqueles que mais precisam.

## Funcionalidades

O projeto de adoção de bens possui as seguintes funcionalidades principais:

- Criação de contas para doadores e receptores.
- Autenticação de usuários com login e recuperação de senha.
- Listagem de doações disponíveis para adoção.
- Realização de doações por parte dos doadores.
- Recebimento e registro de doações por parte dos receptores.

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias:

- Linguagem de programação: [Python](https://www.python.org)
- Framework web: [Django](https://www.djangoproject.com)
- Banco de dados: [SQLite](https://www.sqlite.org)
- HTML, CSS e JavaScript para a interface do usuário.

## Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. Certifique-se de ter o Python instalado. Recomenda-se utilizar a versão 3.7 ou superior.

2. Clone este repositório para o seu ambiente local:

   ```shell
   git clone https://github.com/corteisjr/Desapego.git
   ```

3. Acesse o diretório do projeto:

   ```shell
   cd Desapego
   ```

4. Crie um ambiente virtual para isolar as dependências do projeto:

   ```shell
   python -m venv venv
   ```

5. Ative o ambiente virtual:

   - No Windows:

     ```shell
     venv\Scripts\activate
     ```

   - No Linux ou macOS:

     ```shell
     source venv/bin/activate
     ```

6. Instale as dependências do projeto:

   ```shell
   pip install -r requirements.txt
   ```

7. Execute as migrações do banco de dados:

   ```shell
   python manage.py migrate
   ```

8. Inicie o servidor de desenvolvimento:

   ```shell
   python manage.py runserver
   ```

9. Acesse o aplicativo em seu navegador em [http://localhost:8000](http://localhost:8000).

## Contribuição

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Crie um fork deste repositório em sua conta do GitHub.

2. Clone o fork para o seu ambiente local:

   ```shell
   git clone https://github.com/corteisjr/Desapego.git
   ```

3. Crie um branch para suas alterações:

   ```shell
   git checkout -b minha-feature
   ```

4. Faça as alterações desejadas e adicione os arquivos modificados:

   ```shell
   git add .
   ```

5. Faça um commit das suas alterações:

   ```shell
   git commit -m "Minha feature: descrição das alterações"
   ```

6. Faça um push para o seu fork:

   ```shell
   git push origin minha-feature
   ```

7. Abra um pull request no repositório original para revisão das suas alterações.

## Licença

Este projeto é distribuído

 sob a licença [MIT](LICENSE). Sinta-se à vontade para utilizar, modificar e distribuir o projeto de acordo com os termos da licença.

## Contato

Em caso de dúvidas ou sugestões, entre em contato conosco:

- Nome: Corteis
- Email: corteisjunior@gmail.com
- GitHub: [corteisjr](https://github.com/corteisjr)
