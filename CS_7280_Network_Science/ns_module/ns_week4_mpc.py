lesson_4_question_1 = {
    'question': "What did researchers observe in real networks in the late 1990s regarding degree distribution?",
    'options_list': [
        "Real networks follow a binomial degree distribution",
        "Real networks are well-modeled by random ER graphs",
        "Real networks often have highly skewed degree distributions",
        "The degree distribution of real networks cannot be measured"
    ],
    'correct_answer': "Real networks often have highly skewed degree distributions",
    'explanation': "In the late 1990s, researchers observed that real networks are very different from random ER graphs and often have highly skewed degree distributions, with power-law degree distributions being more appropriate in many cases.",
    'chapter_information': 'Topic: Degree Distribution of Real Networks, Lesson 4'
}

lesson_4_question_2 = {
    'question': "Which of the following is an example of a network that is better modeled by a power-law degree distribution?",
    'options_list': [
        "A protein-protein interaction network",
        "A random ER graph",
        "A regular grid network",
        "A complete graph"
    ],
    'correct_answer': "A protein-protein interaction network",
    'explanation': "Protein-protein interaction networks are examples of real-world networks where a power-law degree distribution better captures the large variability and skewness in the connectivity of the nodes.",
    'chapter_information': 'Topic: Real-World Networks, Lesson 4'
}

lesson_4_question_3 = {
    'question': "True or False: The Poisson distribution is a better model for highly skewed degree distributions in real-world networks.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The Poisson distribution is a poor model for real-world networks with highly skewed degree distributions. Power-law distributions are more appropriate because they capture the large variability and the probability of nodes with high degrees.",
    'chapter_information': 'Topic: Poisson Distribution vs. Power-Law Networks, Lesson 4'
}

lesson_4_question_4 = {
    'question': "In a log-log plot of degree distribution, what does a straight line indicate?",
    'options_list': [
        "The degree distribution follows a Poisson distribution",
        "The degree distribution is binomial",
        "The degree distribution follows a power law",
        "The network has a uniform degree distribution"
    ],
    'correct_answer': "The degree distribution follows a power law",
    'explanation': "A straight line in a log-log plot indicates a power-law distribution. This means that the probability of a node having degree k drops as a power law of k: \( p_k \sim k^{-\alpha} \).",
    'chapter_information': 'Topic: Power-Law Distributions, Lesson 4'
}

lesson_4_question_5 = {
    'question': "Why is the Poisson distribution considered a poor model for real-world networks?",
    'options_list': [
        "It cannot capture the large variability and skewness of degree distributions",
        "It only applies to directed networks",
        "It is a symmetric distribution",
        "It is only used for small networks"
    ],
    'correct_answer': "It cannot capture the large variability and skewness of degree distributions",
    'explanation': "The Poisson distribution is considered a poor model for real-world networks because it cannot capture the large variability and skewness of the degree distribution. In contrast, power-law distributions can explain the presence of highly connected nodes (hubs) in networks.",
    'chapter_information': 'Topic: Poisson vs Power-Law Networks, Lesson 4'
}

lesson_4_question_6 = {
    'question': "True or False: In a linear-linear scale plot, the Poisson distribution has a bell-shaped form, while the power-law distribution extends over several orders of magnitude.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In a linear-linear plot, the Poisson distribution forms a bell-shaped curve centered around its mean, whereas the power-law distribution extends over several orders of magnitude, highlighting the long tail of highly connected nodes in real-world networks.",
    'chapter_information': 'Topic: Poisson vs Power-Law Distributions, Lesson 4'
}

plotting_distribution_question_1 = {
    'question': "Why is plotting a power-law distribution on a linear-linear scale a bad way to visualize the distribution?",
    'options_list': [
        "It clearly shows the exponential decay",
        "It does not capture the power-law tail correctly",
        "It shows the binning too clearly",
        "It highlights high-degree nodes"
    ],
    'correct_answer': "It does not capture the power-law tail correctly",
    'explanation': "A linear-linear scale does not effectively show the tail of a power-law distribution. This is because the power-law distribution decays too quickly for a linear scale to display the high-degree nodes properly.",
    'chapter_information': 'Topic: Plotting Power-Law Distributions, Lesson 4'
}

plotting_distribution_question_2 = {
    'question': "What is the best approach to plot a power-law degree distribution according to the lesson?",
    'options_list': [
        "Linear-linear scale",
        "Log-log scale with linear binning",
        "Log-log scale with logarithmic binning",
        "Complementary Cumulative Distribution Function (C-CDF)"
    ],
    'correct_answer': "Complementary Cumulative Distribution Function (C-CDF)",
    'explanation': "Using the C-CDF is considered the best approach to plot a power-law degree distribution. It avoids the issues with binning and directly plots the probability of having a degree greater than or equal to \( k \).",
    'chapter_information': 'Topic: Plotting Power-Law Distributions, Lesson 4'
}

