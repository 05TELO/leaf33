import logging

import colorlog
from gunicorn.glogging import Logger


class CustomGunicornLogger(Logger):
    def setup(self, cfg):
        super().setup(cfg)

        access_logger = logging.getLogger("gunicorn.access")

        formatter = colorlog.ColoredFormatter(
            "%(asctime)s [%(log_color)s%(levelname)s%(reset)s] %(message)s"
        )

        if self.cfg.accesslog:
            self._set_handler(access_logger, self.cfg.accesslog, fmt=formatter)
        else:
            self._set_handler(access_logger, "-", fmt=formatter)

        error_logger = logging.getLogger("gunicorn.error")
        error_logger.handlers[0].setFormatter(formatter)
