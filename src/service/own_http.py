from utils.logger import logger
from utils.common import get_file_name
from constants.constants import VIEWS_URL, HttpResponse


def http_get_handler(request: str) -> str:
    filename = get_file_name(request)
    logger.info("Requested File: " + filename)

    try:
        file = open(VIEWS_URL + filename)
        content = file.read()
        file.close()
        response = HttpResponse.OK + content
    except FileNotFoundError:
        logger.error(f"File: {filename} not found")
        response = HttpResponse.NOT_FOUND + f"File: {filename} not found"
    except Exception as e:
        logger.error(f"Error: {e}")
        response = HttpResponse.INTERNAL_SERVER_ERROR + str(e)
    return response