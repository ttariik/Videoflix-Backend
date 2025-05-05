from rq_win.worker import WindowsWorker as BaseWindowsWorker


class PatchedWindowsWorker(BaseWindowsWorker):
    def __init__(self, *args, worker_ttl=None, **kwargs):
        if 'worker_ttl' in kwargs:
            del kwargs['worker_ttl']
        super().__init__(*args, **kwargs)
