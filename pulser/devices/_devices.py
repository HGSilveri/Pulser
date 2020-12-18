# Copyright 2020 Pulser Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Definitions of Pasqal's devices."""

from pulser.devices._pasqal_device import PasqalDevice
from pulser.channels import Raman, Rydberg


Chadoq2 = PasqalDevice(
            name="Chadoq2",
            dimensions=2,
            max_atom_num=100,
            max_radial_distance=50,
            min_atom_distance=4,
            _channels=(
                ("rydberg_global", Rydberg.Global(50, 2.5)),
                ("rydberg_local", Rydberg.Local(50, 10, 100)),
                ("rydberg_local2", Rydberg.Local(50, 10, 100)),
                ("raman_local", Raman.Local(50, 10, 100)),
                ),
            )