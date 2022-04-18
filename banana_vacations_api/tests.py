import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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

    def create_note(notes_text, days):
        """ Create a planner note with the given `notes_text` and published the given number of `days` 
        offset to now (negative for notes published in the past, positive for notes that have 
        yet to be published)."""
        time = timezone.now() + datetime.timedelta(days=days)
        return PlannerNote.objects.create(notes_text=notes_text, pub_date=time)

   
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

    def create_entry(diary_entry, days):
        """ Create a diary entry with the given `diary_entry` and published the given number of `days` 
        offset to now (negative for entries published in the past, positive for entries that have 
        yet to be published)."""
        time = timezone.now() + datetime.timedelta(days=days)
        return Diary.objects.create(diary_entry=diary_entry, pub_date=time)

    