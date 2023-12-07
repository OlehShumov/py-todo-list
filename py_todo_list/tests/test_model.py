from django.test import TestCase
from django.utils import timezone
from pyTodoList.models import Task, Tag


class TaskModelTests(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")

    def test_task_creation(self):
        task = Task.objects.create(
            content="Test Task",
            deadline=timezone.now(),
            is_completed=False,
        )
        task.tag.add(self.tag1, self.tag2)

        self.assertEqual(Task.objects.count(), 1)
        saved_task = Task.objects.first()
        self.assertEqual(saved_task.content, "Test Task")
        self.assertEqual(saved_task.tag.count(), 2)

    def test_task_str_method(self):
        task = Task.objects.create(
            content="Test Task",
            deadline=timezone.now(),
            is_completed=False,
        )
        task.tag.add(self.tag1)

        expected_str = (
            f"Task: Test Task, "
            f"status: Not done, "
        )
        self.assertEqual(str(task), expected_str)


class TagModelTests(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(Tag.objects.count(), 1)
        saved_tag = Tag.objects.first()
        self.assertEqual(saved_tag.name, "Test Tag")

    def test_tag_str_method(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")
