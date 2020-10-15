# Requirement 8 - 404 Page

**Description**: Redirects to 404 page when the user attempts to access invalid pages. 

## R8.1.1 - For any requests except those in the specification's routes table, the system should return a 404 error (GET, non-existent page)
Mocking:

N/A

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/nonexistent-page`
- Validate that the resulting page contains the text '404'
- Validate that the resulting page contains the text 'error'

## R8.1.2 - For any requests except those in the specification's routes table, the system should return a 404 error (GET on POST-only pages)
Mocking:

N/A

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/sell`
- Validate that the resulting page contains the text '404'
- Validate that the resulting page contains the text 'error'
- Open `/update`
- Validate that the resulting page contains the text '404'
- Validate that the resulting page contains the text 'error'
- Open `/buy`
- Validate that the resulting page contains the text '404'
- Validate that the resulting page contains the text 'error'
