from setuptools import setup

# a dummy setup.py used to reserve the name somo on pypi following
# https://stackoverflow.com/questions/47676721/register-an-internal-package-on-pypi

setup(
    name="somogym_fork_vitoria",
    version=open("environments/_version.py").readlines()[-1].split()[-1].strip("\"'"), #assk to change name of this directory
    description="A light framework for the simulation of continuum manipulators",
    long_description="",
    url="git@github.com:vitoriarlima/somogym_fork_vitoria",
    author="Moritz A. Graule",
    author_email="moritz@graule.ch",
    license="unlicense",
    # remember to add all additional submodules to this list
    # packages=["somo", "somo.sweep", "somo.logger"],
    # ASK here if you can refactor the name of this directory because environments might be slightly
    # general, maybe somo_environments would be more suitable
    packages=["environments", "environments.AntipodalGripper", "environments.InHandManipulation",
              "environments.InHandManipulationInverted", "environments.PenSpinner", "environments.PlanarBlockPushing",
              "environments.PlanarReaching", "environments.PlanarReachingObstacle",
              "environments.SnakeLocomotionDiscrete",
              "environments.utils",
              "sample_trajectories"],

    classifiers=["Development Status :: 1 - Planning"],
    package_data={'environments': ['*/benchmark_run_config.yaml',
                                   '*/env_utils/*',
                                   '*/definitions/*',
                                   '*/definitions/additional_urdfs/*',
                                   'general_definitions/plane_urdf/*'],
                  'sample_trajectories': ['*/traj.yaml']
                  },
    include_package_data=True,


)


