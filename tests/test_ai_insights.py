import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.ai_insights import generate_insights
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class TestAIIntegration(unittest.TestCase):
    @patch("src.ai_insights.genai.GenerativeModel")
    @patch("src.ai_insights.genai.configure")
    def test_generate_insights(self, mock_configure, mock_generative_model):
        # Mock the API response
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value.text = "Mocked insights"
        mock_generative_model.return_value = mock_model_instance

        # Create a sample DataFrame
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

        # Test the generate_insights function
        insights = generate_insights(df)

        # Verify the mock was called
        mock_configure.assert_called_once_with(api_key=getenv('GEMINI_API_KEY'))
        mock_generative_model.assert_called_once_with("gemini-1.5-flash")
        mock_model_instance.generate_content.assert_called_once_with("Analyze the following dataset and provide insights:\n   A  B\n0  1  4\n1  2  5\n2  3  6")

        # Verify the response
        self.assertIsInstance(insights, str)
        self.assertEqual(insights, "Mocked insights")


if __name__ == "__main__":
    unittest.main()
