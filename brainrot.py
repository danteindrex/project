from langchain_ollama import OllamaLLM

# Set your Hugging Face API key for authentication
api_key = "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"
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

def translate(content):
    messages = [
	{
		"role": "slung gen z language translator",
		"content": content}]
    completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct", 
            messages=messages, 
            max_tokens=500
                            )
    return    print(completion.choices[0].message["content"])






def inputs():
    try:
        word = input("Enter: Brainrot... /English...")
    except ValueError:
        print("incorrect format")
    return word

def translate_text_with_llama(word):
    yoursentence = input("Enter the text:").strip()

    # Initialize the OllamaLLM with Llama 3.3 model and authentication key
    llm = OllamaLLM(model="llama3.3", api_key=api_key)  # Using Llama 3.3 and your API key

    if word == "brainrot" or word=="Brainrot":
        content=f" The sentence provided is a slung language spoken by teenagers provide it's equivalence in traditional spoken english word per word .the sentence is  --({yoursentence})--  be brief and do not explain "
        translate(content)
	
        #print(messages)
    elif word == "english" or word=="English":
        content = f" The sentence provided is in traditional english language,what is it's equivalence in  slung language spoken by teenagers.The sentence is  --({yoursentence} )--  be brief and do not explain "
        translate(content)
    else:
        print("Invalid")

def main():
    """Main function to handle translation."""
    print("""
BBBBB   RRRRR    AAAAA   III  N   N  RRRRR    OOO   TTTTT
B    B  R    R   A   A    I   NN  N  R    R  O   O    T
BBBBB   RRRRR    AAAAA    I   N N N  RRRRR   O   O    T
B    B  R  R     A   A    I   N  NN  R  R    O   O    T
BBBBB   R   RR   A   A   III  N   N  R   RR   OOO     T
""")

    word=inputs()

    translate_text_with_llama(word)

if __name__ == "__main__":
    main()