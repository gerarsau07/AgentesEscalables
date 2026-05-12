# AgenteProduccion 

Este es un proyecto base profesional para el desarrollo de agentes inteligentes utilizando **LangGraph** y la gestión de paquetes de **uv**. El sistema está diseñado con una arquitectura de código limpio (carpeta `src/`) y utiliza **Groq** como motor de inferencia gratuito para una ejecución ultra rápida.

## Estructura del Proyecto

```text
AGENTEPRODUCCION/
├── notebooks/           # Experimentación y visualización del grafo
│   └── notebook.ipynb
├── src/
│   ├── agents/          # Lógica del agente (Grafos)
│   │   ├── __init__.py
│   │   └── main.py      # Definición del agente y herramientas
│   ├── api/             # Configuración y entorno
│   │   └── .env         # API Keys (No subir a Git)
│   └── __init__.py
├── langgraph.json       # Configuración para LangGraph Studio
├── pyproject.toml       # Dependencias y empaquetado
└── uv.lock              # Bloqueo de versiones
```

## Requisitos de instalacion



uv init 
uv venv


uv add --pre langgraph langchain langchain-openai
uv add langchain-groq
uv add "langgraph-cli[inmem]" -- dev


uv run langgraph dev


uv add ipykernel --dev


uv pip install -e .


```toml
[tool.setuptools.packages.find]
where = ["src"]
include = ["*"]
```