# FlowMindz Modular Core 🚀🧠

Este repositório contém o núcleo modular da plataforma **FlowMindz**, com os seguintes módulos ativados:

- ✅ FlowOps (Inteligência Fiscal e Tributária)
- ✅ FlowGov (Radar Nacional de Licitações Públicas)
- ✅ Painel Vite com conexão à FlowMind

## 🚀 Como rodar localmente

```bash
git remote add origin https://github.com/Andrew183023/flowmindz-modular-core-final.git
cd flowmindz-modular-core
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🧠 Deploy com Docker

```bash
docker build -t flowmindz-core .
docker run -d -p 8000:8000 flowmindz-core
```

## 🌐 Deploy na Railway

Configure variáveis `.env` com sua URL de banco e chaves de API.

---

**Criado por:** Andrew Michael de Oliveira  
**Projeto:** Flow Core Group 🌎
