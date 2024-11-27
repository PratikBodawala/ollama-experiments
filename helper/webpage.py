from bs4 import BeautifulSoup
from selenium import webdriver

from helper.utils import cache_tmp


def fetch_text_recursive(element, depth=0, max_depth=2):
    if depth > max_depth:
        return ""

    # Fetch text from the current element and its children
    text = element.getText()
    # for child in element.find_elements_by_xpath('./*'):
    #     text += fetch_text_recursive(child, depth + 1, max_depth)
    return text


@cache_tmp
def fetch_html_content(url: str) -> str:
    driver = webdriver.Chrome()  # Ensure correct path to your WebDriver
    try:
        driver.get(url)

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        root_element = soup.find('body')  # Adjust this if needed

        # Fetch text recursively up to a certain depth
        content_text = fetch_text_recursive(root_element, max_depth=2)
        return content_text.strip()
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Game_of_Thrones"  # Replace with the URL you want to scrape
    text_content = fetch_html_content(url)
    print(text_content)
