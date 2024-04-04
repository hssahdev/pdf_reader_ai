from langchain_community.llms import Ollama
import config

llm_model = Ollama(model=config.LLM_MODEL)