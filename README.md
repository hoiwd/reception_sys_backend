# Reception_backend

## Overview
### Brief description of what the project does.

- Entities: Guest entity (domain/entities.py)  
- Repositories: Abstract interface + SQLite implementation  
- Read Models: CQRS-lite optimized for querying active or historical guests  
- Services: Orchestrate adding, withdrawing, restoring guests  
- Utils: Validators and helpers 

 ## Architecture
  - Clean Architecture + CQRS-lite.

 ## Features
  - Guest check-in
  - Soft delete (withdraw)
  - Prevent double booking
  - SQLite persistence
  - Read models with indexes

## Project Structure
- Folder tree with explanations:

         *---------------*
         |    main.py    | <-- CLI / API entry point
         *---------------*
                 |
        *-------------------*
        |     Services      | <-- Business use cases
        *-------------------*
          |               |
       Repositories     Read Models
      (write/commands)  (read/queries)
            |            |
            *------------*
            |   SQLite   | <-- Database with soft deletes, 
            *------------*     indexes 
## Database
- Schema overview
- Soft delete strategy
- Partial unique indexes

## Migrations
- How migrations work
- How to reset DB in development

## Tech Stack
- Python
- SQLite
- Clean Architecture
- CQRS-lite

## Upcoming Improvements
- REST API (FastAPI)
- Authentication
- PostgreSQL
  
---

## Requirements

- Python 3.10+  
- SQLite (bundled with Python)  
- Optional: pytest for running tests  

---

## Setup & Usage
- Clone the repo:
`bash
git clone <repo-url>
cd reception_sys# reception_sys_backend
