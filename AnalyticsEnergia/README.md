# Análise de Potencial Energético - Brasil

## Descrição
Este projeto realiza uma análise completa do potencial de instalação de capacidade energética por estado brasileiro, considerando:

- Capacidade atual instalada
- Características demográficas (população, densidade)
- Indicadores econômicos (PIB, PIB per capita)
- Consumo energético per capita
- Déficit/superávit energético atual

## Como Executar

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Executar análise:
```bash
python analise_potencial_energetico.py
```

## Outputs Gerados

- **Relatório no console**: Top 10 estados com maior potencial
- **Gráficos**: Visualizações salvas como PNG
- **Arquivo Excel**: Resultados completos para análise detalhada

## Metodologia

O score de potencial é calculado considerando:
- 40% - Déficit energético atual
- 30% - Potencial de crescimento econômico  
- 30% - Fatores demográficos

## Interpretação dos Resultados

Estados com **maior score** têm:
- Alto déficit energético atual
- Bom potencial econômico
- Características demográficas favoráveis

Ideal para priorização de investimentos em infraestrutura energética.

### Passo 1: Configuração do Ambiente

Certifique-se de que você tem o Python e a biblioteca Pandas instalados. Você pode instalar o Pandas usando o pip, se ainda não o fez:

```bash
pip install pandas
```

### Passo 2: Criar um Novo Script Python

Crie um novo arquivo Python, por exemplo, `analise_energia_brasil.py`.

### Passo 3: Importar Bibliotecas Necessárias

No seu script, comece importando as bibliotecas necessárias:

```python
import pandas as pd
```

### Passo 4: Criar a Tabela de Capacidade Elétrica Instalada

Você pode criar um DataFrame do Pandas que contenha dados sobre a capacidade elétrica instalada no Brasil. Aqui está um exemplo de como você pode fazer isso:

```python
# Dados de exemplo sobre a capacidade elétrica instalada no Brasil
dados_capacidade = {
    'Fonte': ['Hidrelétrica', 'Termelétrica', 'Eólica', 'Solar', 'Biomassa'],
    'Capacidade Instalada (MW)': [109000, 30000, 19000, 15000, 10000],
    'Porcentagem do Total (%)': [60, 15, 10, 8, 7]
}

# Criar DataFrame
df_capacidade = pd.DataFrame(dados_capacidade)

# Exibir a tabela
print("Capacidade Elétrica Instalada no Brasil:")
print(df_capacidade)
```

### Passo 5: Análise do Potencial de Produção

Você pode adicionar algumas análises básicas, como calcular a capacidade total instalada e a porcentagem de cada fonte em relação ao total.

```python
# Calcular a capacidade total instalada
capacidade_total = df_capacidade['Capacidade Instalada (MW)'].sum()
print(f"\nCapacidade Total Instalada: {capacidade_total} MW")

# Calcular a porcentagem de cada fonte em relação ao total
df_capacidade['Porcentagem do Total (%)'] = (df_capacidade['Capacidade Instalada (MW)'] / capacidade_total) * 100

# Exibir a tabela atualizada
print("\nCapacidade Elétrica Instalada com Porcentagens Atualizadas:")
print(df_capacidade)
```

### Passo 6: Executar o Script

Salve o arquivo e execute-o em seu terminal ou ambiente de desenvolvimento. Você verá a tabela de capacidade elétrica instalada e algumas análises básicas.

### Exemplo Completo do Código

Aqui está o código completo para referência:

```python
import pandas as pd

# Dados de exemplo sobre a capacidade elétrica instalada no Brasil
dados_capacidade = {
    'Fonte': ['Hidrelétrica', 'Termelétrica', 'Eólica', 'Solar', 'Biomassa'],
    'Capacidade Instalada (MW)': [109000, 30000, 19000, 15000, 10000],
    'Porcentagem do Total (%)': [60, 15, 10, 8, 7]
}

# Criar DataFrame
df_capacidade = pd.DataFrame(dados_capacidade)

# Exibir a tabela
print("Capacidade Elétrica Instalada no Brasil:")
print(df_capacidade)

# Calcular a capacidade total instalada
capacidade_total = df_capacidade['Capacidade Instalada (MW)'].sum()
print(f"\nCapacidade Total Instalada: {capacidade_total} MW")

# Calcular a porcentagem de cada fonte em relação ao total
df_capacidade['Porcentagem do Total (%)'] = (df_capacidade['Capacidade Instalada (MW)'] / capacidade_total) * 100

# Exibir a tabela atualizada
print("\nCapacidade Elétrica Instalada com Porcentagens Atualizadas:")
print(df_capacidade)
```

### Conclusão

Esse é um exemplo básico de como você pode começar a analisar o potencial de produção de energia elétrica no Brasil usando Python e Pandas. Você pode expandir essa análise incluindo mais dados, gráficos e outras fontes de informação conforme necessário.