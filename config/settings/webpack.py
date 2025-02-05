import os

from config.django.base import BASE_DIR

WEBPACK_LOADER = {
    "DEFAULT": {
        "STATS_FILE": os.path.join(BASE_DIR, "frontend", "webpack-stats.json"),
    },
}