scale_free_networks_question_1 = {
    'question': "Why are power-law networks referred to as 'scale-free'?",
    'options_list': [
        "They do not have a typical scale for node degree",
        "They follow the Central Limit Theorem",
        "They have a finite variance",
        "They have nodes with the same degree"
    ],
    'correct_answer': "They do not have a typical scale for node degree",
    'explanation': "Power-law networks are referred to as 'scale-free' because the node degrees are highly variable, meaning there is no typical degree that most nodes have. Instead, there is a wide range of degrees, with some nodes having very high degrees (hubs).",
    'chapter_information': 'Topic: Scale-Free Nature of Power-Law Networks, Lesson 4'
}

scale_free_networks_question_2 = {
    'question': "True or False: In a power-law network with \( 2 < \alpha < 3 \), the variance is infinite.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In a power-law network with an exponent \( 2 < \alpha < 3 \), the mean exists, but the variance is infinite. This is because the tail of the distribution is heavy enough to make higher moments undefined.",
    'chapter_information': 'Topic: Scale-Free Nature of Power-Law Networks, Lesson 4'
}

maximum_degree_question_1 = {
    'question': "How does the maximum degree in a power-law network increase with the network size n?",
    'options_list': [
        "It increases linearly with n",
        "It increases logarithmically with n",
        "It remains constant",
        "It decreases as n increases"
    ],
    'correct_answer': "It increases logarithmically with n",
    'explanation': "In a power-law network, the maximum degree increases logarithmically with the network size \( n \), meaning that even for very large networks, the degree of the most connected nodes does not grow as fast as the size of the network.",
    'chapter_information': 'Topic: Maximum Degree in Power-Law Networks, Lesson 4'
}

maximum_degree_question_2 = {
    'question': "True or False: The maximum degree in a power-law network with \( \alpha = 3 \) grows with the square root of the network size \( n \).",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "When \( \alpha = 3 \), the maximum degree in a power-law network grows with the square root of the network size \( n \). This reflects a faster increase in degree compared to the logarithmic increase seen for smaller values of \( \alpha \).",
    'chapter_information': 'Topic: Maximum Degree in Power-Law Networks, Lesson 4'
}


random_failures_question_1 = {
    'question': "How do power-law networks respond to random failures compared to targeted attacks?",
    'options_list': [
        "They are more robust to random failures but more sensitive to targeted attacks",
        "They are equally sensitive to both random failures and targeted attacks",
        "They are more sensitive to random failures and more robust to targeted attacks",
        "They are equally robust to both random failures and targeted attacks"
    ],
    'correct_answer': "They are more robust to random failures but more sensitive to targeted attacks",
    'explanation': "Power-law networks are highly robust to random failures due to the presence of many low-degree nodes. However, they are very sensitive to targeted attacks because removing the high-degree hub nodes can cause the network to disintegrate.",
    'chapter_information': 'Topic: Random Failures and Targeted Attacks, Lesson 4'
}

random_failures_question_2 = {
    'question': "What is the critical threshold for random failures in a power-law network according to the lesson?",
    'options_list': [
        "Around \( f = 0.7 \)",
        "Around \( f = 0.15 \)",
        "Around \( f = 0.25 \)",
        "Around \( f = 0.5 \)"
    ],
    'correct_answer': "Around \( f = 0.7 \)",
    'explanation': "For random failures in power-law networks, the largest connected component remains intact until a large fraction of nodes (around \( f = 0.7 \)) is removed, reflecting the robustness of these networks.",
    'chapter_information': 'Topic: Random Failures and Targeted Attacks, Lesson 4'
}

random_failures_question_3 = {
    'question': "True or False: Poisson networks are more sensitive to random failures than power-law networks.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "Poisson networks disintegrate quickly under random failures because they lack high-degree hubs, which power-law networks have to maintain connectivity even after significant node loss.",
    'chapter_information': 'Topic: Random Failures and Targeted Attacks, Lesson 4'
}

degree_preserving_randomization_question_1 = {
    'question': "What does degree-preserving randomization achieve?",
    'options_list': [
        "It keeps the degree distribution the same while randomizing the edges",
        "It changes the degree distribution",
        "It adds new nodes to the network",
        "It removes nodes from the network"
    ],
    'correct_answer': "It keeps the degree distribution the same while randomizing the edges",
    'explanation': "Degree-preserving randomization shuffles the edges of a network while keeping the degree of each node the same. This allows for studying properties of the network that depend on the structure but not on the degree distribution.",
    'chapter_information': 'Topic: Degree-Preserving Randomization, Lesson 4'
}

