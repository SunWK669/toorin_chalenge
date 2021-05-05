import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Author, PublishingCompany, Book

class TestBooks(TestCase):

    def setUp(self):
        Author.objects.create(name="Joãozinho")
        PublishingCompany.objects.create(name="Editora 1")

    def test_CRUD(self):
        url = "/api/books/"
        client = APIClient()
        payload = {
            "title": "João e o pé de feijão",
            "isbn": "1234567890912",
            "number_of_pages": 159,
            "description": "alisdjksd",
            "author": 1,
            "publishing_company": 1
        }
        expected_result = [{
            "id": 1,
            "title": "João e o pé de feijão",
            "isbn": "1234567890912",
            "number_of_pages": 159,
            "description": "alisdjksd",
            "author": 1,
            "publishing_company": 1
        }]
        response_post = client.post(url, payload)
        response_get_list = client.get(url, payload)
        response_get_retrieve = client.get(url + "1/")

        #POST, LIST, RETRIEVE
        self.assertEqual(expected_result[0], json.loads(response_post.content))
        self.assertTrue(Book.objects.filter(pk=1).exists())
        self.assertEqual(expected_result, json.loads(response_get_list.content))
        self.assertEqual(expected_result[0], json.loads(response_get_retrieve.content))

        #PUT
        payload['number_of_pages'] = 200
        response_put = client.put(url + "1/", payload)
        expected_result[0]['number_of_pages'] = 200
        self.assertEqual(expected_result[0], json.loads(response_put.content))

        #DELETE
        response_delete = client.delete(url + "1/")
        self.assertEqual(response_delete.status_code, 204)

    def test_error_post_isbn_author_company(self):
        url = "/api/books/"
        client = APIClient()
        payload = {
            "title": "João e o pé de feijão",
            "isbn": "12345678909122",
            "number_of_pages": 159,
            "description": "alisdjksd",
            "author": 73,
            "publishing_company": 98
        }
        expected_result = {
        "isbn": [
            "Ensure this field has no more than 13 characters."
        ],
        "author": [
            "Invalid pk \"73\" - object does not exist."
        ],
        "publishing_company": [
            "Invalid pk \"98\" - object does not exist."
        ]
        }
        response = client.post(url, payload)
        self.assertEqual(expected_result, json.loads(response.content))
