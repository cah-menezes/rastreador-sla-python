"""Lê chamados de um CSV e verifica se estão no prazo ou vencidos conforme o SLA definido."""

from datetime import datetime, timedelta

CHAMADOS_CSV = "chamados.csv"

#Funções
def ler_chamados(chamados):
    chamados_abertos = []
    with open (chamados, "r", encoding="utf-8") as arquivo:
        next(arquivo)
        for linha in arquivo:
            separacao = linha.strip().split(";")
            chamados_abertos.append({
                "id": separacao[0],
                "descricao": separacao[1],
                "data_abertura": separacao[2],
                "prazo_dias": separacao[3]})
    return chamados_abertos

def verificar_sla(status):
    for coluna in status:
        abertura = datetime.strptime(coluna["data_abertura"], "%d/%m/%Y")
        limite = abertura + timedelta(days=int(coluna["prazo_dias"]))
        hoje = datetime.now()

        if hoje.date() > limite.date():
            print(f"{coluna['id']} - {coluna['descricao']}: 🔴 Vencido!")
        elif hoje.date() == limite.date():
            print(f"{coluna['id']} - {coluna['descricao']}: 🟡 Vence hoje!")
        else:
            print(f"{coluna['id']} - {coluna['descricao']}: 🟢 No prazo!")

#Programa Principal
if __name__ == "__main__":
    chamados = ler_chamados(CHAMADOS_CSV)
    verificar_sla(chamados)
    pass

