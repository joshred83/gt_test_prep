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
from ISYE_6644_Simulation.simulation_questions.module2 import SIM_MODULE_2_MPC
from ISYE_6644_Simulation.simulation_questions.module3 import SIM_MODULE_3_MPC
from ISYE_6644_Simulation.simulation_questions.module4 import SIM_MODULE_4_MPC
from ISYE_6644_Simulation.simulation_questions.module5 import SIM_MODULE_5_MPC
from ISYE_6644_Simulation.simulation_questions.module6 import SIM_MODULE_6_MPC
from ISYE_6644_Simulation.simulation_questions.module7 import SIM_MODULE_7_MPC
from ISYE_6644_Simulation.simulation_questions.module8 import SIM_MODULE_8_MPC
from ISYE_6644_Simulation.simulation_questions.module9 import SIM_MODULE_9_MPC
from ISYE_6644_Simulation.simulation_questions.module10 import SIM_MODULE_10_MPC

questions_dictionary = {
    # Probability Modules
    '0': MODULE_0_MPC, '1': MODULE_1_MPC, '2': MODULE_2_MPC, '3': MODULE_3_MPC, 
    '4': MODULE_4_MPC, '5': MODULE_5_MPC, '6': MODULE_6_MPC, '7': MODULE_7_MPC, '8': MODULE_8_MPC,
    # Simulation Modules
    'SIM_1': SIM_MODULE_1_MPC, 'SIM_2': SIM_MODULE_2_MPC, 'SIM_3': SIM_MODULE_3_MPC, 
    'SIM_4': SIM_MODULE_4_MPC, 'SIM_5': SIM_MODULE_5_MPC, 'SIM_6': SIM_MODULE_6_MPC, 
    'SIM_7': SIM_MODULE_7_MPC, 'SIM_8': SIM_MODULE_8_MPC, 'SIM_9': SIM_MODULE_9_MPC, 
    'SIM_10': SIM_MODULE_10_MPC
}

REVIEW_SETS = {
    "ISYE_6739_Final": ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
    "Midterm_1": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5'],
    "Midterm_2": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7'],
    "Final": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7', 'SIM_8', 'SIM_9', 'SIM_10']
}

class Token():
    def __init__(self, STATE="1"):
        self.STATE = STATE
        self.mpc_questions = []
        self.num_questions = 10
        self.chapters_to_review = None

    def initialize_mpc_questions(self):
        if self.STATE in REVIEW_SETS:
            self.chapters_to_review = REVIEW_SETS[self.STATE]
        
        if not self.chapters_to_review:
            print("chapters_to_review not set.")
            return
        
        self.mpc_questions = []
        while len(self.mpc_questions) < self.num_questions:
            chapters = np.random.choice(self.chapters_to_review, size=len(self.chapters_to_review), replace=False)
            for chapter in chapters:
                try:
                    review_questions = questions_dictionary[chapter]
                    list_length = len(review_questions)
                    if list_length == 0:
                        print(f'Chapter {chapter} is empty.')
                        continue
                    mpc_idx = np.random.choice(range(list_length), size=1, replace=False)
                    self.mpc_questions.append(review_questions[int(mpc_idx)])
                except KeyError:
                    print(f"Chapter {chapter} not found in questions dictionary.")

if __name__ == "__main__":
    token = Token('Final')
    token.initialize_mpc_questions()
    print(token.mpc_questions)
