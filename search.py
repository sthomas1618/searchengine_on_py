from search_engine import SearchEngine

search = SearchEngine()
welcome = "Seach by \"Title\", \"Call Number\", \"Subjects\",  \"Other\" or \"Quit\": "

while True:
    input = raw_input(welcome)
    if input.upper().strip() == "QUIT":
        break

    search_string = raw_input("Please enter a search string: ")

    if input.upper().strip() == "TITLE":
        search.search_by_title(search_string)
    elif (input.upper().strip() == "CALL NUMBER"
            or input.upper().strip() == "CALLNUMBER"):
        search.search_by_call_number(search_string)
    elif (input.upper().strip() == "SUBJECTS"
            or input.upper().strip() == "SUBJECT"):
        search.search_by_subjects(search_string)
    elif input.upper().strip() == "OTHER":
        search.search_by_other(search_string)
