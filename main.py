"""
    Main file for project

    Description:
    - This program is main file for project.
    - It is used to create FastAPI object and add all routes to it.

"""

# Importing Python Packages

# Importing FastAPI Packages
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

# Importing Project Files
from core import (
    core_configuration,
    custom_generate_unique_id,
    exception_handling,
    router,
)


# Router Object to Create Routes
app = FastAPI(
    docs_url=core_configuration.DOCS_URL,
    redoc_url=core_configuration.REDOC_URL,
    generate_unique_id_function=custom_generate_unique_id,
    title=core_configuration.PROJECT_TITLE,
    description=core_configuration.PROJECT_DESCRIPTION,
    version=core_configuration.VERSION,
)


# -----------------------------------------------------------------------------


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[core_configuration.CORS_ALLOW_ORIGINS],
    allow_methods=[core_configuration.CORS_ALLOW_METHODS],
    allow_headers=[core_configuration.CORS_ALLOW_HEADERS],
)


# Custom http middleware
app.middleware(middleware_type="http")(exception_handling)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Home page",
    description="This function is used to create root route.",
    response_description="Home page",
    include_in_schema=False,
    tags=["Root"],
)
async def root():
    """
    Root

    Description:
    - This function is used to create root route.

    Parameter:
    - **None**

    Return:
    - **None**

    """

    return RedirectResponse(
        url=app.url_path_for("display_form"),
        status_code=status.HTTP_303_SEE_OTHER,
    )


@app.get(
    path=f"{core_configuration.DOCS_URL}",
    status_code=status.HTTP_200_OK,
    summary="Swagger UI",
    description="This function is used to create swagger UI route.",
    response_description="Swagger UI",
    include_in_schema=False,
    tags=["Documentation"],
)
async def custom_swagger_ui_html():
    """
    Custom Swagger UI HTML

    Description:
    - This function is used to create a custom swagger UI HTML page.

    Parameter:
    - **None**

    Return:
    - **None**

    """

    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(
    path=f"{core_configuration.REDOC_URL}",
    status_code=status.HTTP_200_OK,
    summary="Redoc UI",
    description="This function is used to create redoc UI route.",
    response_description="Redoc UI",
    include_in_schema=False,
    tags=["Documentation"],
)
async def custom_redoc_ui_html():
    """
    Custom Redoc UI HTML

    Description:
    - This function is used to create a custom redoc UI HTML page.

    Parameter:
    - **None**

    Return:
    - **None**

    """

    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


# Add all file routes to app
app.include_router(router)
