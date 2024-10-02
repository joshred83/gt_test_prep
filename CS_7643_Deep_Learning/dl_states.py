import numpy as np
from .dl_week1_mpc import WEEK_1_MPC
from .dl_week2_mpc import WEEK_2_MPC
from .dl_week3_mpc import WEEK_3_MPC
from .dl_week4_mpc import WEEK_4_MPC
from .dl_week5_mpc import WEEK_5_MPC
from .dl_week6_mpc import WEEK_6_MPC
from .dl_week7_mpc import WEEK_7_MPC

############################
questions_dictionary = {'1': WEEK_1_MPC,
                        '2': WEEK_2_MPC,
                        '3': WEEK_3_MPC,
                        '4': WEEK_4_MPC,
                        '5': WEEK_5_MPC,
                        '6': WEEK_6_MPC,
                        '7': WEEK_7_MPC}
all = list(questions_dictionary.values())

OPEN_QUESTIONS = []
IMAGE_QUESTIONS = []
#====================TOKEN===================
class Token():
    def __init__(self, STATE="1"):
        self.STATE = STATE
        self.mpc_questions = []
        self.picture_questions = None
        self.islr_questions = None
        self.num_questions = 15
        self.chapters_to_review = None
        # self.image = None

    def initialize_mpc_questions(self):
        # self.STATE = 'review'
        if self.STATE == 'all':
            if self.chapters_to_review is None:
                self.chapters_to_review = [0,1,2]
            self.mpc_questions = []
            while len(self.mpc_questions)<self.num_questions :
                chapters = np.random.choice(self.chapters_to_review, size=len(self.chapters_to_review), replace=False)
                for chapter in chapters:
                    list_length = len(all[chapter])
                    mpc_idx = np.random.choice(range(list_length), size=1, replace=False)
                    # print(list_length, mpc_idx)
                    self.mpc_questions.append(all[chapter][int(mpc_idx)])
            # print('aloha')
        else:
            review_questions = questions_dictionary[self.STATE]
            list_length = len(review_questions)
            mpc_idxs = np.random.choice(range(list_length), size=self.num_questions, replace=False)
            print('______________________________________________')
            print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
            print('______________________________________________')
            for idx in mpc_idxs:
                self.mpc_questions.append(review_questions[idx])


    def initialize_open_questions(self):
        self.STATE = 'open'
        review_questions = OPEN_QUESTIONS
        list_length = len(review_questions)
        open_idxs = np.random.choice(range(list_length), size=1, replace=False)
        # print('______________________________________________')
        # print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
        # print('______________________________________________')
        for idx in open_idxs:
            self.mpc_questions.append(review_questions[idx])

    def initialize_image_questions(self):
        self.STATE = 'chart'
        review_questions = IMAGE_QUESTIONS
        list_length = len(review_questions)
        open_idxs = np.random.choice(range(list_length), size=2, replace=False)
        # print('______________________________________________')
        # print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
        # print('______________________________________________')
        for idx in open_idxs:
            # print(review_questions[idx])
            self.mpc_questions.append(review_questions[idx])


if __name__ == "__main__":
    1
    # token = Token('all')
    # token.initialize_mpc_questions()