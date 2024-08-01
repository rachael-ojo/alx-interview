0x01 Lockboxes
Description
0x01-lockboxes is a Node.js project that explores solutions to a problem involving lockboxes. The goal is to determine if all lockboxes can be unlocked starting from the first box. Each box may contain keys to other boxes, and you need to find a way to unlock all of them.

Requirements
Node.js (>= 12.x)
npm (>= 6.x)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/0x01-lockboxes.git
cd 0x01-lockboxes
Install the dependencies:

bash
Copy code
npm install
Usage
To run the main program, execute:

bash
Copy code
node main.js
You can modify the input directly in main.js to test different sets of lockboxes.

Testing
To run the tests, use:

bash
Copy code
npm test
Example
If main.js contains the following input:

javascript
Copy code
const lockboxes = [[1], [2], [3], []];
console.log(canUnlockAll(lockboxes));
The output will be:

bash
Copy code
true
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-foo).
Commit your changes (git commit -am 'Add feature foo').
Push to the branch (git push origin feature-foo).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to all contributors and those who helped in the development of this project.
