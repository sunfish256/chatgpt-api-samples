import openai


class NewChat:

    def __init__(self, role: str = None, engine: str = None):
        """
        role: input a system role
        engine: if you use Azure OpenAI API, input your deployment name
        """
        self.engine = engine
        if role:
            self.role = role
            self.messages = [
                {'role': 'system', 'content': self.role},
            ]
        else:
            self.role = None
            self.messages = []

    def generate(self, message: str, **kwargs):
        """
        massage: input a user message
        kwargs: For openai.ChatCompletion.create(**kwargs)
                Examples of kwargs:
                temperature=0.1
                top_p=0.1
                max_tokens=400
                # Only one of "temperature" and "top_p" should be modified.
        """
        # input message
        self.messages.append(
            {'role': 'user', 'content': message},
        )
        # get reply
        chat_completion = openai.ChatCompletion.create(
            engine=self.engine,
            messages=self.messages,
            **kwargs
        )
        reply = chat_completion.choices[0].message.content
        self.messages.append(
            {'role': 'assistant', 'content': reply}
        )
        return reply

    def clear(self):
        # clear messages without system role
        if self.role:
            self.messages = [
                {'role': 'system', 'content': self.role},
            ]
        else:
            self.messages = []

    def reset_role(self, role: str = None):
        """
        role: input a new system role
        """
        # reset system role
        if role:
            self.role = role
            self.messages = [
                {'role': 'system', 'content': self.role},
            ]
        else:
            self.messages = []
