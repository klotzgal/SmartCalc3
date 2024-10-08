#include "credit_model.h"

#include <iostream>

namespace s21 {

void CreditModel::S21Calc(const double S, const double n, double p,
                          bool annuity) {
  p = p / 100 / 12;
  if (annuity) {
    double k = p * pow(1 + p, n) / (pow(1 + p, n) - 1);
    double result = k * S * n;
    first_payment_ = k * S;
    last_payment_ = -1;
    overpayment_ = result - S;
    total_ = result;
  } else {
    double d = S / n;
    double firstPay = 0, lastPay = 0, result = 0;
    for (int i = 1; i <= n; i++) {
      lastPay = d + (S - d * (i - 1)) * p;
      result += lastPay;
      if (i == 1) {
        firstPay = result;
      }
    }
    first_payment_ = firstPay;
    last_payment_ = lastPay;
    overpayment_ = result - S;
    total_ = result;
  }
}

CreditModel *credit_model_new() { return new CreditModel(); }
void credit_model_del(CreditModel *m) { delete m; }
void credit_calc(CreditModel *m, const double S, const double n, double p,
                 bool annuity) {
  m->S21Calc(S, n, p, annuity);
}
double get_total(CreditModel *m) { return m->getTotal(); }
double get_overpayment(CreditModel *m) { return m->getOverpayment(); }
double get_first_payment(CreditModel *m) { return m->getFirstPayment(); }
double get_last_payment(CreditModel *m) { return m->getLastPayment(); }
}  // namespace s21