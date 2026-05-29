import csv



def ler_csv(caminho_arquivo):

    with open(
        caminho_arquivo,
        mode="r",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        return list(leitor)


