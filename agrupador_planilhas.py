import pandas as pd
import time
import argparse

def main():
    # Configurar argumentos de linha de comando
    parser = argparse.ArgumentParser(
        description='Agrega dados municipais por código geográfico (Geocod)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  python3 agrupador_planilhas.py -i dados.csv -o resultado.csv
  python3 agrupador_planilhas.py -i dados.csv -o resultado.csv -s "," -d "."
  python3 agrupador_planilhas.py --input dados.csv --output resultado.csv --separator ";" --decimal ","
        '''
    )
    
    parser.add_argument(
        '-i', '--input',
        default='dados.csv',
        help='Caminho do arquivo CSV de entrada (padrão: dados_entrada_convertidos.csv)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='resultado.csv',
        help='Caminho do arquivo CSV de saída (padrão: resultado_final_dados_agrupados.csv)'
    )
    
    parser.add_argument(
        '-s', '--separator',
        default=';',
        help='Separador de colunas do arquivo de saída (padrão: ";")'
    )
    
    parser.add_argument(
        '-e', '--encoding',
        default='utf-8',
        help='Codificação do arquivo de saída (padrão: utf-8)'
    )
    
    parser.add_argument(
        '-d', '--decimal',
        default=',',
        help='Separador decimal do arquivo de saída (padrão: ",")'
    )
    
    args = parser.parse_args()
    
    # Atribuir valores dos argumentos
    INPUT_CSV_FILE_PATH = args.input
    OUTPUT_CSV_FILE_PATH = args.output
    OUTPUT_SEPARATOR_CSV = args.separator
    OUTPUT_ENCODING = args.encoding
    OUTPUT_DECIMAL_SEPARATOR = args.decimal
    
    print(f"\n{'='*60}")
    print("CONFIGURAÇÕES")
    print(f"{'='*60}")
    print(f"Arquivo de entrada:    {INPUT_CSV_FILE_PATH}")
    print(f"Arquivo de saída:      {OUTPUT_CSV_FILE_PATH}")
    print(f"Separador CSV:         '{OUTPUT_SEPARATOR_CSV}'")
    print(f"Encoding:              {OUTPUT_ENCODING}")
    print(f"Separador decimal:     '{OUTPUT_DECIMAL_SEPARATOR}'")
    print(f"{'='*60}\n")

    # Ler a planilha de dados
    print(f"Lendo arquivo '{INPUT_CSV_FILE_PATH}'...")
    df_municipio = pd.read_csv(INPUT_CSV_FILE_PATH)
    
    # Converter colunas para numeric, coercendo erros para NaN
    colunas_numericas = ['V012', 'V013', 'V014', 'V015']
    for col in colunas_numericas:
        df_municipio[col] = pd.to_numeric(df_municipio[col], errors='coerce')
        
    # Células a substituir (contar os Nan)
    total_nans = df_municipio[colunas_numericas].isna().sum().sum()
    print(f"\nTotal de valores NaN nas colunas {colunas_numericas}: {total_nans}")
    


    # Substituir valores que contêm NaN em qualquer uma das colunas numéricas por ZERO
    df_municipio.fillna(0, inplace=True)

    

    # Agrupar por Geocod e somar as colunas V012, V013, V014, V015
    print("\n\nAgrupando dados por Geocod e somando os valores...")
    df_agrupado = df_municipio.groupby('Geocod', as_index=False)[colunas_numericas].sum()

    # Converter para int ou float dependendo se há casas decimais
    for col in colunas_numericas:
        # Verifica se todos os valores são inteiros (sem casas decimais)
        if (df_agrupado[col] % 1 == 0).all():
            df_agrupado[col] = df_agrupado[col].astype(int)
            print(f"Coluna {col} convertida para int")
        else:
            df_agrupado[col] = df_agrupado[col].astype(float)
            print(f"Coluna {col} mantida como float (possui casas decimais)")
    
    print("\nDados agrupados (primeiras 15 linhas):")
    print(df_agrupado.head(15))
    
    # Salvar o resultado em um novo arquivo CSV
    print(f"\n\nSalvando dados agrupados em '{OUTPUT_CSV_FILE_PATH}'...")
    df_agrupado.to_csv(OUTPUT_CSV_FILE_PATH, index=False, sep=OUTPUT_SEPARATOR_CSV, encoding=OUTPUT_ENCODING, decimal=OUTPUT_DECIMAL_SEPARATOR)

    
    print(f"Arquivo '{OUTPUT_CSV_FILE_PATH}' gerado com sucesso!")
    print(f"Total de municípios únicos: {len(df_agrupado)}")

if __name__ == "__main__":
    
    start_time = time.time()
    print("Iniciando o processamento às :", time.strftime("%H:%M:%S", time.localtime(start_time)))
    main()
    end_time = time.time()
    print(f"Tempo de execução: {end_time - start_time:.2f} segundos")
    print("Processamento finalizado às :", time.strftime("%H:%M:%S", time.localtime(end_time)))