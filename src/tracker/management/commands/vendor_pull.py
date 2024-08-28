from tracker.utils import download_to_local

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand


STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "htmx.js": "https://unpkg.com/htmx.org@2.0.2",
    "tailwind.js": "https://cdn.tailwindcss.com?plugins=typography",
    "daisy-ui.css": "https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css",
}


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {url}"))
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files.")
            )
        else:
            self.stdout.write(self.style.WARNING("Some files were not updated."))
