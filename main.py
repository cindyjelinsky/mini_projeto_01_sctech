from funcoes import (
    ler_csv,
    )


def main():

    print("Iniciando ETL...\n")
    
    caminho_pedidos = "dataset/olist_orders_dataset.csv"
    caminho_produtos = "dataset/olist_products_dataset.csv"

    linhas_pedidos = 0 
    linhas_produtos = 0

    nulos_aprovacao = 0
    nulos_categoria = 0
    nulos_dimensoes = 0
    total_cancelados = 0

    total_nulos_corrigidos = 0
    hipotese_confirmada = True

    # ----PROCESSAMENTO DATASET PRODUTOS ----

    dados_pedidos = ler_csv(caminho_produtos)

    print(dados_pedidos[:10])

    


    


if __name__ == "__main__":
    main()