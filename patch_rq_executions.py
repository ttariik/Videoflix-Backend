import types
import sys
dummy_module = types.ModuleType("rq.executions")


class DummyExecution:
    pass


dummy_module.Execution = DummyExecution
sys.modules["rq.executions"] = dummy_module
