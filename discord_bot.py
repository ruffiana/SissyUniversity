import asyncio
import logging

import sissy_university


def main():
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sissy_university.main.run())


if __name__ == '__main__':
    #main()
    print(dir(sissy_university))
