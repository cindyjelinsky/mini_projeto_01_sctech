import csv
import re
from datetime import datetime

#SPRINT 1 LEITURA CSV

def ler_csv(caminho_arquivo):

    with open(
        caminho_arquivo,
        mode="r",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        return list(leitor)


#SPRINT 2 LIMPEZA DE TEXTO

def tratar_categoria(nome_categoria):
 

 if not nome_categoria or nome_categoria.strip() == "":
    return "sem categoria"
 
 nome_categoria = nome_categoria.lower().strip()
 
 nome_categoria = nome_categoria.replace("_", " ")

 nome_categoria = re.sub(

 r"[^a-zA-ZÀ-ÿ0-9\s]",

 "",

 nome_categoria
)

 return nome_categoria

#SPRINT 3 LIMPEZA DE NULOS

#Optei pelo descarte dos registros com campos nulos, pois representavam fração muito pequena do dataset,
#Foram identificados apenas 8 campos nulos  em 2 produtos específicos.
#mantendo assim a qualidade e integridade dos dados para treinamento

def tratar_dim_produto(produto):
    
    dimensoes = [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]

    nulos_dim =0

    for dim in dimensoes:
       
        
        valor = produto.get(dim)

        if valor is None or (isinstance(valor, str) and valor.strip() == ""):
            nulos_dim += 1

    return nulos_dim



#SPRINT 4 REGRAS de NEGOCIO e DATAS

def analise_hipotese_entrega(pedido):
   
    data_entrega = pedido.get("order_delivered_customer_date")
    status = pedido.get("order_status")
    
    
    if data_entrega and data_entrega.strip() != "":
        return "entregue"
        
   
    else:
        return status
    



def formatar_data_br(string_data):
   
    if not string_data or string_data.strip() == "":
        return string_data
        
    try:
        
        data_objeto = datetime.strptime(string_data.strip(), "%Y-%m-%d %H:%M:%S")
        
        data_br = data_objeto.strftime("%d/%m/%Y")
        
        return data_br
        
    except ValueError:
        return string_data