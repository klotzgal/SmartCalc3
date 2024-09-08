from model import Model

if __name__ == '__main__':
    m = Model()
    m.expression = '2 * 2'
    print(m.calc())
    m.expression = ''
    print(m.calc())
    m.x = 32
    m.expression = 'x + 8'
    print(m.calc())
