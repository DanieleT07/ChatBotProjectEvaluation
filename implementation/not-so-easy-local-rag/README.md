# Not so Easy Local RAG

A Python implementation of Retrieval-Augmented Generation (RAG) that runs completely locally using Ollama for embeddings and text generation. Perfect for creating chatbots that can answer questions about your documentation while maintaining privacy and control.

This project takes some inspiration (and code) from https://github.com/AllAboutAI-YT/easy-local-rag and is under MIT License.

## Features

- **Fully Local Operation**: Uses Ollama for both embeddings and text generation
- **Document Context Retrieval**: Intelligently fetches relevant context from your documents
- **Flexible Configuration**: Easy to customize via YAML configuration
- **Benchmarking System**: Test and evaluate responses
- **Efficient Caching**: Saves embeddings to avoid regeneration
- **Error Code Support**: Special handling for error codes in format Axxx or Axxx/yyy

## Prerequisites

- Python 3.x
- Ollama running locally
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
At this moment the repository is not acessible standlone because it is part of the BoatoPack ChatBotProjectEvaluation.

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Ollama:
   - Ensure Ollama is running locally on port 11434
   - Have the required models available:
     - llama3.1 (or your preferred model for generation)
     - mxbai-embed-large (for embeddings)

## Configuration

The system is configured via `config.yaml`. Default configuration:

```yaml
ollama_api_base_url: "http://localhost:11434/v1"
ollama_api_key: "llama3.1"
vault_file: "vault/vault.txt"
vault_old_file: "vault/old/vault_old.txt"
embeddings_file: "embeddings/embeddings.json"
ollama_model: "llama3.1"
ollama_model_emebeding: "mxbai-embed-large"
top_k: 7
benchmark: False
benchmark_response: "benchmark/response.txt"
history: False
benchmark_path: "benchmark/benchmark.yaml"
```

## Usage

### Interactive Mode

Run the application:
```bash
python localrag.py
```

Ask questions about your documents when prompted. The system will:
1. Find relevant context from your documents
2. Generate a response using the provided context
3. Format the response with proper references

### Benchmark Mode

1. Set `benchmark: True` in config.yaml
2. Prepare test cases in benchmark/benchmark.yaml
3. Run the application to process all test cases
4. Review results in benchmark/response.txt

## Response Format

Responses are formatted in Markdown:
```markdown
# [Answer Title]
## References:
- [Chapter Number/Error Code]
- [Chapter Number/Error Code]
[Answer Content]
```

## License

See [LICENSE file in the repository](LICENSE).