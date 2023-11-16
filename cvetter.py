import requests
from googletrans import Translator
from termcolor import colored

def search_cve(cve_number, lang='en'):
    try:
        base_url = "https://services.nvd.nist.gov/rest/json/cve/1.0/"
        search_url = f"{base_url}{cve_number}"

        response = requests.get(search_url)

        if response.status_code == 200:
            cve_data = response.json()

            if 'result' in cve_data and 'CVE_Items' in cve_data['result']:
                for cve_item in cve_data['result']['CVE_Items']:
                    cve_description = cve_item['cve']['description']['description_data'][0]['value']
                    translator = Translator()
                    translation = translator.translate(cve_description, dest=lang)

                    print(f"CVE Number: {cve_number}")
                    print("Description (Original):", colored(cve_description, 'yellow'), '\n')
                    print("Description (Translated):", colored(translation.text, 'green'), '\n')
            else:
                print(f"CVE Number {cve_number} not found in the NVD database.")
        else:
            print(f"Error: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    cve_number = input("Enter CVE Number: ").strip()

    if not cve_number.startswith("CVE-"):
        print("Invalid CVE Number format. It should start with 'CVE-'.")
        return

    lang = input("Enter language code for translation (e.g., 'tr' for Turkish): ").strip().lower()

    search_cve(cve_number, lang)

if __name__ == "__main__":
    main()
