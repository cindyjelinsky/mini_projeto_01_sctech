from funcoes import (
    ler_csv,
    tratar_categoria,
    tratar_dim_produto,
    analise_hipotese_entrega,
    formatar_data_br
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
    teste_nulas = 0
    total_nulos_corrigidos = 0

    nulos_em_transito = 0
    nulos_processando = 0
    nulos_outros = 0
   

    # ----PROCESSAMENTO DATASET PRODUTOS ----

    dados_produtos = ler_csv(caminho_produtos)

    linhas_produtos = len(dados_produtos)

    
    #print(dados_produtos[:10])

    print("======TRATANDO DATASET PRODUTOS======")

    for produto in dados_produtos:
       
     

     categoria_original = produto.get("product_category_name")
     categoria_limpa =  tratar_categoria(categoria_original)

     produto["product_category_name"] = categoria_limpa

     if categoria_limpa == "sem categoria":
        nulos_categoria +=1
        
   
     qnt_dimendoes_corrigidas = tratar_dim_produto(produto)
     nulos_dimensoes += qnt_dimendoes_corrigidas
    

    # ----PROCESSAMENTO DATASET PEDIDOS ----

    dados_ordens = ler_csv(caminho_pedidos)
    linhas_pedidos = len(dados_ordens)

    print("======TRATANDO DATASET PEDIDOS======")

    for pedido in dados_ordens:
        
       
        resultado = analise_hipotese_entrega(pedido)
        
        
        if resultado == "entregue":
            pass 
            
        elif resultado == "canceled":
           total_cancelados += 1
            
        elif resultado == "shipped":
           
            nulos_em_transito += 1  

        elif resultado == "processing" or resultado == "approved":
            
            nulos_processando += 1  
            
        else:
            nulos_outros += 1

        data_original = pedido.get("order_approved_at")
        pedido["order_approved_at"] = formatar_data_br(data_original)
    

    
    
   
if __name__ == "__main__":
    main()