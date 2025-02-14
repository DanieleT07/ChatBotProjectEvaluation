# Implementazione

## Lista dei software inclusi

> [!CAUTION]
> Tutto il codice è stato provato su linux (`Debian GNU/Linux 12 (bookworm) x86_64`).
> `localrag.py/localragApi.py` è stato testato anche su windows (`Windows 11 pro`).

### Not so Easy Local RAG
- **Path:**  
  ```bash
  cd /implementation/not-so-easy-local-rag
  ```
- **Istruzioni:**
  - Creare un ambiente virtuale:
    ```bash
    python3 -m venv venv
    ```
  - Attivare l'ambiente virtuale:
    ```bash
    source venv/bin/activate
    ```
  - Installare le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```
  - Installare **Ollama**, **llama** e **mxbai-embed-large** (vedi istruzioni su [ollama.com](https://ollama.com/))
  - Eseguire LocalRAG (versione terminale) o LocalRAG API (versione server API):
    ```bash
    python3 localrag.py  # oppure localragApi.py
    ```
- **Configurazioni:**  
  Modifica `config.yaml` per le impostazioni.

---

### Sito
- **Path:**  
  ```bash
  cd /implementation/site
  ```
- **Descrizione:**  
  Prototipo di sito per dimostrare l'API.

---

### Benchmark
- **Path:**  
  ```bash
  cd /implementation/not-so-easy-local-rag/benchmark
  ```
- **Istruzioni:**
  - Attivare l'opzione benchmark in `config.yaml`
  - Inserire le domande in `benchmark.yaml`
  - Usare `check.py` per controllare i risultati (sempre con l'ambiente virtuale attivo)
  - Eseguire `check.py` più volte in modalità `-c`, salvare i file con nomi diversi, quindi usare l'opzione `cmp` per comparare le risposte.

---

### Refactor
- **Path:**  
  ```bash
  cd /implementation/tools
  ```
- **Istruzioni:**  
  - Eseguire:
    ```bash
    python3 refactor.py <file>
    ```
  - Questo migliora la formattazione dei dati per la suddivisione in chunk per la RAG (ogni riga rappresenta un chunk).

---

### Viz Suite
- **Descrizione:**  
  Contiene tre script Python grezzi per visualizzare la distanza vettoriale in vari modi e un progetto in C più raffinato basato su **RayLib**.
- **Compilazione:**  
  ```bash
  cd /implementation/tools/viz/CosDistSim
  make
  ```
  Non è un progetto avanzato, ma mostra bene la distanza vettoriale.