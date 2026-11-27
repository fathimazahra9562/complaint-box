from django.test import TestCase
from .models import (
    complaintboxregister,
    complaintboxfaculty,
    complaintboxcomplaint,
    complaintboxacknowledgement,
    complaintboxackadmfac,
)


class ComplaintBoxModelTests(TestCase):

    def test_student_registration(self):
        student = complaintboxregister.objects.create(
            name="Test Student",
            phone="9876543210",
            email="student@example.com",
            image="test.jpg",
            password="testpassword"
        )
        self.assertEqual(student.name, "Test Student")

    def test_faculty_registration(self):
        faculty = complaintboxfaculty.objects.create(
            designation="Professor",
            name="Test Faculty",
            email="faculty@example.com",
            password="testpassword"
        )
        self.assertEqual(faculty.name, "Test Faculty")

    def test_complaint_creation(self):
        complaint = complaintboxcomplaint.objects.create(
            userid=1,
            complaintto="1",
            date="2026-11-27",
            name="Test Student",
            email="student@example.com",
            complaintmesg="Test complaint",
            status="pending"
        )
        self.assertEqual(complaint.status, "pending")

    def test_acknowledgement_creation(self):
        acknowledgement = complaintboxacknowledgement.objects.create(
            replyto=1,
            date="2026-11-27",
            name="Test Faculty",
            email="faculty@example.com",
            ackmesg="Complaint received"
        )
        self.assertEqual(acknowledgement.replyto, 1)

    def test_admin_faculty_acknowledgement(self):
        acknowledgement = complaintboxackadmfac.objects.create(
            ackto=1,
            date="2026-11-27",
            name="Test Admin",
            email="admin@example.com",
            ackmesg="Acknowledged"
        )
        self.assertEqual(acknowledgement.ackto, 1)
