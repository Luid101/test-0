test-0
------

The following are simple tests to Shopper Army job posting. Extra details such as folder structure, coding style, and more that's not mentioned here are up to you.

- [x] Fork this repository to your GitHub account - both frontend and backend should be placed in the same repo
- [x] [Python, backend] Create a django project directory (LTS version only)
- [x] Create a `Member` model referencing or extending django's `User` model - add `gender` and `country` field
- [x] Create a command that creates a `Member` object which contains required and/or optional arguments
- [x] [Node.js, frontend] Create a vue project directory
- [x] Create a vue form component for adding a `Member` - use bootstrap or vuetify for UI (added as dependency)
- [x] When done, create a pull request to `submit-0` branch


Optional
--------

- [ ] Lock all dependencies
- [x] Implement `django-rest-framework` or `GraphQL` - tie in both frontend and backend using this
- [ ] Implement `elasticsearch` - index `Member` objects
- [ ] Implement `celery` - `Member` creation to be run by worker
- [x] Implement `docker` / `docker-compose` to simultaneously launch frontend and backend (along with DB, if applicable)

Running Instructions
--------------------

* Install docker and docker-compose
* Start a docker swarm, with "sudo docker swarm init --advertise-addr {available ip, press tab to see them}"
* Run ./shopperarmy/docker_start to start both the backend and frontend with docker
* Go to "http://localhost:8080/" to view the vue.js app.
* Go to "http://localhost:8070/" to view the Django REST framework.
