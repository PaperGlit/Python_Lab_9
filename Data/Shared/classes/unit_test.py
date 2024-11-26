"""Tests the lab works"""
import os
import unittest
from unittest.mock import patch, Mock
from Data.Shared.functions.calculator import calculate
from Data.Lab7.DAL.classes.database_handler import DBHandler
from Data.Lab7.DAL.classes.api_repository import ApiRepository


class UnitTest(unittest.TestCase):
    """Tests the lab works"""
    def setUp(self):
        """Sets up everything for testing."""
        self.base_url = "https://jsonplaceholder.typicode.com/posts"
        self.api_repo = ApiRepository(self.base_url)
        self.db_handler = DBHandler(":memory:")

    def test_addition(self):
        """Tests the addition of two numbers."""
        self.assertEqual(calculate(17, 8, "+"), 25)
        self.assertEqual(calculate(-17, 8, "+"), -9)

    def test_subtraction(self):
        """Tests the subtraction of two numbers."""
        self.assertEqual(calculate(17, 8, "-"), 9)
        self.assertEqual(calculate(8, 17, "-"), -9)

    def test_multiplication(self):
        """Tests the multiplication of two numbers."""
        self.assertEqual(calculate(20, 0.2, "*"), 4)
        self.assertEqual(calculate(5, -4, "*"), -20)
        self.assertEqual(calculate(5, 0, "*"), 0)

    def test_division(self):
        """Tests the division of two numbers."""
        self.assertEqual(calculate(10, 0.5, "/"), 20)
        self.assertEqual(calculate(10, -2, "/"), -5)
        self.assertEqual(calculate(10, 4, "/"), 2.5)
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    def test_invalid_operation(self):
        """Tests the invalid operator functionality"""
        with self.assertRaises(ValueError):
            calculate(10, 0, "&")
        with self.assertRaises(ValueError):
            calculate("a", 0, "*")
        with self.assertRaises(ValueError):
            calculate(0, "b", "+")

    @patch("requests.get")
    def test_get_all(self, mock_get):
        """Test the GET ALL request."""
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
        mock_get.assert_called_once_with(self.base_url, timeout=10)

    @patch("requests.get")
    def test_get_by_id(self, mock_get):
        """Test the GET BY request."""
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: {"id": 1, "title": "Post 1"}
        )

        result = self.api_repo.get_by_id(1)
        self.assertEqual(result["title"], "Post 1")
        mock_get.assert_called_once_with(f"{self.base_url}/1", timeout=10)

    @patch("requests.post")
    def test_add(self, mock_post):
        """Test the POST request."""
        mock_post.return_value = Mock(
            status_code=201,
            json=lambda: {"id": 101, "title": "New Post"}
        )

        data = {"title": "New Post", "body": "Content of the post"}
        result = self.api_repo.add(data)

        self.assertEqual(result["id"], 101)
        self.assertEqual(result["title"], "New Post")
        mock_post.assert_called_once_with(self.base_url, json=data, timeout=10)

    @patch("requests.patch")
    def test_update(self, mock_patch):
        """Test the PATCH request."""
        mock_patch.return_value = Mock(
            status_code=200,
            json=lambda: {"id": 1, "title": "Updated Post"}
        )

        data = {"title": "Updated Post"}
        result = self.api_repo.update(1, data)

        self.assertEqual(result["title"], "Updated Post")
        mock_patch.assert_called_once_with(f"{self.base_url}/1", json=data, timeout=10)

    @patch("requests.delete")
    def test_delete(self, mock_delete):
        """Test the DELETE request."""
        mock_delete.return_value = Mock(status_code=200)

        result = self.api_repo.delete(1)
        self.assertTrue(result)
        mock_delete.assert_called_once_with(f"{self.base_url}/1", timeout=10)

    def test_create_table(self):
        """Test that the history table is created successfully."""
        self.db_handler.cursor.execute("SELECT name FROM sqlite_master "
                                       "WHERE type='table' AND name='history'")
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

        with open("test_history.txt", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("GET", content)
            self.assertIn("posts", content)

        os.remove("test_history.txt")

    def test_export_to_csv(self):
        """Test exporting history to a .csv file."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.export_to_csv("test_history.csv")

        with open("test_history.csv", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("GET", content)
            self.assertIn("posts", content)

        os.remove("test_history.csv")

    def test_export_to_json(self):
        """Test exporting history to a .json file."""
        self.db_handler.insert_history("posts", "GET", "all")
        self.db_handler.export_to_json("test_history.json")

        with open("test_history.json", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn('"type": "GET"', content)
            self.assertIn('"link": "posts"', content)

        os.remove("test_history.json")

    def tearDown(self):
        """Clean up by closing the database connection."""
        self.db_handler.close()

    @staticmethod
    def run_unit_tests():
        """Runs unit tests"""
        print("Running unit tests...\n")
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest)
        runner = unittest.TextTestRunner()
        runner.run(suite)