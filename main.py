
import random as rd
import time

# extension ideas:
# - change letter frequency to get keyboard mash vibe:
# (keyboard layout frequency? Mapped onto hand position? Nearby keys more likely?
# repeated keys more likely? Hold key by default with chance to un-press?)
# - visualization of multiple instances (hollywood-squares style)
# - make a web frontend for multiple monkeys
# - make an emoji keyboard one (tie in to search for large even primes as a similar endeavor)


hamlet = "Enter two Sentinels-[first,] Francisco, [who paces up and down at his post; then] " \
         "Bernardo, [who approaches him]." \
         "\nBernardo. Who's there?" \
         "\nFrancisco. Nay, answer me. Stand and unfold yourself." \
         "\nBernardo. Long live the King!" \
         "\nFrancisco. Bernardo?" \
         "\nBernardo. He." \
         "\nFrancisco. You come most carefully upon your hour." \
         "\nBernardo. 'Tis now struck twelve. Get thee to bed, Francisco." \
         "\nFrancisco. For this relief much thanks. 'Tis bitter cold," \
         "\nAnd I am sick at heart." \
         "\nBernardo. Have you had quiet guard?" \
         "\nFrancisco. Not a mouse stirring." \
         "\nBernardo. Well, good night." \
         "\nIf you do meet Horatio and Marcellus," \
         "\nThe rivals of my watch, bid them make haste."

alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4,
            'g': 7, 'f': 6, 'i': 9, 'h': 8,
            'k': 11, 'j': 10, 'm': 13, 'l': 12,
            'o': 15, 'n': 14, 'q': 17, 'p': 16,
            's': 19, 'r': 18, 'u': 21, 't': 20,
            'w': 23, 'v': 22, 'y': 25, 'x': 24,
            'z': 26, ' ': 27, '.': 28, ',': 29,
            '\'': 30, '\n': 31, '-': 32, '[': 33,
            ']': 34, '!': 35, '?': 36
            }

alphabet_rev = {value: key for key, value in alphabet.items()}


class Monkey:

    def __init__(self, seed):
        self.seed = seed
        rd.seed(self.seed)
        self.text = ""
        self.length = 0
        self.error_detected = 0
        self.refractory_period = 0.5  # in seconds

    def type(self):
        self.text += alphabet_rev[rd.randint(1, 36)]
        self.length += 1
        print(self.text)
        time.sleep(self.refractory_period)

    def check(self):
        if self.text == hamlet:
            print("HAMLET AChieVED. Shakespeare monkey!")
        elif self.text[:self.length] == hamlet[:self.length]:  # if we're on our way to Hamlet
            self.error_detected = 0
        else:
            self.error_detected = 1

    def restart(self):
        self.text = ""
        self.error_detected = 0

    def run(self):
        self.type()

    def test(self):
        self.check()
        if self.error_detected:
            self.restart()


def main():

    monkey1 = Monkey(1)
    timestep = 0

    while True:

        monkey1.run()
        timestep += 1
        if timestep % 15 == 0:  # Note: this should change with the refractory_period
            monkey1.test()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
