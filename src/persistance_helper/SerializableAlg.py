from typing import Optional

from persistance_helper.PersistHelper import PersistHelper
from persistance_helper.Version import Version


class SerializableAlg(object):

    class Config(object):
        def __init__(self, version: str = None):
            super().__init__()
            if version is None:
                version = self.get_latest_version()
            if isinstance(version, Version):
                version = str(version)
            self.version = version

        @classmethod
        def get_latest_version(cls):
            return Version(0, 1, 0)

    def __init__(self, config: Optional[Config] = None):
        super().__init__()
        config = config if config is not None else self.Config()
        self.config = config

    class PersistConfig(object):
        def __init__(self, filename: Optional[str] = None):
            super().__init__()
            self.filename = filename if filename is not None else self.get_default_filename()

        @classmethod
        def get_default_filename(cls):
            return 'SerializableAlg.json'

    def save_config(self, folder_path, persist_config: PersistConfig = None):
        if persist_config is None:
            persist_config = self.PersistConfig()
        PersistHelper.save_object_to_json(self.config,
                                          path=PersistHelper.merge_paths([folder_path, persist_config.filename]))

    @classmethod
    def load_config(cls, folder_path, persist_config: PersistConfig = None):
        if persist_config is None:
            persist_config = cls.PersistConfig()
        return PersistHelper.load_json_to_object(
            path=PersistHelper.merge_paths([folder_path, persist_config.filename])
        )
