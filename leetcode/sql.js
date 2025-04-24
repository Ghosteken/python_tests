module.exports = (sequelize, DataTypes) => {
    const Customer = sequelize.define('Customer', {
      id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
      },
      name: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
      email: {
        type: DataTypes.STRING(100),
        unique: true,
        allowNull: false,
      },
      phone_number: {
        type: DataTypes.STRING(15),
      },
      address: {
        type: DataTypes.STRING(255),
      },
    });
  
    Customer.associate = (models) => {
      Customer.hasMany(models.Account, { foreignKey: 'customer_id', as: 'accounts' });
      Customer.hasMany(models.Loan, { foreignKey: 'customer_id', as: 'loans' });
    };
  
    return Customer;
  };
  