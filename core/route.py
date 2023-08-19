"""
    FastAPI Route module

    Description:
    - This module is used to create main route for the application.

"""

# Importing Python Packages

# Importing FastAPI Packages
from fastapi import APIRouter

# Importing Project Files
from apps import blog_router
from .configuration import core_configuration


# Router Object to Create Routes
router = APIRouter(prefix=core_configuration.API_PREFIX)


# -----------------------------------------------------------------------------


# Include all file routes
router.include_router(blog_router)
