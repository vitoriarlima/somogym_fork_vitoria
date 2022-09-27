import os, sys
import pdb

import pytest
import yaml

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, path)
# print(path)
# print(sys.path.insert(0, path))
from pathlib import Path
from sample_trajectories.run_traj import gen_expert_data as run_traj


env_name = "InHandManipulation"
run_config_file = (
        Path(os.path.dirname(__file__))
        / "../somogym_fork_vitoria/environments"
        / env_name
        / "benchmark_run_config.yaml"
)

# pdb.set_trace()

with open(run_config_file, "r") as config_file:
    run_config = yaml.safe_load(config_file)

# print(run_config)
# /home/vitoria/Desktop/thesis_project_new1/somogym_fork_vitoria/environments/InHandManipulation/benchmark_run_config.yaml

run_config["expert_name"] = "InHandManipulation-gaiting" #traj_name

run_traj(
    env_name,
    run_config,
    num_steps=1000,
    run_render=True,
    debug=False,
    record_data=False,
)