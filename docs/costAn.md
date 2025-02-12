# Analisi dei costi

# LLM

## OpenAi

Costi in USD.

### Costi di input:

Token per input query: 1500-2500

Costo token in input: 0.000015

Costo di una domanda: 0.0225-0.0375

### Costi di output:

Token per output query: 250+

Costo token in output:  0.00006

Costo di una risposta: 0.015+

### Conclusione

OpenAi ha un costo stimato di 0.04 (a salire) USD per domanda e risposta.

## Ollama

Ollama è un software FOSS, quindi non rappresenta un costo di per se.
Ollama però riciede un infrastruttura interna che può risultare costosa.
Segue una tablella con le specifiche necessarie a eseguire un [LLM](/docs/dictionary/llm.md) da 70B.

| **Component** | **Specification** | **Recommended Components** | **Estimated Cost** |
|---------------|-------------------|----------------------------|--------------------|
| **GPU**       | High VRAM capacity | multiple NVIDIA RTX 3090/4090 GPUs con NVLink | NVIDIA RTX 3090: $2000 (l'una) |
| **CPU**       | High-core count   | AMD Threadripper PRO 32-core, Intel Xeon W 32-core | AMD Threadripper PRO 32-core: $5,000 |
| **RAM**       | 256 GB | Corsair Vengeance LPX 256 GB (4 x 64 GB) DDR4-3200 | Corsair Vengeance LPX 256 GB DDR4-3200: $1,200 |
| **Storage**   | NVMe SSD, 8 TB | Samsung 970 Pro 8 TB NVMe SSD | Samsung 970 Pro 8 TB NVMe SSD: $1,500 |

# RAG

La rag è un processo meno intensivo e può essere eseguito con meno risorse in un server locale, considerando anche che deve contenere tutta la documentazione che si vuole che sia disponibile tramite il chatbot.



