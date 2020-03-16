Requirements
============

Recommended having **Docker** and **Docker Compose** installed in order to set this project up more easily. If you still don't have it, you can install it through **Snap**:

    ``sudo snap install docker -y``

I built everything using these versions:

- **Docker** 19.03.6
- **docker-compose** 1.23.2

============
Executing
============

Once you got the requirements, execute the following at the project root:

    ``sudo docker-compose up``

You should see everything being set up automatically. It may take some time to download all dependencies. At the end, you should see the server up ready. Try navigating the browsable RESTful API on your browser through this address: http://localhost:80

You can also access the GraphQL API: http://localhost/graphql

Or check the docs: http://localhost/docs

