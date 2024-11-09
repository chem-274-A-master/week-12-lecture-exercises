#include <iostream>
#include <cassert>
#include <Eigen/Eigen>

using namespace Eigen;

/*
Using the eigen library, create a symmetrized version of a matrix.

A matrix can be symmetrized by adding it to its transpose and multiplying by 0.5.

`S = 0.5(A + AT)`

Where A is a matrix and AT is its transpose.
*/

int main() {
  MatrixXd m = MatrixXd::Random(5,5);

  std::cout << m << std::endl << std::endl;

  /* Create a matrix m2 that is a symmetrized version of m */
  
    
  std::cout << m2 << std::endl << std::endl;

  /* Testing code below */
  assert(m2(0, 0) == m(0, 0));
  assert(m2(0, 0) == m(0, 0));
  assert(m2(1, 0) == m2(0, 1));
  assert(m2(2, 0) == m2(0, 2));
  assert(m2(2, 3) == m2(3, 2));
  std::cout << "All ok!" << std::endl;
} 
