# Problem 4 - REST API

## Objective
The goal is to build a REST API that provides weather data and weather statistics, allowing clients to filter by date and station ID, with data being paginated. The API also includes a Swagger/OpenAPI endpoint for automatic documentation.

## Technologies Used
- **Django**: For building the web framework.
- **Django REST Framework (DRF)**: For creating the API endpoints.
- **drf-yasg**: For generating the Swagger/OpenAPI documentation.
- **PostgreSQL**: For the database to store weather data and statistics.

## API Endpoints
The following endpoints are implemented:

1. **`/api/weather/`**
   - Returns ingested weather data from the database.
   - Allows filtering by station ID and date using query parameters.
   - Data is paginated.

   Example: `GET /api/weather/?station=USC001&date=2022-01-01`

2. **`/api/weather/stats/`**
   - Returns the aggregated weather statistics (average temperatures and total precipitation).
   - Allows filtering by station ID and year using query parameters.
   - Data is paginated.

   Example: `GET /api/weather/stats/?station=USC001&year=2022`

3. **`/swagger/`**
   - Provides the OpenAPI documentation for the API.
   - This is generated using `drf-yasg`.

## Setup Instructions

1. **Install Dependencies**
   Ensure that you have all the required Python libraries installed. Run the following command inside the virtual environment:
   ```bash
   pip install -r requirements.txt
