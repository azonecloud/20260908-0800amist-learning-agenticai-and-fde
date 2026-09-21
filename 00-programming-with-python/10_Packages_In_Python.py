# In Python, a package is a way of organizing related modules into a single directory hierarchy. 
# Packages provide a hierarchical structure for organizing modules, making it easier to manage large projects and avoid naming conflicts between modules. 
# A package is essentially a directory that contains a special file called `__init__.py`, which is executed when the package is imported.


# 1. **Creating a Package:**
# To create a package, you need to create a directory and place a file named `__init__.py` inside it. 
# This file can be empty, or it can contain initialization code for the package.

# loans_packages/
    # __init__.py
    # creditScore.py
    # creditGrades.py


# 2. **Importing Modules from a Package:**
# You can import modules from a package using the `import` statement. 
# When you import a module from a package, Python executes the `__init__.py` file inside the package (if it exists) to perform any initialization tasks.


# Importing a module from a module1
import utils.banking_packages.InterestAmount as calInterestAmount
import utils.banking_packages.TaxAmount as calTaxAmount


# Using a function from the imported module
result_InterestAmount   = calInterestAmount.genereateInterestAmount(20000,10)
result_TaxAmount        = calTaxAmount.genereatTaxAmount(result_InterestAmount)


print("Interest Amount to be paid = ",result_InterestAmount)
print("Tax to be Paid on Interest Levied =",result_TaxAmount)
