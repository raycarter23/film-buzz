# Testing

Navigate back to the [README.md](https://github.com/raycarter23/film-buzz/blob/main/README.md) file.

## Code Validation

### HTML

### CSS

### JavaScript

### Python

## Browser Compatibility

I tested my deployed project on all of the following browsers to check for compatibility and rendering issues.

| Browser   | Home Page                                                                                     | About Page                                                                                      | Blog Page                                                                                      | Notes |
|-----------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------|
| Chrome    | ![Chrome - Home - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-home-1.png) ![Chrome - Home - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-home-2.png)                                                   | ![Chrome - About - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-about-1.png) ![Chrome - About - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-about-2.png)                                                  | ![Chrome - Blog - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-blog-1.png) ![Chrome - Blog - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-blog-2.png)                                                   |  No issues detected, works as expected     |
| Firefox   | ![Firefox - Home - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-home-1.png) ![Firefox - Home - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-home-2.png)                                                 | ![Firefox - About - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-about-1.png) ![Firefox - About - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-about-2.png)                                                | ![Firefox - Blog - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-blog-1.png) ![Firefox - Blog - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-blog-2.png)                                                 |  Text rendering issues on homepage trending post section; Issue resolved by      |
| Safari    | ![Safari - Home - 1](/documentation/testing/browser-compatibility/safari/safari-bt-home-1.png) ![Safari - Home - 2](/documentation/testing/browser-compatibility/safari/safari-bt-home-2.png)                                                   | ![Safari - About - 1](/documentation/testing/browser-compatibility/safari/safari-bt-about-1.png) ![Safari - About - 2](/documentation/testing/browser-compatibility/safari/safari-bt-about-2.png)                                                  | ![Safari - Blog - 1](/documentation/testing/browser-compatibility/safari/safari-bt-blog-1.png) ![Safari - Blog - 2](/documentation/testing/browser-compatibility/safari/safari-bt-blog-2.png)                                                   |   No issues detected, works as expected    |
| Edge      | ![Edge - Home - 1](/documentation/testing/browser-compatibility/edge/edge-bt-home-1.png) ![Edge - Home - 2](/documentation/testing/browser-compatibility/edge/edge-bt-home-2.png)                                                       | ![Edge - About - 1](/documentation/testing/browser-compatibility/edge/edge-bt-about-1.png) ![Edge - About - 2](/documentation/testing/browser-compatibility/edge/edge-bt-about-2.png)                                                      | ![Edge - Blog - 1](/documentation/testing/browser-compatibility/edge/edge-bt-blog-1.png) ![Edge - Blog - 2](/documentation/testing/browser-compatibility/edge/edge-bt-blog-2.png)                                                       |   No issues detected, works as expected    |


## Responsiveness

## Lighthouse Audit

## Defensive Programming

## User Story Testing

Below are all of my implemented user stories, with accompanying screenshots to demonstrate their functionality and how they meet the project requirements.

| ID  | User Story                                                                                  | Implementation |
|-----|---------------------------------------------------------------------------------------------|----------------|
| 1   | As a first-time site visitor, I can clearly see the website's purpose so that I can use it in the future. | [Website's Purpose]()           |
| 2   | As a developer, I can get an idea of the whole design system so that I can work on the UI/UX design.       | [Whole Design System]()           |
| 3   | As a developer, I can get an idea of which components to build so that I can work on the design system.    | [Design System Components]()           |
| 4   | As a developer, I can build the pages based on the Figma designs so that I can check how the website looks in real time. | [Figma Designs]()           |
| 5   | As a user, I can create an account so that I can make my profile.                                         | [Create an account]()           |
| 6   | As a registered user, I can log in to my account so that I can access the site.                           | [Login to account]()           |
| 7   | As a registered user, I can log out of my account so that I can delete the session on my current device.  | [Log out of account]()           |
| 8   | As a registered user, I can update my profile information so that other users can identify me.           | [Update my profile]()           |
| 9   | As a registered user, I can create posts so that I can share my thoughts about different movies.          | [Create Posts]()           |
| 10  | As an author, I can edit my posts so that I can correct information in the future.                        | [Edit Posts]()           |
| 11  | As an author, I can delete my posts so that I can remove content that I no longer want to be published.   | [Delete Posts]()           |
| 12  | As a user, I can view all the posts so that I can learn about different movies.                           | [View all Posts]()           |
| 13  | As a registered user, I can comment on other users' posts so that I can engage with them in a discussion. | [Comment on other posts]()           |
| 14  | As a commenter, I can edit my existing comments so that I can correct information.                        | [Edit my Comments]()           |
| 15  | As a commenter, I can delete existing comments so that I can remove my opinions.                         | [Delete my Comments]()           |
| 16  | As a user, I can filter posts so that I can view posts of a specific movie genre.                         | [Filter Posts]()           |
| 17  | As a user, I can search posts so that I can filter posts based on titles.                                 | [Search Posts]()           |
| 18  | As a registered user, I can create, update, and delete my own watchlist so that I can track movies I am interested in watching. | [Create, update and delete Watchlist]()           |
| 19  | As a site visitor/user, I can easily navigate the site on any device so that I have a seamless experience whether on desktop or mobile. | [Responsive Navigation]()           |
| 20  | As an admin, I can add, edit, or delete posts so that the database remains accurate.                      | [Admin - add, edit, or delete posts]()           |



