from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # You can use Firefox() for Firefox

# Navigate to the webpage containing the <dt> tags
# edge_url = "file:///C:/Users/aravi/Downloads/edge%20favourite.html"
chrome_url = "file:///C:/Users/aravi/Downloads/Chrome%20bookmark.html"
driver.get(chrome_url)
driver.maximize_window()

# Find all <dt> tags
dt_tags = driver.find_elements(By.TAG_NAME,"dt")

# Create a list to store the results
results = []

# Iterate through the <dt> tags
for dt_tag in dt_tags:
    # Find the <a> tag within the <dt> tag
    a_tag = dt_tag.find_element(By.TAG_NAME,"a")

    # Get the href attribute and the text content
    href = a_tag.get_attribute("href")
    content = a_tag.text

    # Append the result to the list
    results.append({"href": href, "content": content})

# Print the results
with open("web.txt", "w", encoding="utf-8") as file:
    for result in results:
        file.write(result["href"] + "*" + result["content"] + "\n")
        # file.write("Content: " + result["content"] + "\n\n")