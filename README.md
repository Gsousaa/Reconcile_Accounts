# Reconcile_Accounts

Realizar a conciliação (ou batimento) entre dois grupos de transações financeiras.

A função reconcile_accounts recebe duas listas (representando as linhas dos dados financeiros) e irá devolver cópias dessas duas listas com uma nova coluna acrescente à direitas das demais, que designará se a transação pode ser encontrada (FOUND) na outra lista ou não (MISSING).

As listas de listas representarão os dados em quatro colunas:
- Data
- Departamento
- Valor
- Beneficiário
