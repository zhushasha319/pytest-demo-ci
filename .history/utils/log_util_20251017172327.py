import logging
import os
from datetime import datetime

# 定义日志目录
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 定义日志文件名
LOG_FILE = os.path.join(LOG_DIR, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# 获取 logger 对象
logger = logging.getLogger("pytest_demo")
logger.setLevel(logging.INFO)
logger.propagate = False  # 防止重复输出

# 如果没有 handler，再添加（避免重复添加）
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
