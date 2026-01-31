# SDLC Review: Poster_Wall Project

## This project follows a Waterfall approach, but with iterative improvements typical of Agile approach

## 1. Requirements Analysis
- The project provides a social wall for posting, viewing, and managing tweets with image support.
- Core requirements: user authentication (register, login, logout), CRUD for tweets, image uploads, and a responsive UI.

## 2. Design
- Follows Django’s MVT (Model-View-Template) architecture.
- Models: `Tweet` with user, title, text, photo, timestamps.
- Views: Separate views for listing all tweets, user’s own tweets, create/edit/delete, and registration.
- Templates: Clean separation for layout, tweet list, forms, and registration.
- Uses Tailwind CSS for modern, responsive design.

## 3. Implementation
- Uses Django 6.0, Tailwind CSS, and Pillow for image handling.
- Authentication leverages Django’s built-in system.
- Code is modular: models, forms, views, and templates are well-organized.
- Navigation and UI are user-friendly, with clear separation of user and global tweet views.

## 4. Testing
- Manual testing is evident (based on questions and fixes).
- No automated tests found; consider adding Django unit tests for models, forms, and views for better reliability.

## 5. Deployment
- Uses SQLite for development; can be switched to PostgreSQL/MySQL for production.
- Static/media file handling is set up for local development.
- No deployment scripts or Docker setup found; consider adding for easier production deployment.

## 6. Maintenance
- Code is readable and maintainable, with clear separation of concerns.
- README is professional and provides setup instructions.
- Adding more documentation and automated tests will further improve maintainability.

---

**Strengths:**
- Good use of Django conventions and built-in features.
- Clean UI with Tailwind CSS.
- Clear authentication and user management.

**Areas for Improvement:**
- Add automated tests for reliability.
- Consider Docker or deployment scripts for production.
- Expand documentation for contributors.
