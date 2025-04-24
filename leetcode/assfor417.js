// Aigberua Nicholas
// AUL/CMP/22/012
// CMP 417
// Full ERD for Banking Management System
// The Entity-Relationship Diagram (ERD) represents the logical structure of the Banking Management System, focusing on the relationships between its core entities.

// Entities and Their Attributes
// 1. Customer
// Attributes:
// id: Unique identifier for the customer (Primary Key).
// name: Full name of the customer.
// email: Contact email address (Unique).
// phone_number: Customer's phone number.
// address: Residential address.
// 2. Account
// Attributes:
// id: Unique identifier for the account (Primary Key).
// customer_id: Foreign Key linking to the Customer entity.
// type: Type of account (Savings, Current, Fixed Deposit).
// balance: Current account balance.
// 3. Transaction
// Attributes:
// id: Unique transaction identifier (Primary Key).
// account_id: Foreign Key linking to the Account entity.
// employee_id: Foreign Key linking to the Employee entity.
// type: Type of transaction (Deposit, Withdrawal, Transfer).
// amount: Transaction amount.
// date: Date and time of the transaction.
// 4. Loan
// Attributes:
// id: Unique loan identifier (Primary Key).
// customer_id: Foreign Key linking to the Customer entity.
// type: Loan type (Home, Auto, Personal).
// amount: Loan amount.
// interest_rate: Interest rate for the loan.
// start_date: Loan issuance date.
// end_date: Loan repayment end date.
// 5. Employee
// Attributes:
// id: Unique identifier for the employee (Primary Key).
// name: Employee's name.
// email: Contact email address (Unique).
// position: Role in the bank (e.g., Teller, Loan Officer).

// Relationships Between Entities
// Customer ↔ Account


// Relationship: One Customer can have many Accounts (1:N).
// Keys: customer_id in Account references id in Customer.
// Account ↔ Transaction


// Relationship: One Account can have many Transactions (1:N).
// Keys: account_id in Transaction references id in Account.
// Customer ↔ Loan


// Relationship: One Customer can have many Loans (1:N).
// Keys: customer_id in Loan references id in Customer.
// Employee ↔ Transaction


// Relationship: One Employee can process many Transactions (1:N).
// Keys: employee_id in Transaction references id in Employee.
// Employee ↔ Loan


// Relationship: One Employee can manage multiple Loans (1:N).
// Keys: employee_id in Loan references id in Employee.


// SQL Code for Table Creation
// CREATE TABLE Customer (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     name VARCHAR(100) NOT NULL,
//     email VARCHAR(100) UNIQUE NOT NULL,
//     phone_number VARCHAR(15),
//     address VARCHAR(255)
// );


// CREATE TABLE Account (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     customer_id INT NOT NULL,
//     type ENUM('Savings', 'Current', 'Fixed Deposit') NOT NULL,
//     balance DECIMAL(15, 2) DEFAULT 0.00,
//     FOREIGN KEY (customer_id) REFERENCES Customer(id) ON DELETE CASCADE
// );


// CREATE TABLE Employee (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     name VARCHAR(100) NOT NULL,
//     email VARCHAR(100) UNIQUE NOT NULL,
//     position VARCHAR(50)
// );


// CREATE TABLE Transaction (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     account_id INT NOT NULL,
//     employee_id INT,
//     type ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL,
//     amount DECIMAL(15, 2) NOT NULL,
//     date DATETIME DEFAULT CURRENT_TIMESTAMP,
//     FOREIGN KEY (account_id) REFERENCES Account(id) ON DELETE CASCADE,
//     FOREIGN KEY (employee_id) REFERENCES Employee(id) ON DELETE SET NULL
// );


// CREATE TABLE Loan (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     customer_id INT NOT NULL,
//     type ENUM('Home', 'Auto', 'Personal') NOT NULL,
//     amount DECIMAL(15, 2) NOT NULL,
//     interest_rate DECIMAL(5, 2) NOT NULL,
//     start_date DATE NOT NULL,
//     end_date DATE NOT NULL,
//     FOREIGN KEY (customer_id) REFERENCES Customer(id) ON DELETE CASCADE
// );



// Features
// Primary Keys:
// id columns in all tables serve as unique identifiers.
// Foreign Keys:
// customer_id in Account and Loan references Customer(id).
// account_id in Transaction references Account(id).
// employee_id in Transaction references Employee(id).
// Constraints:
// Unique constraints for email in Customer and Employee tables.
// ENUM for predefined values in Account.type, Transaction.type, and Loan.type.
// Cascade Deletion:
// If a Customer is deleted, associated Account and Loan records are also deleted.
// If an Account is deleted, related Transaction records are removed.



