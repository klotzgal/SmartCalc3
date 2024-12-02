#ifndef _SMART_CALC_2_SRC_MODULES_MODEL_H
#define _SMART_CALC_2_SRC_MODULES_MODEL_H

/**
 * @file model.h
 * @author klotzgal (klotzgal@student.21-school.ru)
 * @brief SmartCalc_v2.0
 * @version 0.1
 * @date 2023-11-01
 *
 * @copyright Copyright (c) 2023
 *
 */

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <exception>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

namespace s21 {

class Model {
  typedef struct {
    char oper;
    int priority;
  } Operator;

 public:
  typedef struct {
    double xMin;
    double xMax;
    double yMin;
    double yMax;
  } Graphic;

  Model()
      : data_(0),
        str_(""),
        x_(0),
        last_token_('n'),
        cur_token_('n'),
        unary_count_(0),
        graphic_(),
        Px_(),
        Py_() {}
  ~Model() {}

  //* Методы класса

  void S21Calc();
  void Plot(bool autoscale, double limit);
  void setStr(const std::string str) { str_ = str; }
  void setX(double x) { x_ = x; }
  double getData() const { return data_; }
  std::vector<double> &getPx() { return Px_; }
  std::vector<double> &getPy() { return Py_; }
  Graphic getPlot() const { return graphic_; }

 private:
  double data_;
  std::string str_;
  double x_;
  char last_token_;
  char cur_token_;
  int unary_count_;
  Graphic graphic_;
  std::vector<double> Px_;
  std::vector<double> Py_;

  //* Вспомогательные приват методы
  //? Методы для парсинга
  char AllOperators(std::stack<Operator> &stack_c, size_t &i);
  char TakeFunction(size_t &i);
  char TakeOperator(const char &c);
  int GetPriority(char oper);
  size_t SkipNum(size_t i);
  void ReplaceX();

  //? Методы для вычислений
  void Calculation(std::stack<double> &stack_d, std::stack<Operator> &stack_c);
  void Dijkstra(std::stack<double> &stack_d, std::stack<Operator> &stack_c);

  //? Методы валидации
  void Validator(std::stack<double> &stack_d, std::stack<Operator> &stack_c);
  bool EqCountOfLists(const std::stack<double> &stack_d,
                      std::stack<Operator> &stack_c) const noexcept;
  void UnaryOperations(std::stack<double> &stack_d,
                       std::stack<Operator> &stack_c);
};

//? Функции для привязки к Python
extern "C" {
Model *model_new();
void model_del(Model *m);
void set_string(Model *m, char *str);
void set_x(Model *m, double x);
const char *calc(Model *m);
void plot(Model *m, bool autoscale, double limit);
Model::Graphic get_plot(Model *m);
double get_pxi(Model *m, int i);
double get_pyi(Model *m, int i);
int len_px(Model *m);
int len_py(Model *m);
}

}  // namespace s21

#endif  //_SMART_CALC_2_SRC_MODULES_MODEL_H
