# Docker

[*Wikipedia*](https://en.wikipedia.org/wiki/Docker_(software))

Docker è una piattaforma per creare, distribuire e gestire applicazioni in **container**, che sono ambienti isolati e portabili. Ogni container include tutto ciò che serve per eseguire un'applicazione: codice, runtime, librerie e dipendenze.  

#### **Vantaggi di Docker:**  
- **Portabilità:** Funziona su qualsiasi sistema con Docker installato.  
- **Isolamento:** Ogni container ha le sue dipendenze, evitando conflitti.  
- **Efficienza:** Usa meno risorse rispetto alle VM, condividendo il kernel del sistema operativo.  

### **Docker Compose**  
Docker Compose è uno strumento per definire e gestire **applicazioni multi-container** con un singolo file `docker-compose.yml`.  

#### **Esempio di file `docker-compose.yml` per un'app con un database:**  
```yaml
version: "3.8"
services:
  app:
    image: myapp
    ports:
      - "8080:80"
    depends_on:
      - db

  db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: example
```

Il seguente schema spiega la differenza tra l'esecuzione di software su Bare Metal (Direttamente su un device con OS installato), su un sistema di VM (macchine virtuali) e su un Docker (container).

#### Bare Metal
```mermaid
graph TD
    A[Hardware] -->|OS| B[Host OS]
    B -->|App 1| C[Application 1]
    B -->|App 2| D[Application 2]
    B -->|App 3| E[Application 3]
```

#### VM
```mermaid
graph TD
    A[Hardware] -->|OS| B[Host OS]
    B -->|Hypervisor| C[Hypervisor]
    C -->|VM 1| D[Guest OS 1]
    D -->|App| E[Application]
    C -->|VM 2| F[Guest OS 2]
    F -->|App| G[Application]
    C -->|VM 3| H[Guest OS 3]
    H -->|App| I[Application]
```

#### Docker
```mermaid
graph TD
    A[Hardware] -->|OS| B[Host OS]
    B -->|Docker| C[Docker Engine]
    C -->|Container 1| D[App 1 + Libs]
    C -->|Container 2| E[App 2 + Libs]
    C -->|Container 3| F[App 3 + Libs]
```

---
[Home](/indice.md) [Dizionario](/docs/dictionary/indice.md)