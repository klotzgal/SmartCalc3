#ifndef _SMART_CALC_2_SRC_MODULES_CREDIT_MODEL_H
#define _SMART_CALC_2_SRC_MODULES_CREDIT_MODEL_H

#include <cmath>
#include <string>

namespace s21 {

class CreditModel {
 public:
  CreditModel()
      : first_payment_(0), last_payment_(0), overpayment_(0), total_(0) {}
  ~CreditModel() {}

  //* Методы класса

  void S21Calc(const double S, const double n, double p, bool annuity);
  double getFirstPayment() { return first_payment_; }
  double getLastPayment() { return last_payment_; }
  double getOverpayment() { return overpayment_; }
  double getTotal() { return total_; }

 private:
  double first_payment_;
  double last_payment_;
  double overpayment_;
  double total_;
};

//? Функции для привязки к Python
extern "C" {
CreditModel *credit_model_new();
void credit_model_del(CreditModel *m);
void credit_calc(CreditModel *m, const double S, const double n, double p,
                 bool annuity);
double get_overpayment(CreditModel *m);
double get_first_payment(CreditModel *m);
double get_last_payment(CreditModel *m);
double get_total(CreditModel *m);
}
}  // namespace s21

#endif  //_SMART_CALC_2_SRC_MODULES_CREDIT_MODEL_H
