# Prefeitura + Próxima de Você

Prefeitura + Próxima de Você" é uma plataforma integrada desenvolvida para aprimorar a comunicação entre os cidadãos e as entidades públicas municipais. Seu principal objetivo é estreitar o relacionamento entre a população e o poder público, promovendo uma interação mais eficiente, acessível e transparente.

## O que foi feito:

✅ CRUD de Chamados
✅Configuração do admin
✅criação de script com signals para criação 
de credenciais padrão de admin e de usuários para teste.
✅inclusão da função de alteração do status do chamado pelo admin
✅Criação de formulário para cadastro de usuários
✅ função de aprovação de usuários pelo admin 
✅nos layouts de cadastro e login, com a utilização de inputmask
(para preenchimento correto dos dados de telefone e cpf)


## Observações para utilização do sistema:
para empregar a responsividade inicial do sistema para o presente momento, foram criadas  condições das quais:

- no nome não serão aceitados números;
- quando o email não for preenchido de forma correta, surge uma sugestão em formato pop-up, para auxílio;
- antes de rodar o projeto todo, pela nossa utilização de banco de dados, sugere-se que sejam feitas as migrações pelos seguintes comandos: 
python manage.py makemigrations e logo após, python manage.py migrate, assim, criando credenciais de admin e de usuário, deixando o período de testes mais rápidos.

Credenciais que serão adicionadas pelo signals: 
Para admin:
username = "admin"
    password = "admin123"
    email = admin@example.com

Para usuário comum:
cpf = "12345678900"
    senha = "senha123"
    email = "usuario@example.com"
    nome = "Usuário Padrão"

## Autores

- Beatriz Cristina Roecker [@beatrizrckr97](https://github.com/beatrizrckr97)
- Cristian Rafael Da Rosa [@Cristiantdi](https://github.com/Cristiantdi)
- Guilherme Estevão Silva [@GuilhermeES](https://github.com/GuilhermeES)
- Julia Lima Goulart  [@julialg-220](https://github.com/julialg-220)
- Renan da Silva Cunha  [@BaraoRJ](https://github.com/BaraoRJ)
