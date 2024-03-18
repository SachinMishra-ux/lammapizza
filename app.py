from flask import Flask, jsonify, request
import json
import re
import torch
from transformers import pipeline
from langchain_community.llms import CTransformers
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate




# Accessing the Model (approval required)
model_name = "TheBloke/Llama-2-7B-Chat-GGML"  # Replace if using a different model
llm = CTransformers(model=model_name)
pipe = None 

with open("instruction.txt") as fileHandle:
    custom_instructions = fileHandle.read()


app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to PizzaAroma"

@app.route('/chat', methods=["POST"])
def generate_response():
    global pipe  # Access the global pipeline variable

    # Ensure pipeline is loaded (if not already)
    '''
    if pipe is None:
        pipe = pipeline(
            "text-generation",
            model=model,
            torch_dtype=torch.bfloat16,  # Consider device-specific optimization
            device_map="auto"
        )
    '''

    # Get the prompt from the request data
    query = request.form['query']  # Assuming prompt field in the form
    # Prepare messages for the chat template
    '''messages = [
        {"role": "system", "content": custom_instructions},
        {"role": "user", "content": prompt},
    ]'''
    custom_instructions= """
    You are a humble & helpful pizza bot, who takes orders from customer and reply to customers questions.
    question: {question}
    """
    prompt = PromptTemplate.from_template(custom_instructions)
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    response = llm_chain.run(query)
    

    # Generate chat response with safety measures
    '''try:
      


        # Implement safety checks here (e.g., filter out inappropriate language)
        # ... (replace with your safety filter logic)
        pattern= r'\[\/INST]\s*(.*)'
        response_list= re.findall(pattern, response)
        #print(f"System: {response_list[0]}")

        return jsonify({"response": response_list[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    '''
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)
