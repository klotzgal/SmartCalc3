from model import Model

if __name__ == '__main__':
    m = Model()
    m.expression = '2 * 2'
    print(m.calc())
