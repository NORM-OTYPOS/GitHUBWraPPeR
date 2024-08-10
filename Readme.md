# GitHub Wrapper

## Description

GitHub Wrapper is a web application designed to generate comprehensive reports based on GitHub profiles. Users can input their GitHub profile URL or connect their GitHub account to receive a detailed report evaluating their tech stack, experience, and repository impact. The application provides a downloadable PDF report with a scoring system across these areas.

## Features

- **GitHub Profile Input**: Users can drop their GitHub profile URL or connect their GitHub account.
- **Automatic Report Generation**: Generate a detailed report evaluating tech stack, experience, and repository impact.
- **PDF Download**: Download the report as a PDF.
- **Advanced Analysis**: Utilizes Hugging Face models for in-depth analysis and improved user experience.

## Technologies

- **Frontend**: React with TypeScript
- **Backend**: Python FastAPI
- **PDF Generation**: Integrated PDF generation for reports
- **Hugging Face Models**: For advanced analysis

## Directory Structure

### Frontend
```plaintext
frontend
├── public
│   └── index.html
├── src
│   ├── components
│   │   ├── Dashboard.tsx
│   │   ├── ProfileInput.tsx
│   │   └── ReportCard.tsx
│   ├── hooks
│   │   └── useGithubProfile.ts
│   ├── pages
│   │   ├── Home.tsx
│   │   └── Report.tsx
│   ├── services
│   │   └── api.ts
│   ├── App.tsx
│   ├── index.tsx
│   └── styles.css
├── package.json
├── tsconfig.json
└── Dockerfile

### Backend
```plaintext
backend
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services
│   │   ├── github_service.py
│   │   └── pdf_service.py
│   ├── utils.py
│   ├── test_model.py
│   ├── test_routes.py
│   └── test_services.py
├── requirements.txt
└── Dockerfile

## Setup and Installation

### Prerequisites

- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **Docker** (for containerized deployment)

### Frontend Setup

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm start
    ```

### Backend Setup

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

### Docker Setup

To build and run the application using Docker, follow these steps:

1. **Build and Run Containers:**

    ```bash
    docker-compose up --build
    ```

2. Access the frontend at `http://localhost:3000` and the backend API at `http://localhost:8000`.

## Usage

1. Open the frontend application in your web browser.
2. Enter your GitHub profile URL or connect your GitHub account.
3. Generate and download the report.

## Note
remember that the project is still in development face, it has not been completed completely, and just the basic idea as to how the project could procced in the future.

## Contributing
Feel free to submit issues and pull requests. Contributions are welcome!