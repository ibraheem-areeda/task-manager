# Task Manager  
A simple, deployment-ready Task Management application using Django, Django REST Framework (DRF), and JWT authentication.  

## Setup Instructions  

1. Clone the project from GitHub.  
2. Install Docker on your machine.  
3. Run the following commands in your shell:  

   ```sh
   docker-compose up
   docker-compose exec web python manage.py migrate

4.  Run the following command in your shell to test the application:  
    ```sh
    docker-compose exec web python manage.py test 

5. Run the following command in your shell to create a superuser:  
    ```sh
    docker-compose exec web python manage.py createsuperuser

6. Open your web browser and go to the following URL to access the project on your local machine:  
   **[http://localhost:8000/](http://localhost:8000/)**

# Git Branching Strategy  

In this project, a structured **Git branching strategy** is used to manage development efficiently.  

## Main Branches  
- **`main`** – The stable branch containing production-ready code.  
- **`development`** – The primary branch for active development, where new features and fixes are merged before being pushed to `main`.  

## Feature and Task-Based Branching  
- **Feature branches** (`feature/*`) – Used for developing new functionalities.  
  - Examples: `feature/tasks-details-views`, `feature/users-app`, `feature/task-api`, `feature/task-model`  
- **Frontend branches** – Handle UI-related updates.  
  - Example: `feature/frontend-templates`  
- **Styling branches** – Focus on design improvements.  
  - Example: `styles/basic-styling`  
- **Configuration branches** – Manage Docker and other configurations.  
  - Example: `docker/add-docker-configuration`  
- **Testing branches** – Ensure robust validation.  
  - Example: `tests/tasks-api-test`  

This strategy ensures a clean workflow, allowing parallel development while maintaining code stability.