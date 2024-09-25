import unittest
from unittest.mock import patch, MagicMock
import twitter_service


class TestTwitterService(unittest.TestCase):
    @patch("twitter_service.requests.get")
    def test_get_user_details(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        expected_data = {"data": {"id": "123", "name": "Test User"}}
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the function
        result = twitter_service.get_user_details()

        # Check if the API was called correctly
        mock_get.assert_called_once_with(
            "https://api.x.com/2/users/me",
            auth=twitter_service.auth_api,
            headers={"Content-Type": "application/json"},
        )
        # Assert the result is as expected
        self.assertEqual(result, expected_data)
        print("ttest_get_user_details: Sucess")

    @patch("twitter_service.requests.get")
    def test_get_user_by_username(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        expected_data = {"data": {"id": "456", "username": "testuser"}}
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the function
        result = twitter_service.get_user_by_username("testuser")

        # Check if the API was called correctly
        mock_get.assert_called_once_with(
            "https://api.x.com/2/users/by/username/testuser",
            auth=twitter_service.auth_api,
            headers={"Content-Type": "application/json"},
        )
        # Assert the result is as expected
        self.assertEqual(result, expected_data)
        print("test_get_user_by_username:: Success")

    @patch("twitter_service.requests.post")
    def test_create_tweet(self, mock_post):
        # Mock the response
        mock_response = MagicMock()
        expected_data = {"data": {"id": "789", "text": "Hello, world!"}}
        mock_response.json.return_value = expected_data
        mock_post.return_value = mock_response

        # Call the function
        result = twitter_service.create_tweet("Hello, world!")

        # Check if the API was called correctly
        mock_post.assert_called_once_with(
            "https://api.x.com/2/tweets",
            auth=twitter_service.auth_api,
            headers={"Content-Type": "application/json"},
            data='{"text": "Hello, world!"}',
        )
        # Assert the result is as expected
        self.assertEqual(result, expected_data)
        print("test_create_tweet: Sucess")

    @patch("twitter_service.requests.delete")
    def test_delete_tweet(self, mock_delete):
        # Mock the response
        mock_response = MagicMock()
        expected_data = {"data": {"id": "789"}}
        mock_response.json.return_value = expected_data
        mock_delete.return_value = mock_response

        # Call the function
        result = twitter_service.delete_tweet("789")

        # Check if the API was called correctly
        mock_delete.assert_called_once_with(
            "https://api.x.com/2/tweets/789", auth=twitter_service.auth_api
        )
        # Assert the result is as expected
        self.assertEqual(result, expected_data)
        print("test_delete_tweet: Success")

    @patch("twitter_service.requests.delete")
    def test_delete_tweet_fail(self, mock_delete):
        # Mock the response
        mock_response = MagicMock()
        expected_data = {"data": {"id": "789"}}
        mock_response.json.return_value = expected_data
        mock_delete.return_value = mock_response

        # Call the function
        result = twitter_service.delete_tweet("789")

        # Check if the API was called correctly
        mock_delete.assert_called_once_with(
            "https://api.x.com/2/tweets/789", auth=twitter_service.auth_api
        )
        # Assert the result is as expected
        self.assertEqual(result, expected_data)
        print("test_delete_tweet: Success")


if __name__ == "__main__":
    unittest.main()