// Model Definitions in Nodejs
// 1.
// module.exports = (sequelize, DataTypes) => {
//     const Customer = sequelize.define('Customer', {
//       id: {
//         type: DataTypes.INTEGER,
//         primaryKey: true,
//         autoIncrement: true,
//       },
//       name: {
//         type: DataTypes.STRING(100),
//         allowNull: false,
//       },
//       email: {
//         type: DataTypes.STRING(100),
//         unique: true,
//         allowNull: false,
//       },
//       phone_number: {
//         type: DataTypes.STRING(15),
//       },
//       address: {
//         type: DataTypes.STRING(255),
//       },
//     });
 
//     Customer.associate = (models) => {
//       Customer.hasMany(models.Account, { foreignKey: 'customer_id', as: 'accounts' });
//       Customer.hasMany(models.Loan, { foreignKey: 'customer_id', as: 'loans' });
//     };
 
//     return Customer;
//   };
 

// 2.
// module.exports = (sequelize, DataTypes) => {
//     const Account = sequelize.define('Account', {
//       id: {
//         type: DataTypes.INTEGER,
//         primaryKey: true,
//         autoIncrement: true,
//       },
//       customer_id: {
//         type: DataTypes.INTEGER,
//         allowNull: false,
//       },
//       type: {
//         type: DataTypes.ENUM('Savings', 'Current', 'Fixed'),
//         allowNull: false,
//       },
//       balance: {
//         type: DataTypes.FLOAT,
//         defaultValue: 0.0,
//       },
//     });
 
//     Account.associate = (models) => {
//       Account.belongsTo(models.Customer, { foreignKey: 'customer_id', as: 'customer' });
//       Account.hasMany(models.Transaction, { foreignKey: 'account_id', as: 'transactions' });
//     };
 
//     return Account;
//   };
 




// ERD DIAGRAM:

// Customer
//     |--< Account
//     |       |--< Transaction
//     |
//     |--< Loan

// Employee
//     |--< Transaction






// Customer Table

// | id  | name         | email              | phone_number | address                |
// |-----|--------------|--------------------|--------------|------------------------|
// | 1   | John Doe     | john@example.com   | 1234567890   | 123 Elm Street         |
// | 2   | Jane Smith   | jane@example.com   | 9876543210   | 456 Oak Avenue         |
// | 3   | Bob Johnson  | bob@example.com    | 1122334455   | 789 Pine Road          |


// Account Table

// | id  | customer_id | type        | balance    |
// |-----|-------------|-------------|------------|
// | 1   | 1           | Savings     | 5000.00    |
// | 2   | 1           | Current     | 2000.00    |
// | 3   | 2           | Savings     | 10000.00   |
// | 4   | 3           | Fixed       | 25000.00   |



// Transaction Table

// | id  | account_id | employee_id | type        | amount   | date                |
// |-----|------------|-------------|-------------|----------|---------------------|
// | 1   | 1          | 1           | Deposit     | 2000.00  | 2025-01-15 10:30:00 |
// | 2   | 2          | NULL        | Withdrawal  | 500.00   | 2025-01-16 14:15:00 |
// | 3   | 3          | 2           | Transfer    | 1000.00  | 2025-01-16 16:00:00 |
// | 4   | 4          | 3           | Deposit     | 5000.00  | 2025-01-17 09:45:00 |



// Loan Table
// | id  | customer_id | type        | amount    | interest_rate | start_date | end_date   |
// |-----|-------------|-------------|-----------|---------------|------------|------------|
// | 1   | 1           | Home        | 50000.00  | 3.5           | 2025-01-01 | 2035-01-01 |
// | 2   | 2           | Auto        | 15000.00  | 4.0           | 2025-02-01 | 2030-02-01 |
// | 3   | 3           | Personal    | 2000.00   | 5.0           | 2025-03-01 | 2027-03-01 |



// Employee Table
// | id  | name          | email                | position        |
// |-----|---------------|----------------------|-----------------|
// | 1   | Alice Walker  | alice@example.com    | Teller          |
// | 2   | Mark Evans    | mark@example.com     | Manager         |
// | 3   | Sarah Johnson | sarah@example.com    | Loan Officer    |

// ---


// Notes
// Relationships:


// Customer is related to Account (1-to-Many).
// Account is related to Transaction (1-to-Many).
// Transaction is related to Employee (Many-to-1).
// Customer is related to Loan (1-to-Many).
// Data Types:


// Primary keys are Integer with auto-increment.
// Enumerations (Enum) represent specific types like account and transaction types.
// Decimal is used for monetary values.
// Constraints:


// ON DELETE CASCADE ensures related data is deleted when a parent record is removed.
// ON DELETE SET NULL for Transaction.employee_id ensures no orphaned foreign keys.

