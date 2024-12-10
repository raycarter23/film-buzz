# Film Buzz 

## Introduction

Film Buzz is a movie blog platform built with Django, featuring full CRUD functionality that allows for creating, reading, updating, and deleting content. Users can explore insightful blogs, discover curated movie recommendations, and read thought-provoking reviews.

The aim of this project was to create a site that provides an engaging space for movie lovers to stay informed, share their passion for cinema, and connect with a like-minded community while offering dynamic content management capabilities.


Developed by **Ray Carter**

View live site here: [Film Buzz website](https://film-buzz-3729799f06ec.herokuapp.com/)

------

## Table of Contents

- [Overview](#overview)
  - [About](#about)
  - [Purpose](#purpose)
  - [Target Audience](#target-audience)
- [UX](#ux)
  - [Design Inspiration](#design-inspiration)
  - [Colour Scheme](#colour-scheme)
  - [Contrast Ratio: Primary Colours](#contrast-ratio-primary-colours)
  - [Contrast Ratio: Secondary Colours](#contrast-ratio-secondary-colours)
  - [Typography](#typography)
  - [Logo Design](#logo-design)
- [User Stories](#user-stories)
  - [Developer](#developer)
  - [Site Admin](#site-admin)
  - [New Site Users](#new-site-users)
  - [Registered Users](#registered-users)
- [Wireframes](#wireframes)
  - [Low-Fidelity Wireframes](#low-fidelity-wireframes)
  - [High-Fidelity Wireframes](#high-fidelity-wireframes)
- [Features](#features)
- [Database Design](#database-design)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Models Overview](#models-overview)
  - [Standard Models](#standard-models) 
  - [Custom Models](#custom-models)
- [Agile Development Process](#agile-development-process)
  - [MoSCoW Prioritisation](#moscow-prioritisation)
  - [GitHub Projects](#github-projects)
  - [GitHub Issues](#github-issues)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Heroku Deployment](#heroku-deployment)
  - [Clone Project](#clone-project)
  - [Fork Project](#fork-project)
- [Tools & Technologies Used](#tools--technologies-used)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools and Programmes](#tools-and-programmes)
- [Credits](#credits)
  - [Content](#content)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
  
## Overview

### About

Film Buzz is a dynamic movie blog platform built with Django, designed to celebrate cinema and provide a space for movie lovers to explore, discuss, and engage with the world of film. 

The goal of this project is to create an accessible and engaging platform for casual viewers, film enthusiasts, and aspiring movie bloggers alike. Built with the powerful Django framework, Film Buzz combines functionality with user-friendly design to deliver an enjoyable and seamless experience for all.

### Purpose

Many movie enthusiasts struggle to find a platform where they can read insightful reviews, explore curated movie recommendations, and stay updated on the latest in cinema. While casual viewers seek engaging content to guide their next movie choice, aspiring reviewers and bloggers often lack a centralised space to share their thoughts and connect with like-minded individuals. This gap leaves movie lovers without an accessible, community-driven hub for exploring and discussing their passion for film.

Film Buzz aims to solve this problem by providing a simple and engaging platform for movie enthusiasts to:
- Discover insightful reviews on a variety of films.
- Explore curated movie recommendations tailored to different tastes and genres.
- Read thought-provoking blogs and articles about cinema, including behind-the-scenes content and trends.
- Engage with content designed to inspire a deeper appreciation for the art of film.
- Offer a space for aspiring movie bloggers and critics to share their perspectives and grow their audience.

By offering these features, Film Buzz becomes a hub for celebrating cinema, fostering connection, and guiding viewers in their cinematic journeys.

### Target Audience

Film Buzz is designed to cater to a wide range of movie lovers, each with unique needs and interests:
- **Movie Enthusiasts**:
    - People who are passionate about watching, reviewing, and discussing movies.
- **Casual Viewers**:
    - Individuals looking for movie recommendations and reviews to decide what to watch next.
- **Reviewers and Bloggers**:
    - Professionals or hobbyists who want to share detailed critiques and engage with their audience.
- **Social Users**:
    - Users who enjoy following others, discovering popular content, and engaging in discussions.
- **Students and Professionals in the Film Industry**:
    - Aspiring filmmakers, critics, and actors seeking inspiration and community insights.

## UX

### Design Inspiration

### Colour Scheme

- YinMn Blue `#294E79` - used as the primary site colour, and secondary background colour for the footer.

- White `#FFFFFF` - used as site background colour for a clean and minimalistic design.

- Light Cyan `#D3F3FA` - used as an accent text colour on the YinMn Blue footer.

- Quinacridone Magenta `#79425B` - used as a secondary colour to add contrast and variety.

- Seal Brown `#603317` - used for the trash icon,  notification icon and warning buttons to ensure prominence and clarity.


![Colour Scheme](documentation/images/colour-scheme.png)

To design a visually appealing and thematic colour palette for my website, I utilised a combination of [Color Hunt](https://colorhunt.co/) and [Coolors](https://coolors.co/). My goal was to craft a palette that resonates with movie enthusiasts, blending style and accessibility.

The centrepiece of this palette is **YInMn Blue**, chosen as the primary colour to define the brand identity of Film Buzz with its vibrant and modern appeal. Complementing this, I selected **White** as the background colour to ensure a clean, easy-to-read layout that enhances the overall user experience.

### Contrast Ratio: Primary Colours

I wanted to ensure that the chosen primary text colour (**YInMn Blue** - `#294E79`) and background colour (**White** - `#FFFFFF`) met the web accessibility standards outlined by [WCAG](https://www.wcag.com/). WCAG defines a minimum colour contrast ratio of **4.5:1** for normal text and **3:1** for large text.

I tested the contrast ratio using [Adobe’s](https://color.adobe.com/create/color-contrast-analyzer) colour contrast checker tool, which gave me a contrast ratio of **8.54:1**, and ensured that good readability for visually impaired site users. 

![Primary Colours Contrast Ratio](documentation/images/blue-white-colour-contrast.png)

### Contrast Ratio: Secondary Colours

I also used [Venngage’s Accessible Color Palette Generator](https://venngage.com/tools/accessible-color-palette-generator) to create complementary colours that harmonise seamlessly with my primary colour while adhering to WCAG colour accessibility standards. To ensure optimal readability, I tested the contrast ratios of these colours using Adobe's Colour Contrast Checker tool. This process guided my design decisions and helped me pair colours effectively throughout my website.

For light cyan on a YInMn Blue background, I achieveed a contrast ratio of **7.3:1** 

![Cyan and Blue Contrast](documentation/images/cyan-blue-colour-contrast.png)


For quinacridone magenta on a white background, I achieved a contrast ratio of **7.65:1**

![Magenta and White Contrast](documentation/images/magenta-white-colour-contrast.png)


For seal brown on a white background, I achieved a contrast ratio of **10.59:1**

![Brown and White Contrast](documentation/images/brown-white-colour-contrast.png)

### Typography

- [Raleway](https://fonts.google.com/specimen/Raleway) - Used for headings and buttons.
- [Inter](https://fonts.google.com/specimen/Inter) - Used for site text and paragraphs.

![Fonts Used](documentation/images/typography.png)

### Logo design

I used [Logo Design AI](https://logodesign.ai/) to generate the following logo design for my website. I also generated the same logo with a white background, which was used in the footer section of the website, and I removed the background using [Remove Bg](https://www.remove.bg/)

![Logo](documentation/images/logo.png)

## User Stories

### Developer

- As a developer I can get an idea of the whole design system so that I can work on the UI/UX design. `Must Have`

- As a developer I can get an idea of which components to build so that I can work on the design system. `Must Have`

- As a developer I can build the pages based on the Figma designs so that I can check how the website looks in real time. `Must Have`

### Site Admin

- As an admin I can add, edit, or delete posts so that the database remains accurate. `Must Have`

- As a site admin, I can access a page exclusive to admins to view flagged user posts so that I can review posts that may need moderation or deletion. `Could Have`

- As a site admin, I can unflag a post if it does not require deletion so that I can remove it from the list of flagged posts. `Could Have`

- As an admin I can suspend user accounts who violate site guidelines so that I can prevent users from breaking the site rules. `Won’t Have`

- As an admin, I can view analytics on user activity and engagement so that I can better understand how the platform is performing. `Won’t Have`

### New Site users

- As a first time site visitor I can clearly see the website's purpose so that I can use it in the future. `Must Have`

- As a new site user I can create an account so that I can make my profile. `Must Have`

- As a site visitor/user I can easily navigate the site on any device so that I have a seamless experience whether on desktop or mobile. `Must Have`

- As a user/visitor I can see trending movies on the homepage so that I can discover what movies are popular right now. `Won’t Have`

### Registered users

- As a registered user I can login to my account so that I can access the site. `Must Have`

- As a registered user I can log out of my account so that I can delete session on my current device. `Must Have`

- As a registered user I can create posts so that I can share my thoughts about different movies. `Must Have`

- As an author I can edit my posts so that I can correct information in the future. `Must Have`

- As an author I can delete my posts so that I can remove content that I no longer want to be published. `Must Have`

- As a user I can view all the posts so that I can learn about different movies. `Must Have`

- As a commenter I can delete existing comments so that I can remove my opinions. `Must Have`

- As a user I can filter posts so that I can view posts of a specific movie genre. `Must Have`

- As a user I can search posts so that I can filter posts based on titles. `Must Have`

- As a registered user I can delete my account so that I can stop using the site when I no longer need it. `Should Have`

- As a registered user I can comment on other users' posts so that I can engage with them in a discussion. `Should Have`

- As a user I can follow other users so that I can keep up with their posts. `Should Have`

- As a registered user I can create my own watchlist so that I can track movies I am interested in watching. `Could Have`

- As a commenter I can edit my existing comments so that I can correct information. `Could Have`

- As a registered user I can update my profile information so that other users can identify me. `Could Have`

- As a registered user I can receive personalised movie recommendations based on my watchlist and reviews so that I can discover films tailored to my preferences. `Won’t Have`

- As a reviewer I can tag other users in comments so that I can engage directly with the community. `Won’t Have`

- As a registered user I can sync my watchlist with streaming platforms so that I know where to watch my saved movies. `Won’t Have`

## Wireframes

### Low-Fidelity Wireframes

### High-Fidelity Wireframes


## Features



## Database Design

I created an Entity Relationship Diagram using [Miro](https://miro.com/) to visually represent the relationships between the data models in Film Buzz, such as users, posts, comments, categories, and watchlists. This diagram highlights key relationships, such as the one-to-many connection between users and posts, and the many-to-many self-referential relationship for followers. 

To improve clarity, I colour-coded the database tables: standard models, such as users, posts and comments, are shown in grey; while custom models, such as watchlists, categories, follows and flagged posts, are displayed in blue. This approach ensures the database structure aligns with the application’s requirements and supports features like flagging posts, filtering by categories, and tracking personalised watchlists.

### Entity Relationship Diagram

![ER Diagram](documentation/images/film-buzz-er-diagram.jpg)

### Models Overview

The Film Buzz platform uses three standard models (**User**, **Post**, and **Commen**t) and four custom models (**Category**, **Watchlist**, **Follow**, and **FlaggedPost**) to manage its data structure. The standard models provide the foundation for user authentication, content creation, and engagement, while the custom models introduce features such as post categorisation, personalised watchlists, social connections, and content moderation. These models are interconnected through carefully designed foreign key relationships, ensuring data integrity, consistency, and efficient interaction across the platform's features.

### Standard Models 

**User Model**

The User model represents registered users on the Film Buzz platform. It is the central model for user authentication, profile management, and role determination. This model allows for features such as user sign-up, login, and account customisation.

- User - Django AllAuth Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `userId`    | INTEGER (PK) | Unique identifier for each user          |
|               | `username`   | VARCHAR(50)  | Display name chosen by the user          |
|               | `email`      | VARCHAR(255) | User's email for authentication and contact |
|               | `password`   | VARCHAR(255) | Hashed password for secure login         |
|               | `is_admin`   | BOOLEAN      | Indicates whether the user has admin privileges |
|               | `bio`        | VARCHAR(255) | Optional biography or personal description |
|               | `date_joined`| DATE         | Date when the user registered on the platform |

**Relationships**

- **One-to-Many with the Post model**:
  - A user can create multiple posts.
  - Linked via the `author` field in the Post model, which is a foreign key to the User model.
- **One-to-Many with the Comment model**:
  - A user can leave multiple comments on posts.
  - Linked via the `author` field in the Comment model, which is a foreign key to the User model.
- **Many-to-Many with itself (Follow model)**:
  - Represents user-to-user connections, such as followers and followees.
  - Managed through a self-referential relationship in the Follow model.

---

**Post Model**

The Post model represents a blog post or movie review created by a user on the Film Buzz platform. Each post serves as a piece of content that users can view, interact with, and categorise. Posts are associated with an author (user), timestamps, and categories to provide structure and allow for filtering and moderation.

- Post Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `post_id`   | INTEGER (PK) | Unique identifier for each post          |
|               | `title`      | VARCHAR(255) | Title of the post or review              |
|               | `content`    | VARCHAR(5000)| Main body of the post or review          |
|               | `created_at` | TIMESTAMP    | Records the date and time the post was created |
|               | `updated_at` | TIMESTAMP    | Records the date and time the post was last modified |
| **Foreign Key**| `author_id`  | INTEGER (FK) | Links the post to the user who created it |
|               | `is_flagged` | BOOLEAN      | Indicates whether the post is flagged for review |
|               | `category`   | VARCHAR(20)  | Categorises the post into a specific genre or type |

**Relationships**

- **One-to-Many with User**:
  - A single user (author) can create multiple posts.
  - The `author_id` field serves as a foreign key linking the Post model to the User model.
- **One-to-Many with Comment**:
  - A single post can have multiple comments.
  - Linked via the `post_id` field in the Comment model.
- **Many-to-One with Category**:
  - Each post belongs to one category, which helps users filter posts by genre.

---

**Comment Model**

The Comment model represents user-generated comments on posts in Film Buzz. It allows users to share their thoughts or feedback on a specific post, fostering engagement and community interaction on the platform. Each comment is tied to a specific user (the author of the comment) and a specific post.

- Comment Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `comment_id`| INTEGER (PK) | Unique identifier for each comment       |
|               | `content`    | VARCHAR(500) | Stores the text of the comment           |
|               | `created_at` | TIMESTAMP    | Records when the comment was created     |
| **Foreign Key**| `author_id`  | INTEGER (FK) | Links the comment to the user who authored it |
|               | `post_id`    | INTEGER (FK) | Links the comment to the post it belongs to |

**Relationships**

- **One-to-Many with User**:
  - A single user (User) can author multiple comments (Comment).
  - The `author_id` field links the Comment model to the User model.
- **One-to-Many with Post**:
  - A single post (Post) can have multiple comments (Comment).
  - The `post_id` field links the Comment model to the Post model.

### Custom Models

**Category Model**

The Category model represents the predefined genres or classifications for blog posts or reviews on Film Buzz. Each category groups related posts to improve organisation, filtering, and discoverability.

- Category Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `category_id`| INTEGER (PK) | Unique identifier for each category      |
|               | `name`       | VARCHAR(20)  | Stores the name of the category (e.g. "Comedy") |

**Relationships**

- **One-to-Many with Post**:
  - A single category can have many posts assigned to it.
  - The `category_id` field is referenced as a foreign key in the Post model.

---

**Watchlist Model**

The Watchlist model represents a personalised list of movies that a user wants to keep track of on Film Buzz. It allows users to save the titles of movies they are interested in watching, creating an organised system for tracking and revisiting their favourite picks or upcoming films.

- Watchlist Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `watchlist_id`| INTEGER (PK) | Unique identifier for each watchlist entry |
| **Foreign Key**| `user_id`    | INTEGER (FK) | Links the watchlist entry to the owning user |
|               | `movie_title`| VARCHAR(30)  | Stores the title of the movie in the watchlist |

**Relationships**

- **One-to-Many with User**:
  - A single user can have multiple movies in their watchlist.
  - The `user_id` field acts as a foreign key linking the Watchlist model to the User model.

---

**Follow Model**

The Follow model represents the social relationship between users on Film Buzz, allowing one user to follow another. This feature fosters community interaction and connection by enabling users to stay updated with posts and activities from those they follow.

- Follow Model

| Key           | Field       | Type         | Purpose                                  |
|---------------|-------------|--------------|------------------------------------------|
| **Primary Key** | `follow_id` | INTEGER (PK) | Unique identifier for each follow relationship |
| **Foreign Key**| `follower_id`| INTEGER (FK) | Links the follower to the User model     |
| **Foreign Key**| `followed_id`| INTEGER (FK) | Links the followed user to the User model |
|               | `created_at` | TIMESTAMP    | Records when the follow relationship was created |

**Relationships**

- **Many-to-Many Self-Referential Relationship**:
  - A user can follow multiple other users, and a user can be followed by multiple users.
  - Implemented using the Follow table, which connects the `follower_id` and `followed_id` fields to the same User model.

---

**FlaggedPost Model**

The FlaggedPost model represents posts on Film Buzz that users or admins have flagged for review. This table tracks flagged posts, the reason for flagging, and the time the flag was created. It enables site administrators to efficiently review and moderate potentially problematic content.

- FlaggedPost Model

| Key           | Field         | Type         | Purpose                                  |
|---------------|---------------|--------------|------------------------------------------|
| **Primary Key** | `flagged_id` | INTEGER (PK) | Unique identifier for each flagged record |
| **Foreign Key**| `post_id`     | INTEGER (FK) | Links the flagged record to the Post model |
|               | `flagged_reason` | VARCHAR(255) | Provides the reason for flagging the post |
|               | `flagged_at`  | TIMESTAMP    | Records when the post was flagged        |

**Relationships**

- **One-to-One with Post**:
  - Each flagged post in the FlaggedPost table corresponds to exactly one post in the Post model.
  - The `post_id` field serves as a foreign key linking the two models.


## Agile Development Process

### MoSCoW Prioritisation

### GitHub Projects 

I used [GitHub Projects](https://github.com/users/raycarter23/projects/3) as an Agile tool to streamline the development process for this project.

The **Kanban Board** provided by GitHub Projects enabled me to:
- Organise tasks according to the development cycle phases: Backlog, To Do, In Progress, and Done
- Map out the workflow for user stories and their implementation
- Visualise the progression of user stories at every stage
- Track progress by moving tasks across columns as they were completed

Here is an overview of my GitHub Projects setup at the beginning of the development process:

![GitHub Project Board](documentation/agile-process/user-stories-stage-1.png)

### GitHub Issues

I used GitHub Issues to create and manage my User Stories.

My User Stories were created using the following template:

- As a **role** I can **capability** so that **received benefit** 

For each user story, I defined its acceptance criteria, and any tasks relating to its completion.

Once I mapped out my user stories, I added them to my GitHub Projects board with their MoSCoW prioritisation labels

Here is what my GitHub issues looked like at the **start** of the initial development process:

![GitHub Issues Part 1](documentation/agile-process/github-issues-p1.png)

![GitHub Issues Part 2](documentation/agile-process/github-issues-p2.png)

![GitHub Issues Part](documentation/agile-process/github-issues-p3.png)

Here is what my GitHub issues looked like at the **end** of the development process:


## Testing 

For detailed information on testing, please see the [TESTING.md](https://github.com/raycarter23/film-buzz/blob/main/TESTING.md) file.

## Deployment

### Connecting to GitHub

To start this project, you will need to create a new GitHub repository using the Code Institute’s Template. This template provides essential configurations and tools to streamline development. 

Follow these steps:
1. **Log In or Sign Up**:
    * Log in to your [GitHub account](https://github.com) or create a new one if you don’t already have an account.
2. **Navigate to the Template**:
    * Open the **CI Full Template** repository provided by Code Institute. You can usually find it at this [link](https://github.com/Code-Institute-Org/ci-full-template).
3. **Use the Template**:
    * Click the Use this template button in the top-right corner of the page and select Create a new repository from the dropdown.
4. **Name Your Repository**:
    * Enter a meaningful name for your repository. Consider using a name that reflects your project (e.g., my-django-project).
    * Optionally, add a description for your repository to clarify its purpose.
5. **Adjust Settings**:
    * Choose whether to make the repository public or private. For most Code Institute projects, the default should be public unless instructed otherwise.
6. **Create the Repository**:
    * Click the Create repository from template button to generate your new repository with all the pre-configured settings.
7. **Verify Your Setup**:
    * Open the repository in your development environment (e.g., Gitpod or VS Code) and ensure the template files have been copied over.

### Django Project Setup

### Cloudinary API

### Heroku Deployment

### Clone Project

### Fork Project

## Tools & Technologies Used 

### Libraries and Frameworks

-
-
-

Additional details can be found in the [requirements.txt](https://github.com/raycarter23/film-buzz/blob/main/requirements.txt) file

### Tools and Programmes 

-
-
-

## Credits

### Content

### Code

### Media

### Acknowledgements
