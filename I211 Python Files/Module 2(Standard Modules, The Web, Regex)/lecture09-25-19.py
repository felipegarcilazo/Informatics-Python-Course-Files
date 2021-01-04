import csv
##data = open("people_header.csv", "r")
##people = list(csv.reader(data))
##for line in people:
##    print(line)


state = input("Search for companies in what states? ")
companies = [[entry["company_name"], entry["web"]] for entry in csv.DictReader(open("companies.csv", "r")) if entry["state"] == state]
companies.sort()
print("-" * 70)
for company in companies:
    print(company[0] + " " * (35 - len(company[0])) + company[1], sep="\t")
