import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {
        "role": "system",
        "content": "Welcome to the PC Care Center. I'm Dr. Intel, your dedicated PC health assistant. How may I assist you with optimizing and maintaining the health of your gaming PC today?",
    },
    {"role": "user", "content": "can you tell about intel i9 processor"},
    {"role": "assistant", "content": "Greetings! We're thrilled to assist you with any inquiries or guidance related to Intel products. To ensure we provide you with the most relevant information, could you please share your specific interests or needs? Whether you're exploring the latest innovations, seeking product recommendations, or have questions about our technology, we're here to help you make the most informed decisions."
},
]

prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

# Access the generated text from the output
assistant_response = outputs[0]['generated_text'].split('</s>')[-1].strip()

assistant_response_bot = assistant_response.replace("<|assistant|>","")

print(assistant_response_bot)

