from ninja_extra import NinjaExtraAPI

from demo_app.api import BookController

api = NinjaExtraAPI(
    version="1.0.0",
    title="Project API",
)

api.register_controllers(BookController)  # <-- register controller
