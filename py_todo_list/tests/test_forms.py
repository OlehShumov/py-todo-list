from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from pyTodoList.forms import TaskForm
from pyTodoList.models import Task, Tag


class TaskFormTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_task_form_valid_data(self):
        form_data = {
            "content": "Test Content",
            "deadline": timezone.now(),
            "tag": [self.tag.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form_data = {}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_submission(self):
        form_data = {
            "content": "Test Content",
            "deadline": timezone.now(),
            "tag": [self.tag.id],
        }

        response = self.client.post(reverse("pyTodoList:task-create"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.content, "Test Content")

    def test_task_form_rendering(self):
        response = self.client.get(reverse("pyTodoList:task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form-control")
