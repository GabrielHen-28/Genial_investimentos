import json

def calcula_risco_carteira(carteira_atual):
    soma_riscos= 0
    valor_investido = 0
    for acao in carteira_atual:
        soma_riscos = soma_riscos + (acao["valor_investido"]*acao["risco"])
        valor_investido += acao["valor_investido"]
    rc = soma_riscos/valor_investido
    return rc


def validacao_suitability(perfil, carteira_atual, nova_ordem):
    carteira_nova = carteira_atual.copy()
    
    ordem_atual = { "ativo": nova_ordem["ativo"], 
        "risco": nova_ordem["risco"],
        "valor_investido": nova_ordem["valor_ordem"]
    }

    carteira_nova.append(ordem_atual)
    rc = calcula_risco_carteira(carteira_nova)
    limite_alerta = perfil["score_max_risco"]*1.1
    limite_recusa = perfil["score_max_risco"]*1.4

    if rc <= limite_alerta:
        status = "Aprovado"
        mensagem = "Ordem executada. Carteira em conformidade."
    elif rc < limite_recusa and rc > limite_alerta:
        status = "Alerta"
        mensagem = f"Atenção: O risco da carteira ultrapassará o limite de {limite_alerta}. É necessário termo de ciência."
    elif rc >= limite_recusa:
        status = "Rejeitado"
        mensagem = "Risco excessivo. A operação viola a política de Suitability."

    return {
        "status": status,
        "risco_projetado": round(rc,2),
        "mensagem": mensagem
    }


perfil_cliente = {"perfil": "Moderado", "score_max_risco": 2.5}
carteira_atual = [
    {"ativo": "CDB XPTO", "risco": 1.2, "valor_investido": 50000},
    {"ativo": "Ação ABC", "risco": 4.0, "valor_investido": 10000}
]
nova_ordem_compra = {"ativo": "FII YYY", "risco": 3.5, "valor_ordem": 5000}

resultado = validacao_suitability(perfil_cliente, carteira_atual, nova_ordem_compra)
print(json.dumps(resultado, indent=2, ensure_ascii=False))

    