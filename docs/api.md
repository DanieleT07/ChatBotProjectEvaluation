# Documentazione API Document Chat

Questa API consente di interagire con un sistema di chat basato su documenti che utilizza embeddings per fornire un contesto rilevante dai documenti quando risponde alle domande.

## URL Base

```
http://localhost:8000
```

## Endpoint

### Chat

Invia un messaggio e ricevi una risposta con il contesto rilevante dai documenti.

```
POST /chat
```

#### Corpo della richiesta

| Campo         | Tipo    | Obbligatorio | Descrizione                                           |
|--------------|---------|--------------|-------------------------------------------------------|
| message      | string  | Sì           | Il messaggio o la domanda dell'utente                |
| clear_history| boolean | No           | Se true, cancella la cronologia della conversazione (default: false) |

>[!WARNING]
Attualmente clear_history non è supportato, la history viene cancellata ad ogni query.

Esempio di richiesta:
```json
{
    "message": "Quali sono le caratteristiche principali del prodotto?",
    "clear_history": false
}
```

#### Risposta

| Campo    | Tipo     | Descrizione                                        |
|----------|---------|----------------------------------------------------|
| response | string  | La risposta dell'AI al messaggio dell'utente       |
| context  | string[] | Array di estratti di documenti rilevanti per il contesto |

Esempio di risposta:
```json
{
    "response": "In base alla documentazione, le caratteristiche principali includono...",
    "context": [
        "Caratteristica 1: Analisi avanzata con elaborazione in tempo reale",
        "Caratteristica 2: Misure di sicurezza integrate con crittografia"
    ]
}
```

#### Codici di stato

- `200`: Risposta avvenuta con successo
- `500`: Errore del server (dettagli inclusi nella risposta)

### Salvataggio dello stato

Salva lo stato attuale degli embeddings e del vault.

```
POST /save
```

#### Risposta

| Campo   | Tipo   | Descrizione                          |
|---------|--------|--------------------------------------|
| message | string | Conferma del salvataggio avvenuto con successo |

Esempio di risposta:
```json
{
    "message": "Stato salvato con successo"
}
```

#### Codici di stato

- `200`: Stato salvato con successo
- `500`: Errore durante il salvataggio dello stato (dettagli inclusi nella risposta)

## Esempi di utilizzo

### cURL

```bash
# Invia un messaggio in chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quali sono le caratteristiche principali?", "clear_history": false}'

# Cancella la cronologia della chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "", "clear_history": true}'

# Salva lo stato attuale
curl -X POST http://localhost:8000/save
```

### Python

```python
import requests

API_URL = "http://localhost:8000"

# Invia un messaggio in chat
response = requests.post(
    f"{API_URL}/chat",
    json={
        "message": "Quali sono le caratteristiche principali?",
        "clear_history": False
    }
)
data = response.json()
print("Risposta:", data["response"])
print("Contesto:", data["context"])

# Cancella la cronologia della chat
requests.post(
    f"{API_URL}/chat",
    json={
        "message": "",
        "clear_history": True
    }
)

# Salva lo stato
requests.post(f"{API_URL}/save")
```

### JavaScript

```javascript
// Invia un messaggio in chat
const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: "Quali sono le caratteristiche principali?",
        clear_history: false
    })
});
const data = await response.json();
console.log("Risposta:", data.response);
console.log("Contesto:", data.context);

// Cancella la cronologia della chat
await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: "",
        clear_history: true
    })
});

// Salva lo stato
await fetch('http://localhost:8000/save', {
    method: 'POST'
});
```

## Gestione degli errori

L'API restituisce errori nel seguente formato:

```json
{
    "detail": "Messaggio di errore che descrive il problema"
}
```
---
[Home](/indice.md) [Dizionario](/docs/dictionary/indice.md)