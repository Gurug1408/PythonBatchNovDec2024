import os
from pathlib import Path  # Python 3.6+ only

import dotenv

print(f"{dotenv.find_dotenv() =}")

dotenv.load_dotenv(verbose=True)

print(
    f"""
    {os.getenv('REDIS_ADDRESS')   =}
    {os.getenv('MEANING_OF_LIFE') =}
    {os.getenv('MULTILINE_VAR')   =}

    {os.getenv('S3_BUCKET')       =}
    {os.getenv('SECRET_KEY')      =}

    {os.getenv('server')          =}
    {os.getenv('port')            =}
    {os.getenv('url_format')      =}
    {os.getenv('url')             =}
"""
)