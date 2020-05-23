import requests
from loguru import logger


def contributions():
    """Get my GitHub contributions for the last year

    Returns:
        Dictionary -- Contribution contents
    """
    request = requests.get(
        'https://github-contributions-api.now.sh/v1/Matt-Gleich', params={'format': 'nested'})
    if request.status_code != 200:
        logger.error('Failed to get GitHub Contributions')
    logger.info('Got GitHub Contributions')
    return request.json()
