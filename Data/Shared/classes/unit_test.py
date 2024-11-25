import os
import unittest
from unittest.mock import patch, Mock
from Data.Lab6.BLL.classes.calculator import Calculator
from Data.Lab7.DAL.classes.database_handler import DBHandler
from Data.Lab7.DAL.classes.api_repository import ApiRepository


class UnitTest(unittest.TestCase):
    def setUp(self):
        """Set up an instance of ApiRepository for testing."""
        self.base_url = "https://jsonplaceholder.typicode.com/posts"
        self.api_repo = ApiRepository(self.base_url)
        self.db_handler = DBHandler(":memory:")

    def test_addition(self):
        self.assertEqual(Calculator(17, 8, "+").result, 25)
        self.assertEqual(Calculator(-17, 8, "+").result, -9)

    def test_subtraction(self):
        self.assertEqual(Calculator(17, 8, "-").result, 9)
        self.assertEqual(Calculator(8, 17, "-").result, -9)

    def test_multiplication(self):
        self.assertEqual(Calculator(20, 0.2, "*").result, 4)
        self.assertEqual(Calculator(5, -4, "*").result, -20)
        self.assertEqual(Calculator(5, 0, "*").result, 0)

    def test_division(self):
        self.assertEqual(Calculator(10, 0.5, "/").result, 20)
        self.assertEqual(Calculator(10, -2, "/").result, -5)
        self.assertEqual(Calculator(10, 4, "/", 1).result, 2.5)
        with self.assertRaises(ZeroDivisionError):
            Calculator(10, 0, "/")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            Calculator(10, 0, "&")
        with self.assertRaises(ValueError):
            Calculator("a", 0, "*")
        with self.assertRaises(ValueError):
            Calculator(0, "b", "+")

    @patch("requests.get")
    def test_get_all(self, mock_get):
        """Test the get_all method."""
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: [
                {"id": 1, "title": "Post 1"},
                {"id": 2, "title": "Post 2"}
            ],
        )

        result = self.api_repo.get_all()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["title"], "Post 1")
        mock_get.assert_called_once_with(self.base_url)

    @patch("requests.get")
    def test_get_by_id(self, mock_get):
        """Test the get_by_id method."""
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: {"id": 1, "title": "Post 1"}
        )

        result = self.api_repo.get_by_id(1)
        self.assertEqual(result["title"], "Post 1")
        mock_get.assert_called_once_with(f"{self.base_url}/1")

    @patch("requests.post")
    def test_add(self, mock_post):
        """Test the add method."""
        mock_post.return_value = Mock(
            status_code=201,
            json=lambda: {"id": 101, "title": "New Post"}
        )

        data = {"title": "New Post", "body": "Content of the post"}
        result = self.api_repo.add(data)

        self.assertEqual(result["id"], 101)
        self.assertEqual(result["title"], "New Post")
        mock_post.assert_called_once_with(self.base_url, json=data)

    @patch("requests.patch")
    def test_update(self, mock_patch):
        """Test the update method."""
        mock_patch.return_value = Mock(
            status_code=200,
            json=lambda: {"id": 1, "title": "Updated Post"}
        )

        data = {"title": "Updated Post"}
        result = self.api_repo.update(1, data)

        self.assertEqual(result["title"], "Updated Post")
        mock_patch.assert_called_once_with(f"{self.base_url}/1", json=data)

    @patch("requests.delete")
    def test_delete(self, mock_delete):
        """Test the delete method."""
        mock_delete.return_value = Mock(status_code=200)

        result = self.api_repo.delete(1)
        self.assertTrue(result)
        mock_delete.assert_called_once_with(f"{self.base_url}/1")

    def test_create_table(self):
        """Test that the history table is created successfully."""
        self.db_handler.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history'")
        table = self.db_handler.cursor.fetchone()
        self.assertIsNotNone(table)

    def test_insert_history(self):
        """Test inserting a history record."""
        self.db_handler.insert_history("posts", "GET", "all")
        history = self.db_handler.fetch_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0][1], "posts")  # Check link
        self.assertEqual(history[0][2], "GET")  # Check request type
        self.assertEqual(history[0][3], "all")  # Check entity ID

    def test_fetch_history(self):
        """Test fetching history records."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.insert_history("users", "POST", "1")
        history = self.db_handler.fetch_history()
        self.assertEqual(len(history), 2)

    def test_export_to_txt(self):
        """Test exporting history to a .txt file."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.export_to_txt("test_history.txt")

        with open("test_history.txt", "r") as file:
            content = file.read()
            self.assertIn("GET", content)
            self.assertIn("posts", content)

        os.remove("test_history.txt")

    def test_export_to_csv(self):
        """Test exporting history to a .csv file."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.export_to_csv("test_history.csv")

        with open("test_history.csv", "r") as file:
            content = file.read()
            self.assertIn("GET", content)
            self.assertIn("posts", content)

        os.remove("test_history.csv")

    def test_export_to_json(self):
        """Test exporting history to a .json file."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.export_to_json("test_history.json")

        with open("test_history.json", "r") as file:
            content = file.read()
            self.assertIn('"type": "GET"', content)
            self.assertIn('"link": "posts"', content)

        os.remove("test_history.json")

    def tearDown(self):
        """Clean up by closing the database connection."""
        self.db_handler.close()