degree_preserving_randomization_question_2 = {
    'question': "Why is degree-preserving randomization useful?",
    'options_list': [
        "It allows researchers to isolate network properties that are not dependent on the degree distribution",
        "It helps in adding new edges to the network",
        "It simplifies the network by removing nodes",
        "It increases the degree variance of the network"
    ],
    'correct_answer': "It allows researchers to isolate network properties that are not dependent on the degree distribution",
    'explanation': "By preserving the degree distribution while randomizing the edges, degree-preserving randomization helps researchers identify network properties that are due to the structure of connections rather than the degree distribution itself.",
    'chapter_information': 'Topic: Degree-Preserving Randomization, Lesson 4'
}

degree_preserving_randomization_question_3 = {
    'question': "True or False: Degree-preserving randomization can be used to study the impact of network topology on certain properties without changing the number of edges or nodes.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "Degree-preserving randomization keeps the number of edges and nodes the same while randomizing the topology, making it useful for studying how the structure affects network properties.",
    'chapter_information': 'Topic: Degree-Preserving Randomization, Lesson 4'
}


average_degree_nearest_neighbor_question_1 = {
    'question': "What is the key characteristic of a power-law network with respect to the average neighbor degree?",
    'options_list': [
        "The average neighbor degree is always equal to the network’s average degree",
        "The average neighbor degree is typically higher than the network’s average degree",
        "The average neighbor degree is typically lower than the network’s average degree",
        "The average neighbor degree is equal to the degree of the highest-degree node"
    ],
    'correct_answer': "The average neighbor degree is typically higher than the network’s average degree",
    'explanation': "In power-law networks, the average neighbor degree can be much higher than the network's average degree, intensifying the friendship paradox.",
    'chapter_information': 'Topic: Average Degree of the Nearest Neighbor in a Power-law Network, Lesson 4'
}

configuration_model_question_1 = {
    'question': "In the configuration model, how is the network generated?",
    'options_list': [
        "By preferentially attaching new nodes to nodes with higher degree",
        "By randomly selecting nodes and connecting their stubs",
        "By iteratively adding edges between randomly selected nodes",
        "By rewiring existing edges while preserving degree distribution"
    ],
    'correct_answer': "By randomly selecting nodes and connecting their stubs",
    'explanation': "The configuration model generates a network by selecting nodes and connecting their available 'stubs' randomly until no stubs remain.",
    'chapter_information': 'Topic: Configuration Model, Lesson 4'
}

configuration_model_question_2 = {
    'question': "What is a key feature of the configuration model?",
    'options_list': [
        "It creates networks with a uniform degree distribution",
        "It can create self-loops and multi-edges",
        "It preserves the number of nodes but changes the degree distribution",
        "It does not allow the formation of hubs"
    ],
    'correct_answer': "It can create self-loops and multi-edges",
    'explanation': "The configuration model can create self-loops (a node connecting to itself) and multi-edges (two or more edges between the same pair of nodes), although these features may be removed in some applications.",
    'chapter_information': 'Topic: Configuration Model, Lesson 4'
}

preferential_attachment_question_1 = {
    'question': "What is the preferential attachment mechanism based on?",
    'options_list': [
        "New nodes are randomly connected to existing nodes",
        "New nodes preferentially connect to nodes with higher degree",
        "New nodes connect to nodes with the smallest degree",
        "New nodes attach to isolated nodes only"
    ],
    'correct_answer': "New nodes preferentially connect to nodes with higher degree",
    'explanation': "In the preferential attachment model, new nodes are more likely to connect to nodes that already have a higher degree, which is the 'rich get richer' effect.",
    'chapter_information': 'Topic: Preferential Attachment Model, Lesson 4'
}

preferential_attachment_question_2 = {
    'question': "True or False: The configuration model explains how networks can acquire power-law degree distributions through node growth.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The configuration model generates networks with a given degree distribution but does not explain how networks grow or acquire a power-law distribution. The preferential attachment model explains this growth mechanism.",
    'chapter_information': 'Topic: Preferential Attachment Model, Lesson 4'
}

preferential_attachment_question_3 = {
    'question': "How would you modify the preferential attachment model to produce a power-law network with an exponent between 2 and 3?",
    'options_list': [
        "Increase the number of edges added by each new node",
        "Decrease the number of edges added by each new node",
        "Change the degree distribution to be uniform",
        "Remove all multi-edges and self-loops"
    ],
    'correct_answer': "Increase the number of edges added by each new node",
    'explanation': "To achieve an exponent between 2 and 3, increasing the number of edges added by each new node increases the likelihood of creating higher-degree nodes, which alters the degree distribution.",
    'chapter_information': 'Topic: Preferential Attachment Model, Lesson 4'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_4_MPC = KC_MPC_QUESTIONS[:-1]
