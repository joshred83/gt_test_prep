question_gatech_MDP_1_1 = {
    'question': (
        'Which of the following is NOT a challenge of reinforcement learning as defined in the lectures? (Probability of appearing on test: 0.894)'
    ),
    'options_list': [
        'A. Reward functions for actions that were not taken',
        'B. Long-term planning for delayed rewards',
        'C. Non-stationary data distributions caused by policy updates',
        'D. Requirement of a labeled dataset for reward predictions'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Reinforcement learning does not rely on labeled datasets for training; instead, it uses evaluative feedback in the form of rewards for actions taken. Challenges include trial and error (A), the need for long-term planning due to delayed rewards (B), and the non-stationarity caused by changing policies (C).'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_2 = {
    'question': (
        'In the context of Markov Decision Processes (MDPs), which statement is FALSE? (Probability of appearing on test: 0.906)'
    ),
    'options_list': [
        'A. The Markov property implies that the next state depends only on the current state and action.',
        'B. The reward distribution R(s,a,s′) is assumed to be known in reinforcement learning.',
        'C. A policy can be deterministic or stochastic.',
        'D. The discount factor γ assigns more weight to earlier rewards than to later ones.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In reinforcement learning, the reward distribution is not known beforehand. Instead, the agent observes samples of rewards during interactions with the environment. Statements A, C, and D accurately reflect the properties of MDPs.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_3 = {
    'question': (
        'What is the primary reason dynamic programming methods are difficult to apply directly to reinforcement learning problems? (Probability of appearing on test: 0.890)'
    ),
    'options_list': [
        'A. The reward functions are known.',
        'B. Transition functions are linear in reinforcement learning.',
        'C. State and action spaces are often prohibitively large.',
        'D. Policies do not require iterative refinement.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Dynamic programming requires looping over all possible states and actions, which becomes computationally infeasible for problems with very large state or action spaces. Options A and B are incorrect since the reward and transition functions are not typically known in reinforcement learning. D is incorrect because policies are refined iteratively.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_4 = {
    'question': (
        'Which of the following correctly describes the relationship between a policy π and the Q-function Qπ(s,a)? (Probability of appearing on test: 0.878)'
    ),
    'options_list': [
        'A. The Q-function is independent of the policy.',
        'B. The policy can be derived from the Q-function by selecting actions with the lowest values at each state.',
        'C. The Q-function represents the expected sum of discounted rewards when following policy π after taking action a at state s.',
        'D. The Q-function can only be used with deterministic policies.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The Q-function Qπ(s,a) quantifies the expected discounted rewards starting from a state s, taking an action a, and then following the policy π. A is incorrect because the Q-function depends on the policy. B is wrong because actions with the highest (not lowest) Q-values are preferred. D is false because Q-functions are applicable to both deterministic and stochastic policies.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_6 = {
    'question': (
        'True or False: Dynamic programming methods for MDPs, such as value iteration, assume that the transition and reward distributions are known. (Probability of appearing on test: 0.924)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Dynamic programming algorithms like value iteration rely on complete knowledge of the transition and reward distributions to compute exact policy updates.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_7 = {
    'question': (
        'True or False: The discount factor γ can take values greater than 1 if the reward distribution favors long-term rewards. (Probability of appearing on test: 0.841)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The discount factor γ must lie between 0 and 1, ensuring that future rewards are weighted less than or equal to current rewards. A γ > 1 would cause instability by disproportionately amplifying future rewards.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_8 = {
    'question': (
        'True or False: Policy gradients involve the direct optimization of the policy’s parameters to maximize expected rewards. (Probability of appearing on test: 0.945)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Policy gradient methods explicitly compute the gradient of the expected reward with respect to the policy\'s parameters, allowing direct optimization.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_1_9 = {
    'question': (
        'True or False: The exploration-exploitation tradeoff requires balancing between selecting actions with the highest known rewards and trying new actions to discover potentially better rewards. (Probability of appearing on test: 0.708)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Exploration enables the agent to learn about potentially better actions, while exploitation focuses on maximizing the rewards based on current knowledge.'
    ),
    'chapter_information': 'gatech MDP lecture'
}


# question_gatech_MDP_1_1 = {
#     'question': (
#         'Which of the following is NOT a challenge of reinforcement learning as defined in the lectures? (Probability of appearing on test: 0.894)'
#     ),
#     'options_list': [
#         'A. Reward functions for actions that were not taken',
#         'B. Long-term planning for delayed rewards',
#         'C. Non-stationary data distributions caused by policy updates',
#         'D. Requirement of a labeled dataset for reward predictions'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'Reinforcement learning does not rely on labeled datasets for training; instead, it uses evaluative feedback in the form of rewards for actions taken. Challenges include trial and error (A), the need for long-term planning due to delayed rewards (B), and the non-stationarity caused by changing policies (C).'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_2 = {
#     'question': (
#         'In the context of Markov Decision Processes (MDPs), which statement is FALSE? (Probability of appearing on test: 0.906)'
#     ),
#     'options_list': [
#         'A. The Markov property implies that the next state depends only on the current state and action.',
#         'B. The reward distribution R(s,a,s′) is assumed to be known in reinforcement learning.',
#         'C. A policy can be deterministic or stochastic.',
#         'D. The discount factor γ assigns more weight to earlier rewards than to later ones.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'In reinforcement learning, the reward distribution is not known beforehand. Instead, the agent observes samples of rewards during interactions with the environment. Statements A, C, and D accurately reflect the properties of MDPs.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_3 = {
#     'question': (
#         'What is the primary reason dynamic programming methods are difficult to apply directly to reinforcement learning problems? (Probability of appearing on test: 0.890)'
#     ),
#     'options_list': [
#         'A. The reward functions are known.',
#         'B. Transition functions are linear in reinforcement learning.',
#         'C. State and action spaces are often prohibitively large.',
#         'D. Policies do not require iterative refinement.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Dynamic programming requires looping over all possible states and actions, which becomes computationally infeasible for problems with very large state or action spaces. Options A and B are incorrect since the reward and transition functions are not typically known in reinforcement learning. D is incorrect because policies are refined iteratively.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_4 = {
#     'question': (
#         'Which of the following correctly describes the relationship between a policy π and the Q-function Qπ(s,a)?'
#     ),
#     'options_list': [
#         'A. The Q-function is independent of the policy.',
#         'B. The policy can be derived from the Q-function by selecting actions with the lowest values at each state.',
#         'C. The Q-function represents the expected sum of discounted rewards when following policy π after taking action a at state s.',
#         'D. The Q-function can only be used with deterministic policies.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'The Q-function Qπ(s,a) quantifies the expected discounted rewards starting from a state s, taking an action a, and then following the policy π. A is incorrect because the Q-function depends on the policy. B is wrong because actions with the highest (not lowest) Q-values are preferred. D is false because Q-functions are applicable to both deterministic and stochastic policies.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }



# question_gatech_MDP_1_6 = {
#     'question': (
#         'True or False: Dynamic programming methods for MDPs, such as value iteration, assume that the transition and reward distributions are known.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Dynamic programming algorithms like value iteration rely on complete knowledge of the transition and reward distributions to compute exact policy updates.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_7 = {
#     'question': (
#         'True or False: The discount factor γ can take values greater than 1 if the reward distribution favors long-term rewards.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The discount factor γ must lie between 0 and 1, ensuring that future rewards are weighted less than or equal to current rewards. A γ > 1 would cause instability by disproportionately amplifying future rewards.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_8 = {
#     'question': (
#         'True or False: Policy gradients involve the direct optimization of the policy’s parameters to maximize expected rewards.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Policy gradient methods explicitly compute the gradient of the expected reward with respect to the policy\'s parameters, allowing direct optimization.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_1_9 = {
#     'question': (
#         'True or False: The exploration-exploitation tradeoff requires balancing between selecting actions with the highest known rewards and trying new actions to discover potentially better rewards.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Exploration enables the agent to learn about potentially better actions, while exploitation focuses on maximizing the rewards based on current knowledge.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }


# question_gatech_MDP_2_1 = {
#     'question': (
#         'Which of the following statements about reinforcement learning and MDPs is least correct?'
#     ),
#     'options_list': [
#         'A. Reinforcement learning uses trial and error to find optimal actions.',
#         'B. MDPs assume the Markov property holds true.',
#         'C. Evaluative feedback ensures the agent knows the best action at every state.',
#         'D. Delayed rewards can complicate learning in reinforcement learning.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Evaluative feedback provides rewards for actions taken but does not give explicit information about the best action. The agent must discover the best action through trial and error.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_2 = {
#     'question': (
#         'In the context of reinforcement learning, which of the following scenarios exemplifies "evaluative feedback"?'
#     ),
#     'options_list': [
#         'A. An agent receives a labeled dataset with optimal actions.',
#         'B. An agent receives a delayed reward after completing a task.',
#         'C. An agent uses a predefined policy to determine actions.',
#         'D. An agent performs random actions without receiving any reward.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Evaluative feedback refers to rewards based on the outcome of actions taken, which can include delayed rewards. Option B captures this concept best.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_3 = {
#     'question': (
#         'Consider the Bellman equation for value iteration. Which modification would not affect the time complexity of the algorithm?'
#     ),
#     'options_list': [
#         'A. Increasing the size of the state space.',
#         'B. Increasing the size of the action space.',
#         'C. Introducing more stochastic transitions.',
#         'D. Reducing the discount factor gamma to near zero.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'The discount factor γ affects the weight of future rewards but does not influence the computational complexity of the algorithm. Time complexity depends on the size of the state and action spaces, as well as stochastic transitions.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_4 = {
#     'question': (
#         'When comparing policy iteration and value iteration, which of the following is accurate?'
#     ),
#     'options_list': [
#         'A. Policy iteration uses a single step of value update per iteration.',
#         'B. Value iteration requires evaluating the policy after each update.',
#         'C. Policy iteration only updates values without changing the policy.',
#         'D. Policy iteration greedily updates the policy based on the current value function.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'Policy iteration involves two steps: evaluating the value of the current policy and greedily updating it to improve. This is distinct from value iteration, which updates value estimates without explicitly refining the policy at each step.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_5 = {
#     'question': (
#         'Which of these could invalidate the Markov property in an environment modeled as an MDP?'
#     ),
#     'options_list': [
#         'A. States are defined using the complete trajectory history.',
#         'B. Transition probabilities depend only on the current state and action.',
#         'C. Rewards are determined by the current state and action.',
#         'D. The environment is stochastic.'
#     ],
#     'correct_answer': 'A',
#     'explanation': (
#         'The Markov property assumes that the next state depends only on the current state and action. Including the complete trajectory history violates this assumption.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_6 = {
#     'question': (
#         'True or False: A discount factor γ closer to 1 emphasizes long-term rewards over immediate ones, potentially prioritizing unreachable states with high rewards.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'A higher γ gives more weight to future rewards, sometimes prioritizing states that are impractical to reach.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_7 = {
#     'question': (
#         'True or False: Dynamic programming methods such as Q-iteration and value iteration cannot be applied to environments with stochastic transitions.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'Dynamic programming methods explicitly account for stochastic transitions in the environment by considering expected values over all possible outcomes.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_8 = {
#     'question': (
#         'True or False: The Bellman equation ensures that the sum of discounted rewards over a trajectory is always greater than the immediate reward for any given state.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The Bellman equation balances immediate rewards and future rewards; the discounted sum can be smaller if future rewards are heavily discounted.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_9 = {
#     'question': (
#         'True or False: In reinforcement learning, an agent can infer the optimal action at a state even without trying all possible actions at that state.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'Without trying all actions, the agent cannot determine which action yields the highest reward, as reinforcement learning relies on exploration to gather information.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_2_10 = {
#     'question': (
#         'True or False: A stochastic policy assigns a deterministic action to each state based on maximum reward likelihood.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'A stochastic policy assigns probabilities to each action for a given state, meaning the action is selected probabilistically rather than deterministically.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }



# question_gatech_MDP_3_1 = {
#     'question': (
#         'Which of the following statements is true regarding Deep Q-Learning?'
#     ),
#     'options_list': [
#         'A. Deep Q-Learning updates a single Q-network using stochastic updates.',
#         'B. The Q-old network updates more frequently than the Q-new network to stabilize training.',
#         'C. Experience replay buffers reduce data correlation, improving gradient stability.',
#         'D. The epsilon-greedy policy only gathers data with the greedy action.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Experience replay buffers help reduce correlation by sampling from past transitions, ensuring diverse minibatches for training. The other options misrepresent the training process.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_2 = {
#     'question': (
#         'What is the main reason for maintaining two Q-networks (Q-new and Q-old) during training in Deep Q-Learning?'
#     ),
#     'options_list': [
#         'A. To double the number of actions the agent can consider in each state.',
#         'B. To make the gradient updates more aggressive.',
#         'C. To prevent unstable updates caused by highly correlated Q-values.',
#         'D. To ensure every state-action pair is updated at least once per iteration.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Using separate networks for target and current Q-values stabilizes the updates, avoiding feedback loops from correlated predictions.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_3 = {
#     'question': (
#         'Which of the following challenges is most addressed by the epsilon-greedy strategy in reinforcement learning?'
#     ),
#     'options_list': [
#         'A. The problem of biased gradients caused by correlated data points.',
#         'B. Ensuring exploration of less rewarding but potentially optimal states.',
#         'C. Assigning credit to specific actions within a trajectory.',
#         'D. Balancing the update rates of Q-old and Q-new networks.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Epsilon-greedy strategies encourage exploration by occasionally selecting random actions, which helps discover better strategies.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_4 = {
#     'question': (
#         'Why is a baseline used in policy gradient methods?'
#     ),
#     'options_list': [
#         'A. To ensure the policy assigns maximum credit to the best action in a trajectory.',
#         'B. To reduce the variance of gradient updates without affecting their expected value.',
#         'C. To simplify the calculation of Q-functions during updates.',
#         'D. To eliminate the dependency on rewards in policy updates.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Baselines preserve the mean gradient but reduce variance, making the updates more stable and efficient.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_5 = {
#     'question': (
#         'In policy gradient methods, the term "credit assignment" refers to:'
#     ),
#     'options_list': [
#         'A. Determining the value of each state visited in a trajectory.',
#         'B. Assigning responsibility for rewards to specific actions in a trajectory.',
#         'C. Calculating the probability of each action based on the policy.',
#         'D. Balancing exploration and exploitation in the data collection policy.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Credit assignment involves determining which actions in a sequence contributed to the overall reward.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_6 = {
#     'question': (
#         'True or False: The main purpose of experience replay buffers is to improve exploration in reinforcement learning.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'Experience replay buffers improve gradient stability by reducing data correlation, not exploration.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_7 = {
#     'question': (
#         'True or False: In Deep Q-Learning, the epsilon-greedy strategy ensures that every state-action pair is explored an equal number of times.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The epsilon-greedy strategy ensures some exploration but does not guarantee uniform exploration across all states and actions.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_8 = {
#     'question': (
#         'True or False: Policy gradient methods directly optimize a policy by maximizing the expected return through gradient updates.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Policy gradient methods parameterize policies and use gradients of the expected return to improve them iteratively.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

question_gatech_MDP_3_1 = {
    'question': (
        'Which of the following statements is true regarding Deep Q-Learning? (Probability of appearing on test: 0.733)'
    ),
    'options_list': [
        'A. Deep Q-Learning updates a single Q-network using stochastic updates.',
        'B. The Q-old network updates more frequently than the Q-new network to stabilize training.',
        'C. Experience replay buffers reduce data correlation, improving gradient stability.',
        'D. The epsilon-greedy policy only gathers data with the greedy action.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Experience replay buffers help reduce correlation by sampling from past transitions, ensuring diverse minibatches for training. The other options misrepresent the training process.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_2 = {
    'question': (
        'What is the main reason for maintaining two Q-networks (Q-new and Q-old) during training in Deep Q-Learning? (Probability of appearing on test: 0.847)'
    ),
    'options_list': [
        'A. To double the number of actions the agent can consider in each state.',
        'B. To make the gradient updates more aggressive.',
        'C. To prevent unstable updates caused by highly correlated Q-values.',
        'D. To ensure every state-action pair is updated at least once per iteration.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Using separate networks for target and current Q-values stabilizes the updates, avoiding feedback loops from correlated predictions.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_3 = {
    'question': (
        'Which of the following challenges is most addressed by the epsilon-greedy strategy in reinforcement learning? (Probability of appearing on test: 0.653)'
    ),
    'options_list': [
        'A. The problem of biased gradients caused by correlated data points.',
        'B. Ensuring exploration of less rewarding but potentially optimal states.',
        'C. Assigning credit to specific actions within a trajectory.',
        'D. Balancing the update rates of Q-old and Q-new networks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Epsilon-greedy strategies encourage exploration by occasionally selecting random actions, which helps discover better strategies.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_4 = {
    'question': (
        'Why is a baseline used in policy gradient methods? (Probability of appearing on test: 0.930)'
    ),
    'options_list': [
        'A. To ensure the policy assigns maximum credit to the best action in a trajectory.',
        'B. To reduce the variance of gradient updates without affecting their expected value.',
        'C. To simplify the calculation of Q-functions during updates.',
        'D. To eliminate the dependency on rewards in policy updates.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Baselines preserve the mean gradient but reduce variance, making the updates more stable and efficient.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_5 = {
    'question': (
        'In policy gradient methods, the term "credit assignment" refers to: (Probability of appearing on test: 0.778)'
    ),
    'options_list': [
        'A. Determining the value of each state visited in a trajectory.',
        'B. Assigning responsibility for rewards to specific actions in a trajectory.',
        'C. Calculating the probability of each action based on the policy.',
        'D. Balancing exploration and exploitation in the data collection policy.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Credit assignment involves determining which actions in a sequence contributed to the overall reward.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_6 = {
    'question': (
        'True or False: The main purpose of experience replay buffers is to improve exploration in reinforcement learning. (Probability of appearing on test: 0.859)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Experience replay buffers improve gradient stability by reducing data correlation, not exploration.'
    ),
    'chapter_information': 'gatech MDP lecture'
}



question_gatech_MDP_3_7 = {
    'question': (
        'True or False: Actor-critic algorithms substitute the total trajectory reward in REINFORCE with the Q-function of the policy. (Probability of appearing on test: 0.774)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Actor-critic methods use the Q-function or advantage function instead of the total trajectory reward, reducing variance and improving learning stability.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_8 = {
    'question': (
        'True or False: In deep Q-learning, the replay buffer introduces correlation between sampled transitions to speed up convergence. (Probability of appearing on test: 0.757)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The replay buffer is used to reduce correlation between transitions by random sampling, which stabilizes training rather than speeding up convergence through increased correlation.'
    ),
    'chapter_information': 'gatech MDP lecture'
}


# question_gatech_MDP_3_9 = {
#     'question': (
#         'True or False: Adding a baseline to policy gradients affects the expected value of the gradient updates.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'A baseline reduces variance without affecting the expected value of gradient updates.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_3_10 = {
#     'question': (
#         'True or False: Actor-critic methods use both policy gradients and value functions to improve training efficiency.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Actor-critic methods combine policy gradients (actor) with value functions (critic) to improve stability and efficiency.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }


# question_gatech_MDP_4_1 = {
#     'question': (
#         'Which of the following is a primary benefit of using two Q-networks (Qold and Qnew) in deep Q-learning?'
#     ),
#     'options_list': [
#         'A. It reduces the time complexity of the algorithm.',
#         'B. It prevents overestimation of Q-values by separating target computation and updates.',
#         'C. It allows for dynamic adjustment of the discount factor γ.',
#         'D. It eliminates the need for an experience replay buffer.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Maintaining two Q-networks ensures stability in training by preventing overestimation, as the Qold network provides a fixed target during updates, while Qnew learns from it. This separation is critical for stable convergence.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_2 = {
#     'question': (
#         'In the context of deep Q-learning, what is the primary role of the experience replay buffer?'
#     ),
#     'options_list': [
#         'A. To maintain a set of optimal policies for quick reference.',
#         'B. To store transitions and reduce the correlation between sampled data points for training.',
#         'C. To dynamically adjust the exploration-exploitation tradeoff.',
#         'D. To estimate the reward distribution for all actions.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'The experience replay buffer reduces correlations between transitions, ensuring that updates are made with diverse and representative minibatches, which stabilizes training and reduces variance in gradient updates.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_3 = {
#     'question': (
#         'Which challenge does the epsilon-greedy strategy in deep Q-learning address?'
#     ),
#     'options_list': [
#         'A. Ensuring that the replay buffer is not biased.',
#         'B. Promoting exploration to avoid suboptimal policies.',
#         'C. Accelerating the convergence of the Q-network.',
#         'D. Balancing the variance of policy gradients.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Epsilon-greedy ensures exploration by occasionally selecting random actions, preventing the agent from getting stuck in locally optimal but globally suboptimal policies.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_4 = {
#     'question': (
#         'In the REINFORCE algorithm, why is the gradient of the policy objective scaled by the total reward of a trajectory?'
#     ),
#     'options_list': [
#         'A. To prioritize actions with higher immediate rewards.',
#         'B. To assign credit based on the overall success of the trajectory.',
#         'C. To reduce the computational cost of backpropagation.',
#         'D. To maximize the Q-function directly.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'The total reward determines the gradient magnitude, which adjusts the likelihood of actions proportional to the success of the entire trajectory, aligning with the trial-and-error nature of reinforcement learning.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_5 = {
#     'question': (
#         'What is the primary purpose of adding a baseline b in the policy gradient algorithm?'
#     ),
#     'options_list': [
#         'A. To ensure the gradient magnitude is always positive.',
#         'B. To stabilize training by reducing the variance of gradient updates.',
#         'C. To increase the likelihood of selecting exploratory actions.',
#         'D. To simplify the computation of Q-values.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Adding a baseline preserves the mean of the gradient expectation while reducing its variance, improving the stability and efficiency of policy updates.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_6 = {
#     'question': (
#         'True or False: Deep Q-learning updates the Q-values by minimizing a mean squared error loss inspired by the Bellman equation.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'The Bellman equation serves as the foundation for the Q-network updates, with the MSE loss measuring the difference between predicted and target Q-values.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_7 = {
#     'question': (
#         'True or False: Epsilon-greedy policies select random actions with a fixed probability throughout training.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The probability of selecting random actions (epsilon) typically decays over time to balance exploration early on and exploitation in later stages.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_8 = {
#     'question': (
#         'True or False: In policy gradient methods, log probabilities of actions are adjusted based on the sign and magnitude of rewards.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'The policy gradient algorithm increases or decreases the log probability of an action proportionally to its associated reward, driving the policy toward better actions.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_9 = {
#     'question': (
#         'True or False: Actor-critic algorithms substitute the total trajectory reward in REINFORCE with the Q-function of the policy.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Actor-critic methods improve upon REINFORCE by using the Q-function, which provides more granular information about the value of state-action pairs.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_gatech_MDP_4_10 = {
#     'question': (
#         'True or False: In deep Q-learning, the replay buffer introduces correlation between sampled transitions to speed up convergence.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The replay buffer reduces correlation between transitions by randomizing samples, which enhances stability and efficiency during training.'
#     ),
#     'chapter_information': 'gatech MDP lecture'
# }

# question_MDP_Reading_1_1 = {
#     'question': (
#         'Which of the following is a primary benefit of using two Q-networks (Qold and Qnew) in deep Q-learning?'
#     ),
#     'options_list': [
#         'A. It reduces the time complexity of the algorithm.',
#         'B. It prevents overestimation of Q-values by separating target computation and updates.',
#         'C. It allows for dynamic adjustment of the discount factor γ.',
#         'D. It eliminates the need for an experience replay buffer.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'In Deep Q-Learning, instability during training is addressed by maintaining two separate Q-networks:'
#         '\n\nQnew (Newer Network): This network is updated continuously during training using gradient descent.'
#         '\n\nQold (Older Network): This network remains unchanged during training and is periodically synchronized '
#         'with the parameters of Qnew. This approach helps in stabilizing training by preventing the oscillations '
#         'that can occur when using a single network for both prediction and target generation. The use of two '
#         'networks reduces the correlations between the target and the predicted Q-values, leading to more stable updates.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_1_2 = {
#     'question': (
#         'In the context of Markov Decision Processes (MDPs), which of the following statements is always true?'
#     ),
#     'options_list': [
#         'A. The Markov property implies that future states depend only on the past states and actions, not on the current state.',
#         'B. An optimal policy in a finite horizon MDP is always time-invariant.',
#         'C. In an MDP, the reward function can depend on future states.',
#         'D. The transition model in an MDP specifies the probability of transitioning to a new state given the current state and action.',
#         'E. The discount factor γ in an MDP must be strictly less than 1 to guarantee convergence of the value function.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'Option D is always true. In an MDP, the transition model specifies the probability of moving to a new state '
#         'given the current state and action, which is fundamental to the definition of an MDP.'
#         '\n\nA. False. The Markov property implies that future states depend only on the current state and action, not on past states and actions.'
#         '\n\nB. False. In finite horizon MDPs, the optimal policy can be time-dependent because the optimal action may '
#         'change as the remaining time decreases.'
#         '\n\nC. False. In an MDP, the reward function depends on the current state and action (and possibly the next state), '
#         'but not on future states beyond the immediate transition.'
#         '\n\nE. False. While a discount factor γ < 1 helps ensure convergence in infinite horizon problems, convergence can '
#         'sometimes occur even when γ = 1, depending on the specifics of the MDP (e.g., when the rewards are bounded and the process is terminating).'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_1_3 = {
#     'question': (
#         'Regarding dynamic programming methods for solving MDPs, which of the following statements is NOT correct?'
#     ),
#     'options_list': [
#         'A. Value iteration computes the optimal value function by iteratively updating value estimates based on the Bellman equation.',
#         'B. Policy iteration involves evaluating a given policy and then improving it by acting greedily with respect to the value function.',
#         'C. Backwards induction in finite horizon MDPs can produce a time-dependent optimal policy.',
#         'D. In value iteration, the policy is explicitly updated at each iteration to ensure convergence.',
#         'E. Both value iteration and policy iteration can be used to find the optimal policy in MDPs.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'Option D is NOT correct. In value iteration, the policy is not explicitly updated at each iteration. Instead, '
#         'value iteration focuses on updating the value function estimates using the Bellman equation. The policy can '
#         'be derived after the value function has converged by choosing actions that minimize (or maximize) the expected value.'
#         '\n\nA. Correct. Value iteration updates value estimates iteratively based on the Bellman equation.'
#         '\n\nB. Correct. Policy iteration involves evaluating the current policy and then improving it.'
#         '\n\nC. Correct. In finite horizon MDPs, backwards induction can produce a time-dependent policy.'
#         '\n\nE. Correct. Both value iteration and policy iteration are methods used to find the optimal policy in MDPs.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_1_4 = {
#     'question': (
#         'Consider an agent navigating a grid world using an epsilon-greedy strategy. Which of the following scenarios best illustrates the exploration vs. exploitation dilemma?'
#     ),
#     'options_list': [
#         'A. The agent always chooses the action with the highest known reward, ignoring less-known options.',
#         'B. The agent chooses actions completely at random, with no regard for past experiences.',
#         'C. The agent occasionally selects a suboptimal action to gather more information about the environment.',
#         'D. The agent updates its policy using only the most recent experience, disregarding older data.',
#         'E. The agent increases its discount factor over time to prioritize immediate rewards.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Option C best illustrates the exploration vs. exploitation dilemma. By occasionally selecting suboptimal actions, '
#         'the agent explores the environment to gather more information, which might lead to discovering better strategies in the long run.'
#         '\n\nA. This represents pure exploitation with no exploration, ignoring potentially better actions.'
#         '\n\nB. This represents pure exploration without using past experiences, not balancing with exploitation.'
#         '\n\nD. This is about policy updates and disregards older data, which is related to learning stability, not directly to exploration vs. exploitation.'
#         '\n\nE. Adjusting the discount factor affects how future rewards are valued but is less directly related to the exploration vs. exploitation trade-off.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_1_5 = {
#     'question': (
#         'In the derivation of policy gradients, the "log derivative trick" is used. Which of the following statements about this technique is false?'
#     ),
#     'options_list': [
#         'A. It allows us to express the gradient of an expectation as an expectation of the gradient.',
#         'B. It involves multiplying and dividing by the probability of the trajectory under the policy.',
#         'C. It is essential for deriving the policy gradient in continuous action spaces.',
#         'D. It enables us to compute gradients without knowing the integral form of the probability density.',
#         'E. It results in an expression that can be approximated using samples from the policy.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Option C is false. The log derivative trick is not exclusively essential for continuous action spaces; it is used in '
#         'policy gradient derivations for both discrete and continuous action spaces. The trick allows us to move the gradient '
#         'operator inside the expectation, which is crucial for deriving policy gradients in general.'
#         '\n\nA. True. The log derivative trick lets us express the gradient of an expectation as the expectation of a gradient.'
#         '\n\nB. True. It involves multiplying and dividing by the probability of the trajectory under the policy.'
#         '\n\nD. True. It enables us to compute gradients without needing the integral form of the probability density.'
#         '\n\nE. True. The resulting expression can be approximated using samples drawn from the policy.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_2_1 = {
#     'question': (
#         'In the derivation of the policy gradient, we encounter the "likelihood ratio" expression for the gradient. Which of the following statements is true regarding this expression?'
#     ),
#     'options_list': [
#         'A. The policy gradient can be expressed as the expected total reward times the gradient of the log of the transition probabilities.',
#         'B. The policy gradient depends solely on the gradient of the log probabilities of the actions chosen under the policy.',
#         'C. The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model.',
#         'D. The gradient of the log probability of the trajectory includes terms from both the policy and the transition model.',
#         'E. The policy gradient is unbiased only if the transition model is deterministic.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model. '
#         'In the derivation, we eliminate the dependency on the transition probabilities because the gradient of the log probability '
#         'of the trajectory only involves the policy parameters when the transition model is independent of those parameters.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_2_2 = {
#     'question': (
#         'Which of the following is not a reason for high variance in the REINFORCE algorithm\'s gradient estimates?'
#     ),
#     'options_list': [
#         'A. The use of total reward of entire trajectories without considering individual action contributions.',
#         'B. The fact that actions can affect rewards only in future time steps, leading to delayed credit assignment.',
#         'C. The stochastic nature of the policy leading to different trajectories in each iteration.',
#         'D. The dependency of the gradient estimate on the transition probabilities, which are unknown.',
#         'E. The possibility that all sampled trajectories have high rewards, making it difficult to differentiate among them.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'The dependency of the gradient estimate on the transition probabilities is not a source of high variance because, '
#         'in the likelihood ratio method, the transition probabilities cancel out or are independent of the policy parameters.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_2_3 = {
#     'question': (
#         'In policy gradient methods, introducing a baseline function b(s) serves what primary purpose?'
#     ),
#     'options_list': [
#         'A. It introduces bias into the gradient estimate to ensure convergence.',
#         'B. It reduces the variance of the gradient estimate without changing its expected value.',
#         'C. It accelerates learning by scaling the gradient proportionally to the baseline.',
#         'D. It modifies the policy gradient to account for the action-value function Q(s,a).',
#         'E. It ensures that the gradient estimate depends only on future rewards.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Introducing a baseline function b(s) reduces the variance of the gradient estimate without changing its expected value. '
#         'This is because subtracting a baseline that does not depend on the action (and policy parameters) preserves the unbiased '
#         'nature of the gradient estimate while potentially reducing variance.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_2_4 = {
#     'question': (
#         'Which of the following statements about the natural policy gradient is false?'
#     ),
#     'options_list': [
#         'A. The natural policy gradient adjusts the policy parameters in the direction that maximizes the expected reward while considering the geometry of the parameter space.',
#         'B. The natural policy gradient uses the inverse of the Fisher Information Matrix to precondition the gradient update.',
#         'C. The Fisher Information Matrix measures the sensitivity of the policy\'s probability distribution to changes in the parameters.',
#         'D. The natural policy gradient requires knowledge of the transition model to compute the Fisher Information Matrix.',
#         'E. The natural policy gradient aims to make small changes in the policy distribution rather than the parameter values.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'The natural policy gradient does not require knowledge of the transition model to compute the Fisher Information Matrix. '
#         'The Fisher Information Matrix is computed based on the policy\'s probability distribution and its sensitivity to parameter changes, '
#         'and it can be estimated using samples of states and actions without needing the transition model.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_2_5 = {
#     'question': (
#         'In actor-critic methods, the "critic" component primarily serves to:'
#     ),
#     'options_list': [
#         'A. Estimate the policy gradient directly from sampled trajectories.',
#         'B. Evaluate and improve the policy by selecting actions with the highest estimated value.',
#         'C. Approximate the value function or advantage function to reduce variance in the policy gradient estimate.',
#         'D. Provide the exact Q-values required for the policy gradient theorem.',
#         'E. Ensure that the policy updates are unbiased and converge to the optimal policy.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'In actor-critic methods, the critic approximates the value function or advantage function, which is used to reduce '
#         'variance in the policy gradient estimate. The critic helps by providing a learned estimate of the expected future rewards, '
#         'which informs the actor\'s updates.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_1 = {
#     'question': (
#         'What is the main difference between on-policy methods like SARSA and off-policy methods like Q-learning?'
#     ),
#     'options_list': [
#         'A. SARSA updates the Q-function using the maximum possible future reward, while Q-learning updates it using the current policy\'s reward.',
#         'B. SARSA relies on data collected from the current policy, while Q-learning can use data from any policy.',
#         'C. SARSA requires experience replay, whereas Q-learning does not.',
#         'D. SARSA assumes a deterministic transition model, while Q-learning assumes a stochastic one.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'On-policy methods like SARSA update based on the current policy, while off-policy methods like Q-learning can leverage samples '
#         'from any policy, making Q-learning more versatile.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_2 = {
#     'question': (
#         'Which of the following is TRUE about Temporal Difference (TD) learning?'
#     ),
#     'options_list': [
#         'A. It requires the entire trajectory to compute the value update.',
#         'B. It updates the value function based on the TD error after each state transition.',
#         'C. TD learning cannot be used with a continuous state space.',
#         'D. It minimizes the exact Bellman error using offline batch updates.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'TD learning performs incremental updates to the value function using the TD error $r + \\gamma \\tilde{V}(x\') - \\tilde{V}(x)$, '
#         'which allows online learning without needing the full trajectory.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_3 = {
#     'question': (
#         'Why is an experience replay buffer used in Q-learning?'
#     ),
#     'options_list': [
#         'A. To make online updates computationally efficient.',
#         'B. To address correlation between samples and enable reuse of past experiences.',
#         'C. To prioritize exploring new states with high uncertainty.',
#         'D. To replace the need for exploration policies.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Experience replay reduces sample correlation by allowing random sampling of past experiences, enabling better generalization '
#         'and stabilizing training.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_4 = {
#     'question': (
#         'What condition is required for Q-learning to guarantee convergence to the optimal Q-function?'
#     ),
#     'options_list': [
#         'A. The reward distribution must be deterministic.',
#         'B. The learning rate must remain constant over time.',
#         'C. Each state-action pair must be visited infinitely often.',
#         'D. The exploration policy must be strictly greedy throughout training.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'To ensure convergence, Q-learning requires that all state-action pairs are visited infinitely often and that the learning rate '
#         'decreases appropriately over time.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_5 = {
#     'question': (
#         'Which of the following statements about policy iteration is FALSE?'
#     ),
#     'options_list': [
#         'A. Policy iteration alternates between policy evaluation and policy improvement steps.',
#         'B. Policy iteration requires solving a system of linear equations during policy evaluation.',
#         'C. Policy iteration does not guarantee convergence to the optimal policy.',
#         'D. Modified Policy Iteration can speed up the evaluation step by warm-starting from the previous value function.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Policy iteration is guaranteed to converge to the optimal policy as it monotonically improves the policy at each step.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_6 = {
#     'question': (
#         'The Bellman residual method guarantees convergence to the optimal Q-function if we can generate independent successor states.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Bellman residual updates are unbiased if independent successor states are available, ensuring accurate gradient descent updates.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_7 = {
#     'question': (
#         'Boltzmann exploration selects actions based on a weighted probability distribution of Q-values.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Boltzmann exploration assigns probabilities to actions based on their Q-values, with a parameter $b$ controlling the balance '
#         'between exploration and exploitation.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_8 = {
#     'question': (
#         'In the Grid-World example, the Temporal Difference (TD) update rule adjusts the value of a state only when the reward is non-zero.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'The TD update rule adjusts state values based on the TD error, which includes rewards and the estimated value of the next state, '
#         'even if the immediate reward is zero.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_9 = {
#     'question': (
#         'Q-learning requires the current policy to compute the optimal Q-function.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'Q-learning is an off-policy method and does not rely on the current policy, allowing it to learn the optimal Q-function from any policy\'s experiences.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_3_10 = {
#     'question': (
#         'Modified Policy Iteration combines aspects of value iteration and policy iteration to improve efficiency.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Modified Policy Iteration warm-starts the policy evaluation step using the previous value function and performs a limited number '
#         'of updates, combining the strengths of both methods.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_4_1 = {
#     'question': (
#         'In the derivation of the policy gradient, we encounter the "likelihood ratio" expression for the gradient. '
#         'Which of the following statements is true regarding this expression?'
#     ),
#     'options_list': [
#         'A. The policy gradient can be expressed as the expected total reward times the gradient of the log of the transition probabilities.',
#         'B. The policy gradient depends solely on the gradient of the log probabilities of the actions chosen under the policy.',
#         'C. The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model.',
#         'D. The gradient of the log probability of the trajectory includes terms from both the policy and the transition model.',
#         'E. The policy gradient is unbiased only if the transition model is deterministic.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model. '
#         'In the derivation, we eliminate the dependency on the transition probabilities because the gradient of the log probability '
#         'of the trajectory only involves the policy parameters when the transition model is independent of those parameters.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_4_2 = {
#     'question': (
#         'Which of the following is not a reason for high variance in the REINFORCE algorithm\'s gradient estimates?'
#     ),
#     'options_list': [
#         'A. The use of total reward of entire trajectories without considering individual action contributions.',
#         'B. The fact that actions can affect rewards only in future time steps, leading to delayed credit assignment.',
#         'C. The stochastic nature of the policy leading to different trajectories in each iteration.',
#         'D. The dependency of the gradient estimate on the transition probabilities, which are unknown.',
#         'E. The possibility that all sampled trajectories have high rewards, making it difficult to differentiate among them.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'The dependency of the gradient estimate on the transition probabilities is not a source of high variance because, '
#         'in the likelihood ratio method, the transition probabilities cancel out or are independent of the policy parameters.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_4_3 = {
#     'question': (
#         'In policy gradient methods, introducing a baseline function $b(s)$ serves what primary purpose?'
#     ),
#     'options_list': [
#         'A. It introduces bias into the gradient estimate to ensure convergence.',
#         'B. It reduces the variance of the gradient estimate without changing its expected value.',
#         'C. It accelerates learning by scaling the gradient proportionally to the baseline.',
#         'D. It modifies the policy gradient to account for the action-value function $Q(s, a)$.',
#         'E. It ensures that the gradient estimate depends only on future rewards.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Introducing a baseline function $b(s)$ reduces the variance of the gradient estimate without changing its expected value. '
#         'This is because subtracting a baseline that does not depend on the action (and policy parameters) preserves the unbiased '
#         'nature of the gradient estimate while potentially reducing variance.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_4_4 = {
#     'question': (
#         'Which of the following statements about the natural policy gradient is false?'
#     ),
#     'options_list': [
#         'A. The natural policy gradient adjusts the policy parameters in the direction that maximizes the expected reward while considering the geometry of the parameter space.',
#         'B. The natural policy gradient uses the inverse of the Fisher Information Matrix to precondition the gradient update.',
#         'C. The Fisher Information Matrix measures the sensitivity of the policy\'s probability distribution to changes in the parameters.',
#         'D. The natural policy gradient requires knowledge of the transition model to compute the Fisher Information Matrix.',
#         'E. The natural policy gradient aims to make small changes in the policy distribution rather than the parameter values.'
#     ],
#     'correct_answer': 'D',
#     'explanation': (
#         'The natural policy gradient does not require knowledge of the transition model to compute the Fisher Information Matrix. '
#         'The Fisher Information Matrix is computed based on the policy\'s probability distribution and its sensitivity to parameter changes, '
#         'and it can be estimated using samples of states and actions without needing the transition model.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_MDP_Reading_4_5 = {
#     'question': (
#         'In actor-critic methods, the "critic" component primarily serves to:'
#     ),
#     'options_list': [
#         'A. Estimate the policy gradient directly from sampled trajectories.',
#         'B. Evaluate and improve the policy by selecting actions with the highest estimated value.',
#         'C. Approximate the value function or advantage function to reduce variance in the policy gradient estimate.',
#         'D. Provide the exact Q-values required for the policy gradient theorem.',
#         'E. Ensure that the policy updates are unbiased and converge to the optimal policy.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'In actor-critic methods, the critic approximates the value function or advantage function, which is used to reduce '
#         'variance in the policy gradient estimate. The critic helps by providing a learned estimate of the expected future rewards, '
#         'which informs the actor\'s updates.'
#     ),
#     'chapter_information': 'MDP Reading'
# }

# question_Semi_Supervised_1 = {
#     'question': (
#         'What is the primary goal of semi-supervised learning as discussed in the module?'
#     ),
#     'options_list': [
#         'A. To generate labeled data from scratch using clustering techniques.',
#         'B. To learn from a large amount of labeled data combined with small amounts of unlabeled data.',
#         'C. To use small amounts of labeled data combined with large amounts of unlabeled data.',
#         'D. To train a model to perform surrogate tasks like rotation prediction or image reconstruction.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Semi-supervised learning focuses on leveraging a small labeled dataset along with a large unlabeled dataset '
#         'from the same distribution to improve learning.'
#     ),
#     'chapter_information': 'Semi-Supervised Learning'
# }

# question_Semi_Supervised_2 = {
#     'question': (
#         'Which of the following describes a "pseudo-labeling" approach in semi-supervised learning?'
#     ),
#     'options_list': [
#         'A. Generating synthetic labels for unlabeled data and training on the confident ones.',
#         'B. Using clustering methods to assign labels to unlabeled data.',
#         'C. Creating surrogate tasks to force feature learning from unlabeled data.',
#         'D. Learning low-dimensional feature representations to improve classification accuracy.'
#     ],
#     'correct_answer': 'A',
#     'explanation': (
#         'Pseudo-labeling involves training a model on labeled data, using it to predict labels for unlabeled data, '
#         'selecting confident predictions, and iteratively retraining the model on these predictions.'
#     ),
#     'chapter_information': 'Semi-Supervised Learning'
# }

# question_Self_Supervised_1 = {
#     'question': (
#         'Which of the following is NOT an example of a surrogate task for self-supervised learning?'
#     ),
#     'options_list': [
#         'A. Predicting the amount of rotation applied to an image.',
#         'B. Reconstructing an input image using an autoencoder.',
#         'C. Generating pseudo-labels from labeled data for semi-supervised training.',
#         'D. Learning a compressed representation of the data using dimensionality reduction.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'Pseudo-labeling is a semi-supervised technique, not a surrogate task. Surrogate tasks are designed to force '
#         'feature learning without labels, such as rotation prediction or reconstruction.'
#     ),
#     'chapter_information': 'Self-Supervised Learning'
# }

# question_Reinforcement_Learning_1 = {
#     'question': (
#         'Which of the following is TRUE about reinforcement learning as described in the module?'
#     ),
#     'options_list': [
#         'A. It relies on dense supervision for each state-action pair.',
#         'B. Rewards can be sparse or dense, depending on the environment.',
#         'C. The agent directly learns the optimal action without interacting with the environment.',
#         'D. The environment must always be fully observable to the agent.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'In reinforcement learning, rewards can be sparse (e.g., win/lose signals in chess) or dense (e.g., continuous '
#         'score updates in Atari games). The agent interacts with the environment to learn optimal actions.'
#     ),
#     'chapter_information': 'Reinforcement Learning'
# }

# question_GANs_VAEs_1 = {
#     'question': (
#         'What is a key difference between Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs)?'
#     ),
#     'options_list': [
#         'A. GANs explicitly model the joint probability distribution, while VAEs do not.',
#         'B. VAEs tend to produce sharper images than GANs.',
#         'C. GANs involve a generator-discriminator setup, while VAEs rely on encoder-decoder architectures.',
#         'D. Both GANs and VAEs use supervised labels to generate realistic data.'
#     ],
#     'correct_answer': 'C',
#     'explanation': (
#         'GANs consist of a generator and discriminator network that compete during training, while VAEs use an encoder-decoder '
#         'framework to learn latent representations and reconstruct inputs.'
#     ),
#     'chapter_information': 'Generative Models'
# }

# question_Self_Supervised_2 = {
#     'question': (
#         'Self-supervised learning uses labels derived from the data itself to train models.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Self-supervised learning relies on pseudo-labels or surrogate tasks generated from unlabeled data to drive training.'
#     ),
#     'chapter_information': 'Self-Supervised Learning'
# }

# question_Reinforcement_Learning_2 = {
#     'question': (
#         'Reinforcement learning always requires an explicitly known model of the environment.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'Reinforcement learning can work with unknown environments, where the agent learns policies through interaction and feedback.'
#     ),
#     'chapter_information': 'Reinforcement Learning'
# }

# question_GANs_VAEs_2 = {
#     'question': (
#         'GANs and VAEs both require labeled data to generate new samples from the learned data distribution.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'False',
#     'explanation': (
#         'GANs and VAEs are unsupervised methods that learn from unlabeled data to generate new samples.'
#     ),
#     'chapter_information': 'Generative Models'
# }

# question_Semi_Supervised_3 = {
#     'question': (
#         'The fixed match algorithm in semi-supervised learning combines labeled and unlabeled data by generating pseudo-labels and training with augmentations.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'Fixed match uses pseudo-labels for unlabeled data, incorporating them into the training process with strong augmentations.'
#     ),
#     'chapter_information': 'Semi-Supervised Learning'
# }

# question_Reinforcement_Learning_3 = {
#     'question': (
#         'In reinforcement learning, Markov Decision Processes provide a framework for modeling sequential decision-making tasks.'
#     ),
#     'options_list': [
#         'True',
#         'False'
#     ],
#     'correct_answer': 'True',
#     'explanation': (
#         'MDPs formalize reinforcement learning tasks by defining states, actions, rewards, and transition probabilities.'
#     ),
#     'chapter_information': 'Reinforcement Learning'
# }

question_gatech_MDP_3_9 = {
    'question': (
        'True or False: Adding a baseline to policy gradients affects the expected value of the gradient updates. (Probability of appearing on test: 0.853)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'A baseline reduces variance without affecting the expected value of gradient updates.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MDP_3_10 = {
    'question': (
        'True or False: Actor-critic methods use both policy gradients and value functions to improve training efficiency. (Probability of appearing on test: 0.878)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Actor-critic methods combine policy gradients (actor) with value functions (critic) to improve stability and efficiency.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gat1ech_MDP_4_1 = {
    'question': (
        'Which of the following is a primary benefit of using two Q-networks (Qold and Qnew) in deep Q-learning? (Probability of appearing on test: 0.825)'
    ),
    'options_list': [
        'A. It reduces the time complexity of the algorithm.',
        'B. It prevents overestimation of Q-values by separating target computation and updates.',
        'C. It allows for dynamic adjustment of the discount factor γ.',
        'D. It eliminates the need for an experience replay buffer.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Maintaining two Q-networks ensures stability in training by preventing overestimation, as the Qold network provides a fixed target during updates, while Qnew learns from it. This separation is critical for stable convergence.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gate1ch_MDP_4_2 = {
    'question': (
        'In the context of deep Q-learning, what is the primary role of the experience replay buffer? (Probability of appearing on test: 0.429)'
    ),
    'options_list': [
        'A. To maintain a set of optimal policies for quick reference.',
        'B. To store transitions and reduce the correlation between sampled data points for training.',
        'C. To dynamically adjust the exploration-exploitation tradeoff.',
        'D. To estimate the reward distribution for all actions.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The experience replay buffer reduces correlations between transitions, ensuring that updates are made with diverse and representative minibatches, which stabilizes training and reduces variance in gradient updates.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatec1h_MDP_4_3 = {
    'question': (
        'Which challenge does the epsilon-greedy strategy in deep Q-learning address? (Probability of appearing on test: 0.862)'
    ),
    'options_list': [
        'A. Ensuring that the replay buffer is not biased.',
        'B. Promoting exploration to avoid suboptimal policies.',
        'C. Accelerating the convergence of the Q-network.',
        'D. Balancing the variance of policy gradients.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Epsilon-greedy ensures exploration by occasionally selecting random actions, preventing the agent from getting stuck in locally optimal but globally suboptimal policies.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_ga1tech_MDP_4_4 = {
    'question': (
        'In the REINFORCE algorithm, why is the gradient of the policy objective scaled by the total reward of a trajectory? (Probability of appearing on test: 0.549)'
    ),
    'options_list': [
        'A. To prioritize actions with higher immediate rewards.',
        'B. To assign credit based on the overall success of the trajectory.',
        'C. To reduce the computational cost of backpropagation.',
        'D. To maximize the Q-function directly.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The total reward determines the gradient magnitude, which adjusts the likelihood of actions proportional to the success of the entire trajectory, aligning with the trial-and-error nature of reinforcement learning.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_ga1tech_MDP_4_5 = {
    'question': (
        'What is the primary purpose of adding a baseline b in the policy gradient algorithm? (Probability of appearing on test: 0.773)'
    ),
    'options_list': [
        'A. To ensure the gradient magnitude is always positive.',
        'B. To stabilize training by reducing the variance of gradient updates.',
        'C. To increase the likelihood of selecting exploratory actions.',
        'D. To simplify the computation of Q-values.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Adding a baseline preserves the mean of the gradient expectation while reducing its variance, improving the stability and efficiency of policy updates.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gate1ch_MDP_4_6 = {
    'question': (
        'True or False: Deep Q-learning updates the Q-values by minimizing a mean squared error loss inspired by the Bellman equation. (Probability of appearing on test: 0.728)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The Bellman equation serves as the foundation for the Q-network updates, with the MSE loss measuring the difference between predicted and target Q-values.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gate1ch_MDP_4_7 = {
    'question': (
        'True or False: Epsilon-greedy policies select random actions with a fixed probability throughout training. (Probability of appearing on test: 0.904)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The probability of selecting random actions (epsilon) typically decays over time to balance exploration early on and exploitation in later stages.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gat1ech_MDP_4_8 = {
    'question': (
        'True or False: In policy gradient methods, log probabilities of actions are adjusted based on the sign and magnitude of rewards. (Probability of appearing on test: 0.893)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The policy gradient algorithm increases or decreases the log probability of an action proportionally to its associated reward, driving the policy toward better actions.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gat1ech_MDP_4_9 = {
    'question': (
        'True or False: Actor-critic algorithms substitute the total trajectory reward in REINFORCE with the Q-function of the policy. (Probability of appearing on test: 0.774)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Actor-critic methods improve upon REINFORCE by using the Q-function, which provides more granular information about the value of state-action pairs.'
    ),
    'chapter_information': 'gatech MDP lecture'
}

question_gatech_MD1P_4_10 = {
    'question': (
        'True or False: In deep Q-learning, the replay buffer introduces correlation between sampled transitions to speed up convergence. (Probability of appearing on test: 0.757)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The replay buffer reduces correlation between transitions by randomizing samples, which enhances stability and efficiency during training.'
    ),
    'chapter_information': 'gatech MDP lecture'
}


question_MDP_Read1ing_1_1 = {
    'question': (
        'Which of the following is a primary benefit of using two Q-networks (Qold and Qnew) in deep Q-learning? (Probability of appearing on test: 0.825)'
    ),
    'options_list': [
        'A. It reduces the time complexity of the algorithm.',
        'B. It prevents overestimation of Q-values by separating target computation and updates.',
        'C. It allows for dynamic adjustment of the discount factor γ.',
        'D. It eliminates the need for an experience replay buffer.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In Deep Q-Learning, maintaining two Q-networks ensures stability in training by preventing overestimation, '
        'as the Qold network provides a fixed target during updates, while Qnew learns from it. This separation is critical for stable convergence.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MD1P_Reading_1_2 = {
    'question': (
        'In the context of Markov Decision Processes (MDPs), which of the following statements is always true? (Probability of appearing on test: 0.966)'
    ),
    'options_list': [
        'A. The Markov property implies that future states depend only on the past states and actions, not on the current state.',
        'B. An optimal policy in a finite horizon MDP is always time-invariant.',
        'C. In an MDP, the reward function can depend on future states.',
        'D. The transition model in an MDP specifies the probability of transitioning to a new state given the current state and action.',
        'E. The discount factor γ in an MDP must be strictly less than 1 to guarantee convergence of the value function.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Option D is always true. In an MDP, the transition model specifies the probability of moving to a new state given the current state and action.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_R1eading_1_3 = {
    'question': (
        'Regarding dynamic programming methods for solving MDPs, which of the following statements is NOT correct? (Probability of appearing on test: 0.985)'
    ),
    'options_list': [
        'A. Value iteration computes the optimal value function by iteratively updating value estimates based on the Bellman equation.',
        'B. Policy iteration involves evaluating a given policy and then improving it by acting greedily with respect to the value function.',
        'C. Backwards induction in finite horizon MDPs can produce a time-dependent optimal policy.',
        'D. In value iteration, the policy is explicitly updated at each iteration to ensure convergence.',
        'E. Both value iteration and policy iteration can be used to find the optimal policy in MDPs.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'In value iteration, the policy is not explicitly updated at each iteration. Instead, value iteration focuses on updating the value function estimates. '
        'The policy can be derived after the value function has converged.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_1_4 = {
    'question': (
        'Consider an agent navigating a grid world using an epsilon-greedy strategy. Which of the following scenarios best illustrates the exploration vs. exploitation dilemma? (Probability of appearing on test: 0.283)'
    ),
    'options_list': [
        'A. The agent always chooses the action with the highest known reward, ignoring less-known options.',
        'B. The agent chooses actions completely at random, with no regard for past experiences.',
        'C. The agent occasionally selects a suboptimal action to gather more information about the environment.',
        'D. The agent updates its policy using only the most recent experience, disregarding older data.',
        'E. The agent increases its discount factor over time to prioritize immediate rewards.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C best illustrates the exploration vs. exploitation dilemma. By occasionally selecting suboptimal actions, the agent explores the environment to gather more information, which might lead to discovering better strategies in the long run.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_1_5 = {
    'question': (
        'In the derivation of policy gradients, the "log derivative trick" is used. Which of the following statements about this technique is false? (Probability of appearing on test: 0.995)'
    ),
    'options_list': [
        'A. It allows us to express the gradient of an expectation as an expectation of the gradient.',
        'B. It involves multiplying and dividing by the probability of the trajectory under the policy.',
        'C. It is essential for deriving the policy gradient in continuous action spaces.',
        'D. It enables us to compute gradients without knowing the integral form of the probability density.',
        'E. It results in an expression that can be approximated using samples from the policy.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The log derivative trick is not exclusively essential for continuous action spaces; it is used in policy gradient derivations for both discrete and continuous action spaces.'
    ),
    'chapter_information': 'MDP Reading'
}


question_MDP_Reading_2_1 = {
    'question': (
        'In the derivation of the policy gradient, we encounter the "likelihood ratio" expression for the gradient. '
        'Which of the following statements is true regarding this expression? (Probability of appearing on test: 0.977)'
    ),
    'options_list': [
        'A. The policy gradient can be expressed as the expected total reward times the gradient of the log of the transition probabilities.',
        'B. The policy gradient depends solely on the gradient of the log probabilities of the actions chosen under the policy.',
        'C. The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model.',
        'D. The gradient of the log probability of the trajectory includes terms from both the policy and the transition model.',
        'E. The policy gradient is unbiased only if the transition model is deterministic.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model. '
        'This makes it particularly useful for reinforcement learning, where transition models are often unknown.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_2_2 = {
    'question': (
        'Which of the following is not a reason for high variance in the REINFORCE algorithm\'s gradient estimates? '
        '(Probability of appearing on test: 0.885)'
    ),
    'options_list': [
        'A. The use of total reward of entire trajectories without considering individual action contributions.',
        'B. The fact that actions can affect rewards only in future time steps, leading to delayed credit assignment.',
        'C. The stochastic nature of the policy leading to different trajectories in each iteration.',
        'D. The dependency of the gradient estimate on the transition probabilities, which are unknown.',
        'E. The possibility that all sampled trajectories have high rewards, making it difficult to differentiate among them.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The dependency of the gradient estimate on the transition probabilities is not a source of high variance because '
        'the transition probabilities do not directly influence the REINFORCE gradient computation.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_2_3 = {
    'question': (
        'In policy gradient methods, introducing a baseline function b(s) serves what primary purpose? '
        '(Probability of appearing on test: 0.974)'
    ),
    'options_list': [
        'A. It introduces bias into the gradient estimate to ensure convergence.',
        'B. It reduces the variance of the gradient estimate without changing its expected value.',
        'C. It accelerates learning by scaling the gradient proportionally to the baseline.',
        'D. It modifies the policy gradient to account for the action-value function Q(s, a).',
        'E. It ensures that the gradient estimate depends only on future rewards.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Introducing a baseline reduces variance in the gradient estimate while maintaining its unbiased nature, '
        'thereby stabilizing training in policy gradient methods.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_2_4 = {
    'question': (
        'Which of the following statements about the natural policy gradient is false? (Probability of appearing on test: 0.985)'
    ),
    'options_list': [
        'A. The natural policy gradient adjusts the policy parameters in the direction that maximizes the expected reward while considering the geometry of the parameter space.',
        'B. The natural policy gradient uses the inverse of the Fisher Information Matrix to precondition the gradient update.',
        'C. The Fisher Information Matrix measures the sensitivity of the policy\'s probability distribution to changes in the parameters.',
        'D. The natural policy gradient requires knowledge of the transition model to compute the Fisher Information Matrix.',
        'E. The natural policy gradient aims to make small changes in the policy distribution rather than the parameter values.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The natural policy gradient does not require knowledge of the transition model; it focuses on the geometry of the parameter space.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_2_5 = {
    'question': (
        'In actor-critic methods, the "critic" component primarily serves to: (Probability of appearing on test: 0.922)'
    ),
    'options_list': [
        'A. Estimate the policy gradient directly from sampled trajectories.',
        'B. Evaluate and improve the policy by selecting actions with the highest estimated value.',
        'C. Approximate the value function or advantage function to reduce variance in the policy gradient estimate.',
        'D. Provide the exact Q-values required for the policy gradient theorem.',
        'E. Ensure that the policy updates are unbiased and converge to the optimal policy.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The critic estimates the value function or advantage function, which helps reduce variance in the policy gradient updates.'
    ),
    'chapter_information': 'MDP Reading'
}


question_MDP_Reading_3_1 = {
    'question': (
        'What is the main difference between on-policy methods like SARSA and off-policy methods like Q-learning? '
        '(Probability of appearing on test: 0.918)'
    ),
    'options_list': [
        'A. SARSA updates the Q-function using the maximum possible future reward, while Q-learning updates it using the current policy\'s reward.',
        'B. SARSA relies on data collected from the current policy, while Q-learning can use data from any policy.',
        'C. SARSA requires experience replay, whereas Q-learning does not.',
        'D. SARSA assumes a deterministic transition model, while Q-learning assumes a stochastic one.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'On-policy methods like SARSA update based on the current policy, while off-policy methods like Q-learning can leverage samples '
        'from any policy, making Q-learning more versatile.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_2 = {
    'question': (
        'Which of the following is TRUE about Temporal Difference (TD) learning? (Probability of appearing on test: 0.934)'
    ),
    'options_list': [
        'A. It requires the entire trajectory to compute the value update.',
        'B. It updates the value function based on the TD error after each state transition.',
        'C. TD learning cannot be used with a continuous state space.',
        'D. It minimizes the exact Bellman error using offline batch updates.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'TD learning performs incremental updates to the value function using the TD error, allowing online learning without needing the full trajectory.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_3 = {
    'question': (
        'Why is an experience replay buffer used in Q-learning? (Probability of appearing on test: 0.611)'
    ),
    'options_list': [
        'A. To make online updates computationally efficient.',
        'B. To address correlation between samples and enable reuse of past experiences.',
        'C. To prioritize exploring new states with high uncertainty.',
        'D. To replace the need for exploration policies.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Experience replay reduces sample correlation by allowing random sampling of past experiences, enabling better generalization and stabilizing training.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_4 = {
    'question': (
        'What condition is required for Q-learning to guarantee convergence to the optimal Q-function? (Probability of appearing on test: 0.756)'
    ),
    'options_list': [
        'A. The reward distribution must be deterministic.',
        'B. The learning rate must remain constant over time.',
        'C. Each state-action pair must be visited infinitely often.',
        'D. The exploration policy must be strictly greedy throughout training.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'To ensure convergence, Q-learning requires that all state-action pairs are visited infinitely often and that the learning rate decreases appropriately over time.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_5 = {
    'question': (
        'Which of the following statements about policy iteration is FALSE? (Probability of appearing on test: 0.924)'
    ),
    'options_list': [
        'A. Policy iteration alternates between policy evaluation and policy improvement steps.',
        'B. Policy iteration requires solving a system of linear equations during policy evaluation.',
        'C. Policy iteration does not guarantee convergence to the optimal policy.',
        'D. Modified Policy Iteration can speed up the evaluation step by warm-starting from the previous value function.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Policy iteration is guaranteed to converge to the optimal policy as it monotonically improves the policy at each step.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_6 = {
    'question': (
        'The Bellman residual method guarantees convergence to the optimal Q-function if we can generate independent successor states. (Probability of appearing on test: 0.876)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Bellman residual updates are unbiased if independent successor states are available, ensuring accurate gradient descent updates.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_7 = {
    'question': (
        'Boltzmann exploration selects actions based on a weighted probability distribution of Q-values. (Probability of appearing on test: 0.803)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Boltzmann exploration assigns probabilities to actions based on their Q-values, with a parameter $b$ controlling the balance between exploration and exploitation.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_8 = {
    'question': (
        'In the Grid-World example, the Temporal Difference (TD) update rule adjusts the value of a state only when the reward is non-zero. (Probability of appearing on test: 0.633)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The TD update rule adjusts state values based on the TD error, which includes rewards and the estimated value of the next state, even if the immediate reward is zero.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_9 = {
    'question': (
        'Q-learning requires the current policy to compute the optimal Q-function. (Probability of appearing on test: 0.840)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Q-learning is an off-policy method and does not rely on the current policy, allowing it to learn the optimal Q-function from any policy\'s experiences.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_3_10 = {
    'question': (
        'Modified Policy Iteration combines aspects of value iteration and policy iteration to improve efficiency. (Probability of appearing on test: 0.832)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Modified Policy Iteration warm-starts the policy evaluation step using the previous value function and performs a limited number of updates, combining the strengths of both methods.'
    ),
    'chapter_information': 'MDP Reading'
}


question_MDP_Reading_4_1 = {
    'question': (
        'In the derivation of the policy gradient, we encounter the "likelihood ratio" expression for the gradient. '
        'Which of the following statements is true regarding this expression? (Probability of appearing on test: 0.977)'
    ),
    'options_list': [
        'A. The policy gradient can be expressed as the expected total reward times the gradient of the log of the transition probabilities.',
        'B. The policy gradient depends solely on the gradient of the log probabilities of the actions chosen under the policy.',
        'C. The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model.',
        'D. The gradient of the log probability of the trajectory includes terms from both the policy and the transition model.',
        'E. The policy gradient is unbiased only if the transition model is deterministic.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The likelihood ratio trick allows us to express the policy gradient without requiring knowledge of the transition model. '
        'This makes it particularly useful for reinforcement learning, where transition models are often unknown.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_4_2 = {
    'question': (
        'Which of the following is not a reason for high variance in the REINFORCE algorithm\'s gradient estimates? '
        '(Probability of appearing on test: 0.885)'
    ),
    'options_list': [
        'A. The use of total reward of entire trajectories without considering individual action contributions.',
        'B. The fact that actions can affect rewards only in future time steps, leading to delayed credit assignment.',
        'C. The stochastic nature of the policy leading to different trajectories in each iteration.',
        'D. The dependency of the gradient estimate on the transition probabilities, which are unknown.',
        'E. The possibility that all sampled trajectories have high rewards, making it difficult to differentiate among them.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The dependency of the gradient estimate on the transition probabilities is not a source of high variance because '
        'the transition probabilities do not directly influence the REINFORCE gradient computation.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_4_3 = {
    'question': (
        'In policy gradient methods, introducing a baseline function $b(s)$ serves what primary purpose? '
        '(Probability of appearing on test: 0.959)'
    ),
    'options_list': [
        'A. It introduces bias into the gradient estimate to ensure convergence.',
        'B. It reduces the variance of the gradient estimate without changing its expected value.',
        'C. It accelerates learning by scaling the gradient proportionally to the baseline.',
        'D. It modifies the policy gradient to account for the action-value function $Q(s, a)$.',
        'E. It ensures that the gradient estimate depends only on future rewards.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Introducing a baseline reduces variance in the gradient estimate while maintaining its unbiased nature, '
        'thereby stabilizing training in policy gradient methods.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_4_4 = {
    'question': (
        'Which of the following statements about the natural policy gradient is false? (Probability of appearing on test: 0.985)'
    ),
    'options_list': [
        'A. The natural policy gradient adjusts the policy parameters in the direction that maximizes the expected reward while considering the geometry of the parameter space.',
        'B. The natural policy gradient uses the inverse of the Fisher Information Matrix to precondition the gradient update.',
        'C. The Fisher Information Matrix measures the sensitivity of the policy\'s probability distribution to changes in the parameters.',
        'D. The natural policy gradient requires knowledge of the transition model to compute the Fisher Information Matrix.',
        'E. The natural policy gradient aims to make small changes in the policy distribution rather than the parameter values.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The natural policy gradient does not require knowledge of the transition model; it focuses on the geometry of the parameter space.'
    ),
    'chapter_information': 'MDP Reading'
}

question_MDP_Reading_4_5 = {
    'question': (
        'In actor-critic methods, the "critic" component primarily serves to: (Probability of appearing on test: 0.922)'
    ),
    'options_list': [
        'A. Estimate the policy gradient directly from sampled trajectories.',
        'B. Evaluate and improve the policy by selecting actions with the highest estimated value.',
        'C. Approximate the value function or advantage function to reduce variance in the policy gradient estimate.',
        'D. Provide the exact Q-values required for the policy gradient theorem.',
        'E. Ensure that the policy updates are unbiased and converge to the optimal policy.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The critic estimates the value function or advantage function, which helps reduce variance in the policy gradient updates.'
    ),
    'chapter_information': 'MDP Reading'
}

question_Semi_Supervised_1 = {
    'question': (
        'What is the primary goal of semi-supervised learning as discussed in the module? (Probability of appearing on test: 0.727)'
    ),
    'options_list': [
        'A. To generate labeled data from scratch using clustering techniques.',
        'B. To learn from a large amount of labeled data combined with small amounts of unlabeled data.',
        'C. To use small amounts of labeled data combined with large amounts of unlabeled data.',
        'D. To train a model to perform surrogate tasks like rotation prediction or image reconstruction.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Semi-supervised learning focuses on leveraging a small labeled dataset along with a large unlabeled dataset '
        'from the same distribution to improve learning.'
    ),
    'chapter_information': 'Semi-Supervised Learning'
}


question_Semi_Supervised_2 = {
    'question': (
        'Which of the following describes a "pseudo-labeling" approach in semi-supervised learning? (Probability of appearing on test: 0.694)'
    ),
    'options_list': [
        'A. Generating synthetic labels for unlabeled data and training on the confident ones.',
        'B. Using clustering methods to assign labels to unlabeled data.',
        'C. Creating surrogate tasks to force feature learning from unlabeled data.',
        'D. Learning low-dimensional feature representations to improve classification accuracy.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Pseudo-labeling involves training a model on labeled data, using it to predict labels for unlabeled data, selecting confident predictions, and iteratively retraining the model on these predictions.'
    ),
    'chapter_information': 'Semi-Supervised Learning'
}

question_Self_Supervised_1 = {
    'question': (
        'Which of the following is NOT an example of a surrogate task for self-supervised learning? (Probability of appearing on test: 0.839)'
    ),
    'options_list': [
        'A. Predicting the amount of rotation applied to an image.',
        'B. Reconstructing an input image using an autoencoder.',
        'C. Generating pseudo-labels from labeled data for semi-supervised training.',
        'D. Learning a compressed representation of the data using dimensionality reduction.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Pseudo-labeling is a semi-supervised technique, not a surrogate task. Surrogate tasks are designed to force feature learning without labels, such as rotation prediction or reconstruction.'
    ),
    'chapter_information': 'Self-Supervised Learning'
}

question_Reinforcement_Learning_1 = {
    'question': (
        'Which of the following is TRUE about reinforcement learning as described in the module? (Probability of appearing on test: 0.508)'
    ),
    'options_list': [
        'A. It relies on dense supervision for each state-action pair.',
        'B. Rewards can be sparse or dense, depending on the environment.',
        'C. The agent directly learns the optimal action without interacting with the environment.',
        'D. The environment must always be fully observable to the agent.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In reinforcement learning, rewards can be sparse (e.g., win/lose signals in chess) or dense (e.g., continuous score updates in Atari games). The agent interacts with the environment to learn optimal actions.'
    ),
    'chapter_information': 'Reinforcement Learning'
}

question_GANs_VAEs_1 = {
    'question': (
        'What is a key difference between Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs)? (Probability of appearing on test: 0.972)'
    ),
    'options_list': [
        'A. GANs explicitly model the joint probability distribution, while VAEs do not.',
        'B. VAEs tend to produce sharper images than GANs.',
        'C. GANs involve a generator-discriminator setup, while VAEs rely on encoder-decoder architectures.',
        'D. Both GANs and VAEs use supervised labels to generate realistic data.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'GANs consist of a generator and discriminator network that compete during training, while VAEs use an encoder-decoder framework to learn latent representations and reconstruct inputs.'
    ),
    'chapter_information': 'Generative Models'
}

question_Self_Supervised_2 = {
    'question': (
        'Self-supervised learning uses labels derived from the data itself to train models. (Probability of appearing on test: 0.613)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Self-supervised learning relies on pseudo-labels or surrogate tasks generated from unlabeled data to drive training.'
    ),
    'chapter_information': 'Self-Supervised Learning'
}

question_Reinforcement_Learning_2 = {
    'question': (
        'Reinforcement learning always requires an explicitly known model of the environment. (Probability of appearing on test: 0.899)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Reinforcement learning can work with unknown environments, where the agent learns policies through interaction and feedback.'
    ),
    'chapter_information': 'Reinforcement Learning'
}

question_GANs_VAEs_2 = {
    'question': (
        'GANs and VAEs both require labeled data to generate new samples from the learned data distribution. (Probability of appearing on test: 0.780)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'GANs and VAEs are unsupervised methods that learn from unlabeled data to generate new samples.'
    ),
    'chapter_information': 'Generative Models'
}

question_Semi_Supervised_3 = {
    'question': (
        'The fixed match algorithm in semi-supervised learning combines labeled and unlabeled data by generating pseudo-labels and training with augmentations. (Probability of appearing on test: 0.661)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Fixed match uses pseudo-labels for unlabeled data, incorporating them into the training process with strong augmentations.'
    ),
    'chapter_information': 'Semi-Supervised Learning'
}

question_Reinforcement_Learning_3 = {
    'question': (
        'In reinforcement learning, Markov Decision Processes provide a framework for modeling sequential decision-making tasks. (Probability of appearing on test: 0.890)'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'MDPs formalize reinforcement learning tasks by defining states, actions, rewards, and transition probabilities.'
    ),
    'chapter_information': 'Reinforcement Learning'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_17_MPC = KC_MPC_QUESTIONS[:-1]
