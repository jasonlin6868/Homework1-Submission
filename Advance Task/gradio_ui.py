import gradio as gr
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama

# Initialize the model (only once when the script starts)
model = ChatOllama(model="llama2")

# Define the prompt template
prompt = PromptTemplate.from_template(
    "What is the capital of {topic}?"
)

# Create the chain
chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def ask_capital(topic):
    """Function to get the capital of a given topic"""
    try:
        result = chain.invoke(topic)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
def create_interface():
    with gr.Blocks(title="Ollama + LangChain Capital Finder", theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🌍 Capital City Finder
            ### Powered by Ollama + LangChain
            
            Enter a country name to find its capital city!
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                topic_input = gr.Textbox(
                    label="Country Name",
                    placeholder="e.g., Germany, France, Japan",
                    value="Germany"
                )
                submit_btn = gr.Button("Find Capital", variant="primary")
            
            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="Answer",
                    lines=5,
                    interactive=False
                )
        
        # Examples
        gr.Examples(
            examples=["Germany", "France", "Japan", "Brazil", "Australia"],
            inputs=topic_input
        )
        
        # Connect the button to the function
        submit_btn.click(fn=ask_capital, inputs=topic_input, outputs=output)
        
        gr.Markdown(
            """
            ---
            ### About
            This web interface uses:
            - **Ollama** for local LLM inference (llama2 model)
            - **LangChain** with LCEL for chain composition
            - **Gradio** for the web UI
            """
        )
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=False, server_name="127.0.0.1", server_port=7860)
