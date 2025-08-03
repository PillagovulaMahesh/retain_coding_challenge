# CHANGES.md

## Major Issues Identified
- All logic was in a single file (poor separation of concerns).
- No input validation or error handling.
- Insecure handling of user input.
- No modular code or service structure.

## Changes Made
- Split code into `app.py`, `routes.py`, `models.py`, `utils.py`.
- Used Flask blueprints for cleaner routing.
- Added basic validation and status codes.
- Provided dummy in-memory database logic in `models.py`.

## Trade-offs
- Used in-memory list as dummy DB to simplify setup.
- Did not add full authentication due to time constraints.

## AI Usage
- Used ChatGPT to assist with structure and boilerplate.
- Manual review and testing performed after generation.

## With More Time
- Connect to real DB (e.g., SQLite/PostgreSQL).
- Add token-based authentication.
- Implement schema validation with marshmallow or pydantic.
- Add logging and environment configuration.
