import os

# Channel layer configuration for Channels app (used for WebSocket communication between several instances of DISPUTool)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.environ.get("REDIS_HOST", default="broker"), os.environ.get("REDIS_PORT", default=6379))],
            "capacity": 1500,
            "expiry": 10,
        },
    },
}

CHANNELS_ROOT_URLCONF = "config.routing"
