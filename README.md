# MobileSam Segmentation Model Service

This project provides a FastAPI-based microservice to deploy the MobileSam segmentation model. The service processes image inputs and returns segmentation results. The project is containerized using Docker to ensure easy deployment and scalability.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Testing](#testing)
- [Development](#development)
- [Improvements](#improvements)

## Installation

### Prerequisites

- Docker
- Python 3.8 or higher (for local development)
- `pip` (Python package installer)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Slpn/mobilesam-task.git
   cd mobilesam-task
   ```

2. **Build the Docker image:**

   ```sh
   docker build -t mobilesam-app .
   ```

3. **Run the Docker container:**

   ```sh
   docker run -p 80:80 mobilesam-app
   ```

## Usage

### Running the Service Locally

1. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Start the FastAPI application:**

   ```sh
   uvicorn api:app --reload
   ```

### API Endpoint

Framework : FastApi
Package use:

- **Uvicorn** ASGI server
- **Pillow** Library for manipulating image and use here for convertion

  The service exposes the following endpoint:

#### POST `/segment-image`

- **Description:** Accepts an image file and returns the segmented image.
- **Request:**
  - **File:** `file` (JPEG, JPG, or PNG image)
- **Response:**
  - **Success:** Returns the segmented image as a PNG file.
  - **Error:** Returns a JSON object with an error message.

#### Test

Test by made with unittest and test

- Invalid file
- No file
- None image file

```sh
   python3 test_api/test_api.py
```

**Example Request:**

```sh
curl -X POST -F "file=@path_to_your_image.jpg" http://localhost:80/segment-image --output segmented_img.jpg
```

**_Improvements_**

- **Add Prometheus:** open-source systems monitoring and alerting toolkit for API
- **Add Healthcheck:** Check if the API is running well
