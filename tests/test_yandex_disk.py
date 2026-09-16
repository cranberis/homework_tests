import os
import unittest
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['YANDEX_DISK_POLIGON_TOKEN']
TESTING_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

class TestYandexDick(unittest.TestCase):
    
    def tearDown(self):
        headers = {'Authorization': f'OAuth: {TOKEN}'}
        # Гарантированно чистим за собой обе возможные папки, если они вдруг остались
        folders_to_clean = ["test-folder-pos-1", "test-folder-neg-1"]
        for folder in folders_to_clean:
            requests.delete(TESTING_URL, params={"path": folder}, headers=headers)

    def test_create_folder_positive(self):
        # Arrange
        headers = {'Authorization': f'OAuth: {TOKEN}'}
        params = {"path": "test-folder-pos-1"}

        # Act
        response = requests.put(TESTING_URL, params=params, headers=headers)
        meta_info = requests.get(TESTING_URL, params=params, headers=headers)

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(meta_info.status_code, 200)

    def test_create_folder_negative_re_creating_folder(self):
        # Arrange
        headers = {'Authorization': f'OAuth: {TOKEN}'}
        params = {"path": "test-folder-neg-1"}

        # Act
        response_1 = requests.put(TESTING_URL, params=params, headers=headers)
        response_2 = requests.put(TESTING_URL, params=params, headers=headers)

        # Assert
        self.assertEqual(response_1.status_code, 201)
        self.assertEqual(response_2.status_code, 409)

    def test_create_folder_negative_folder_wrong_name(self):
        # Arrange
        headers = {'Authorization': f'OAuth: {TOKEN}'}
        params = {"path": ""}

        # Act
        response = requests.put(TESTING_URL, params=params, headers=headers)

        # Assert
        self.assertEqual(response.status_code, 400)