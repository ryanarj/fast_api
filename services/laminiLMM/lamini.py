import lamini


class LaminiService:

    def __init__(self):
        self.api_key = "463f53863e605253918a957926ef578cbc0864ca5e73acc8decb0999fc8b46fb"
        self.lamini_llm = "meta-llama/Llama-2-7b-chat-hf"


    def generate_answer_from_prompt(self, prompt, llm=None):
        if not llm:
            llm = lamini.LlamaV2Runner(config={'api_key': self.api_key})
            print(llm)
        try:
            res = llm(prompt)
            return res
        except Exception as e:
            raise e
