# Copyright (c) 2019-2023, NVIDIA CORPORATION.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from cugraph.utilities.api_tools import deprecated_warning_wrapper
from cugraph.link_prediction.jaccard import jaccard
from cugraph.link_prediction.jaccard import jaccard_coefficient
from cugraph.link_prediction.overlap import overlap
from cugraph.link_prediction.wjaccard import jaccard_w

jaccard_w = deprecated_warning_wrapper(jaccard_w)
from cugraph.link_prediction.woverlap import overlap_w

overlap_w = deprecated_warning_wrapper(overlap_w)
from cugraph.link_prediction.wsorensen import sorensen_w

sorensen_w = deprecated_warning_wrapper(sorensen_w)
from cugraph.link_prediction.jaccard import jaccard_coefficient
from cugraph.link_prediction.sorensen import sorensen_coefficient
from cugraph.link_prediction.sorensen import sorensen
from cugraph.link_prediction.overlap import overlap_coefficient
