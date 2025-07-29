from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
import openai
from utils.db_utils import get_connection

app = FastAPI()

class AnaliseInput(BaseModel):
    cnpj: str
    razao_social: str
    tipo_empresa: str
    regime_tributario: str
    resultado: dict

# 🧠 Gera o prompt de análise tributária
def gerar_prompt_analise(dados: AnaliseInput) -> str:
    return f"""
Você é um analista tributário com ampla experiência. Analise a seguinte empresa e gere:

1. Uma pontuação de 0 a 100 indicando o posicionamento tributário atual.
2. Um rótulo de "Risco", "Neutro" ou "Oportunidade".
3. Uma recomendação estratégica para melhorar a situação fiscal.

Dados da empresa:
- CNPJ: {dados.cnpj}
- Razão Social: {dados.razao_social}
- Tipo: {dados.tipo_empresa}
- Regime Tributário: {dados.regime_tributario}
- Resultado Fiscal: {json.dumps(dados.resultado)}
"""

# 🔗 Conecta à OpenAI e recebe a resposta estruturada
def avaliar_com_ia(prompt: str) -> str:
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um consultor tributário especialista."},
                {"role": "user", "content": prompt}
            ]
        )
        return resposta['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro ao consultar IA: {str(e)}"

# 🚀 Endpoint com score de IA
@app.post("/salvar_analise")
def salvar_analise(analise: AnaliseInput):
    try:
        print("[DEBUG] DATABASE_URL:", os.getenv("DATABASE_URL"))

        # Conexão com o banco
        conn = get_connection()
        cur = conn.cursor()

        # Inserir dados
        cur.execute("""
            INSERT INTO analises_tributarias (cnpj, razao_social, tipo_empresa, regime_tributario, resultado)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """, (
            analise.cnpj,
            analise.razao_social,
            analise.tipo_empresa,
            analise.regime_tributario,
            json.dumps(analise.resultado)
        ))

        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        # Avaliação com IA
        prompt = gerar_prompt_analise(analise)
        resultado_ia = avaliar_com_ia(prompt)

        return {
            "status": "sucesso",
            "id": new_id,
            "analise_ia": resultado_ia
        }

    except Exception as e:
        return {
            "status": "erro",
            "detalhe": str(e)
        }

@app.get("/")
def read_root():
    return {"FlowMind": "Operacional"}
