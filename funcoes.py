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
    
    
    if not data_entrega and data_entrega.strip() == "":
        return status
        
   
    return "entregue"
    
def valida_hipotese(total_cancelados,total_outros_status):
    if total_cancelados < total_outros_status:
        return "Hipótese Invalidada"
    
    return "Hipótese Validada"


def formatar_data_br(string_data):
   
    if not string_data or string_data.strip() == "":
        return string_data
        
    try:
        
        data_objeto = datetime.strptime(string_data.strip(), "%Y-%m-%d %H:%M:%S")
        
        data_br = data_objeto.strftime("%d/%m/%Y")
        
        return data_br
        
    except ValueError:
        return string_data
    

def exportar_relatorio_txt(
    caminho_saida,
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
):
    
    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("====== RELATÓRIO FINAL ======\n")
        arquivo.write(f"Total de linhas processadas: {linhas_pedidos+linhas_produtos}\n")
        arquivo.write(f"Total de Registros Nulos Corrigidos: {total_nulos}\n")
        arquivo.write(f"  |__ Nulos por Categoria (Tratados): {nulos_categoria}\n")
        arquivo.write(f"  |__ Campos Nulos por Dimensão (Detectados): {nulos_dimensoes}\n")
        arquivo.write(f"Total de Linhas descartadas: {produtos_descartados}\n\n")
        
        arquivo.write("------ Validação Hipótese ------\n")
        arquivo.write(f"Total de pedidos sem data de entrega CANCELADOS: {total_cancelados}\n")
        arquivo.write(f"Total de pedidos sem data de entrega OUTROS STATUS: {total_outros_status}\n")
        arquivo.write(f"  |__ Em Trânsito (shipped): {nulos_em_transito}\n")
        arquivo.write(f"  |__ Processando (processing): {nulos_processando}\n")
        arquivo.write(f"  |__ Outros Status: {nulos_outros}\n\n")
        arquivo.write(valida_hipotese(total_cancelados,total_outros_status))
        