import logging
import toml
import random

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class QuestionController():
    
    def __init__(self):
        self.dir = ""
        self.title = ""
        self.total = 0
        self.current = 1

    def load(self, _dir):
        self.dir = _dir
        logging.debug("change dir to " + _dir)

        self.config = toml.load(_dir+"/config.toml")
        self.title = self.config["title"]
        self.answer = self.config["answer"]
        self.total = len(self.answer)

    def next(self):
        if(self.current + 1 > self.total):
            self.current = 1
        else:
            self.current += 1

    def randomNext(self):
        self.current = random.randint(1, self.total)
    def back(self):
        if(self.current - 1 == 0):
            self.current = self.total
        else:
            self.current -= 1

    def getImage(self):
        return "{0}/image{1}_c.jpg".format(self.dir,str(self.current))
    
    def getTitle(self):
        return self.title

    def getAns(self):
        return self.answer[str(self.current)]

    def getNo(self):
        return str(self.current)

if __name__ == "__main__":
    qc = QuestionController()
    qc.load("test")
    print(qc.getAns())