from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import tensorflow


def get_model(name="gpt2"):
    tokenizer = GPT2Tokenizer.from_pretrained(name)
    model = TFGPT2LMHeadModel.from_pretrained(name,
                                      pad_token_id=tokenizer.eos_token_id)
    return model, tokenizer
