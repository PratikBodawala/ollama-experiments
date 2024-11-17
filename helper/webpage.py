from selenium import webdriver
from bs4 import BeautifulSoup

def fetch_text_recursive(element, depth=0, max_depth=2):
    if depth > max_depth:
        return ""

    # Get text from the current element and its children
    text = element.get_attribute('innerText')
    for child in element.find_elements_by_xpath('./*'):
        text += fetch_text_recursive(child, depth + 1, max_depth)
    return text

def fetch_html_content(url: str) -> str:
    # Set up the WebDriver (make sure the path to your driver is correct)
    driver = webdriver.Chrome()  # Update this path
    try:
        driver.get(url)

        # Fetch the entire page source
        html_source = driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')

        # Recursive function to fetch text up to a certain depth
        root_element = soup.find('body')  # You can change this to any element you want as the starting point
        content_text = fetch_text_recursive(root_element, max_depth=1)  # Set your desired depth

        return content_text.strip()
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Game_of_Thrones"  # Replace with the URL you want to scrape
    text_content = fetch_html_content(url)
    print(text_content)
