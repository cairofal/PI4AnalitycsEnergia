import subprocess
import sys
import os

def instalar_dependencias():
    """Instala as dependências necessárias"""
    print("Instalando dependências necessárias...")
    
    dependencias = [
        'pandas',
        'numpy', 
        'matplotlib',
        'seaborn',
        'openpyxl'
    ]
    
    for pacote in dependencias:
        print(f"Instalando {pacote}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', pacote])
            print(f"✓ {pacote} instalado com sucesso!")
        except subprocess.CalledProcessError:
            print(f"✗ Erro ao instalar {pacote}")
            return False
    
    print("\n" + "="*50)
    print("Todas as dependências foram instaladas!")
    print("="*50 + "\n")
    return True

def executar_analise():
    """Executa o script de análise"""
    print("Executando análise de potencial energético...\n")
    
    try:
        # Importar e executar o script principal
        from analise_potencial_energetico import main
        main()
    except ImportError as e:
        print(f"Erro ao importar: {e}")
        return False
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return False
    
    return True

def main():
    """Função principal"""
    print("INSTALADOR E EXECUTOR - ANÁLISE ENERGÉTICA BRASIL")
    print("="*60)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('analise_potencial_energetico.py'):
        print("ERRO: Arquivo 'analise_potencial_energetico.py' não encontrado!")
        print("Certifique-se de estar no diretório correto.")
        input("Pressione Enter para sair...")
        return
    
    # Instalar dependências
    if not instalar_dependencias():
        print("Falha na instalação das dependências!")
        input("Pressione Enter para sair...")
        return
    
    # Executar análise
    if executar_analise():
        print("\n" + "="*60)
        print("ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("="*60)
        print("Arquivos gerados:")
        print("• analise_potencial_energetico.png (gráficos)")
        print("• resultados_analise_energetica.xlsx (dados)")
    else:
        print("Erro durante a execução da análise!")
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()
