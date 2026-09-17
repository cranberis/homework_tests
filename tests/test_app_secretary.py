import unittest

from app_secretary import (
    add_new_shelf,
    check_document_existance,
    directories,  # Импортируем словари для проверки изменений
    get_all_doc_owners_names,
    remove_doc_from_shelf,
)


class TestSecretaryApp(unittest.TestCase):
    def test_check_doc_exists(self):
        # Arrange
        doc_to_find = "2207 876234"
        expected = True

        # Act
        result = check_document_existance(doc_to_find)

        # Assert
        self.assertEqual(result, expected)

    def test_check_doc_not_exists(self):
        # Arrange
        doc_to_find = "9999 999999"
        expected = False

        # Act
        result = check_document_existance(doc_to_find)

        # Assert
        self.assertEqual(result, expected)

    def test_get_all_owners(self):
        # Arrange
        expected_owners = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}

        # Act
        result = get_all_doc_owners_names()

        # Assert
        self.assertSetEqual(result, expected_owners)

    def test_add_new_shelf_success(self):
        # Arrange
        new_shelf = "99"

        # Act
        shelf_and_status = add_new_shelf(new_shelf)

        # Assert
        self.assertTupleEqual(shelf_and_status, ("99", True))

    def test_remove_doc_from_shelf(self):
        # Arrange
        doc_to_remove = "11-2"
        self.assertIn(doc_to_remove, directories["1"])

        # Act
        result = remove_doc_from_shelf(doc_to_remove)

        # Assert
        self.assertNotIn(doc_to_remove, directories["1"])
        self.assertTrue(result)
        directories["1"].append("11-2")


if __name__ == "__main__":
    unittest.main()