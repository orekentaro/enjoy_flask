import logging.config
from common.db import DbConnecter
from common.config import get_config
from common.db import Transaction


class BaseModel():
  def __init__(self):
    # コンフィグファイル読み込み
    self._config = get_config()

    # ログの設定を行う
    logging.config.dictConfig(self._config['log'])
    self._logger = logging.getLogger("app_logger")

    # DBの設定
    db_info = self._config['database']
    self._connector = DbConnecter(
      db_info['dbname'],
      db_info['host'],
      db_info['user'],
      db_info['password']
    )

  def start_transaction(self, read_only=False):
    return Transaction(self._connector, self._logger, read_only)
