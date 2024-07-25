# 0x00. Pascal's Triangle

## Description

This project implements Pascal's Triangle, a triangular array of the binomial coefficients. Each number is the sum of the two directly above it. The triangle starts with a single 1 at the top and has an additional row added below, with the coefficients computed iteratively.

## Structure

0x00. Pascal's Triangle
│
├── pascals_triangle.js # Main implementation file
├── README.md # This readme file
└── test # Directory containing test cases
├── test_cases.json # Sample test cases
└── test_runner.js # Script to run tests

csharp
Copy code

## Usage

### Prerequisites

Ensure you have Node.js installed on your machine. You can download it from [Node.js](https://nodejs.org/).

### Installation

Clone this repository to your local machine using:
```sh
git clone https://github.com/your_username/0x00-pascals-triangle.git
Navigate to the project directory:

sh
Copy code
cd 0x00-pascals-triangle
Install dependencies (if any):

sh
Copy code
npm install
Running the Program
To generate Pascal's Triangle, run:

sh
Copy code
node pascals_triangle.js
Running Tests
To run the provided test cases, navigate to the test directory and run:

sh
Copy code
node test/test_runner.js
Example
Generating Pascal's Triangle for 5 rows:

sh
Copy code
node pascals_triangle.js 5
Expected Output:

csharp
Copy code
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure you follow the coding style and include relevant tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Pascal's Triangle concept from mathematics
Node.js for the runtime environment
