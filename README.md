# PDF Maker 📝

Just a small project to practice using the FPDF Python library and object-oriented programming principles.

## About The Project

This script generates a custom lined PDF notebook from a simple CSV file. Each row in the CSV defines a topic section and the number of pages it should have. The project is structured using Object-Oriented Programming (OOP) to separate concerns:

* **Data Handling**: A dedicated class reads and parses the input file.
* **PDF Generation**: A dedicated class handles all PDF creation logic (adding pages, headers, footers, and lines).
* **Orchestration**: A main script coordinates the data reader and the PDF generator.

Key libraries used:
* [fpdf2](https://github.com/py-pdf/fpdf2/)
* [Pandas](https://pandas.pydata.org/)

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.8+ and pip installed.

* **Python Installation**
    * [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Installation

1.  **Clone the repository** (or download the files to a local directory).
    ```sh
    git clone https://github.com/GustavoSantosgcs/PDF_Maker.git
    cd pdfMaker
    ```

2.  **Create a `requirements.txt` file** in the project's root directory with the following content:
    ```txt
    fpdf2
    pandas
    ```

3.  **Install the required packages** using pip:
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

To generate your PDF notebook, follow these steps:

1.  **Customize the input file**
    Create or edit the `topics.csv` file in the root directory. It must contain two columns: `Topic` and `Pages`.

    **Example `topics.csv`:**
    ```csv
    Topic,Pages
    Scrum,3
    Python Basics,5
    Object-Oriented Programming,4
    ```

2.  **Run the main script**
    Execute the `main.py` script from your terminal:
    ```sh
    python main.py
    ```

3.  **Find your file**
    The script will generate an `output.pdf` file in the same directory, which is your custom-lined notebook.

---

## Project Structure

The project is organized into the following files:

```
pdfMaker/
├── main.py             # The main script that runs the application
├── PDFGenerator.py     # Class responsible for generating the PDF
├── topics.py           # Class responsible for reading the input CSV
├── topics.csv          # The input data file with topics and page counts
└── requirements.txt    # Lists the project dependencies

```

---

## Acknowledgments

This project was developed as a practice exercise following the instructions from the Udemy course: **[Learn Python from Beginner to Pro. Build 20 Real-World Apps with Python Including AI Agents with LangChain](https://www.udemy.com/course/your-course-link-here/)**.

This application is one of several real-world projects from the course designed to solidify Python programming concepts.