
# Título do Projeto

Uma breve descrição sobre o que esse projeto faz e para quem ele é  




## Autores

- [Patrick Augusto Lins de Oliveira Damião](https://github.com/Pack0042)

- [Pedro Henrique de Paula Andrade](https://github.com/phandrad3)


## Documentação da API

#### Piloto

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idPiloto` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | **Obrigatório**. A chave da sua API |
| `nivel` | `INT` | **Obrigatório**. A chave da sua API |
| `Nave_idNave` | `INT` | Chave estrangeira de **Nave** |


#### Nave

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idNave` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | **Obrigatório**. A chave da sua API |
| `capacidade` | `FLOAT` | **Obrigatório**. A chave da sua API |
| `velocidadeMaxima` | `FLOAT` | **Obrigatório**. A chave da sua API |

#### Missao

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idMissao` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | **Obrigatório**. A chave da sua API |
| `duracao` | `TIME` | **Obrigatório**. A chave da sua API |
| `status` | `ENUM` | "Planejada", "Em Andamento", "Concluída" |
| `Piloto_idPiloto` | `INT` | Chave estrangeira de **Piloto** |

#### Planeta

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nomePlaneta` | `VARCHAR(45)` | **Chave Primária** |
| `tipo` | `ENUM` | "Gasoso", "Aquático" |
| `habitavel` | `BINARY` | "True", "False" |

#### Recurso

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nomeRecurso` | `VARCHAR(45)` | **Chave Primária** |
| `tipo` | `ENUM` | "Combustível", "Gás" |
| `valorUnitario` | `FLOAT` | **Obrigatório**. A chave da sua API |


#### Planeta_has_Recurso

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Planeta_nomePlaneta` | `VARCHAR(45)` | **Chave Primária** |
| `Recurso_nomeRecurso` | `VARCHAR(45)` | **Chave Primária** |
| `QuantidadeRecurso` | `FLOAT` | **Obrigatório**. A chave da sua API |

