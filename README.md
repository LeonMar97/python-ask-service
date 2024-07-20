# Flask OpenAI Question Service

This application provides a REST API that allows users to send questions to OpenAI and receive answers. The questions and answers are stored in a PostgreSQL database. The application and database are set up in separate containers using Docker Compose, with the Flask app defined by a Dockerfile.

## Features


- **POST /ask**: Sends a question to OpenAI and retrieves the answer.
- **GET /ping**: Checks the connectivity of the application.
- **GET /questions**: Checks the persistence of the questions in the PostgreSQL database.

## Prerequisites

- **Docker**: To build and run containers.
- **Docker Desktop**: Required for Windows users.

## Environment Configuration

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY='your_openai_api_key'
DBNAME='postgres'
USER='postgres'
PASSWORD='your_secure_password'
PORT='5432'
HOST=db_service
DATABASE_URL=postgresql+psycopg2://${USER}:${PASSWORD}@${HOST}:${PORT}/${DBNA.ME} 
```
## Running the Application

1. Ensure you have Docker and Docker Desktop installed.

2. Create a .env file with the necessary environment variables (see above).

3. Navigate to the root directory of your project.

4. Run the following command to start the application and database:
```bash
docker-compose up
 ```
 
## Local Development

If you want to run the application locally without Docker:
Ensure you have Python and Poetry installed.
Create a .env just like before, but change the host to local:

### in .env
    HOST=localhost

<b style="color: red;">!!dont forget to add password and port aswell!!
</b>   

run:
```bash
make install
make run 
  ```
## Testing

There is a testing library included to run tests. You can run the tests using the following command:
```bash
make test
```