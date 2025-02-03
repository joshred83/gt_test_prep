import numpy as np
from ISYE_6644_Simulation.probability_questions.module0 import MODULE_0_MPC
from ISYE_6644_Simulation.probability_questions.module1 import MODULE_1_MPC
from ISYE_6644_Simulation.probability_questions.module2 import MODULE_2_MPC
from ISYE_6644_Simulation.probability_questions.module3 import MODULE_3_MPC
from ISYE_6644_Simulation.probability_questions.module4 import MODULE_4_MPC
from ISYE_6644_Simulation.probability_questions.module5 import MODULE_5_MPC
from ISYE_6644_Simulation.probability_questions.module6 import MODULE_6_MPC
from ISYE_6644_Simulation.probability_questions.module7 import MODULE_7_MPC
from ISYE_6644_Simulation.probability_questions.module8 import MODULE_8_MPC

from ISYE_6644_Simulation.simulation_questions.module1 import SIM_MODULE_1_MPC
from ISYE_6644_Simulation.simulation_questions.midterm import SIM_MIDTERM_1_MPC
from ISYE_6644_Simulation.simulation_questions.module2 import SIM_MODULE_2_MPC
from ISYE_6644_Simulation.simulation_questions.module3 import SIM_MODULE_3_MPC
from ISYE_6644_Simulation.simulation_questions.module4 import SIM_MODULE_4_MPC
from ISYE_6644_Simulation.simulation_questions.module5 import SIM_MODULE_5_MPC
from ISYE_6644_Simulation.simulation_questions.module6 import SIM_MODULE_6_MPC
from ISYE_6644_Simulation.simulation_questions.module7 import SIM_MODULE_7_MPC
from ISYE_6644_Simulation.simulation_questions.module8 import SIM_MODULE_8_MPC
from ISYE_6644_Simulation.simulation_questions.module9 import SIM_MODULE_9_MPC
from ISYE_6644_Simulation.simulation_questions.module10 import SIM_MODULE_10_MPC

# Questions Dictionary
questions_dictionary = {
    # Probability Modules
    'PROB_0': MODULE_0_MPC, 'PROB_1': MODULE_1_MPC, 'PROB_2': MODULE_2_MPC, 
    'PROB_3': MODULE_3_MPC, 'PROB_4': MODULE_4_MPC, 'PROB_5': MODULE_5_MPC, 
    'PROB_6': MODULE_6_MPC, 'PROB_7': MODULE_7_MPC, 'PROB_8': MODULE_8_MPC,

    # Simulation Modules
    'SIM_1': SIM_MODULE_1_MPC, 'SIM_2': SIM_MODULE_2_MPC, 
    'SIM_3': SIM_MODULE_3_MPC, 'SIM_4': SIM_MODULE_4_MPC, 
    'SIM_5': SIM_MODULE_5_MPC, 'SIM_6': SIM_MODULE_6_MPC, 
    'SIM_7': SIM_MODULE_7_MPC, 'SIM_8': SIM_MODULE_8_MPC, 
    'SIM_9': SIM_MODULE_9_MPC, 'SIM_10': SIM_MODULE_10_MPC,
    'MIDTERM_1':SIM_MIDTERM_1_MPC
}

# Updated Review Sets
REVIEW_SETS = {
    # Individual Probability Modules
    'PROB_0': ['PROB_0'], 'PROB_1': ['PROB_1'], 'PROB_2': ['PROB_2'], 
    'PROB_3': ['PROB_3'], 'PROB_4': ['PROB_4'], 'PROB_5': ['PROB_5'], 
    'PROB_6': ['PROB_6'], 'PROB_7': ['PROB_7'], 'PROB_8': ['PROB_8'],

    # Probability Exam-Level Reviews
    "ISYE_6739_Midterm1": ['PROB_0', 'PROB_1', 'PROB_2'],
    "ISYE_6739_Midterm2": ['PROB_0', 'PROB_1', 'PROB_2', 'PROB_3', 'PROB_4', 'PROB_5'],
    "ISYE_6739_Final": ['PROB_0', 'PROB_1', 'PROB_2', 'PROB_3', 'PROB_4', 'PROB_5', 'PROB_6', 'PROB_7', 'PROB_8'],

    # Individual Simulation Modules
    'SIM_1': ['SIM_1'], 'SIM_2': ['SIM_2'], 'SIM_3': ['SIM_3'], 
    'SIM_4': ['SIM_4'], 'SIM_5': ['SIM_5'], 'SIM_6': ['SIM_6'], 
    'SIM_7': ['SIM_7'], 'SIM_8': ['SIM_8'], 'SIM_9': ['SIM_9'], 'SIM_10': ['SIM_10'],

    # Simulation Exam-Level Reviews
    "Midterm_1": ['MIDTERM_1','SIM_1', 'SIM_2'], # 'SIM_3', 'SIM_4', 'SIM_5'],
    "Midterm_2": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7'],
    "Final": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7', 'SIM_8', 'SIM_9', 'SIM_10']
}

# Token Class
class Token:
    def __init__(self, STATE="1"):
        self.STATE = STATE
        self.mpc_questions = []
        self.num_questions = 8
        self.chapters_to_review = []

    def initialize_mpc_questions(self):
        # Validate the STATE
        if self.STATE not in REVIEW_SETS:
            print(f"Error: Invalid STATE '{self.STATE}' passed to Token. Check REVIEW_SETS definition.")
            return

        self.chapters_to_review = REVIEW_SETS[self.STATE]

        if not self.chapters_to_review:
            print(f"Error: chapters_to_review not set for STATE: {self.STATE}")
            return

        # Generate Questions
        self.mpc_questions = []
        while len(self.mpc_questions) < self.num_questions:
            chapters = np.random.choice(self.chapters_to_review, size=len(self.chapters_to_review), replace=False)
            for chapter in chapters:
                try:
                    review_questions = questions_dictionary[chapter]
                    if not review_questions:
                        print(f'Warning: Chapter {chapter} is empty.')
                        continue

                    # Add Random Questions
                    mpc_idx = np.random.choice(range(len(review_questions)), size=1, replace=False)
                    self.mpc_questions.append(review_questions[int(mpc_idx)])

                    if len(self.mpc_questions) >= self.num_questions:
                        break
                except KeyError:
                    print(f"Error: Chapter {chapter} not found in questions dictionary.")

if __name__ == "__main__":
    token = Token('Final')
    token.initialize_mpc_questions()
    print(token.mpc_questions)
