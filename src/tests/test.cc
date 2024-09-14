#include <gtest/gtest.h>

// #include "../Modules/credit_model.h"
#include "../lib/model.h"

class MyTests : public ::testing::Test {
 protected:
  s21::Model model;
  const double abs_error = 0.0000001;
};

TEST_F(MyTests, s21_calc_1) {
  model.setStr("((1 * 2) - 1)");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 1.0, abs_error);
}

TEST_F(MyTests, s21_calc_2) {
  model.setStr("(-1 +(4 / 2))");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 1.0, abs_error);
}

TEST_F(MyTests, s21_calc_3) {
  model.setStr("1+(-1 +(1 * 2))");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 2.0, abs_error);
}

TEST_F(MyTests, s21_calc_4) {
  model.setStr("(-1 +(1 * 2))-2");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), -1.0, abs_error);
}

TEST_F(MyTests, s21_calc_5) {
  model.setStr("sin(2-1) + cos(1 * 2) + tan(3)");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 0.2827776, abs_error);
}

TEST_F(MyTests, s21_calc_6) {
  model.setStr("asin(2-1) + acos(0.33) + atan(3)");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 4.0543349, abs_error);
}

TEST_F(MyTests, s21_calc_7) {
  model.setStr("(log(100000) + 2) mod sqrt(4)+ ln(2.3)");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 1.8329091, abs_error);
}

TEST_F(MyTests, s21_calc_8) {
  model.setStr("2^3^2");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 512.0000000, abs_error);
}

TEST_F(MyTests, s21_calc_9) {
  model.setStr("(1 * 1 + (1 * 2 ");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 3.0000000, abs_error);
}

TEST_F(MyTests, s21_calc_10) {
  model.setStr("(sin(1 + 1");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 0.9092974, abs_error);
}

TEST_F(MyTests, s21_calc_11) {
  model.setStr("(sin(.1 + 1.9");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), 0.9092974, abs_error);
}

TEST_F(MyTests, s21_calc_12) {
  model.setStr("-(sin(.1 + 1.9");
  model.S21Calc();
  EXPECT_NEAR(model.getData(), -0.9092974, abs_error);
}

// incorrect
TEST_F(MyTests, s21_calc_incorrect_1) {
  model.setStr("(--1 +(1 * 2))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_2) {
  model.setStr("()-1 +(1 /)) 2))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_3) {
  model.setStr("()");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_4) {
  model.setStr("(1 * -1 + (1 * 2))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_5) {
  model.setStr("(1 * [1 + (1 * 2))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_6) {
  model.setStr("(1 * 1 3 (1 * 2))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_7) {
  model.setStr("(1 * 1 +(1 * 2))-2 - ");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_8) {
  model.setStr("(1 * 1 (1 * 2)))-2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_9) {
  model.setStr(". + 1");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_10) {
  model.setStr("* 3 + 2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_11) {
  model.setStr("3 *+ 2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_12) {
  model.setStr("3 +* 2");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_13) {
  model.setStr("3 + 2)");
  EXPECT_ANY_THROW(model.S21Calc());
}

TEST_F(MyTests, s21_calc_incorrect_14) {
  model.setStr("3.10.0 + 1");
  EXPECT_ANY_THROW(model.S21Calc());
}

int main(int argc, char** argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}