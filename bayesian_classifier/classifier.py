'''
Simple example of a Naive bayes classifier

'''

from __future__ import division

class Classifier:

    cats = {}
    total_examples = 0

    def __init__(self):
        '''Set up classifier'''


    def classify(self, text):

        def k(x): 
            return x[1]

        probabilities = []

        for c in self.cats.keys():
            cat = self.cats[c]

            running_total = 1

            for word in text.split(" "):
                if not cat['words'].has_key( word ): 
                    pass
                else: 
                    p = cat['words'][word] / cat['total']

                    print "%s occurs %d/%d times in %s" % (word,
                        cat['words'][word],
                        cat['total'],
                        c)

                    running_total *= p

            probabilities.append( (c, running_total))

        print probabilities

        return max(probabilities, key=k) 


    def train(self, examples):
        """Given examples, train the classifier
        """

        for cat,data in examples:

            if not self.cats.has_key(cat): 
               self.cats[cat] = {'total' : 0, 'words' : {} }
           
            cat = self.cats[cat]

            for word in data.split(" "):
                if(cat['words'].has_key(word)):
                    cat['words'][word] += 1
                else:
                    cat['words'][word] = 1

            cat['total'] += 1
            self.total_examples += 1

    

if __name__ == "__main__":

    c = Classifier()

    examples = [("spam", "enlarge your genitalia using viagra from our company today"),
    ("ham", "I like food especially ham, don't like viagra though"),
    ("spam", "make love better using a much bigger genitalia, buy viagra from penocorp"),
    ("ham", "Hello John, I was wondering if I could set up a meeting about making love bears for the stuffed bear foundation?"),
    ("spam", "Buy shares in the genitalia corporation today - the company with most viagra"),
    ("ham", "Every day when I go to work I share a lift with Don but now he's left. What do?"),
    ("spam", "Special offers from amazon.com - buy your christmas gifts now before it's too late"),
    ("ham", "Hey honey, what do you want me to get you for christmas this year?"),
    ("spam", "I am a nigerian prince and would like to award you 10 million dollars. Send me your bank details"),
    ("ham", "I'll pay you that money later, could you let me know your bank details sweetie?"),
    ("spam", "Your girlfriend will love your huge genitalia when you buy nigerian viagra"),
    ("spam", "genitalia genitalia viagra company")
    ]

    c.train(examples)
    print c.classify("""enlarge your genitalia with the viagra corporation company
    today. become a nigerian prince! send us your bank details""")
