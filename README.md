# Tutorial - Banco de Dados com Python do jeito FÁCIL
Tutorial de como usar Banco de Dados com Python do Jeito Facil. Baseado no Video do Empowerdata | Python ([Clique aqui para assistir](https://youtube.com/watch?v=7xQhlf8qnsE))

## Definições
<p>Usaremos um banco de dados sem precisar instalar nenhuma plataforma.</p>

**SQLAlchemy:** 
* Um *ORM* (Object Relational Mapping). Permite trabalhar com BDs utilizando classes e objetos na linguagem de programação - no nosso caso Python. <br>
* Podemos *abstrair o SQL*, ou seja, manipulamos os dados sem uso dessa linguagem. 
* Ele é portável <br> 
* Suporte a consulta complexas
* Controle transacional como Commit e Rollback
* Permite utilizar o SQL nativo.

## Requisito
* Coloque o nome que quiser no seu projeto.
* Utilize o terminal que quiser (no meu caso, utilizei o terminal do meu ambiente wsl2, o bash), no tutorial baseado, o autor utiliza o gitbash
* acesse o seu vscode
* opcional: prepare o ambiente com a virtualização. No exemplo, usamos a lib poetry para tratar o ambiente. O Comando é  ```poetry init``` (prepara o ambiente) e ```poetry shell``` inicializa o ambiente virtual.
* Adiciona o complemento do vscode chamado *SQLite Viewer*
* instale a lib do SQLAlchemy para utilização deste tutorial ```poetry add sqlalchemy```
