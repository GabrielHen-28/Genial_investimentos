## 1. Regulação Vs. Negócio

### Implicações Técnológicas
Caso o cliente ao receber o alerta, queira continuar com a compra. O código tem que primeiramente, gerar um arquivo em pdf do termo de ciência com base no risco do investimento e das implicações previstas e tem que ser possível de ser assinado digitalmente. Esse arquivo tem que identificado com uma hash e armazenado no banco de dados da Genial, tem que conter ID do cliente, data e hora da assinatura.

Outra implicação seria gerar um log de auditoria imutável para consulta e registro de todos os termos de ciência assinados, com carimbo de tempo e identificação do usuário que executou a ação.

### Implicações de compliance
O setor de Compliance tem que conseguir consultar os termos assinados de maneira automática, assim como relatórios que contenham a quantidade de termos assinados, o percentual de ordens executadas sobre o risco de alerta e o perfil de clientes que assinam o termo mesmo que não tenham o perfil de investidor arriscado.

## 2. Desenquadramento passivo
O desenquadramento passivo acontece quando o risco do ativo aumenta com a volatilidade do mercado mesmo sem a participação do investidor, utilizando esse código seria muito fácil calcular quando o risco da carteira aumenta fazendo checagens periódicas, de semana em semana, desde que o risco dos ativos aumentasse automaticamente no banco de dados.

O Melhor canal de comunicação seria o próprio app da genial caso o investidor seja ativo nesse aplicativo, caso isso não seja verdade, canais de comunicação mais tradicionais como e-mail e um assessor para comunicar direto com o investidor se torna mais eficiente