from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import tensorflow


def get_model(name="gpt2"):
    tokenizer = GPT2Tokenizer.from_pretrained(name)
    model = TFGPT2LMHeadModel.from_pretrained(name,
                                      pad_token_id=tokenizer.eos_token_id)
    return model, tokenizer


def predict(inp, context):
    model, tokenizer = context
    input_ids = tokenizer.encode(inp, return_tensors='tf')
    beam_output = model.generate(input_ids, max_length=100, num_beams=5,
                                 no_repeat_ngram_size=2, early_stopping=True)
    output = tokenizer.decode(beam_output[0], skip_special_tokens=True,
                              clean_up_tokenization_spaces=True)
    return ".".join(output.split(".")[:-1]) + "."
