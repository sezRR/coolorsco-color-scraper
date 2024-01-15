# Coolors Scraper

This project is a web scraping tool that retrieves color codes from the [Coolors website](https://coolors.co/colors) and saves them in JSON format. Additionally, there is an unittest example to verify the accuracy of this tool.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sezRR/coolorsco-color-scraper
    ```

2. Navigate to the project directory:
    ```bash
    cd coolorsco-color-scraper
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

6. Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) and place it in a suitable location on your computer. Then, update the path information in the `webdriver.Chrome()` statement in the `scrape.py` file to point to this location.

7. Run the project:
    ```bash
    python scrape.py
    ```

## Project Structure

- **scrape.py:** The main module that retrieves color information from the website and saves it to JSON files.

## Testing

To run the provided unittest, execute the following command in the terminal or command prompt:

```bash
python test_scrape.py
