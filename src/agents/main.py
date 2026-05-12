from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

# 1. Herramienta de ejemplo
@tool
def get_weather(city: str) -> str:
    """Consulta el clima de una ciudad."""
    return f"¡Siempre hace sol en {city}!"

# 2. Configuración con Llama 3.1 (Actualizado)
model = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0
)

# 3. Definición de herramientas
tools = [get_weather]

# 4. Creación del agente
agent = create_react_agent(model, tools)