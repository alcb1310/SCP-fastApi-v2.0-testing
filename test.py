import requests
import test_companies
import test_users
import test_suppliers
import test_projects
import test_budget_items

SERVER = "http://localhost:8000"
END_POINT = "/api/v1.0"

with open("seq.txt", "r") as file:
    seq = int(file.read())
with open("seq.txt", "w") as file:
    next_seq = seq + 1
    file.write(str(next_seq))


test_companies.run_tests(seq)
print("\n-----------------------------------\n")
# test_users.run_tests()
# print("\n-----------------------------------\n")
# test_suppliers.run_tests()
# print("\n-----------------------------------\n")
# test_projects.run_tests()
# print("\n-----------------------------------\n")
# test_budget_items.run_tests()
