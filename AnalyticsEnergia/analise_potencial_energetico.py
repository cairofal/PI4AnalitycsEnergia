try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from datetime import datetime
    import warnings
    warnings.filterwarnings('ignore')
except ImportError as e:
    print("ERRO: Dependências não instaladas!")
    print(f"Biblioteca em falta: {e}")
    print("\nSolução:")
    print("1. Execute: pip install pandas numpy matplotlib seaborn openpyxl")
    print("2. Ou execute o arquivo: instalar_e_executar.py")
    input("Pressione Enter para sair...")
    exit(1)

class AnalisePotencialEnergetico:
    def __init__(self):
        self.dados_estados = None
        self.resultado_analise = None
        
    def criar_dados_simulados(self):
        """Cria dados simulados baseados em características reais dos estados brasileiros"""
        estados = [
            'SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'PE', 'CE', 'GO', 
            'PA', 'AM', 'MA', 'PB', 'ES', 'PI', 'AL', 'RN', 'MT', 'MS',
            'DF', 'SE', 'RO', 'TO', 'AC', 'RR', 'AP'
        ]
        
        # Dados simulados baseados em características reais
        np.random.seed(42)
        dados = {
            'Estado': estados,
            'Populacao_Milhoes': [45.9, 17.4, 21.4, 11.4, 11.5, 7.3, 14.9, 9.6, 9.2, 7.1,
                                 8.7, 4.2, 7.1, 4.0, 4.1, 3.3, 3.4, 3.5, 3.5, 2.8,
                                 3.1, 2.3, 1.8, 1.6, 0.9, 0.6, 0.9],
            'Capacidade_Atual_MW': [28000, 8500, 12000, 6200, 7800, 4200, 5800, 3200, 2800, 4500,
                                   9500, 2100, 1800, 1200, 2800, 850, 1400, 1600, 3200, 2100,
                                   900, 800, 1200, 950, 300, 150, 400],
            'PIB_Bilhoes_R': [2719, 759, 683, 471, 487, 295, 267, 190, 170, 224,
                             169, 102, 98, 63, 140, 59, 62, 69, 149, 121,
                             254, 42, 52, 36, 16, 13, 18],
            'Area_km2': [248219, 43777, 586521, 281730, 199307, 95737, 564732, 98076, 148886, 340242,
                        1247954, 1559146, 329642, 56469, 46074, 251616, 27843, 52809, 903202, 357145,
                        5760, 21925, 237765, 277466, 164124, 224298, 142470],
            'Consumo_Per_Capita_MWh': [4.2, 3.8, 3.1, 3.9, 4.1, 4.5, 2.1, 2.3, 2.0, 3.8,
                                      2.8, 2.2, 1.8, 2.1, 4.2, 1.9, 2.4, 2.2, 4.8, 4.1,
                                      5.2, 2.6, 3.1, 2.9, 2.1, 2.8, 2.4]
        }
        
        self.dados_estados = pd.DataFrame(dados)
        return self.dados_estados
    
    def calcular_indices_potencial(self):
        """Calcula índices para determinar potencial de expansão energética"""
        df = self.dados_estados.copy()
        
        # Densidade populacional
        df['Densidade_Pop'] = df['Populacao_Milhoes'] * 1000000 / df['Area_km2']
        
        # Demanda total estimada
        df['Demanda_Total_MW'] = df['Populacao_Milhoes'] * df['Consumo_Per_Capita_MWh'] * 1000 / 8760
        
        # Déficit/Superávit atual
        df['Deficit_MW'] = df['Demanda_Total_MW'] - df['Capacidade_Atual_MW']
        
        # Índice econômico (PIB per capita)
        df['PIB_Per_Capita'] = df['PIB_Bilhoes_R'] * 1000000000 / (df['Populacao_Milhoes'] * 1000000)
        
        # Potencial de crescimento econômico (baseado em PIB per capita normalizado)
        df['Potencial_Crescimento'] = (df['PIB_Per_Capita'] - df['PIB_Per_Capita'].min()) / (df['PIB_Per_Capita'].max() - df['PIB_Per_Capita'].min())
        
        # Fator demográfico (população + densidade)
        df['Fator_Demografico'] = (df['Populacao_Milhoes'] / df['Populacao_Milhoes'].max()) * 0.7 + (df['Densidade_Pop'] / df['Densidade_Pop'].max()) * 0.3
        
        # Score de potencial (combinando múltiplos fatores)
        df['Score_Potencial'] = (
            (df['Deficit_MW'] / df['Deficit_MW'].max() * 0.4) +  # 40% déficit atual
            (df['Potencial_Crescimento'] * 0.3) +                # 30% potencial econômico  
            (df['Fator_Demografico'] * 0.3)                      # 30% fator demográfico
        )
        
        # Normalizar score para 0-100
        df['Score_Potencial'] = ((df['Score_Potencial'] - df['Score_Potencial'].min()) / 
                                (df['Score_Potencial'].max() - df['Score_Potencial'].min())) * 100
        
        # Potencial de instalação recomendado (MW)
        df['Potencial_Instalacao_MW'] = df['Score_Potencial'] * 100  # Fator de escala
        
        self.resultado_analise = df
        return df
    
    def gerar_relatorio(self):
        """Gera relatório detalhado da análise"""
        if self.resultado_analise is None:
            print("Execute a análise primeiro!")
            return
            
        df = self.resultado_analise.sort_values('Score_Potencial', ascending=False)
        
        print("="*80)
        print("ANÁLISE DE POTENCIAL ENERGÉTICO POR ESTADO - BRASIL")
        print("="*80)
        print(f"Data da análise: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print()
        
        print("TOP 10 ESTADOS COM MAIOR POTENCIAL DE EXPANSÃO:")
        print("-"*60)
        
        top_10 = df.head(10)[['Estado', 'Score_Potencial', 'Potencial_Instalacao_MW', 
                             'Deficit_MW', 'Populacao_Milhoes', 'PIB_Per_Capita']]
        
        for idx, row in top_10.iterrows():
            print(f"{row['Estado']:2s} - Score: {row['Score_Potencial']:5.1f} | "
                  f"Potencial: {row['Potencial_Instalacao_MW']:6.0f} MW | "
                  f"Déficit: {row['Deficit_MW']:6.0f} MW | "
                  f"Pop: {row['Populacao_Milhoes']:4.1f}M | "
                  f"PIB/capita: R$ {row['PIB_Per_Capita']:,.0f}")
        
        print("\n" + "="*80)
        print("RESUMO GERAL:")
        print(f"• Total de déficit nacional: {df['Deficit_MW'].sum():,.0f} MW")
        print(f"• Potencial total de instalação: {df['Potencial_Instalacao_MW'].sum():,.0f} MW")
        print(f"• Estado com maior potencial: {df.iloc[0]['Estado']} ({df.iloc[0]['Score_Potencial']:.1f} pontos)")
        print(f"• Estado com menor déficit: {df.loc[df['Deficit_MW'].idxmin(), 'Estado']} ({df['Deficit_MW'].min():.0f} MW)")
        
    def criar_visualizacoes(self):
        """Cria gráficos para visualizar os resultados"""
        if self.resultado_analise is None:
            print("Execute a análise primeiro!")
            return
            
        df = self.resultado_analise.sort_values('Score_Potencial', ascending=False)
        
        # Configurar estilo
        plt.style.use('seaborn-v0_8')
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Gráfico 1: Top 10 Score de Potencial
        top_10 = df.head(10)
        ax1.barh(top_10['Estado'], top_10['Score_Potencial'], color='steelblue')
        ax1.set_xlabel('Score de Potencial')
        ax1.set_title('Top 10 Estados - Score de Potencial Energético')
        ax1.grid(axis='x', alpha=0.3)
        
        # Gráfico 2: Déficit vs Potencial de Instalação
        scatter = ax2.scatter(df['Deficit_MW'], df['Potencial_Instalacao_MW'], 
                             c=df['Score_Potencial'], cmap='viridis', alpha=0.7, s=60)
        ax2.set_xlabel('Déficit Atual (MW)')
        ax2.set_ylabel('Potencial de Instalação (MW)')
        ax2.set_title('Déficit vs Potencial de Instalação')
        plt.colorbar(scatter, ax=ax2, label='Score Potencial')
        
        # Gráfico 3: Relação PIB per capita vs Score
        ax3.scatter(df['PIB_Per_Capita'], df['Score_Potencial'], alpha=0.7, color='coral')
        ax3.set_xlabel('PIB per Capita (R$)')
        ax3.set_ylabel('Score de Potencial')
        ax3.set_title('PIB per Capita vs Score de Potencial')
        
        # Gráfico 4: População vs Capacidade Atual
        ax4.scatter(df['Populacao_Milhoes'], df['Capacidade_Atual_MW'], alpha=0.7, color='green')
        ax4.set_xlabel('População (Milhões)')
        ax4.set_ylabel('Capacidade Atual (MW)')
        ax4.set_title('População vs Capacidade Instalada')
        
        plt.tight_layout()
        plt.savefig('analise_potencial_energetico.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def salvar_resultados(self, arquivo='resultados_analise_energetica.xlsx'):
        """Salva os resultados em arquivo Excel"""
        if self.resultado_analise is None:
            print("Execute a análise primeiro!")
            return
            
        with pd.ExcelWriter(arquivo, engine='openpyxl') as writer:
            # Aba principal com todos os dados
            self.resultado_analise.sort_values('Score_Potencial', ascending=False).to_excel(
                writer, sheet_name='Análise Completa', index=False)
            
            # Aba com top 10
            self.resultado_analise.sort_values('Score_Potencial', ascending=False).head(10).to_excel(
                writer, sheet_name='Top 10 Potencial', index=False)
            
            # Aba com resumo estatístico
            resumo = self.resultado_analise.describe()
            resumo.to_excel(writer, sheet_name='Resumo Estatístico')
            
        print(f"Resultados salvos em: {arquivo}")

def main():
    """Função principal para executar a análise"""
    print("Iniciando Análise de Potencial Energético do Brasil...")
    
    # Criar instância da análise
    analise = AnalisePotencialEnergetico()
    
    # Executar etapas da análise
    print("1. Carregando dados dos estados...")
    analise.criar_dados_simulados()
    
    print("2. Calculando índices de potencial...")
    analise.calcular_indices_potencial()
    
    print("3. Gerando relatório...")
    analise.gerar_relatorio()
    
    print("\n4. Criando visualizações...")
    analise.criar_visualizacoes()
    
    print("5. Salvando resultados...")
    analise.salvar_resultados()
    
    print("\nAnálise concluída com sucesso!")

if __name__ == "__main__":
    main()
