import unittest
from app_secretary import (
    check_document_existance,
    get_all_doc_owners_names,
    add_new_shelf,
    remove_doc_from_shelf,
    directories # Импортируем словари, чтобы проверять изменения
)

class TestSecretaryApp(unittest.TestCase):

    # --- ТЕСТ 1: Проверка существования документа (Позитивный) ---
    def test_check_doc_exists(self):
        # Arrange
        doc_to_find = "2207 876234"
        expected = True
        
        # Act
        result = check_document_existance(doc_to_find)
        
        # Assert
        self.assertEqual(result, expected)

    # --- ТЕСТ 2: Проверка существования документа (Негативный) ---
    def test_check_doc_not_exists(self):
        # Arrange
        doc_to_find = "9999 999999"
        expected = False
        
        # Act
        result = check_document_existance(doc_to_find)
        
        # Assert
        self.assertEqual(result, expected)

    # --- ТЕСТ 3: Получение списка владельцев ---
    def test_get_all_owners(self):
        # Arrange
        expected_owners = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        
        # Act
        result = get_all_doc_owners_names()
        
        # Assert
        self.assertSetEqual(result, expected_owners)

    # --- ТЕСТ 4: Добавление новой полки ---
    def test_add_new_shelf_success(self):
        # Arrange
        new_shelf = "99"
        
        # Act
        shelf_and_status = add_new_shelf(new_shelf)
        
        # Assert
        self.assertTupleEqual(shelf_and_status, ("99", True))

    # --- ТЕСТ 5: Удаление документа с полки ---
    def test_remove_doc_from_shelf(self):
        # Arrange
        doc_to_remove = "11-2"
        # Запоминаем, что до удаления он есть на полке '1'
        self.assertIn(doc_to_remove, directories['1'])
        
        # Act
        result = remove_doc_from_shelf(doc_to_remove)
        
        # Assert
        self.assertNotIn(doc_to_remove, directories['1'])
        self.assertTrue(result)
        directories['1'].append("11-2")

if __name__ == '__main__':
    unittest.main()