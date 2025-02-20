from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-large"):
        self.model = pipeline("text2text-generation", model=model_name)
    
    def generate(self, context, query):
        prompt = f"Context: {context} \n Question: {query} \n Answer:"
        response = self.model(prompt, max_length=100)
        return response[0]["generated_text"]
