from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from palettes.models import Palette
from rest_framework import status

User = get_user_model()

class PaletteTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.url_list = reverse('palette-list')
        cls.palette = Palette.objects.create(name='Test palette', user=cls.user)
        cls.url_detail = reverse('palette-detail', kwargs={'pk': cls.palette.id})

    def test_palette_create(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'new palette'}
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Palette.objects.count(), 2)

    def test_palette_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_palette_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test palette')

    def test_palette_update(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Update palette'}
        response = self.client.put(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.palette.refresh_from_db()
        self.assertEqual(self.palette.name, 'Update palette')

    def test_palette_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Palette.objects.filter(id=self.palette.id).exists())

    def test_exit_forbidden(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        self.client.force_authenticate(user=other_user)
        response = self.client.get(self.url_detail, format='json')
        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND])

