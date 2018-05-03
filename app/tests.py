from django.test import TestCase

# Create your tests here.
class AppTestCase(TestCase):

	print("Tests")

	def test_setUp(self):
		status = 'success'
		self.assertEqual(status, 'success')
