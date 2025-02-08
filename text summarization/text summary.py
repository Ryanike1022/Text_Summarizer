import torch
import gradio as gr
from transformers import pipeline

# 🔹 Load the model
model_path = "../Models/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
text_summary = pipeline("summarization", model=model_path, torch_dtype=torch.bfloat16)

# 🔹 Background Image URL
bg_image_url = "https://images.unsplash.com/photo-1611416457332-946853cc75d6?q=80&w=3071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# 🔹 Custom CSS with Light Elegant Title
custom_css = f"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap');

.gradio-container {{
    background: url('{bg_image_url}') no-repeat center center fixed;
    background-size: cover;
    color: #ffffff;
    font-family: 'Arial', sans-serif;
    padding: 20px;
}}

/* Elegant Title */
h1 {{
    text-align: center; 
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    color: #f0f8ff;  /* Light Alice Blue for a Premium Look */
    text-shadow: 2px 2px 10px rgba(240, 248, 255, 0.8);  /* Subtle Glow */
}}

/* Styled Input Box */
textarea {{
    background-color: rgba(30, 30, 30, 0.9);
    color: #ffffff !important;
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #555;
}}

/* Buttons with Hover Effect */
button {{
    background: linear-gradient(135deg, #00C6CF, #0072FF);
    color: #ffffff !important;
    border-radius: 8px;
    font-size: 16px;
    padding: 10px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 10px rgba(0, 198, 207, 0.4);
}}

button:hover {{
    background: linear-gradient(135deg, #0072FF, #00C6CF);
    transform: scale(1.05);
    box-shadow: 0px 6px 15px rgba(0, 198, 207, 0.6);
}}
"""

# 🔹 Summarization Function
def summary(input_text):
    if not input_text.strip():
        return "⚠️ Please enter some text to summarize!"
    
    output = text_summary(input_text)
    return output[0]["summary_text"]

# 🔹 Gradio Interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<h1>✨ Ryan's Text Summarizer ✨</h1>")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="🔷 Enter Text",
                placeholder="Paste your text here...",
                lines=10,
                interactive=True
            )
            char_count = gr.Markdown("**Character Count: 0**")
            
            def update_count(text):
                return f"**Character Count: {len(text)}**"
            
            text_input.change(update_count, inputs=text_input, outputs=char_count)
            
            submit_btn = gr.Button("⚡ Summarize Now")
        
        with gr.Column():
            summary_output = gr.Textbox(
                label="🔶 Summary",
                interactive=False,
                lines=6
            )

    submit_btn.click(summary, inputs=text_input, outputs=summary_output)

# 🔹 Launch the App
demo.launch()
