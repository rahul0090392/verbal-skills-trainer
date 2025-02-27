class ChatModule:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.roles = {
            "Interviewer": "You are a job interviewer. Ask challenging but fair questions.",
            "Coach": "You are a supportive coach helping improve verbal clarity.",
            "Casual Conversation": "You are a friendly conversation partner.",
            "Debate Opponent": "You are a debate opponent, challenging viewpoints respectfully.",
        }

    async def get_response(self, message, role="Coach"):
        system_message = self.roles.get(role, self.roles["Coach"])
        return await self.llm_client.get_completion(message, system_message)
