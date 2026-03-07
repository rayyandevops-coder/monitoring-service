from flask import Flask, jsonify, request
import time
import socket
import logging
import json
from datetime import datetime, timezone

app = Flask(__name__)

start_time = time.time()
request_count = 0


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "event": record.getMessage()
        }
        return json.dumps(log_record)


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route("/health", methods=["GET"])
def health():
    global request_count
    request_count += 1

    logger.info("health_check_requested")

    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/metrics", methods=["GET"])
def metrics():
    global request_count
    request_count += 1

    uptime = int(time.time() - start_time)

    logger.info("metrics_requested")

    return jsonify({
        "uptime_seconds": uptime,
        "request_count": request_count,
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)