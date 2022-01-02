import random
import re

class review:
    def __init__(self, product_id):
        self.product_id = product_id
        self.user_id = ''
        self.profile_name = ''
        self.helpfulness = 1.0
        self.score = 0.0
        self.time = 0
        self.summary = ''
        self.text = ''

        self.dead_flag = 0
        self.short_flag = 0
        self.unhelp_flag = 0
        self.perf_imperf_flag = 0

    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_profile_name(self, profile_name):
        self.profile_name = profile_name
    def set_helpfulness(self, helpfulness):
        self.helpfulness = helpfulness
    def set_score(self, score):
        self.score = score
    def set_time(self, time):
        self.time = time
    def set_summary(self, summary):
        self.summary = summary
    def set_text(self, text):
        self.text = text

    def calculate(self):
        return 5 - (self.dead_flag + self.short_flag + self.unhelp_flag + self.perf_imperf_flag)

    def print(self):
        print("product/productId: {}".format(self.product_id))
        print("review/userId: {}".format(self.user_id))
        print("review/profileName: {}".format(self.profile_name))
        print("review/helpfulness: {}".format(self.helpfulness))
        print("review/score: {}".format(self.score))
        print("review/time: {}".format(self.time))
        print("review/summary: {}".format(self.summary))
        print("review/text: {}".format(self.text))

def get_data(cap):
    txt = open("movies.txt", errors="ignore")
    data = []
    counter = 0
    for line in txt:
        # print(line)
        if counter == 0:
            temp = review(line[19:]) #19:
        elif counter == 1:
            temp.set_user_id(line[15:]) #15:
        elif counter == 2:
            temp.set_profile_name(line[20:]) #20:
        elif counter == 3:
            temp.set_helpfulness(line[20:]) #20:
        elif counter == 4:
            temp.set_score(line[14:]) #14:
        elif counter == 5:
            temp.set_time(line[13:]) #13:
        elif counter == 6:
            temp.set_summary(line[16:]) #16:
        elif counter == 7:
            temp.set_text(line[13:]) #13:
            data.append(temp)
        elif counter == 8:
            counter = -1
        counter += 1
        if len(data) > cap:
            break
    return data

def get_txt_len():
    txt = open("movies.txt", errors="ignore")
    count = 0
    for line in txt:
        count+=1
    print("Number of reviews: {}".format(count/9))

#cap at most should be 100000
def test_print(num, cap):
    test = get_data(cap)
    print("We have collected the first {} reviews of the full data set for testing. \n".format(cap))
    print("FIRST Review in test set: \n")
    test[0].print()
    print("LAST Review in test set: \n")
    test[-1].print()
    print("{} RANDOM Reviews in test set: \n".format(num))
    for i in range(num):
        temp = random.randrange(cap)
        print("Review {}: \n".format(temp))
        test[temp].print()

def dead_word_filter(deadwords, dataset):
    ret = []
    dead = set(deadwords)
    for data in dataset:
        temp = set(word.lower() for word in re.sub(r'[^\w]', ' ', data.text).split())
        if dead.intersection(temp):
            data.dead_flag = 1
            ret.append(data)
    print("There are {} reviews with words from {}.".format(len(ret), dead))
    return ret

def len_filter(length, dataset):
    ret = []
    for data in dataset:
        temp = re.sub(r'[^\w]', ' ', data.text).split()
        if len(temp) < length:
            data.short_flag = 1
            ret.append(data)
    print("There are {} reviews with less than {} words.".format(len(ret), length))
    return ret

def helpfulness_filter(helpfulness, dataset):
    ret = []
    for data in dataset:
        temp = re.split('/|\n', data.helpfulness)
        if not int(temp[1]) or int(temp[0])/int(temp[1]) < helpfulness:
            data.unhelp_flag = 1
            ret.append(data)
    print("There are {} reviews with less than {} helpfulness.".format(len(ret), helpfulness))
    return ret

def perfection_filter(dataset):
    ret = []
    for data in dataset:
        temp = float(data.score[:-1])
        if temp == 1.0 or temp == 5.0:
            data.perf_imperf_flag = 1
            ret.append(data)
    print("There are {} reviews with a score of 1 or 5.".format(len(ret)))
    return ret

def validity_filter(validity, dataset):
    ret = []
    for data in dataset:
        if data.calculate() == validity:
            ret.append(data)
    print("There are {} reviews with a validity score of {}".format(len(ret), validity))
    return ret
