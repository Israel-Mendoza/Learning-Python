import unittest
from src.anonymous_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""

    def setUp(self) -> None:
        """Creates an instance of the AnonymousSurvey class."""
        survey_question: str = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(survey_question)
        self.initial_responses: list[str] = ["English", "Spanish", "French"]

    def test_store_single_response(self) -> None:
        """Test that a single response is stored properly."""
        self.survey.store_response(self.initial_responses[0])
        self.assertIn(self.initial_responses[0], self.survey.responses)

    def test_store_three_responses(self) -> None:
        """Test that three individual responses are stored properly."""
        for response in self.initial_responses:
            self.survey.store_response(response)
        for response in self.initial_responses:
            self.assertIn(response, self.survey.responses)


if __name__ == "__main__":
    unittest.main()
