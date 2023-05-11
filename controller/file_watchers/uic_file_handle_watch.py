from file_watchers.file_watch_handle_base import FileWatchHandleBase

class UicFileWatchHandle(FileWatchHandleBase):
    def __init__(self,watchDir,outDir):
        super().__init__()
        self.watchDir = watchDir
        self.outDir = outDir
        #需要的参数

    def on_moved(self, event):
        super().on_moved(event)

    def on_created(self, event):
        super().on_created(event)

    def on_deleted(self, event):
        super().on_deleted(event)

    def on_modified(self, event):
        super().on_modified(event)

    def on_closed(self, event):
        super().on_closed(event)

    def on_opened(self, event):
        super().on_opened(event)

