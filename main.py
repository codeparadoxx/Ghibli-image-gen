import replicate
import gradio as gr
import os

if "REPLICATE_API_TOKEN" not in os.environ:
    raise ValueError("Missing Replicate API Key! Set it in your environment variables.")

def generate_ghibli_image(prompt):
    output = replicate.run(
        "stability-ai/stable-diffusion",
        input={"prompt": prompt, "width": 512, "height": 512}
    )
    
    return output[0] if output else "No image generated."

iface = gr.Interface(
    fn=generate_ghibli_image,
    inputs=gr.Textbox(placeholder="Enter your Ghibli-style image prompt"),
    outputs=gr.Image(type="filepath"),
    title="Ghibli AI Image Generator",
    description="Generate Studio Ghibli-style images from text prompts."
)

if __name__ == "__main__":
    iface.launch()
