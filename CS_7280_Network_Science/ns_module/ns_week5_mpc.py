# Multiple Choice Questions

granovetter_strength_of_weak_ties_question_1 = {
    'question': "According to Granovetter’s strength of weak ties hypothesis, why are weak ties more valuable than strong ties for accessing new information?",
    'options_list': [
        "Weak ties connect you to closer friends.",
        "Weak ties connect different parts of the social network, offering access to new information.",
        "Weak ties have more trust than strong ties.",
        "Weak ties are more likely to form bridges."
    ],
    'correct_answer': "Weak ties connect different parts of the social network, offering access to new information.",
    'explanation': "Weak ties provide access to information from other parts of the social network that are otherwise unreachable through strong ties.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

triadic_closure_question_1 = {
    'question': "What does triadic closure refer to in social networks?",
    'options_list': [
        "The formation of new ties between two people who have a common friend.",
        "The breaking of a friendship between two people who share a friend.",
        "A mechanism where weak ties are replaced with strong ties.",
        "The tendency of bridges to disappear over time."
    ],
    'correct_answer': "The formation of new ties between two people who have a common friend.",
    'explanation': "Triadic closure occurs when two people who share a mutual friend form a direct connection.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

local_bridge_question_1 = {
    'question': "What is a local bridge in a social network?",
    'options_list': [
        "A connection that only forms within a close-knit group.",
        "A tie between two nodes that have no friends in common, providing access to different parts of the network.",
        "A strong tie that connects two friends within the same group.",
        "A weak tie that directly connects two clusters of a network."
    ],
    'correct_answer': "A tie between two nodes that have no friends in common, providing access to different parts of the network.",
    'explanation': "A local bridge connects two parts of a network that would otherwise be far apart, without any shared friends.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

clustering_coefficient_question_1 = {
    'question': "The clustering coefficient of a node measures:",
    'options_list': [
        "The number of strong ties it has.",
        "How likely two friends of the node are also friends with each other.",
        "The number of weak ties the node forms.",
        "The probability of becoming a bridge in the network."
    ],
    'correct_answer': "How likely two friends of the node are also friends with each other.",
    'explanation': "The clustering coefficient indicates the probability that two friends of a node will also be friends with each other, capturing the level of interconnectedness.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

# True/False Questions

true_false_1 = {
    'question': "True or False: Strong ties are more likely to serve as bridges between different parts of a social network than weak ties.",
    'correct_answer': "False",
    'explanation': "Weak ties are more likely to serve as bridges because they connect different clusters of the network.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

true_false_2 = {
    'question': "True or False: Triadic closure refers to the process where two individuals who share a mutual friend are less likely to become friends.",
    'correct_answer': "False",
    'explanation': "Triadic closure refers to the increased likelihood of two individuals becoming friends if they share a mutual friend.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

true_false_3 = {
    'question': "True or False: Weak ties often provide more novel information than strong ties because they connect different clusters of the network.",
    'correct_answer': "True",
    'explanation': "Weak ties give access to parts of the network that are otherwise disconnected, offering new information.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}

true_false_4 = {
    'question': "True or False: If a node has two strong ties, it is more likely that a connection will form between the two connected individuals.",
    'correct_answer': "True",
    'explanation': "The concept of triadic closure suggests that strong ties lead to increased likelihood of connections forming between friends.",
    'chapter_information': 'Networks, Crowds, and Markets, Chapter 3.1, 3.2'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_5_MPC = KC_MPC_QUESTIONS[:-1]
