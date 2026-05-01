# Copyright 2026 llm-d
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import sub-modules to trigger registration side-effects
from .handlers import generic as generic_handlers  # noqa: F401
from .handlers.generic import SimpleFilter as SimpleFilter
from .handlers.generic import SingleProfileHandler as SingleProfileHandler
from .pickers import generic as generic_pickers  # noqa: F401
from .pickers.generic import MaxScorePicker as MaxScorePicker
from .pickers.generic import RandomPicker as RandomPicker
from .scorers import backpressure as backpressure
from .scorers import generic as generic
from .scorers import prefix_plugin as prefix_plugin
from .scorers.backpressure import (
    KVCacheScorer as KVCacheScorer,
)
from .scorers.backpressure import (
    LeastQueueScorer as LeastQueueScorer,
)
from .scorers.backpressure import (
    QueueLengthScorer as QueueLengthScorer,
)
from .scorers.backpressure import (
    RunningQueueScorer as RunningQueueScorer,
)
from .scorers.backpressure import (
    WaitingQueueScorer as WaitingQueueScorer,
)
from .scorers.generic import ConstantScorer as ConstantScorer
from .scorers.generic import RoundRobinScorer as RoundRobinScorer

# Re-export key plugins if needed, but registry handles dynamic lookup
from .scorers.prefix_plugin import PrefixCacheScorer as PrefixCacheScorer
