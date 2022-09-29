
from environments.utils.import_handler import import_environment
import gym

from stable_baselines3 import PPO

import gym
import os
import sys
import yaml
from pathlib import Path
from stable_baselines3.common.utils import set_random_seed
import pdb


env_name = "InHandManipulation"
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../somo-rl_fork_vitoria"))
sys.path.insert(0, path)

run_config_file = (
        Path(os.path.dirname(__file__))
        / "/home/vitoria/Desktop/thesis_project_new1/somogym_fork_vitoria/environments" #"~/environments"
        / env_name
        / "benchmark_run_config.yaml"
    )

with open(run_config_file, "r") as config_file:
    run_config = yaml.safe_load(config_file)

# pdb.set_trace()

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
# env.reset()


model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

obs = env.reset()

for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()

env.close()
