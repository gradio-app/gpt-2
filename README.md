# GPT-2 on Gradio

- Loads `gpt-2`, but can load `gpt2-medium`, `gpt2-large` or `gpt2-xl`.
- `max_length` set to 100 (The max length of the sequence to be generated.)
- running `".".join(output.split(".")[:-1]) + "."` so that `max_length` doesn't stop an output abruptly. 
