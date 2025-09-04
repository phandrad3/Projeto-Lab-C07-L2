
# Outer Wilds

O Outer Wilds é um sistema voltado para o gerenciamento de missões interplanetárias onde pilotos, equipados com suas naves espaciais, partem em missões rumo à diferentes planetas e catalogam qualquer recurso encontrado.




## Autores

- [Patrick Augusto Lins de Oliveira Damião](https://github.com/Pack0042)

- [Pedro Henrique de Paula Andrade](https://github.com/phandrad3)


## Entidades e Relacionamentos

#### Piloto

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idPiloto` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | Nome do **Piloto** |
| `nivel` | `INT` | Nível de experiência do **Piloto** |
| `Nave_idNave` | `INT` | Chave estrangeira de **Nave** |


#### Nave

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idNave` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | Nome da **Nave** |
| `capacidade` | `FLOAT` | Capacidade máxima de carga da **Nave** |
| `velocidadeMaxima` | `FLOAT` | Velocidade máxima da **Nave** |

#### Missao

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `idMissao` | `INT` | **Chave Primária** |
| `nome` | `VARCHAR(45)` | Nome da **Missao** |
| `duracao` | `TIME` | Duração total da **Missao** |
| `status` | `ENUM` | "Planejada", "Em Andamento", "Concluída" |
| `Piloto_idPiloto` | `INT` | Chave estrangeira de **Piloto** |

#### Missao_Realizada

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Planeta_nomePlaneta` | `VARCHAR(45)` | **Chave Primária / Chave estrangeira de Planeta** |
| `Missao_idMissao` | `INT` | **Chave Primária / Chave estrangeira de Missao** |
| `problemas` | `VARCHAR(200)` | Problemas relatados durante a **Missao** |

#### Planeta

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nomePlaneta` | `VARCHAR(45)` | **Chave Primária** |
| `tipo` | `ENUM` | "Gasoso", "Aquático", "Rochoso" |
| `habitavel` | `TINYINT(1)` | 0 = Falso, 1 = Verdadeiro |

#### Planeta_has_Recurso

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Planeta_nomePlaneta` | `VARCHAR(45)` | **Chave Primária / Chave estrangeira de Planeta** |
| `Recurso_nomeRecurso` | `VARCHAR(45)` | **Chave Primária / Chave estrangeira de Recurso** |
| `quantidadeRecurso` | `FLOAT` | Quantidades de recursos no **Planeta** |

#### Recurso

| Chave   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `nomeRecurso` | `VARCHAR(45)` | **Chave Primária** |
| `tipo` | `ENUM` | "Combustível", "Gás", "Minério", "Alimento" |
| `valorUnitario` | `FLOAT` | Preço por unidade do **Recurso** |


#### Piloto <--> Nave 
    Cada piloto possui uma nave e cada nave só pode ter um piloto. (1:1)

#### Piloto <--> Missão
    Um piloto pode realizar várias missões e cada missão é realizada por apenas um piloto. (1:N)

#### Missão <--> Planeta 
    Uma missão pode visitar vários planetas e um planeta pode ser alvo de várias missões diferentes. (N:M)

#### Planeta <--> Recurso 
    Vários planetas podem conter vários recursos naturais e vários recursos naturais podem existir em vários planetas. (N:M)



