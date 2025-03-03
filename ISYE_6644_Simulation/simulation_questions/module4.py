question_1_simulation_phases = {
    'question': (
        "Which of the following is not a standard phase in conducting a simulation study?\n\n"
        "A. Defining the research problem\n"
        "B. Building and verifying the simulation model\n"
        "C. Running computer experiments and analyzing results\n"
        "D. Overlooking data collection procedures"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "D. Overlooking data collection procedures",
    'explanation': (
        "Every successful simulation study requires careful data collection to ensure that the model reflects the real "
        "system accurately. Ignoring data collection would compromise the study, making option D the correct choice as "
        "the non-essential (in fact, harmful) step."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_2_simulation_state = {
    'question': (
        "TRUE or FALSE: In simulation modeling, the 'state' of the system includes all the information needed to determine "
        "its future behavior without additional external data.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A. True",
    'explanation': (
        "The system state in a simulation is defined as the complete set of variables that describes the current condition "
        "of the system. This comprehensive snapshot ensures that, together with future events, the system's evolution can be "
        "determined without needing extra external information."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_3_simulation_attributes = {
    'question': (
        "In the context of simulation, characteristics such as processing speed, customer priority, or reliability are best "
        "described as:\n\n"
        "A. Parameters\n"
        "B. Attributes\n"
        "C. Variables\n"
        "D. States"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B. Attributes",
    'explanation': (
        "Attributes are the inherent characteristics or properties of entities within the simulation. They help define "
        "differences among entities (e.g., varying speeds or priorities) and are essential for modeling behavior accurately."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_4_discrete_event_components = {
    'question': (
        "TRUE or FALSE: In discrete-event simulation, the simulation clock and the event calendar are the central components "
        "that drive the execution of the model.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A. True",
    'explanation': (
        "The simulation clock keeps track of time progression, while the event calendar (or future event list) schedules and "
        "organizes events in chronological order. Together, they form the core mechanism that advances the simulation."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_5_event_calendar_operations = {
    'question': (
        "Which operations can be performed on the event calendar (future event list) in a discrete-event simulation?\n\n"
        "A. Adding new events as they are scheduled\n"
        "B. Removing events once they occur\n"
        "C. Rescheduling events if system conditions change\n"
        "D. All of the above"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "D. All of the above",
    'explanation': (
        "The event calendar is dynamic; simulation software allows you to insert new events, delete events that have already "
        "been processed, and update (or reschedule) events as needed. Therefore, all the listed operations are valid."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_6_simulation_technique = {
    'question': (
        "What is the primary simulation technique typically used in software like Arena?\n\n"
        "A. Continuous Simulation\n"
        "B. Monte Carlo Simulation\n"
        "C. Discrete-Event Simulation\n"
        "D. Hybrid Simulation"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "C. Discrete-Event Simulation",
    'explanation': (
        "Arena and similar simulation tools primarily use discrete-event simulation, which focuses on modeling systems where "
        "changes occur at distinct points in time (events), rather than continuously over time."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_7_simulation_software_selection = {
    'question': (
        "When selecting a simulation software package, which of the following factors is most important to consider?\n\n"
        "A. The overall cost of the software\n"
        "B. Its ease of use and learning curve\n"
        "C. Its compatibility with your modeling approach and random variate generation capabilities\n"
        "D. Its output analysis and reporting features\n"
        "E. All of the above"
    ),
    'options_list': ["A", "B", "C", "D", "E"],
    'correct_answer': "E. All of the above",
    'explanation': (
        "A comprehensive evaluation of simulation software should include cost, usability, alignment with the chosen modeling "
        "approach (such as discrete-event simulation), robust random number generation for stochastic modeling, and effective "
        "output analysis features. All these factors together determine the software’s suitability for your needs."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_1_simulation_tasks = {
    'question': (
        "In developing a simulation model, which of the following is not a fundamental task? (Select all that apply.)\n\n"
        "A. Clearly defining the problem and objectives\n"
        "B. Establishing the system’s state variables\n"
        "C. Running unplanned random code without testing\n"
        "D. Designing experiments for output analysis\n"
        "E. Ensuring that the model is verified and validated\n"
        "F. Taking an unscheduled break to check social media"
    ),
    'options_list': ["A", "B", "C", "D", "E", "F"],
    'correct_answer': ["C", "F"],
    'explanation': (
        "Successful simulation model development involves structured steps like problem definition, state variable "
        "identification, experimental design, and model verification/validation. Options C and F represent ad hoc "
        "or irrelevant actions that do not contribute to a robust simulation study."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_2_state_variables = {
    'question': (
        "True or False: In simulation modeling, state variables are the minimal set of parameters required to completely "
        "describe the system at any given time.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A",
    'explanation': (
        "State variables capture all necessary information about the system at a specific moment, ensuring that the "
        "future evolution of the system can be determined solely based on these variables and scheduled events."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_3_entity_attributes = {
    'question': (
        "Which term best describes the inherent properties (such as size, priority, or type) of an entity within a simulation model?\n\n"
        "A. Attributes\n"
        "B. Parameters\n"
        "C. Variables\n"
        "D. Events"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "A",
    'explanation': (
        "Attributes are the defining characteristics of entities. They differentiate one entity from another and "
        "influence how the entity interacts with the system. Parameters and variables may also influence the model, "
        "but the inherent qualities of an entity are best called attributes."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_4_discrete_event_clock = {
    'question': (
        "True or False: In a discrete-event simulation, the simulation clock is a programmed variable that advances only "
        "when scheduled events occur, and it does not necessarily correlate with real-world elapsed time.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A",
    'explanation': (
        "The simulation clock is used to track the progress of simulation time rather than real time. It “jumps” "
        "from one event time to the next, meaning its advancement is determined by the occurrence of events in the model."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_5_simulation_state_events = {
    'question': (
        "Which of the following events would typically trigger a change in the simulation state? (Select all that apply.)\n\n"
        "A. A customer arriving at a service counter\n"
        "B. The completion of a transaction\n"
        "C. A scheduled maintenance event for equipment\n"
        "D. A decorative banner changing color on the simulation background"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': ["A", "B", "C"],
    'explanation': (
        "Events that affect the system’s dynamics (like arrivals, service completions, and equipment breakdowns/maintenance) "
        "change the simulation state. A decorative banner changing color is cosmetic and does not impact the underlying process."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_6_fixed_time_step = {
    'question': (
        "True or False: A fixed time-step advancement method is especially common in simulations that solve differential "
        "equations describing continuous processes.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A",
    'explanation': (
        "Fixed time-step methods are widely used in continuous simulations (e.g., for solving differential equations) where "
        "the model state is updated at regular, predetermined intervals."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_7_next_event_advance = {
    'question': (
        "Which statement best describes the next-event time advancement strategy in discrete-event simulation?\n\n"
        "A. The clock advances in fixed increments regardless of event timings.\n"
        "B. The clock leaps directly to the time of the next scheduled event.\n"
        "C. The clock continuously ticks in real time alongside the simulation.\n"
        "D. The clock remains stationary until the user manually advances it."
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B",
    'explanation': (
        "The next-event mechanism updates the simulation clock by jumping directly to the time of the next event in the list, "
        "thus efficiently simulating systems where events occur at irregular intervals."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_8_future_events_list = {
    'question': (
        "True or False: The future events list (FEL) in a discrete-event simulation holds only events scheduled to occur in "
        "the future and is updated dynamically as events occur or new ones are scheduled.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A",
    'explanation': (
        "The FEL is a key data structure that keeps track of all upcoming events in the simulation. It is continually "
        "updated—events are inserted, deleted, or rescheduled—as the simulation state changes."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_9_process_interaction = {
    'question': (
        "In simulation modeling, which approach is characterized by defining the behavior of individual entities as they "
        "interact with various processes in the system?\n\n"
        "A. Next-Event Scheduling\n"
        "B. Process-Interaction Modeling\n"
        "C. Fixed-Increment Simulation\n"
        "D. Differential Equation Modeling"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "B",
    'explanation': (
        "Process-interaction modeling focuses on describing how individual entities (such as customers or parts) flow through "
        "processes in the system, with the simulation software managing the sequence of events automatically."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_10_process_interaction_tools = {
    'question': (
        "True or False: In simulation tools based on the process-interaction paradigm, the underlying engine automatically "
        "manages the sequencing and timing of events for you.\n\n"
        "A. True\n"
        "B. False"
    ),
    'options_list': ["A", "B"],
    'correct_answer': "A",
    'explanation': (
        "Process-interaction simulation environments (like many commercial tools) provide built-in mechanisms that handle "
        "event scheduling and sequencing, allowing modelers to focus on defining processes and entity behaviors."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}

question_11_simulation_software_evaluation = {
    'question': (
        "Which of the following factors is least relevant when evaluating a simulation software package?\n\n"
        "A. The cost of the software\n"
        "B. The compatibility with your chosen modeling approach\n"
        "C. The available documentation and support\n"
        "D. The aesthetic design of the software’s icon"
    ),
    'options_list': ["A", "B", "C", "D"],
    'correct_answer': "D",
    'explanation': (
        "Key factors in selecting simulation software include cost, ease of use, compatibility with the intended modeling "
        "approach, and the quality of documentation/support. The aesthetic design of the software’s icon is trivial by comparison."
    ),
    'chapter_information': "Week 5 - GPT 03-mini Generated"
}


simulation_question_1 = {
    'question': "Which of the following is not a critical step in a simulation study?",
    'options_list': ['A. Data collection', 'B. Model verification', 'C. Hiring a graphic designer', 'D. Scenario analysis'],
    'correct_answer': "C. Hiring a graphic designer",
    'explanation': (
        "Correct! Graphic design is generally not a part of the core simulation steps like data collection, "
        "verification, or scenario analysis."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_2 = {
    'question': "TRUE or FALSE?\nThe system state includes all information needed to resume a simulation from a saved point.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Correct! The system state captures all necessary variables (e.g., queue lengths, resource statuses) "
        "to restart the simulation from a specific point."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_3 = {
    'question': "Properties like a customer’s age or an order’s type are examples of:",
    'options_list': ['A. Variables', 'B. Resources', 'C. Activities', 'D. Attributes'],
    'correct_answer': "D. Attributes",
    'explanation': (
        "Correct! Attributes are properties specific to entities (e.g., a customer's age or an order's type), "
        "whereas variables are system-wide."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_4 = {
    'question': "Which two components drive discrete-event simulation execution?",
    'options_list': ['A. Resource spreadsheet and Process module', 'B. Simulation clock and Future Event List', 
                     'C. Create module and Dispose module', 'D. Variables and Attributes'],
    'correct_answer': "B. Simulation clock and Future Event List",
    'explanation': (
        "Correct! The simulation clock keeps track of time, while the Future Event List schedules future events. "
        "Together, they are the backbone of discrete-event simulation."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_5 = {
    'question': "TRUE or FALSE?\nThe Future Event List only allows adding new events, not modifying existing ones.",
    'options_list': ['True', 'False'],
    'correct_answer': "False",
    'explanation': (
        "Correct! Events can be added, modified, or removed in the Future Event List based on their priority or scheduled time."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_6 = {
    'question': "Which modeling approach focuses on entity flow and resource interactions?",
    'options_list': ['A. Event-Scheduling', 'B. Activity-Centric', 'C. Process-Interaction', 'D. Continuous Modeling'],
    'correct_answer': "C. Process-Interaction",
    'explanation': (
        "Correct! Process-Interaction (used in Arena) focuses on the flow of entities and their interactions with resources."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_7 = {
    'question': "When choosing simulation software, which factor is least important?",
    'options_list': ['A. Cost', 'B. Built-in statistical tools', 'C. Brand of the developer’s laptop', 'D. Ease of animation'],
    'correct_answer': "C. Brand of the developer’s laptop",
    'explanation': (
        "Correct! Hardware specifications (e.g., the brand of the laptop) are less important than software features like statistical tools, cost, or animation quality."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_8 = {
    'question': "TRUE or FALSE?\nA “customer type” (e.g., VIP vs. regular) is best modeled as an attribute.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Correct! A customer type is an entity-specific trait and should be modeled as an attribute (e.g., VIP, regular)."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_9 = {
    'question': "Which term refers to global values that affect the entire simulation?",
    'options_list': ['A. Attributes', 'B. Variables', 'C. Resources', 'D. Queues'],
    'correct_answer': "B. Variables",
    'explanation': (
        "Correct! Variables are global values that affect the entire system (e.g., total revenue or system-wide statistics), "
        "unlike attributes, which belong to individual entities."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}

simulation_question_10 = {
    'question': "TRUE or FALSE?\nThe primary goal of model validation is to ensure the simulation matches real-world behavior.",
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "Correct! The purpose of model validation is to ensure the simulation accurately reflects the real-world system it is modeling."
    ),
    'chapter_information': 'Week 5 - Module 4 DeepSeek'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_4_MPC = KC_MPC_QUESTIONS[:-1]