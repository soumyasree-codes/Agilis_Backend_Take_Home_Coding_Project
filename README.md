# Transit Schedule API

## Overview

This project is a RESTful API web application for public transit services built using Python 3.9+ and Flask. It provides schedules for upcoming public transit services from an origin station to a destination station.

## Features

- Fetch transit schedules between origin and destination stations.
- Swagger UI for API documentation.
- Containerized using Docker.
- Unit and integration tests.
- Pagination for results.

## Prerequisites

- Python 3.9+
- Docker
- MySQL Database

## Setup

1. **Clone the repository**
    ```sh
    git clone <repository-url>
    cd Agilis_Backend_Take_Home_Coding_Project
    ```

2. **Install dependencies**
    ```sh
    pip3 install -r requirements.txt
    ```

3. **Database Configuration**

    Update the `config/db_config.py` file with your MySQL database credentials.

4. **Run the application**
    ```sh
    python3 app.py
    ```

5. **Run with Docker**

    Build and run the Docker container:
    ```sh
    docker build -t agile-image:subway . 
    docker run -p 5000:5000 --name agile-container agile-image:subway
    ```

## API Documentation

Access the API documentation at `http://localhost:5000/api/docs`.

## Running Tests

1. **Unit Tests**
    ```sh
    python3 -m unittest discover -s tests
    ```

2. **Integration Tests**
    ```sh
    python3 tests/test_integration.py
    ```
3. **Code Coverage Report**
    ```sh
    coverage report -m
    ```

## Endpoints

### Get Transit Schedule

- **URL**: `/transit/schedule`
- **Method**: `GET`
- **Query Parameters**:
    - `origin_station_id` (string, required)
    - `destination_station_id` (string, required)
    - `latitude` (number, required)
    - `longitude` (number, required)
    - `page` (integer, optional, default: 1)
    - `per_page` (integer, optional, default: 10)
- **Response**: 
    ```json
    {
        "next_schedules": [
            {
                "transit_mode": "train",
                "estimated_arrival_origin": "2024-06-01 10:00:00",
                "estimated_arrival_destination": "2024-06-01 12:00:00"
            }
        ]
    }
    ```

## Swagger UI

The Swagger UI documentation can be accessed at `http://localhost:5000/api/docs`.

## Docker Setup

To run the application in a Docker container, follow these steps:

1. **Build the Docker image**
    ```sh
    docker build -t agile-image:subway . 
    ```

2. **Run the Docker container**
    ```sh
    docker run -p 5000:5000 --name agile-container agile-image:subway
    ```

## AWS CloudFormation Template

The project includes an AWS CloudFormation template (`alb-ecs-cluster.yaml`) to set up the necessary AWS infrastructure.
