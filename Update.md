### Caveat: Route Case Sensitivity

Please note that routes defined in Flask are case-sensitive. Ensure that when accessing the API endpoints, you use the correct casing. For example:

- The correct route to access document search is `/api/search/document`.
- Using `/api/search/Document` will result in a 404 Not Found error.

This distinction is crucial to ensure that the API endpoints work as expected.
