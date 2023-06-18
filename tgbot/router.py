from aiogram import Router
from .handlers import default_router

module_router = Router()
module_router.include_router(default_router)