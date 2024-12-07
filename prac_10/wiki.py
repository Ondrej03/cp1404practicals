"""
CP1404/CP5632 Practical
Wikipedia API
"""

import wikipedia

def main():
    """Prompts user for a page title and prints details"""
    while True:
        user_input = input("Enter a wikipedia page title : ").strip()

        if not user_input:
            break

        get_page_details(user_input)

    print("Thank you")


def get_page_details(title):
    """Gets and prints details of the Wikipedia page"""
    try:
        page = wikipedia.page(title) # second argument : autosuggest=False is marked as error


        # Print the page details
        print(f"TITLE: {page.title}")
        print(f"SUMMARY: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f"Page not found.")


if __name__ == "__main__":
    main()
