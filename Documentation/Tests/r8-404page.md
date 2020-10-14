# Requirement 8 - 404 Page
## R8.1 - For any other requests except the ones above, the system should return a 404 error
Mocking:

N/A

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/nonexistent-page`
- Validate that the resulting page contains the text '404'
- Validate that the resulting page contains the text 'error'
