import gradio
from gpt import get_model, predict


INPUTS = gradio.inputs.Textbox()
OUTPUTS = gradio.outputs.Textbox()
INTERFACE = gradio.Interface(fn=predict, inputs=INPUTS, outputs=OUTPUTS,
                             load_fn=get_model, capture_session=False)

INTERFACE.launch(inbrowser=True)
