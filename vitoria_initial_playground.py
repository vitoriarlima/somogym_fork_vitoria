from environments.utils.import_handler import import_environment

import gym
import os
import sys
import yaml
from pathlib import Path
from stable_baselines3.common.utils import set_random_seed

total_env_steps=5
from environments.InHandManipulation import InHandManipulation
env_name = "InHandManipulation"

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, path)



run_config_file = (
        Path(os.path.dirname(__file__))
        / "/home/vitoria/Desktop/thesis_project_new1/somogym_fork_vitoria/environments" #"~/environments"
        / env_name
        / "benchmark_run_config.yaml"
    )

with open(run_config_file, "r") as config_file:
    run_config = yaml.safe_load(config_file)



import_environment("InHandManipulation")

env = gym.make(
    run_config["env_id"],
    run_config=run_config,
    run_ID=f"{env_name}-step_test",
    render=True,
    debug=False,
)

run_config["seed"] = 10110
set_random_seed(run_config["seed"])
env.seed(run_config["seed"])
env.reset()

# run env for total_env_steps steps
for _ in range(total_env_steps):
    env.step(env.action_space.sample())  # take a random action
