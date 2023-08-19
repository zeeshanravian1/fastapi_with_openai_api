"""
    Blog Route Module

    Description:
    - This module is responsible for handling Blog routes.
    - It is used to get the product details and return the response in HTML
    format.

"""

# Importing Python Packages
import openai

# Importing FastAPI Packages
from fastapi import APIRouter, Request, Form, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Importing Project Files
from core.configuration import core_configuration

# Router Object to Create Routes
router = APIRouter(prefix="/blog", tags=["Blog"])


# -----------------------------------------------------------------------------


templates = Jinja2Templates(directory="static/templates")


def get_product(
    product_name: str | None = Form(None),
    product_info: str | None = Form(None),
) -> dict[str] | None:
    """
    Get product details.

    Description:
    - This method is used to get the product details.

    Parameter:
    - **product_name** (STR): Product name. **(Required)**
    - **product_info** (STR): Product info. **(Required)**

    Return:
    - **response** (DICT): Product details.

    """
    print("Calling get_product method")

    if product_name and product_info:
        return {"name": product_name, "info": product_info}
    return None


@router.get(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Home Page",
    response_description="Return a form to create a single blog",
    response_class=HTMLResponse,
)
async def display_form(request: Request) -> HTMLResponse:
    """
    Return a form to create a single blog.

    Description:
    - This route is used to return a form to create a single blog.

    Parameter:
    - **request** (Request): Request object. **(Required)**

    Return:
    - **response** (HTMLResponse): HTMLResponse object.

    """
    print("Calling display_form method")

    return templates.TemplateResponse(
        "index.html", {"request": request, "product": None}
    )


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a single blog",
    response_description="Blog created successfully",
    response_class=HTMLResponse,
)
async def handle_form(
    request: Request, product: dict[str] | None = Depends(get_product)
) -> HTMLResponse:
    """
    Create a single blog.

    Description:
    - This route is used to create a single blog.

    Parameter:
    - **request** (Request): Request object. **(Required)**
    - **product_name** (STR): Product name. **(Required)**
    - **product_info** (STR): Product info. **(Required)**

    Return:
    - **response** (HTMLResponse): HTMLResponse object.

    """
    print("Calling handle_form method")

    openai.api_key = core_configuration.OPENAI_API_KEY

    system_prompt = "You are a language model have to understand given text in prompt and return answers to the questions from the users"
    user_prompt = f"""
                    Help me write a blog post for the given product below and return me in the form of HTML which i can read and review.
                    The output should be interesting for readers, ready to publish, and ideally following SEO best practices.

                    Product Name: {product["name"]}

                    Product Notes: {product["info"]}
                """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    content = (
        completion.choices[0].message.content.replace("\n", "")
        if completion.choices
        else "No product data received."
    )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "product_content": content, "product": product},
    )
