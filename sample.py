from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def element_exists(driver, by):
    try:
        element = driver.find_element(*by)
        return element.is_displayed()
    except Exception:
        return False

def is_page_working(driver):
    return element_exists(driver, (By.XPATH, "//*[@id='__next']/div[1]/div[5]/div[1]"))

def main():
    url = "https://luxunlock-frontend.vercel.app/"

    locations = ["India", "Sri Lanka", "Tamil Nadu", "Mahabalipuram", "Ernakulam", "Nilgiris", "Western Ghats",
                 "Kodaikanal", "Marakkanam", "Gujarat", "Chettinad", "Southern Tamil Nadu",
                 "Ooty", "Sayalgudi", "Ahmedabad", "Alamparai Coast", "Coromandel Coast",
                 "Coonoor", "Tharangambadi", "Karnataka", "Gulf of Mannar", "Tranquebar",
                 "Tirupugalur", "Kerala", "Suntikoppa", "Cochin Backwaters", "Karaikudi",
                 "Wayanad", "Pondicherry", "Cauvery Delta", "Galle Coast"]

    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//div[text()='DESTINATIONS']").click()

        for location in locations:
            clicked = False

            if element_exists(driver, (By.XPATH, f"//b[text()='{location}']")):
                driver.find_element(By.XPATH, f"//b[text()='{location}']").click()
                time.sleep(0.5)
                clicked = True

            if not clicked and element_exists(driver, (By.XPATH, f"//a[text()='{location}']")):
                driver.find_element(By.XPATH, f"//a[text()='{location}']").click()
                time.sleep(0.5)
                clicked = True

            if clicked:
                if is_page_working(driver):
                    print(f"{location} destination page is working.")
                else:
                    print(f"{location} destination page is not working.")
                
                driver.find_element(By.XPATH, "//div[text()='DESTINATIONS']").click()
                time.sleep(0.5)
            else:
                print(f"{location} destination link not found.")

    except Exception as e:
        raise RuntimeError(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
