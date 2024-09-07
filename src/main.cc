#include <iostream>

#include "lib/model.h"

int main() {
  s21::Model model;
  std::string s = "34 * 64";
  model.setStr(s);
  model.S21Calc();
  std::cout << s << " = " << model.getData();

  return 0;
}
