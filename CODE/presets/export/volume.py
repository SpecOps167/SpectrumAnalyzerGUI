class main(object):
    def wf(self):
        msg = raw_input("volume: ")
        f = open("volume.txt", "w")
        f.write(msg)
        f.close()
        self.wf()

run = main()
run.wf()
