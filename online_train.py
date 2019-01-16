from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core import utils, train, run
from rasa_core.training import interactive

logger = logging.getLogger(__name__)


def train_agent():
    return train.train_dialogue_model(domain_file="./domain.yml",
                                      stories_file="./data/dialogue/stories.md",
                                      output_path="./models/dialogue/",
                                      policy_config="./policies.yml"
                                      )


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    agent = train_agent()
    interactive.run_interactive_learning(agent, "./data/dialogue/stories.md")
