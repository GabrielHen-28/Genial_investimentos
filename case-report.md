## 1. Regulação Vs. Negócio

### Implicações Técnológicas
Caso o cliente ao receber o alerta, queira continuar com a compra. O código tem que primeiramente, gerar um arquivo em pdf do termo de ciência com base no risco do investimento e das implicações previstas e tem que ser possível de ser assinado digitalmente. Esse arquivo tem que identificado com uma hash e armazenado no banco de dados da Genial, tem que conter ID do cliente, data e hora da assinatura.

Outra implicação seria gerar um log de auditoria imutável para consulta e registro de todos os termos de ciência assinados, com carimbo de tempo e identificação do usuário que executou a ação.

### Implicações de compliance
O setor de Compliance tem que conseguir consultar os termos assinados de maneira automática, assim como relatórios que contenham g