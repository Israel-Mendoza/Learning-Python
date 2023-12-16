class AnonymousSurvey:

    def __init__(self, question: str) -> None:
        """Store a question, and prepare to store responses."""
        self._question: str = question
        self._responses: list[str] = []

    @property
    def question(self) -> str:
        return self._question

    @property
    def responses(self) -> list[str]:
        return self._responses

    def show_question(self) -> None:
        """Show the survey question."""
        print(self._question)

    def store_response(self, new_response: str) -> None:
        """Store a single response to the survey"""
        self._responses.append(new_response)

    def show_results(self) -> None:
        """Shows all the responses that have been given."""
        print("Survey results: ")
        for response in self._responses:
            print(f"\t- {response}")
