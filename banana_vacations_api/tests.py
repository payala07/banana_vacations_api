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


class DiaryTests(TestCase):

    def test_was_published_recently_with_future_date_entry(self):
        """was_published_recently() returns False for entries whose pub_date is in the future."""
        time = timezone.now()+datetime.timedelta(days=30)
        future_entry = Diary(pub_date=time)

        self.assertIs(future_entry.was_published_recently(), False)