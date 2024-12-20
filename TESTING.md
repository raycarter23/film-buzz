# Testing

Navigate back to the [README.md](https://github.com/raycarter23/film-buzz/blob/main/README.md) file.

## Code Validation

### HTML

### CSS

### JavaScript

### Python

## Browser Compatibility

## Responsiveness

## Lighthouse Audit

## Defensive Programming

## User Story Testing

## Python Unit Testing

## Bugs

### Fixed Bugs

| **Bugs**                          | **Location**                          | **Cause**                                                                                                                                     | **Solution / Fix**                                                                                                                                                             |
|------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Environment variable not loading  | `settings.py` and `.env`             | Environment variables defined in `.env` were not being loaded into the project, likely due to missing or incorrect package usage.             | Fixed using `python-dotenv` package.                                                                                                                                          |
| Cloudinary Images not loading     | Media files (e.g., `/media/`)         | Cloudinary was not correctly syncing media files between the cloud and the local host, likely due to missing configurations or unsynced media directory. | Fixed by ensuring that the Cloudinary storage backend was properly configured in `settings.py` and syncing both media directories (local and cloud) to match.                 |
| Missing movies App dependency     | `watchlist/models.py`                 | The `Watchlist` model attempted to import the `Movie` model from a movies app that did not exist in the project, resulting in a `ModuleNotFoundError`. | Fixed by creating a `movies` app to define the `Movie` model.                                                                                                                |
| Comma Error in `INSTALLED_APPS`   | `settings.py` (`INSTALLED_APPS`)      | A missing comma after `'watchlist.apps.WatchlistConfig'` caused Django to concatenate the next entry (`'cloudinary'`), leading to an `ImportError`. | Fixed by adding a missing comma after `'watchlist.apps.WatchlistConfig'`.                                                                                                    |
| Duplicate slug causing IntegrityError | Watchlist `save` method             | The `slug` field was not dynamically ensuring uniqueness, causing an `IntegrityError` when duplicate slugs were generated.                   | Updated the `save` method to dynamically generate unique slugs by appending a counter to the base slug if a conflict is detected.                                             |
| Categories Not Displaying in Dropdown | Admin Panel: Blog > Posts > Add Post | No category instances existed in the database, causing the dropdown for categories to be empty.                                              | Manually added the predefined categories using the Categories section in the admin panel.                                                                                     |
| Comment not submitting to the database | `views.py`                         | Not linking Django form with `details.html`.                                                                                                 | Fixed by using `form.as_p` in `details.html` instead of `textarea`.                                                                                                          |
| CKEditor not loading              | `base.html`                           | CKEditor extra CSS and JavaScript files were not loading.                                                                                     | Used Jinja block templates to define `extra_css` and `extra_js`. Found the solution through Reddit r/django.                                                                 |
| List bullet points not displaying | `about.html`                          | Tailwind CSS overrides the default list style, so bullet points were not visible by default.                                                  | Added the `list-disc` class to the `<ul>` element to explicitly set the bullet points. Reference: [Tailwind CSS Docs - List Style Type](https://tailwindcss.com/docs/list-style-type). |


### Unfixed Bugs




