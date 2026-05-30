from funcoes import (
    ler_csv,
    tratar_categoria,
    tratar_dim_produto,
    analise_hipotese_entrega,
    formatar_data_br,
    exportar_relatorio_txt,
    valida_hipotese
    )


def main():

    print("Iniciando ETL...\n")
    
    caminho_pedidos = "dataset/olist_orders_dataset.csv"
    caminho_produtos = "dataset/olist_products_dataset.csv"

    linhas_pedidos = 0 
    linhas_produtos = 0

    
    nulos_categoria = 0
    nulos_dimensoes = 0
    produtos_descartados = 0

    total_cancelados = 0
   
    nulos_em_transito = 0
    nulos_processando = 0
    nulos_outros = 0
    
    produtos_validos =[]

    # ----PROCESSAMENTO DATASET PRODUTOS ----

    dados_produtos = ler_csv(caminho_produtos)

    linhas_produtos = len(dados_produtos)

    
    #print(dados_produtos[:10])

    print("TRATANDO DATASET PRODUTOS...")

    for produto in dados_produtos:
          
        
     nulos_dim_encontrados = tratar_dim_produto(produto)

     if nulos_dim_encontrados > 0:
        nulos_dimensoes += nulos_dim_encontrados
        produtos_descartados += 1
        continue 
     

     categoria_original = produto.get("product_category_name")
     categoria_limpa =  tratar_categoria(categoria_original)

     produto["product_category_name"] = categoria_limpa

     if categoria_limpa == "sem categoria":
        nulos_categoria +=1

         
     produtos_validos.append(produto)
    
    dados_produtos= produtos_validos
    
    
    # ----PROCESSAMENTO DATASET PEDIDOS ----

    dados_ordens = ler_csv(caminho_pedidos)
    linhas_pedidos = len(dados_ordens)

    print("TRATANDO DATASET PEDIDOS...")
    
    for pedido in dados_ordens:
        
       
        resultado_status = analise_hipotese_entrega(pedido)

        if resultado_status == "canceled":
            total_cancelados += 1
        elif resultado_status == "shipped":
            nulos_em_transito += 1
        elif resultado_status == "processing":
            nulos_processando += 1
        elif resultado_status != "entregue":
            nulos_outros += 1

        data_original = pedido.get("order_approved_at")
        pedido["order_approved_at"] = formatar_data_br(data_original)

    
    # RELATORIO


    total_nulos = nulos_categoria + nulos_dimensoes
    total_outros_status = nulos_em_transito + nulos_processando + nulos_outros
    
    
    print("\n======RELATÓRIO FINAL======")  
    
    print("Total de linhas processadas: ", linhas_pedidos + linhas_produtos)
    print("Total de Registros Nulos Corrigidos: ", total_nulos )
    print("Total de Linhas descartadas: ", produtos_descartados)
   
    
    print("\n------Validação Hipótese------")
    print("Total de pedidos sem data de entrega CANCELADOS: ",total_cancelados)
    print("Total de pedidos sem data de entrega OUTROS STATUS: ", total_outros_status )
    print(valida_hipotese(total_cancelados,total_outros_status))


    exportar_relatorio_txt(
        "relatorio.txt",
        linhas_produtos,
        linhas_pedidos,
        nulos_categoria,
        nulos_dimensoes,
        produtos_descartados,
        total_cancelados,
        nulos_em_transito,
        nulos_processando,
        nulos_outros,
        total_nulos,
        total_outros_status

    )
    
    print("\nRelatório detalhado exportado para 'relatorio.txt'")
    
   
if __name__ == "__main__":
    main()