import gradio
from gpt import get_model, predict


INPUTS = gradio.inputs.Textbox()
OUTPUTS = gradio.outputs.Textbox()
INTERFACE = gradio.Interface(fn=predict, inputs=INPUTS, outputs=OUTPUTS, title="GPT-2",
                 description="GPT-2 is a large transformer-based language model with 1.5 billion parameters, trained on a dataset[1] of 8 million web pages. GPT-2 is trained with a simple objective: predict the next word, given all of the previous words within some text.",
                 thumbnail="https://github.com/gradio-app/gpt-2/raw/master/screenshots/interface.png?raw=true",
                             load_fn=get_model, capture_session=False)

INTERFACE.launch(inbrowser=True)
