from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from palettes.models import Palette
from colors.models import Color
from rest_framework import status

User = get_user_model()

class ColorTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.palette = Palette.objects.create(name='Test palette', user=cls.user)
        cls.color = Color.objects.create(palette=cls.palette, hex_code='#FFFFFF', name='White')

        cls.url_detail = reverse('color-detail', kwargs={'pk': cls.color.id})
        cls.url_list = reverse('color-list')

    def test_color_create(self):
        self.client.force_authenticate(user=self.user)
        data = {'palette': self.palette.id, 'hex_code': '#000000'}
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Color.objects.count(), 2)

    def test_color_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"{self.url_list}?palette_id={self.palette.id}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_color_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'White')

    def test_palette_update(self):
        self.client.force_authenticate(user=self.user)
        data = {'hex_code': '#FF0000'}
        response = self.client.patch(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.color.refresh_from_db()
        self.assertEqual(self.color.name, 'Red')

    def test_palette_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Color.objects.filter(id=self.color.id).exists())

    def test_exit_forbidden(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        self.client.force_authenticate(user=other_user)
        response_retrieve = self.client.get(self.url_detail, format='json')
        response_list = self.client.get(f"{self.url_list}?palette_id={self.palette.id}", format='json')
        self.assertIn(response_retrieve.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND])
        self.assertEqual(len(response_list.data), 0)
