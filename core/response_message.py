"""
    Core Response Message Module

    Description:
    - This module is responsible for core response messages.

"""

# Importing Python Packages

# Importing FastAPI Packages

# Importing Project Files


# -----------------------------------------------------------------------------


class CoreResponseMessage:
    """
    Core Response Message Class

    Description:
    - This class is used to define core response messages.

    """

    API_ERROR: str = "OpenAI API returned an API Error"
    API_CONNECTION_ERROR: str = "Failed to connect to OpenAI API"
    RATE_LIMIT_ERROR: str = "OpenAI API request exceeded rate limit"
    AUTHENTICATION_ERROR: str = "OpenAI API authentication failed"
    TIMEOUT: str = "OpenAI API request timed out"
    INVALID_REQUEST_ERROR: str = "OpenAI API request is invalid"
    SERVICE_UNAVAILABLE_ERROR: str = "OpenAI API service is unavailable"

    INVALID_RESPONSE_BODY: str = "Invalid response body"
    INTERNAL_SERVER_ERROR: str = "Internal server error"


core_response_message = CoreResponseMessage()
