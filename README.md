# 📋 Rastreador de SLA de Chamado

Script em Python que lê chamados de um arquivo `.csv` e verifica automaticamente se cada um está no prazo, vence hoje ou já está vencido conforme o SLA definido.

## ⚙️ Funcionalidades

* Lê chamados com id, descrição, data de abertura e prazo em dias
* Calcula a data limite de cada chamado usando `timedelta`
* Classifica o status:
  * 🔴 Vencido — prazo já passou
  * 🟡 Vence hoje — último dia do SLA
  * 🟢 No prazo — ainda dentro do prazo

## 🚀 Como executar

```
git clone https://github.com/cah-menezes/rastreador-sla-python.git
cd rastreador-sla-python
python3 rastreador-sla.py
```