from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskViewTests(TestCase):
    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_add_task_and_complete_and_delete(self):
        # add a new task
        response = self.client.post(reverse('addTask'), {'task': 'buy milk'})
        self.assertRedirects(response, reverse('home'))
        task = Task.objects.get(task='buy milk')
        self.assertFalse(task.is_completed)

        # mark it complete
        response = self.client.get(reverse('completeTask', args=[task.id]))
        self.assertRedirects(response, reverse('home'))
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

        # delete it
        response = self.client.get(reverse('deleteTask', args=[task.id]))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Task.objects.filter(id=task.id).exists())
