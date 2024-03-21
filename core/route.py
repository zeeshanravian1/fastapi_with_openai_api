"""
FastAPI Route module

Description:
- This module is used to create main route for the application.

"""

from fastapi import APIRouter

from apps import blog_router

from .configuration import core_configuration

router = APIRouter(prefix=core_configuration.API_PREFIX)

router.include_router(blog_router)
