"""
Middlewares Module

Description:
- This module contains all middlewares used in project.

"""

import logging

from fastapi import HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from openai import error
from pydantic import ValidationError

from .response_message import core_response_message

exception_logger = logging.getLogger(__name__)


async def exception_handling(request: Request, call_next):
    """
    Exception Handling Middleware

    Description:
    - This function is used to handle exceptions.

    Parameter:
    - **request** (Request): Request object. **(Required)**
    - **call_next** (Callable): Next function to be called. **(Required)**

    Return:
    - **response** (Response): Response object.

    """
    print("Calling exception_handling middleware")

    try:
        response: Response = await call_next(request)

    except error.APIError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": core_response_message.API_ERROR},
        )

    except error.APIConnectionError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"detail": core_response_message.API_CONNECTION_ERROR},
        )

    except error.RateLimitError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"detail": core_response_message.RATE_LIMIT_ERROR},
        )

    except error.AuthenticationError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": core_response_message.AUTHENTICATION_ERROR},
        )

    except error.Timeout as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            content={"detail": core_response_message.TIMEOUT},
        )

    except error.InvalidRequestError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": core_response_message.INVALID_REQUEST_ERROR},
        )

    except error.ServiceUnavailableError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"detail": core_response_message.SERVICE_UNAVAILABLE_ERROR},
        )

    except ValidationError as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": core_response_message.INVALID_RESPONSE_BODY},
        )

    except HTTPException as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=err.status_code, content={"message": err.detail}
        )

    except Exception as err:
        exception_logger.exception(msg=err)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": core_response_message.INTERNAL_SERVER_ERROR},
        )

    return response
