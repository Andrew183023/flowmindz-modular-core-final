# FlowMindz Modular Core 🚀🧠

Este repositório contém o núcleo modular da plataforma **FlowMindz**, com os seguintes módulos ativados:

- ✅ FlowOps (Inteligência Fiscal e Tributária)  
- ✅ FlowGov (Radar Nacional de Licitações Públicas)  
- ✅ Painel Vite com conexão à FlowMind  

---

## 🚀 Como rodar localmente

```bash
git clone https://github.com/Andrew183023/flowmindz-modular-core-final.git
cd flowmindz-modular-core-final
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn main:app --reload

