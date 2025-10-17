import logging
import os 
from datetime import datetime
#os.path.dirname(__file__)  当前目录的上一级
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()  # 同时打印到控制台
    ]
)

# 对外暴露 logger
logger = logging.getLogger(__name__)