import datetime

from django.test import TestCase
from django.utils import timezone

from .models import PlannerNote, Diary

class PlannerNoteTests(TestCase):

    def test_was_published_recently_with_future_date_note(self):
        """was_published_recently() returns False for notes whose pub_date is in the future."""
        time = timezone.now()+datetime.timedelta(days=30)
        future_note = PlannerNote(pub_date=time)

        self.assertIs(future_note.was_published_recently(), False)

    def test_was_published_recently_with_old_note(self):
        """was_published_recently() returns False for notes whose pub_date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_note = PlannerNote(pub_date=time)
        self.assertIs(old_note.was_published_recently(), False)

    def test_was_published_recently_with_recent_note(self):
        """was_published_recently() returns True for notes whose pub_date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = PlannerNote(pub_date=time)
        self.assertIs(recent_note.was_published_recently(), True)


class DiaryTests(TestCase):

    def test_was_published_recently_with_future_date_entry(self):
        """was_published_recently() returns False for entries whose pub_date is in the future."""
        time = timezone.now()+datetime.timedelta(days=30)
        future_entry = Diary(pub_date=time)

        self.assertIs(future_entry.was_published_recently(), False)

    def test_was_published_recently_with_old_entry(self):
        """was_published_recently() returns False for entries whose pub_date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_entry = Diary(pub_date=time)
        self.assertIs(old_entry.was_published_recently(), False)

    def test_was_published_recently_with_recent_entry(self):
        """was_published_recently() returns True for entries whose pub_date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_entry = Diary(pub_date=time)
        self.assertIs(recent_entry.was_published_recently(), True)