## Python Unit Testing

## Bugs

### Fixed Bugs

| **Bug**                          | **Location**                          | **Cause**                                                                                                                                     | **Solution / Fix**                                                                                                                                                             |
|------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Environment variable not loading  | `settings.py` and `.env`             | Environment variables defined in `.env` were not being loaded into the project, likely due to missing or incorrect package usage.             | Fixed using `python-dotenv` package.                                                                                                                                          |
| Cloudinary Images not loading     | Media files (e.g., `/media/`)         | Cloudinary was not correctly syncing media files between the cloud and the local host, likely due to missing configurations or unsynced media directory. | Fixed by ensuring that the Cloudinary storage backend was properly configured in `settings.py` and syncing both media directories (local and cloud) to match.                 |
| Missing movies App dependency     | `watchlist/models.py`                 | The `Watchlist` model attempted to import the `Movie` model from a movies app that did not exist in the project, resulting in a `ModuleNotFoundError`. | Fixed by creating a `movies` app to define the `Movie` model.                                                                                                                |
| Comma Error in `INSTALLED_APPS`   | `settings.py` (`INSTALLED_APPS`)      | A missing comma after `'watchlist.apps.WatchlistConfig'` caused Django to concatenate the next entry (`'cloudinary'`), leading to an `ImportError`. | Fixed by adding a missing comma after `'watchlist.apps.WatchlistConfig'`.                                                                                                    |
| Duplicate slug causing IntegrityError | Watchlist `save` method             | The `slug` field was not dynamically ensuring uniqueness, causing an `IntegrityError` when duplicate slugs were generated.                   | Updated the `save` method to dynamically generate unique slugs by appending a counter to the base slug if a conflict is detected.                                             |
| Categories Not Displaying in Dropdown | Admin Panel: Blog > Posts > Add Post | No category instances existed in the database, causing the dropdown for categories to be empty.                                              | Manually added the predefined categories using the Categories section in the admin panel.                                                                                     |
| Comment not submitting to the database | `views.py`                         | Not linking Django form with `details.html`.                                                                                                 | Fixed by using `form.as_p` in `details.html` instead of `textarea`.                                                                                                          |
| CKEditor not loading              | `base.html`                           | CKEditor extra CSS and JavaScript files were not loading.                                                                                     | Used Jinja block templates to define `extra_css` and `extra_js`. Found the solution through [Reddit r/django](https://www.reddit.com/r/django/comments/6z38c1/help_with_adding_javascript_to_django_templates/).                                                                 |
| List bullet points not displaying | `about.html`                          | Tailwind CSS overrides the default list style, so bullet points were not visible by default.                                                  | Added the `list-disc` class to the `<ul>` element to explicitly set the bullet points. Reference: [Tailwind CSS Docs - List Style Type](https://tailwindcss.com/docs/list-style-type). |


### Unfixed Bugs




