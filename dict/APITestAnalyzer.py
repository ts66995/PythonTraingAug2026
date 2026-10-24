api_test_results = {
    "Get User API": "Passed",
    "Create User API": "Failed",
    "Update User API": "Passed",
    "Delete User API": "Failed",
    "Login API": "Passed"
}

passedCount = 0
failedCount = 0
for testCase, status in api_test_results.items():
    if status == "Failed":
        print(f"Failed test: {testCase}")
        failedCount += 1
    elif status == "Passed":
        passedCount += 1

print(f"Test cases passed: {passedCount}")
print(f"Failed: {failedCount}")
print(f"Total API test cases: {len(api_test_results)}")
