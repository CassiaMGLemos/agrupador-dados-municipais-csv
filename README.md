# Agrupador de Dados Municipais

## 📋 Descrição do Projeto

Este projeto processa e agrega dados municipais de abastecimento, agrupando informações por código geográfico (Geocod) e calculando somas das variáveis V012, V013, V014 e V015.

O script lê um arquivo CSV com múltiplas linhas por município, remove dados inválidos (valores "X" ou NaN), agrupa os dados por município e gera um arquivo consolidado com as somas totais.

## Dependências do sistema 

- Python 3.6 ou superior
- Bibliotecas: `pandas`
- 

### Baixar o Python (Windows, MacOS, Linux)
- [Python Official Website](https://www.python.org/downloads/)


## 🚀 Como Usar

### 1. Criar Ambiente Virtual

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual (Linux/Mac)
source .venv/bin/activate

# Ativar ambiente virtual (Windows)
.venv\Scripts\activate
```

### 2.1 Instalar Dependências

```bash
pip install pandas
```

### 2.2 Instalar Dependências via requirements.txt (Opcional - Versões das bibliotecas fixas)

```bash
pip install -r requirements.txt
```

### 3. Preparar Arquivo de Entrada

Certifique-se de que o arquivo de entrada está no formato correto:

- **Nome padrão:** `dados.csv`
- **Formato:** CSV com separador vírgula (`,`)
- **Colunas obrigatórias:** `Geocod`, `V012`, `V013`, `V014`, `V015`

Exemplo:
```csv
Geocod,V012,V013,V014,V015
1100015,46,251,0,6
1100015,68,186,0,10
1100023,1,7,0,1
```

### 4. Executar o Script

#### Uso Básico (valores padrão)

```bash
python3 agrupador_planilhas.py
```

#### Com Parâmetros Personalizados

```bash
python3 agrupador_planilhas.py -i dados.csv -o resultado.csv
```

#### Ver Ajuda

```bash
python3 agrupador_planilhas.py --help
```

## ⚙️ Parâmetros de Linha de Comando

O script aceita os seguintes argumentos via linha de comando:

| Argumento | Forma Curta | Forma Longa | Padrão | Descrição |
|-----------|-------------|-------------|--------|-----------|
| Entrada | `-i` | `--input` | `dados.csv` | Caminho do arquivo CSV de entrada |
| Saída | `-o` | `--output` | `resultado.csv` | Caminho do arquivo CSV de saída |
| Separador | `-s` | `--separator` | `;` | Separador de colunas do arquivo de saída |
| Encoding | `-e` | `--encoding` | `utf-8` | Codificação do arquivo de saída |
| Decimal | `-d` | `--decimal` | `,` | Separador decimal (`,` para LibreOffice, `.` para Excel em inglês) |

### Exemplos de Uso

**Exemplo 1:** Usar valores padrão
```bash
python3 agrupador_planilhas.py
```

**Exemplo 2:** Especificar apenas entrada e saída
```bash
python3 agrupador_planilhas.py -i meus_dados.csv -o resultado_processado.csv
```

**Exemplo 3:** Gerar CSV para Excel (separador vírgula, decimal ponto)
```bash
python3 agrupador_planilhas.py -i dados.csv -o resultado.csv -s "," -d "."
```

**Exemplo 4:** Usar todos os parâmetros
```bash
python3 agrupador_planilhas.py --input dados.csv --output resultado.csv --separator ";" --encoding "utf-8" --decimal ","
```

## 📊 Saída Esperada

O script gera um arquivo CSV com os seguintes dados:

- **Nome:** `resultado.csv` (configurável)
- **Formato:** CSV com separador ponto-e-vírgula (`;`)
- **Separador decimal:** Vírgula (`,`) - compatível com LibreOffice
- **Estrutura:** Uma linha por município com as somas agregadas

### Exemplo de Saída

```csv
Geocod;V012;V013;V014;V015
1100015;2500;5800;0;350
1100023;3200;4100;0;180
1100031;1800;2900;0;120
```

### Informações no Console

Durante a execução, o script exibe:

```
Iniciando o processamento às : 14:30:45

============================================================
CONFIGURAÇÕES
============================================================
Arquivo de entrada:    dados.csv
Arquivo de saída:      resultado.csv
Separador CSV:         ';'
Encoding:              utf-8
Separador decimal:     ','
============================================================

Lendo arquivo 'dados.csv'...

Linhas removidas com X/NaN: 15

Agrupando dados por Geocod e somando os valores...
Coluna V012 convertida para int
Coluna V013 convertida para int
Coluna V014 convertida para int
Coluna V015 convertida para int

Dados agrupados (primeiras 15 linhas):
     Geocod   V012   V013  V014  V015
0   1100015   2500   5800     0   350
1   1100023   3200   4100     0   180
...

Salvando dados agrupados em 'resultado.csv'...
Arquivo 'resultado.csv' gerado com sucesso!
Total de municípios únicos: 52
Tempo de execução: 0.45 segundos
Processamento finalizado às : 14:30:46
```

## 🔧 Tratamento de Dados

O script realiza as seguintes operações:

1. **Conversão de tipos:** Força conversão para numérico com `errors='coerce'`
2. **Remoção de inválidos:** Remove linhas com valores "X" ou NaN
3. **Agrupamento:** Agrupa por `Geocod` e soma os valores
4. **Otimização de tipos:** Converte automaticamente para `int` ou `float` conforme necessário
   - Se todos os valores são inteiros (`.0`), converte para `int`
   - Se há casas decimais, mantém como `float`

## 📁 Estrutura do Projeto

```
estrutura_esperada/
├── agrupador_planilhas.py                              # Script principal
├── dados.csv               # Arquivo de entrada (não incluído)
├── resultado.csv         # Arquivo de saída (gerado)
└── README.md                                   # Este arquivo
```

## 📝 Licença

Este projeto está licenciado sob a Licença MIT [LICENSE](LICENSE) - veja os detalhes abaixo:


## 💬 Suporte

Para reportar problemas ou sugerir melhorias:

1. Abra uma [issue](https://github.com/CassiaMGLemos/agrupador-dados-municipais-csv/issues) no GitHub
2. Entre em contato através do e-mail: cassia.mg.lemos@gmail.com

---

## 👥 Autores
- **Cassia MG Lemos** - *Colaborador e Desenvolvedor* - [GitHub](https://github.com/CassiaMGLemos)
- **Mário de Araújo Carvalho** - *Colaborador e Desenvolvedor* - [GitHub](https://github.com/MarioCarvalhoBr)


**Desenvolvido com ❤️ pela equipe AdaptaBrasil para validação rigorosa de dados científicos e ambientais.**