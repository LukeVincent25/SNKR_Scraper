import requests
import selenium

# retreive site source code
site = 'https://www.nike.com/launch'
r = requests.get(site)
page_source = r.text
page_source = page_source.split('\n')
print("\nsite: ", site)
print("---------------------------------")

# print page_source contents
check_string = "productId"
for row in page_source:
    #if check_string in row:
    print(row)
    print("")
    print("------------------------")
    print("")

