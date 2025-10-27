# Gradio Web UI for Ollama + LangChain

This project integrates Ollama (local LLM), LangChain (LCEL), and Gradio (web interface) to create an interactive AI application.

## 📋 Prerequisites

1. **Install Ollama**: Download from [https://ollama.ai/](https://ollama.ai/)
2. **Pull the Llama2 model**:
   ```bash
   ollama pull llama2
   ```
3. **Install Python dependencies**:
   ```bash
   pip install langchain-core langchain-community gradio
   ```

## 🚀 Running the Application

### Basic Script (Longchain.py)
```bash
python Longchain.py
```
This runs the basic example that asks "What is the capital of Germany?"

### Gradio Web UI (gradio_ui.py)
```bash
python gradio_ui.py
```
This launches a web interface at `http://127.0.0.1:7860`

## 🎨 Features

### Gradio UI Includes:
- ✅ Interactive input field for country names
- ✅ Example buttons for quick testing
- ✅ Clean, modern interface
- ✅ Real-time responses from Ollama
- ✅ Error handling

### How to Use:
1. Start Ollama (keep it running)
2. Run the Gradio script
3. Open your browser to `http://127.0.0.1:7860`
4. Enter a country name (e.g., "Germany", "France", "Japan")
5. Click "Find Capital" to get the answer

## 🔧 How It Works

### Architecture:
```
User Input → Gradio UI → ask_capital() → LangChain Chain → Ollama (llama2) → Response
```

### Components:

1. **Ollama**: Runs the LLM locally on your machine
2. **LangChain**: Manages the chain using LCEL (LangChain Expression Language)
3. **Gradio**: Provides the web interface

### LCEL Chain:
```python
chain = (
    {"topic": RunnablePassthrough()}  # Accept input
    | prompt                           # Format prompt
    | model                            # Call Ollama
    | StrOutputParser()                # Parse output
)
```

## 📸 Advanced Work

This project fulfills the "Advanced Work" requirement from Task 3 by:
- Integrating Ollama with LangChain
- Creating a Gradio Web UI for frontend interaction
- Demonstrating a complete AI Agent interface with translation from backend to frontend

## 🐛 Troubleshooting

### Issue: "Connection refused" error
**Solution**: Make sure Ollama is running. Start it with:
```bash
ollama serve
```

### Issue: "Model not found"
**Solution**: Pull the model first:
```bash
ollama pull llama2
```

### Issue: Port already in use
**Solution**: Change the port in `gradio_ui.py`:
```python
demo.launch(share=False, server_name="127.0.0.1", server_port=7861)
```

## 📚 Files

- `Longchain.py` - Basic Ollama + LangChain example
- `gradio_ui.py` - Gradio web interface
- `README_GRADIO.md` - This file

## 🎓 Educational Value

This project demonstrates:
1. Local LLM deployment with Ollama
2. Chain composition using LCEL
3. Frontend-backend integration with Gradio
4. End-to-end AI application development

## 📝 License

See LICENSE file for details.
