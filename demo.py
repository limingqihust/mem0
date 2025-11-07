import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "ollama" # for embedder
os.environ["OPENAI_BASE_URL"]="http://localhost:11434"
os.environ["OLLAMA_BASE_URL"]="http://localhost:11434"
config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "qwen3:32b",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    },

    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest"        
        }
    },

    "vector_store": {
        "provider": "qdrant",
        "config": {
            "embedding_model_dims": 768        
        }
    }
}


m = Memory.from_config(config)

messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})