# ATM-Project
Automated Teller Machine Program - Python

## OVERVIEW
This repository contains the source code and resources for an ATM (Automated Teller Machine) simulation project. The project aims to replicate basic functionalities of an ATM system, allowing users to perform various banking operations such as checking balance, depositing money, withdrawing cash, changing PIN, and viewing transaction statements.
## GIT
I consistently utilized Git to commit and push my progress for the ATM project to GitHub, ensuring regular updates to the repository. My workflow primarily involved working in Visual Studio Code, where I developed and tested the code. I maintained a consistent cadence of uploading code to GitHub through Visual Studio Code, reflecting my contributions and project activity on the GitHub [contribution chart](https://github.com/Rajwaghela369).
## UML Diagrams

Activity Diagram: Illustrates the flow of actions within the ATM system, from login to transaction completion. [Diagram](https://github.com/Rajwaghela369/ATM-Project/blob/main/UML%20Diagrams/Activity%20Raj.png)

Use Case Diagram: Shows possible interactions between users and the ATM, covering actions like login, withdrawals, deposits, and balance inquiries. [Diagram](https://github.com/Rajwaghela369/ATM-Project/blob/main/UML%20Diagrams/Use%20case%20Raj.png)

State Diagram: Describes the various states of the ATM and how they change in response to events, such as idle, processing transactions, and awaiting user input. [Diagram](https://github.com/Rajwaghela369/ATM-Project/blob/main/UML%20Diagrams/Statediagram%20Raj.png)

## DDD 
I've outlined the [problem space](https://github.com/Rajwaghela369/ATM-Project/blob/main/DDD/Raj%20%20dd%20diagarm.png) for the ATM project, dividing it into different subdomains.

## METRICS
  
I employed SonarQube to conduct automated analyses of the ATM project's source code, utilizing a comprehensive set of criteria to evaluate code quality. SonarQube, an open-source tool, facilitates continuous code quality inspection by employing static code analysis to identify bugs, code smells, and other key metrics.

The following metrics offer a comprehensive assessment of the code by SonarCloud:
  
  Quality Gate Status: [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project)
  
  Bugs: [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project)
  
  Code Smells: [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project) 
  
  Duplicated Lines: [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project) 
  
  Lines of Code: [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project) 
  
  Reliability Rating: [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project) 
  
  Security Rating: [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project)
  
  Technical Debt: [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project) 
  
  Maintainability Rating: [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project)
  
  Vulnerabilities: [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Rajwaghela369_ATM-Project&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Rajwaghela369_ATM-Project)
  
## Clean Code Developement 

I have included a main [sheet](https://github.com/Rajwaghela369/ATM-Project/blob/main/Cheat%20Sheet/sheet.txt) that served as a guide throughout the development of this application.  Here are some key points:

  1. The code is split into separate modules, each handling specific tasks. This approach enhances understanding and maintainability by isolating functionality into cohesive units.

  2. Meaningful names are used for variables and functions, enhancing code readability and comprehension. For example, variables like ([eg](https://github.com/Rajwaghela369/ATM-Project/blob/670e259c3710487df09b4f0725d05ac47c1904b8/ATM_Project/Authentication.py#L34)) and functions like ([eg](https://github.com/Rajwaghela369/ATM-Project/blob/670e259c3710487df09b4f0725d05ac47c1904b8/ATM_Project/Account.py#L39)) convey their purpose clearly.

  3.  Standardized naming conventions are followed consistently across the codebase, ensuring clarity and uniformity. For instance, boolean flags like ["valid"](https://github.com/Rajwaghela369/ATM-Project/blob/670e259c3710487df09b4f0725d05ac47c1904b8/ATM_Project/Database.py#L43) are used for user verification, adhering to established conventions.

  4. Informative comments like ([eg](https://github.com/Rajwaghela369/ATM-Project/blob/670e259c3710487df09b4f0725d05ac47c1904b8/ATM_Project/Authentication.py#L32C12-L32C34)) are provided throughout the codebase to clarify complex logic or functionalities. These comments serve as valuable documentation, aiding others in understanding the code better and facilitating collaboration.

## BUILD AND CI/CD

For my project, I've seamlessly integrated the build and Continuous Integration/Continuous Deployment (CI/CD) processes using GitLab CI.

Given that my project is based on Python, I opted for GitLab CI as the build management tool.

In the build stage, I've configured GitLab CI to handle the build process. However, due to limitations with GUI-based projects in GitLab CI, I focused the build process specifically on key Python files like Database.py, Authentication.py, & Transcations.py (present in ATM_Project Folder).

In the subsequent test stage, I executed the test.py file to thoroughly test the functionality of my project.

Throughout the CI/CD pipeline, each stage is meticulously configured and automated using the GitLab CI configuration file (`python-app-build-&-test.yml`). This file not only defines the build, test, and deployment stages but also includes necessary dependencies to trigger and streamline the entire CI/CD pipeline.
Here is workflow [output](https://github.com/Rajwaghela369/ATM-Project/actions/runs/8453946398).

## UNIT TESTS

I have developed a comprehensive unit testing (file: [test.py](https://github.com/Rajwaghela369/ATM-Project/blob/main/ATM_Project/test.py)) suite for the ATM project to ensure the reliability and functionality of its key features.

The test suite consists of 6 test cases, each specifically targeting different functionalities of the ATM application, including user authentication, account details retrieval, balance checking, depositing, withdrawal, and PIN change.

Upon executing the unit tests, all test cases have successfully passed, indicating that the implemented features are working as intended and meeting the specified requirements.

For a detailed overview of the test cases and their outcomes, refer to the provided unit testing code, where each test case is meticulously designed to verify the correctness and robustness of the ATM functionalities.

Additionally, you can find a summary of the passed test cases in the test execution [snapshot](https://github.com/Rajwaghela369/ATM-Project/blob/main/Test_outputs/tests_result.png), ensuring the thorough validation of the application's behavior before deployment.

## IDE Visual Studio Code 

I have utilized Visual Studio Code (VS Code) as the Integrated Development Environment (IDE) for this project on my Mac.
Some useful shortcuts in VS Code that I found particularly helpful:

  1. Cmd + Shift + B: Build project
  2. F5: Run or debug the application
  3. Cmd + /: Comment/uncomment lines of code
  4. Cmd + D: Select next occurrence of the current word
  5. Cmd + F: Search within the file

These shortcuts and features contribute to a smoother development experience in Visual Studio Code for the ATM project on macOS.


Advantages of using Visual Studio Code for development on macOS:

  1. Cross-platform compatibility for seamless development across different operating systems.
  2. Extensive plugin ecosystem for customizable functionality and enhanced productivity.
  3. Active community support for learning, collaboration, and access to helpful resources.

## DSL 

The ATM project facilitates banking operations like withdrawals, deposits, balance inquiries, and PIN changes. It provides a user-friendly interface for customers to interact with their accounts securely. The code is structured into classes like ATM, Database, Authentication, Transaction, and Account_management, each handling specific functionalities to ensure modularity and maintainability. Functional programming principles such as modularity, immutability, and pure functions are emphasized for robustness and ease of maintenance. The code focuses on efficient state management within the application, ensuring a smooth user experience without the need for domain-specific language or external DSLs.

## FUNCTIONAL PROGRAMMING

The provided code exhibits functional programming principles through its modular and reusable design. Let's delve into some examples of functional programming aspects within the code:

  1. Modularity: The code is divided into multiple modules/classes such as ATM, Database, Authentication, Transaction, and Account_management. Each module/class serves a specific purpose and encapsulates related functionalities. This promotes modularity and code organization.

  2. Pure Functions: Many functions within the code exhibit the characteristics of pure functions. For instance, methods like [process_withdrawal](https://github.com/Rajwaghela369/ATM-Project/blob/514b5325e8934db92f834e09473e8b7fce43a6ce/ATM_Project/Transactions.py#L17) and [process_deposit](https://github.com/Rajwaghela369/ATM-Project/blob/514b5325e8934db92f834e09473e8b7fce43a6ce/ATM_Project/Transactions.py#L41) in the Transaction class take input parameters and produce output without modifying any external state. They rely only on their input arguments to produce the output.

  3. Immutability: Immutable data structures are used in several places. For instance, in the Database class, when [updating](https://github.com/Rajwaghela369/ATM-Project/blob/514b5325e8934db92f834e09473e8b7fce43a6ce/ATM_Project/Database.py#L59) user records, a new copy of the records is created with the necessary modifications instead of modifying the existing records directly.

  4. Higher-Order Functions: While not explicitly demonstrated in the provided code, higher-order functions can be implemented in Python. These are functions that take other functions as arguments or return functions as results. Functional programming often encourages the use of higher-order functions for abstraction and code reuse.

  5. Avoidance of Side Effects: Functional programming emphasizes the avoidance of side effects, where functions don't modify state outside their scope. While the provided code interacts with external files (such as YAML database files) and prints messages to the console, it generally adheres to minimizing side effects by encapsulating state changes within functions.

  6. Statelessness: The ATM class utilizes Streamlit's session state to maintain the [current state](https://github.com/Rajwaghela369/ATM-Project/blob/514b5325e8934db92f834e09473e8b7fce43a6ce/ATM_Project/main.py#L56) of the application. By managing state internally and not relying on external or global state, the code remains more predictable and easier to reason about.

These are some of the functional programming principles observed in the provided code. By adhering to these principles, the code becomes more maintainable, testable, and easier to reason about.

## Outputs

All outputs are available in [ATM ouputs](https://github.com/Rajwaghela369/ATM-Project/tree/main/ATM%20outputs) folder
