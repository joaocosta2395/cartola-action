from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/rodada")
def rodada():
    return {
        "status_rodada": "mercado_aberto",
        "rodada": 1
    }

@app.get("/dados")
def dados():
    return {
        "jogos": [
            {
                "mandante": "Flamengo",
                "visitante": "Bahia",
                "favoravel_ataque": True,
                "favoravel_defesa": False
            }
        ],
        "jogadores": [
            {
                "nome": "Pedro",
                "time": "Flamengo",
                "posicao": "ATAQUE",
                "casa_fora": "Casa",
                "preco": 23.5,
                "motivo": "Finaliza muito e joga em casa",
                "capitao": True
            }
        ]
    }
