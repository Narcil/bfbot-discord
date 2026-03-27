from cogs.llm import LLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class LangChainBot:
    def __init__(self):
        self.llm = LLM()
        self.system_prompt = SystemMessage(content="""You are a quiz bot helping users prepare for CompTIA Security+ certification exam. 
                                                      When the user requests a topic, generate ONE multiple choice question (A/B/C/D) in this exact format:
                                                      **Question:** [question text]
                                                        A) ...
                                                        B) ...
                                                        C) ...
                                                        D) ...
                                                        Wait for the user's answer. Then respond with correct/incorrect, the right answer, and a brief explanation (2-3 sentences max).""")
        self.histories = {}

    def get_history(self, user_id):
        if user_id not in self.histories:
            self.histories[user_id] = [self.system_prompt]
        return self.histories[user_id]

    def reset_history(self, user_id):
        self.histories[user_id] = [self.system_prompt]

    async def generate_response(self, user_id: int, user_input: str) -> str:
        try:
            history = self.get_history(user_id)
            history.append(HumanMessage(content=user_input))
            response = await self.llm.ask(history)
            history.append(AIMessage(content=response.content))
            return response.content
        except Exception as e:
            print(f"Error: {e}")
            return "I'm having trouble processing that request."