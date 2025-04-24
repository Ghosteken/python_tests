# class Customer(Base):
#     __tablename__ = 'customer'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     phone_number = Column(String(15))
#     address = Column(String(255))
#     accounts = relationship('Account', back_populates='customer')
#     loans = relationship('Loan', back_populates='customer')


# class Account(Base):
#     __tablename__ = 'account'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
#     type = Column(Enum('Savings', 'Current', 'Fixed Deposit'), nullable=False)
#     balance = Column(DECIMAL(15, 2), default=0.00)
#     customer = relationship('Customer', back_populates='accounts')
#     transactions = relationship('Transaction', back_populates='account')

# class Transaction(Base):
#     __tablename__ = 'transaction'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
#     employee_id = Column(Integer, ForeignKey('employee.id'))
#     type = Column(Enum('Deposit', 'Withdrawal', 'Transfer'), nullable=False)
#     amount = Column(DECIMAL(15, 2), nullable=False)
#     date = Column(DateTime, default=datetime.utcnow)
#     account = relationship('Account', back_populates='transactions')
#     employee = relationship('Employee', back_populates='transactions')
