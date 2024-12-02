#include "model.h"

namespace s21 {
/**
 * @brief Основной публичный метод запуска вычислений модели.
 * Вычисления производятся над строкой, предварительно заданной в параметре str_
 * сеттером setStr. Результат вычислений помещается в поле data_.
 * Вызов метода обязательно должен быть обернут в try-catch.
 *
 */
void Model::S21Calc() {
  setlocale(LC_NUMERIC, "C");
  std::stack<double> stack_d;
  std::stack<Operator> stack_c;
  last_token_ = cur_token_ = 'n';
  size_t i = 0, count_of_num = 0;
  unary_count_ = 0;
  std::string tmp = str_;
  ReplaceX();
  str_.erase(std::remove(str_.begin(), str_.end(), ' '), str_.end());
  while (i < str_.length() && str_[i] != '=') {
    //? если число
    if ((str_[i] >= '0' && str_[i] <= '9') ||
        (str_[i] == '.' && strchr("0123456789", str_[i + 1]))) {
      stack_d.push(atof(&str_[i]));
      UnaryOperations(stack_d, stack_c);
      i = SkipNum(i);
      cur_token_ = '0';
      ++count_of_num;
    } else {
      //? если оператор
      cur_token_ = AllOperators(stack_c, i);
      Dijkstra(stack_d, stack_c);
    }
    Validator(stack_d, stack_c);
    last_token_ = cur_token_;
    ++i;
  }
  while (!stack_c.empty()) {
    Calculation(stack_d, stack_c);
  }
  if (stack_d.size() != 1 || !count_of_num) {
    throw std::invalid_argument("Неверное выражение");
  }
  data_ = stack_d.top();
  str_ = tmp;
}

//* Вспомогательные приват методы
//? Методы для парсинга
/**
 * @brief Метод для работы со всеми операторами выражения.
 *
 * @param stack_c
 * Стек операторов
 * @param i
 * Индекс в строке str_
 * @return char
 * Полученный оператор
 */
char Model::AllOperators(std::stack<Operator> &stack_c, size_t &i) {
  char oper = TakeFunction(i);

  if (oper) {
    if (oper == 'm') {
      stack_c.push({oper, 3});
    } else {
      stack_c.push({oper, 4});
      stack_c.push({'(', 1});
    }
  } else {
    oper = TakeOperator(str_[i]);
    if (oper) {
      stack_c.push({oper, GetPriority(oper)});
    } else {
      std::string error = {str_[i]};
      throw std::invalid_argument("Не корректный символ " + error);
    }
  }
  return oper;
}

/**
 * @brief Записывает в стек функцию. Если функция не найдена возвращает 0.
 *
 * @param i
 * Индекс в строке
 * @return char
 * Короткая запись найденной функции
 */
char Model::TakeFunction(size_t &i) {
  char res = 0;
  if (!strncmp(&str_[i], "cos(", 4)) {
    i += 3;
    res = 'c';

  } else if (!strncmp(&str_[i], "sin(", 4)) {
    i += 3;
    res = 's';

  } else if (!strncmp(&str_[i], "tan(", 4)) {
    i += 3;
    res = 't';

  } else if (!strncmp(&str_[i], "acos(", 5)) {
    i += 4;
    res = 'o';

  } else if (!strncmp(&str_[i], "asin(", 5)) {
    i += 4;
    res = 'i';

  } else if (!strncmp(&str_[i], "atan(", 5)) {
    i += 4;
    res = 'a';

  } else if (!strncmp(&str_[i], "sqrt(", 5)) {
    i += 4;
    res = 'q';

  } else if (!strncmp(&str_[i], "ln(", 3)) {
    i += 2;
    res = 'n';

  } else if (!strncmp(&str_[i], "log(", 4)) {
    i += 3;
    res = 'l';

  } else if (!strncmp(&str_[i], "mod", 3)) {
    i += 2;
    res = 'm';
  }

  return res;
}

/**
 * @brief Записывает в стек оператор. Если оператор не найден возвращает 0.
 *
 * @param c
 * Проверяемый символ
 * @return char
 * Записанный оператор
 */
char Model::TakeOperator(const char &c) {
  char res = 0;
  if (strchr("()^+-*/", c)) {
    res = c;
  }
  return res;
}

/**
 * @brief Проверка приоритета оператора
 *
 * @param oper
 * Проверяемый оператор
 * @return int
 * Приоритет
 */
int Model::GetPriority(char oper) {
  int priority = -1;

  if (strchr("(", oper)) {
    priority = 1;
  } else if (strchr("+-", oper)) {
    priority = 2;
  } else if (strchr("*/m", oper)) {
    priority = 3;
  } else if (strchr("^cstoiaqnl", oper)) {
    priority = 4;
  } else if (strchr("^", oper)) {
    priority = 0;
  }

  return priority;
}

/**
 * @brief Пропуск числа, которое взял atof.
 *
 * @param i
 * Индекс в строке
 * @return size_t
 * Новый индекс
 */
size_t Model::SkipNum(size_t i) {
  bool enough_dots = false, enough_e = false, stop = false;
  while (i < str_.length() && !stop) {
    if (str_[i] == '.' && !enough_dots) {
      enough_dots = true;
    } else if ((str_[i] == 'e' || str_[i] == 'E') && !enough_e) {
      if (str_[i + 1] == '-' || str_[i + 1] == '+') {
        ++i;
      }
      enough_e = true;
    } else if (!(str_[i] >= '0' && str_[i] <= '9')) {
      stop = true;
      --i;
    }
    ++i;
  }
  return i - 1;
}

void Model::ReplaceX() {
  while (str_.find("x") != std::string::npos) {
    str_.replace(str_.find("x"), 1, "(" + std::to_string(x_) + ")");
  }
}

//? Методы для вычислений
/**
 * @brief Вычисление верхней операции.
 *
 * @param stack_d
 * Стек чисел
 * @param stack_c
 * Стек операторов
 */
void Model::Calculation(std::stack<double> &stack_d,
                        std::stack<Operator> &stack_c) {
  long double second = 0, first = 0;
  // два верхних числа
  if (stack_c.empty()) {
    throw std::invalid_argument("Стек операторов пуст");
  }
  if (stack_d.empty()) {
    throw std::invalid_argument("Стек чисел пуст");
  }
  char oper = stack_c.top().oper;
  stack_c.pop();
  second = stack_d.top();
  stack_d.pop();
  if (oper != '(') {
    if (stack_d.empty()) {
      throw std::invalid_argument("В стеке чисел не хватает второго операнда");
    }
    first = stack_d.top();
    stack_d.pop();
  }
  if (oper == '+') {
    stack_d.push(first + second);
  } else if (oper == '-') {
    stack_d.push(first - second);
  } else if (oper == '*') {
    stack_d.push(first * second);
  } else if (oper == '/') {
    stack_d.push(first / second);
  } else if (oper == '^') {
    stack_d.push(pow(first, second));
  } else if (oper == 'm') {
    stack_d.push(fmodl(first, second));
  } else if (oper == '(') {
    if (stack_c.empty()) {
      stack_d.push(second);
    } else {
      oper = stack_c.top().oper;
      stack_c.pop();
      if (oper == 'c') {
        stack_d.push(cosl(second));
      } else if (oper == 's') {
        stack_d.push(sinl(second));
      } else if (oper == 't') {
        stack_d.push(tanl(second));
      } else if (oper == 'o') {
        stack_d.push(acosl(second));
      } else if (oper == 'i') {
        stack_d.push(asinl(second));
      } else if (oper == 'a') {
        stack_d.push(atanl(second));
      } else if (oper == 'q') {
        stack_d.push(sqrtl(second));
      } else if (oper == 'n') {
        stack_d.push(logl(second));
      } else if (oper == 'l') {
        stack_d.push(log10l(second));
      } else {
        stack_c.push({oper, GetPriority(oper)});
        stack_d.push(second);
      }
    }
  }
}

/**
 * @brief Алгоритм Дейкстры. Проверка условий запуска вычислений и вызов самих
 * вычислений.
 *
 * @param stack_d
 * Стек чисел
 * @param stack_c
 * Стек операторов
 */
void Model::Dijkstra(std::stack<double> &stack_d,
                     std::stack<Operator> &stack_c) {
  // стек пуст
  if (stack_c.empty() || stack_c.top().oper == '(') {
    return;
  }
  // в стеке только одна операция
  if (stack_c.size() == 1) {
    if (stack_c.top().oper == ')') {
      throw std::invalid_argument(
          "Введена неправильная скобочная последовательность. В стеке "
          "находится только (");
    }
    return;
  }
  // сравнение верхней операции со следующей
  char top_oper = stack_c.top().oper;
  int priority = stack_c.top().priority;
  stack_c.pop();
  if (top_oper == ')') {
    while (!stack_c.empty() && stack_c.top().oper != '(') {
      Calculation(stack_d, stack_c);
    }
    if (stack_c.empty()) {
      throw std::invalid_argument(
          "Введена неправильная скобочная последовательность. В стеке не "
          "встретилось ( при наличии )");
    }
    Calculation(stack_d, stack_c);
  } else {
    bool stop = false;
    while (!stack_c.empty() && !stop && top_oper != '(') {
      if (priority <= stack_c.top().priority &&
          (top_oper != '^' && stack_c.top().oper != '^')) {
        if (priority > 1) {
          Calculation(stack_d, stack_c);
        }
      } else {
        stop = true;
      }
    }
    stack_c.push({top_oper, priority});
  }
}

//? Методы валидации
/**
 * @brief Текущая валидация. Использует информацию о текущей и предыдущей
 * лексеме. Записывает унарные операции + и -, которые нужно будет выполнить над
 * следующим считаным числом.
 *
 * @param stack_d
 * Стек чисел
 * @param stack_c
 * Стек операторов
 */
void Model::Validator(std::stack<double> &stack_d,
                      std::stack<Operator> &stack_c) {
  if (stack_c.empty()) {
    if (stack_d.size() > 1) {
      throw std::invalid_argument("Два числа подряд без операторов");
    }
    return;
  }
  if (GetPriority(cur_token_) == 4 && cur_token_ != '^') {
    cur_token_ = '(';
  }
  if (GetPriority(last_token_) == 4 && last_token_ != '^') {
    last_token_ = '(';
  }

  // начинается с оператора
  if ((last_token_ == 'n' && cur_token_ != '0')) {
    if (cur_token_ == '-' || cur_token_ == '+') {
      stack_d.push(0);
      ++unary_count_;
    } else if (cur_token_ != '(') {
      throw std::invalid_argument("Выражение начинается с неверного оператора");
    }
    // два оператора подряд
  } else if (last_token_ != '0' && cur_token_ != '0' && last_token_ != ')') {
    if ((cur_token_ == '-' || cur_token_ == '+')) {
      if (strchr("(", last_token_)) {
        if (!EqCountOfLists(stack_d, stack_c)) {
          stack_d.push(0);
          ++unary_count_;
        }
      } else {
        std::string error = {last_token_, cur_token_};
        throw std::invalid_argument(
            "Не правильная последовательность операторов" + error);
      }
    } else if (!strchr("()", cur_token_)) {
      std::string error = {last_token_, cur_token_};
      throw std::invalid_argument(
          "Не правильная последовательность операторов" + error);
    }
    // два операнда
  } else if (last_token_ == '0' && cur_token_ == '0') {
    throw std::invalid_argument("Выражение содержит два числа подряд");
  } else if (last_token_ == '0' && cur_token_ == '(') {
    throw std::invalid_argument(
        "Отсутствует операция между числом и открывающей скобкой");
  }
}

/**
 * @brief Проверка равенства количества чисел и операторов(без учета скобок) в
 * стеке.
 *
 * @param stack_d
 * Стек чисел
 * @param stack_c
 * Стек операторов
 * @return true
 * @return false
 */
bool Model::EqCountOfLists(const std::stack<double> &stack_d,
                           std::stack<Operator> &stack_c) const noexcept {
  std::stack<Operator> stack_c_copy = stack_c;
  size_t count = 0;
  while (!stack_c_copy.empty()) {
    if (stack_c_copy.top().oper != '(' && stack_c_copy.top().oper != ')') {
      ++count;
    }
    stack_c_copy.pop();
  }
  return count == stack_d.size();
}

/**
 * @brief Выполнение унарных операций + и - над считаным числом.
 *
 * @param stack_d
 * Стек чисел
 * @param stack_c
 * Стек операторов
 */
void Model::UnaryOperations(std::stack<double> &stack_d,
                            std::stack<Operator> &stack_c) {
  if (unary_count_ < 1 || stack_d.size() < 2) {
    return;
  }
  double tmp = stack_d.top();
  stack_d.pop();
  if (stack_d.top() == 0 && strchr("+-", stack_c.top().oper)) {
    stack_d.push(tmp);
    while (unary_count_) {
      Calculation(stack_d, stack_c);
      --unary_count_;
    }
  } else {
    stack_d.push(tmp);
  }
}

/**
 * @brief Считает два вектора значений Px_ и Py_, а также границы графика.
 *
 * @param autoscale
 * Флаг для применения автоматического выбора размера
 * @param limit
 * Граница x
 */
void Model::Plot(bool autoscale, double limit) {
  double h = 0.01;
  double xBegin = -limit;
  double xEnd = limit;
  Px_.clear();
  Py_.clear();
  graphic_.yMin = limit;
  graphic_.yMax = -limit;
  graphic_.xMin = limit;
  graphic_.xMax = -limit;
  double xMean, yMean;
  try {
    for (x_ = xBegin; x_ < xEnd; x_ += h) {
      Px_.push_back(x_);
      S21Calc();
      double Y = getData();
      if (autoscale) {
        if (Y < graphic_.yMin) graphic_.yMin = Y;
        if (Y > graphic_.yMax) graphic_.yMax = Y;
        if (x_ < graphic_.xMin) graphic_.xMin = x_;
        if (x_ > graphic_.xMax) graphic_.xMax = x_;
      }
      Py_.push_back(Y);
    }
  } catch (const std::exception &e) {
    Px_.clear();
    Py_.clear();
  }

  xMean = (graphic_.xMax + graphic_.xMin) / 2;
  yMean = (graphic_.yMax + graphic_.yMin) / 2;

  if (autoscale) {
    if (graphic_.yMin < xMean - limit) graphic_.yMin = xMean - limit;
    if (graphic_.yMax > yMean + limit) graphic_.yMax = yMean + limit;
    if (graphic_.xMin < xMean - limit) graphic_.xMin = xMean - limit;
    if (graphic_.xMax > xMean + limit) graphic_.xMax = xMean + limit;
  } else {
    graphic_.yMin = -limit;
    graphic_.yMax = limit;
    graphic_.xMin = -limit;
    graphic_.xMax = limit;
  }
}

//? Функции для привязки к Python
Model *model_new() { return new Model(); }
void model_del(Model *m) { delete m; }
void set_string(Model *m, char *str) { m->setStr(str); }
void set_x(Model *m, double x) { m->setX(x); }
const char *calc(Model *m) {
  std::string s;
  try {
    m->S21Calc();
    s = std::to_string(m->getData());
  } catch (const std::exception &e) {
    s = "Error";
  }
  return s.c_str();
}
void plot(Model *m, bool autoscale, double limit) { m->Plot(autoscale, limit); }
Model::Graphic get_plot(Model *m) { return m->getPlot(); }
double get_pxi(Model *m, int i) { return m->getPx()[i]; }
double get_pyi(Model *m, int i) { return m->getPy()[i]; }
int len_px(Model *m) { return m->getPx().size(); }
int len_py(Model *m) { return m->getPy().size(); }

}  // namespace s21