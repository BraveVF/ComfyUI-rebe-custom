import os

import sentry_sdk
from sentry_sdk import set_tag

from rebe.rebe_enum import RunMode

env = os.getenv("ENV", "dev")

def init_sentry(run_mode: RunMode):
    set_tag("run_mode", run_mode)
    sentry_sdk.init(
        dsn="https://41b37ea55d11b2a4993fbb168fd514d6@o4508636519268352.ingest.us.sentry.io/4508636530671616",
        send_default_pii=True,
        enable_tracing=True,
        environment=env,
        traces_sample_rate=1.0
    )
