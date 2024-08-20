easley_kleinberg_ch2_question_1 = {
    'question': "What is the difference between a directed graph and an undirected graph?",
    'options_list': [
        'A directed graph has weighted edges, while an undirected graph does not',
        'A directed graph allows multiple edges between nodes, while an undirected graph does not',
        'A directed graph has edges with a direction, while an undirected graph does not',
        'A directed graph only connects nodes of the same type, while an undirected graph does not'
    ],
    'correct_answer': 'A directed graph has edges with a direction, while an undirected graph does not',
    'explanation': "In a directed graph, the edges have a specific direction indicating the relationship from one node to another, whereas in an undirected graph, the edges have no direction, representing a mutual relationship.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_2 = {
    'question': "What does a 'path' in a graph represent?",
    'options_list': [
        'A loop within a graph where the first and last nodes are the same',
        'A sequence of edges that connect one node to itself',
        'A sequence of nodes where each consecutive pair is connected by an edge',
        'A set of unconnected nodes in a graph'
    ],
    'correct_answer': 'A sequence of nodes where each consecutive pair is connected by an edge',
    'explanation': "A path in a graph is defined as a sequence of nodes where each consecutive pair of nodes is connected by an edge, showing how one can travel from one node to another through the network.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_3 = {
    'question': "What is a 'cycle' in the context of graph theory?",
    'options_list': [
        'A path that does not repeat any nodes',
        'A path with at least three edges where the first and last nodes are the same',
        'A sequence of nodes where each node has exactly two neighbors',
        'A graph where all nodes are connected in a single loop'
    ],
    'correct_answer': 'A path with at least three edges where the first and last nodes are the same',
    'explanation': "A cycle is a special type of path in a graph where the path starts and ends at the same node, and all other nodes in the cycle are distinct.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_4 = {
    'question': "In graph theory, what does it mean for a graph to be 'connected'?",
    'options_list': [
        'Every node has at least one edge',
        'There is a path between every pair of nodes',
        'Every node is connected to a central hub',
        'All nodes are part of at least one cycle'
    ],
    'correct_answer': 'There is a path between every pair of nodes',
    'explanation': "A graph is considered connected if there is a path between every pair of nodes, meaning you can travel from any node to any other node within the graph.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_5 = {
    'question': "What is a 'connected component' in a graph?",
    'options_list': [
        'A subset of nodes in which every node is connected to every other node, and no node is connected to any node outside this subset',
        'A group of nodes that all have the same degree',
        'A part of the graph where all edges are directed',
        'A cluster of nodes with no edges connecting them to the rest of the graph'
    ],
    'correct_answer': 'A subset of nodes in which every node is connected to every other node, and no node is connected to any node outside this subset',
    'explanation': "A connected component is a subset of a graph in which any two nodes are connected by paths, and which is connected to no additional nodes in the rest of the graph.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_6 = {
    'question': "What is the significance of a 'giant component' in a graph?",
    'options_list': [
        'It is the only component in a graph that is connected',
        'It contains the majority of the nodes in the graph and is typically unique',
        'It is the smallest connected component in a graph',
        'It represents a graph where all nodes are directly connected to each other'
    ],
    'correct_answer': 'It contains the majority of the nodes in the graph and is typically unique',
    'explanation': "A giant component in a graph is a connected component that contains a significant fraction of all the nodes in the graph. When it exists, it is usually unique and represents the largest connected subgraph.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_7 = {
    'question': "In the context of graph theory, what is the purpose of 'breadth-first search'?",
    'options_list': [
        'To find the longest path in a graph',
        'To discover the shortest path between two nodes',
        'To explore all nodes of a graph layer by layer starting from a given node',
        'To identify all cycles in a graph'
    ],
    'correct_answer': 'To explore all nodes of a graph layer by layer starting from a given node',
    'explanation': "Breadth-first search is an algorithm used to explore a graph by visiting all nodes level by level starting from a given node, which helps in finding the shortest path to all reachable nodes from the starting point.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_8 = {
    'question': "How is the 'small-world phenomenon' best described?",
    'options_list': [
        'The idea that most networks are completely disconnected',
        'The observation that most nodes in a large network are directly connected to all other nodes',
        'The concept that most nodes in a large network can be reached from any other node by a small number of steps',
        'The idea that networks grow at a small, constant rate'
    ],
    'correct_answer': 'The concept that most nodes in a large network can be reached from any other node by a small number of steps',
    'explanation': "The small-world phenomenon suggests that in large networks, most nodes can be reached from any other node through a relatively small number of intermediate steps, often referred to as 'six degrees of separation.'",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_9 = {
    'question': "What does it mean for a graph to have 'cycles'?",
    'options_list': [
        'The graph has a path that returns to the starting node',
        'The graph has a path that includes every node exactly once',
        'The graph has no edges connecting its nodes',
        'The graph has multiple edges between some pairs of nodes'
    ],
    'correct_answer': 'The graph has a path that returns to the starting node',
    'explanation': "A cycle in a graph is a path that starts and ends at the same node, with each node in the cycle being distinct except for the starting/ending node.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}

easley_kleinberg_ch2_question_10 = {
    'question': "What is the 'diameter' of a graph?",
    'options_list': [
        'The maximum degree of any node in the graph',
        'The maximum distance between any pair of nodes in the graph',
        'The number of edges in the graph',
        'The average number of connections per node'
    ],
    'correct_answer': 'The maximum distance between any pair of nodes in the graph',
    'explanation': "The diameter of a graph is defined as the maximum distance between any pair of nodes, representing the longest shortest path in the network.",
    'chapter_information': 'Chapter 2: D. Easley and J. Kleinberg, Networks, Crowds and Markets, Cambridge Univ Press, 2010'
}


barabasi_ch2_question_1 = {
    'question': "What was Euler's key insight in solving the Bridges of Königsberg problem?",
    'options_list': [
        "Representing the land areas and bridges as a graph and analyzing the degrees of nodes",
        "Counting the number of possible paths in the city",
        "Constructing a physical model of the bridges to simulate different paths",
        "Analyzing the length and width of each bridge"
    ],
    'correct_answer': "Representing the land areas and bridges as a graph and analyzing the degrees of nodes",
    'explanation': "Euler's key insight was to represent the land areas as nodes and the bridges as edges of a graph. He then showed that for a path to exist that crosses each bridge exactly once, there must be exactly zero or two nodes with an odd number of edges. In the Königsberg problem, there were four such nodes, making the desired path impossible.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_2 = {
    'question': "How does Barabási describe the relationship between networks and graphs?",
    'options_list': [
        "Networks and graphs are entirely different concepts used in separate fields of study",
        "Networks represent real-world systems, while graphs are their mathematical representations",
        "Graphs are more complex structures that can only be used to represent specific types of networks",
        "Networks are theoretical constructs, while graphs are practical tools for data analysis"
    ],
    'correct_answer': "Networks represent real-world systems, while graphs are their mathematical representations",
    'explanation': "In Barabási's framework, networks refer to real-world systems of interconnected components, while graphs are the mathematical representations of these networks. The terms are often used interchangeably, but they highlight the difference between the practical application and theoretical study.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_3 = {
    'question': "What does the degree of a node represent in a network?",
    'options_list': [
        "The number of nodes in the entire network",
        "The total number of edges connected to that node",
        "The shortest path length from that node to any other node",
        "The average distance between the node and all other nodes in the network"
    ],
    'correct_answer': "The total number of edges connected to that node",
    'explanation': "The degree of a node in a network represents the number of edges (or links) connected to it. It is a fundamental property that helps in understanding the node's connectivity within the network.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_4 = {
    'question': "What is a bipartite network?",
    'options_list': [
        "A network where all nodes have an equal degree",
        "A network that has exactly two connected components",
        "A network whose nodes can be divided into two distinct sets with edges only between nodes from different sets",
        "A network in which each node is connected to exactly two other nodes"
    ],
    'correct_answer': "A network whose nodes can be divided into two distinct sets with edges only between nodes from different sets",
    'explanation': "A bipartite network is one in which nodes can be divided into two disjoint sets, U and V, with edges only between nodes from different sets (U to V), and no edges within the same set.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_5 = {
    'question': "Why are most real-world networks considered sparse?",
    'options_list': [
        "Because they have fewer nodes than links",
        "Because the number of links is much smaller than the maximum possible number of links in a complete graph",
        "Because they contain a large number of disconnected components",
        "Because each node in the network is connected to every other node"
    ],
    'correct_answer': "Because the number of links is much smaller than the maximum possible number of links in a complete graph",
    'explanation': "Real-world networks are considered sparse because the number of links (L) is much smaller than the maximum possible number of links (Lmax) in a complete graph, meaning that only a small fraction of all possible connections are realized.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_6 = {
    'question': "What is the significance of the adjacency matrix in network analysis?",
    'options_list': [
        "It stores only the nodes of the network without any link information",
        "It is a visual representation of the network",
        "It provides a way to represent the presence or absence of links between nodes in a matrix format",
        "It is used to calculate the shortest path between any two nodes in the network"
    ],
    'correct_answer': "It provides a way to represent the presence or absence of links between nodes in a matrix format",
    'explanation': "The adjacency matrix is a matrix representation of a network where each element indicates whether a pair of nodes is connected by a link. It is particularly useful for mathematical and computational analysis of network properties.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_7 = {
    'question': "What does the clustering coefficient measure in a network?",
    'options_list': [
        "The total number of nodes in a network",
        "The number of nodes connected to a single node",
        "The degree to which the neighbors of a node are interconnected",
        "The maximum path length between any two nodes in the network"
    ],
    'correct_answer': "The degree to which the neighbors of a node are interconnected",
    'explanation': "The clustering coefficient measures the extent to which the neighbors of a given node are connected to each other. A high clustering coefficient indicates that a node’s neighbors are likely to form a tightly-knit group.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_8 = {
    'question': "Why are real networks often characterized as having a 'small-world' property?",
    'options_list': [
        "Because they are disconnected and isolated",
        "Because they consist of only a few nodes and links",
        "Because they have short average path lengths despite their large size",
        "Because they have very high clustering coefficients"
    ],
    'correct_answer': "Because they have short average path lengths despite their large size",
    'explanation': "Real-world networks often exhibit the 'small-world' property, where even though the network is large, the average path length between any two nodes is relatively short, allowing for efficient communication or interaction across the network.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_9 = {
    'question': "What is the relationship between node degree and the average clustering coefficient in a network?",
    'options_list': [
        "Nodes with higher degrees always have higher clustering coefficients",
        "Nodes with higher degrees tend to have lower clustering coefficients",
        "The clustering coefficient is independent of the node degree",
        "Nodes with higher degrees tend to have no clustering coefficient"
    ],
    'correct_answer': "Nodes with higher degrees tend to have lower clustering coefficients",
    'explanation': "In many networks, nodes with higher degrees tend to have lower clustering coefficients, meaning that highly connected nodes (hubs) are less likely to have their neighbors interconnected, leading to a more hub-and-spoke structure.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

barabasi_ch2_question_10 = {
    'question': "How is a bipartite network different from a regular network?",
    'options_list': [
        "It contains nodes that can have self-loops",
        "It has a strict hierarchical structure with nodes at different levels",
        "It has two distinct sets of nodes, with edges only between nodes from different sets",
        "It is a network where all nodes are connected to every other node"
    ],
    'correct_answer': "It has two distinct sets of nodes, with edges only between nodes from different sets",
    'explanation': "A bipartite network consists of two distinct sets of nodes, with edges only existing between nodes from different sets, and no edges within the same set.",
    'chapter_information': 'Chapter 2: A-L. Barabási, Network Science, 2015'
}

fibonacci_heaps_question_1 = {
    'question': "What is the primary advantage of a Fibonacci heap compared to other heap data structures?",
    'options_list': [
        "It has a better worst-case time complexity for all operations",
        "It allows all operations to be performed in constant time",
        "It has an amortized constant time for decrease-key and insert operations",
        "It requires less memory to store the heap"
    ],
    'correct_answer': "It has an amortized constant time for decrease-key and insert operations",
    'explanation': "The primary advantage of Fibonacci heaps is that they provide amortized constant time for operations like insert and decrease-key, making them highly efficient for algorithms like Dijkstra's shortest path.",
    'chapter_information': 'Topic: Fibonacci Heaps, Source: Wikipedia'
}

fibonacci_heaps_question_2 = {
    'question': "In a Fibonacci heap, what happens during the 'decrease-key' operation?",
    'options_list': [
        "The key is simply decreased, with no other structural changes",
        "The node with the decreased key is cut from its parent and added to the root list if it becomes smaller than its parent's key",
        "All nodes are rearranged to maintain the heap property",
        "The entire heap is rebuilt to ensure the minimum key is at the root"
    ],
    'correct_answer': "The node with the decreased key is cut from its parent and added to the root list if it becomes smaller than its parent's key",
    'explanation': "During the decrease-key operation in a Fibonacci heap, if the decreased key violates the heap property with its parent, the node is cut from its parent and added to the root list to maintain the heap's structural properties.",
    'chapter_information': 'Topic: Fibonacci Heaps, Source: Wikipedia'
}

fibonacci_heaps_question_3 = {
    'question': "What is the amortized time complexity of the 'extract-min' operation in a Fibonacci heap?",
    'options_list': [
        "O(1)",
        "O(log n)",
        "O(n log n)",
        "O(n)"
    ],
    'correct_answer': "O(log n)",
    'explanation': "The extract-min operation in a Fibonacci heap has an amortized time complexity of O(log n), making it efficient for operations that require frequent minimum element extraction.",
    'chapter_information': 'Topic: Fibonacci Heaps, Source: Wikipedia'
}


kosaraju_algorithm_question_1 = {
    'question': "What is the main purpose of Kosaraju's algorithm?",
    'options_list': [
        "To find the shortest path between two nodes in a graph",
        "To sort the nodes of a graph in topological order",
        "To find all strongly connected components (SCCs) in a directed graph",
        "To detect cycles in an undirected graph"
    ],
    'correct_answer': "To find all strongly connected components (SCCs) in a directed graph",
    'explanation': "Kosaraju's algorithm is used to find all strongly connected components (SCCs) in a directed graph. It is efficient and uses two passes of depth-first search.",
    'chapter_information': 'Topic: Kosaraju\'s Algorithm, Source: Wikipedia'
}

kosaraju_algorithm_question_2 = {
    'question': "Which of the following is a correct step in Kosaraju's algorithm?",
    'options_list': [
        "Perform a breadth-first search to find all SCCs",
        "Reverse the direction of all edges in the graph, then perform DFS in the order of the first DFS's finishing times",
        "Sort all nodes by in-degree, then perform a topological sort",
        "Use a priority queue to keep track of the nodes with the lowest out-degree"
    ],
    'correct_answer': "Reverse the direction of all edges in the graph, then perform DFS in the order of the first DFS's finishing times",
    'explanation': "One key step in Kosaraju's algorithm is to reverse the direction of all edges in the graph, and then perform a depth-first search (DFS) in the order determined by the finishing times from the first DFS.",
    'chapter_information': 'Topic: Kosaraju\'s Algorithm, Source: Wikipedia'
}

kosaraju_algorithm_question_3 = {
    'question': "What is the time complexity of Kosaraju's algorithm?",
    'options_list': [
        "O(V^2)",
        "O(V + E)",
        "O(V log V)",
        "O(E log V)"
    ],
    'correct_answer': "O(V + E)",
    'explanation': "Kosaraju's algorithm runs in O(V + E) time, where V is the number of vertices and E is the number of edges. This efficiency makes it a powerful tool for finding SCCs in large graphs.",
    'chapter_information': 'Topic: Kosaraju\'s Algorithm, Source: Wikipedia'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
