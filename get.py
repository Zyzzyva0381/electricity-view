import time
from selenium import webdriver


def main(building, floor, room, wait_time=5):
    driver = webdriver.Chrome()
    url = "http://172.27.2.95:8899/query/"

    driver.get(url)
    time.sleep(wait_time)
    driver.execute_script("document.getElementById('ks-component7540').setAttribute('class', 'ks-overlay');")
    time.sleep(wait_time)
    driver.execute_script(f"const button = document.querySelector('[title=\"{building}\"]');"
                          "button.click();")
    time.sleep(wait_time)
    driver.execute_script(f"const button = document.querySelector('[title=\"{floor}\"]');"
                          "button.click();")
    time.sleep(wait_time)
    driver.execute_script(f"const button = document.querySelector('[title=\"{room}\"]');"
                          "button.click();")
    time.sleep(wait_time)
    result = driver.execute_script("const element = document.getElementById('J_remain');"
                                   "return element.value;")
    driver.quit()
    return result


if __name__ == "__main__":
    results = main("基础实验楼", "第3层", "乙303物理学院")
    print(results)
