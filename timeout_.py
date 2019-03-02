import sys
import getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(
            argv,
            "hi:t:x:l:",
            ["id=", "time=", "text=", "last_turn="]
        )
    except getopt.GetoptError:
        print('test.py -i <id> -t <time> -x <text> -l <last_turn>')
        sys.exit(2)
    id = 0
    _time = 0
    text = ''
    last_turn = ()
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <id> -t <time> -x <text>')
            sys.exit()
        elif opt in ("-i", "--id"):
            id = arg
        elif opt in ("-t", "--time"):
            _time = int(arg)
        elif opt in ("-x", "--text"):
            text = arg
        elif opt in ("-l", "--last_turn"):
            last_turn = tuple(map(int,arg))
    import time
    from config import xo, bot, cnst
    g = xo(id)
    text = text.split('\n', maxsplit=1)
    if _time < 10:
        time.sleep(_time)
    else:
        for _ in range(_time//10):
            time.sleep(10)
            g.pull()
            if not g:
                return 1,0
    g.pull()
    if _time > 60 or _time < 10 or bool(g):
        if _time > 10:
            time.sleep(5)
        g.pull()
        if not g:
            return 2,0
        if len(text) > 1:
            return 3,g.end(text[0], last_turn, text[1])
        return 4,g.end(text[0], last_turn, cnst.time)


if __name__ == "__main__":
    print(main(sys.argv[1:]))
