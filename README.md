# Malicious Link Detector

A machine learning-based application designed to detect malicious links. This project leverages a dataset of 600,000 values to train a model that can accurately identify potentially harmful URLs.

## Features

- **Machine Learning Model**: Utilizes a robust dataset to train a model capable of detecting malicious links.
- **Flask API**: A RESTful API built using Flask to interface with the machine learning model.
- **Scalable**: Designed to handle large datasets and scalable for deployment in various environments.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/malicious-link-detector.git
    cd malicious-link-detector
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset

The model is trained on a dataset of 600,000 values. Due to the size and sensitivity of the data, the dataset is not included in this repository. You can use your dataset following the structure defined in the code.

## Usage

1. **Run the Flask API**:
    ```bash
    python app.py
    ```

2. **Make a request to the API**:
    - **Endpoint**: `/predict`
    - **Method**: POST
    - **Payload**:
      ```json
      {
          "url": "http://example.com"
      }
      ```

3. **Response**:
    ```json
    {
        "url": "http://example.com",
        "prediction": "malicious"
    }
    ```

## Project Structure

- `app.py`: Main Flask application file.
- `model/`: Directory containing the machine learning model and related scripts.
- `data/`: Placeholder directory for the dataset.
- `static/` and `templates/`: Directories for static files and templates (if applicable).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.

## Contact

For any queries or issues, please contact [your-email@example.com](mailto:your-email@example.com).

---

Feel free to customize this README according to your project's specifics and requirements.