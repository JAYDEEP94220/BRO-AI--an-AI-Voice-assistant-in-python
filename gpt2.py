from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained model and tokenizer
model_name = "gpt2"  # You can specify different versions if needed
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Generate text
prompt = "Once upon a time"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate text given the prompt
output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
