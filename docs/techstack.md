# Tech Stack del progetto

Per la definizione di Tech Stack, vedi [Tech-Stack](/docs/dictionary/techstack.md).

Il tech stack ideato per questo progetto è il seguente

```mermaid
graph TD
A[Sito]

    subgraph Server_Locale["Server Locale"]
        subgraph Docker["Docker"]
            B[Manager Python]
            C[RAG]
        end
        D[Docs]
    end

    subgraph API_o_Server_Locale["API o Server Locale"]
        subgraph Servizio_o_Ollama["Servizio o Ollama"]
            C2[LLM]
        end
    end

    A -- 1 --> B
    B -- 7 --> A
    B -- 2 --> C
    C -- 4 --> B
    B -- 5 --> C2
    C2 -- 6 --> B
    C <-- 3 --> D

    %% Miglioramento dei colori e contrasto
    style Server_Locale fill:#2C3E50,stroke:#E74C3C,stroke-width:3px,color:#ECF0F1
    style API_o_Server_Locale fill:#8E44AD,stroke:#9B59B6,stroke-width:3px,color:#ECF0F1
    style Servizio_o_Ollama fill:#EEEEEE,stroke:#bbbbbb,stroke-width:3px,color:#222222
    style Docker fill:#339cff,stroke:#247aca,stroke-width:3px,color:#ECF0F1
    style A fill:#F39C12,stroke:#E67E22,stroke-width:3px,color:#ECF0F1
    style B fill:#E74C3C,stroke:#C0392B,stroke-width:3px,color:#ECF0F1
    style D fill:#95A5A6,stroke:#7F8C8D,stroke-width:3px,color:#ECF0F1
```
1. L'utente utilizza il sito per porre una domanda che viene passata al Manager Python.
2. Il Manager interroga la [RAG](/docs/dictionary/rag.md).
3. La [RAG](/docs/dictionary/rag.md) ricerca nella documentazione il contenuto relativo alla domanda.
4. La [RAG](/docs/dictionary/rag.md) restituisce al Manager la documentazione rilevante.
5. Il manager passa la domanda originale e la documentazione rilevante al [LLM](/docs/dictionary/llm.md).
6. La [LLM](/docs/dictionary/llm.md) genera la risposta e la restituisce al Manager.
7. Il Manager restituisce la risposta all'utente.

L'[LLM](/docs/dictionary/llm.md) in questione potrebbe essere ospitata su un server locale o utilizzata tramite [API](/docs/dictionary/api.md).
Per ulteriori informazioni, vedi [Valutazione LLM](/docs/llmval.md)

---
[Home](/indice.md) [Dizionario](/docs/dictionary/indice.md)