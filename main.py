from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/status-rodada")
def status_rodada():
    return {
        "status_rodada": "mercado_aberto",
        "rodada": 1
    }

@app.get("/jogos")
def jogos():
    return {
        "jogos": [
            {
                "mandante": "Flamengo",
                "visitante": "Bahia",
                "favoravel_ataque": True,
                "favoravel_defesa": False
            }
        ]
    }

@app.get("/jogadores")
def jogadores():
    return {
        "jogadores": [
            {
                "nome": "Pedro",
                "time": "Flamengo",
                "posicao": "ATAQUE",
                "casa_fora": "Casa",
                "preco": 23.5,
                "status": "provavel",
                "motivo_simples": "Finaliza muito e joga em casa",
                "capitao_viavel": True,
                "plano_b": ["Gabigol"]
            }
        ]
    }
