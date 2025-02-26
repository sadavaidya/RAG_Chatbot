from transformers import pipeline
import torch

class Generator:
    def __init__(self, model_name="gpt2"):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = pipeline("text-generation", model=model_name, device=device)
        #self.model = pipeline("text-generation", model=model_name, device=-1)  # Ensure it's using GPU if available
    
    def generate(self, context, query):
        # Clean and prepare prompt
        prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
        
        # Ensure max_length is appropriate, maybe set a higher value if needed
        response = self.model(prompt, max_length=500, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, temperature=0.7)
        
        # Extract the generated answer
        generated_text = response[0]["generated_text"]
        
        # Clean up generated text by removing the prompt part
        answer = generated_text.split("Answer:")[-1].strip()
        
        return answer
