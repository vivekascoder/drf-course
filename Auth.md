# Authentication in rest_framework.

## Types of authentication:
- BasicAuth:
  - In this method you need to provide username and password in every single request.
- SessionAuth:
  - In this authentication method you need use `login()` function.
  - It will add a specific cookie in your browser.
- TokenAuth:
  - Based on a user objects a token will be generated.

