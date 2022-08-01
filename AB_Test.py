################################################ ###
# Comparison of AB Test and Conversion of Bidding Methods
################################################ ###

################################################ ###
# Business Problem
################################################ ###

# Facebook recently available alternative to the bidding type called "maximumbidding"
#Introduced "average bidding", a new type of bid as #. One of our customers, bombbambomba.com,
# decided to test this new feature and have more conversions of averagebidding than maximumbidding
# he wants to do an A/B test to see if it returns. The A/B test has been going on for 1 month and
# bombabomba.com is now waiting for you to analyze the results of this A/B test.
# ultimate success criterion is Purchase. Therefore, the focus should be on Purchasemetric for statistical testing.

################################################ ###
# Dataset Story
################################################ ###
# What users see and click on in this dataset, which includes a company's website information
# There is information such as the number of advertisements, as well as the earnings information from here. Control and Test
#There are two separate data sets, the # group. These datasets are on separate pages of ab_testing.xlsxexcel.
# takes. Maximum Bidding was applied to the control group and AverageBidding was applied to the test group.

# impression: Ad views count
# Click: Number of clicks on the displayed ad
# Purchase: The number of products purchased after the ads clicked
# Earning: Earnings after purchased products

###################################################
# Project Tasks
###################################################
################################################ ###
# Task 1: Preparing and Analyzing Data
################################################ ###
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_Control=pd.read_excel("pyCharm_Protect/datasets/ab_testing.xlsx", sheet_name="Control Group")
df_Test=pd.read_excel("pyCharm_Protect/datasets/ab_testing.xlsx", sheet_name="Test Group")
df_Control.head()
df_Test.head()
df_Test.shape
df_Control.shape
df_Test.info()
df_Test.shape

df_Test.isnull().sum()
df_Control.isnull().sum()

df=pd.concat([df_Test,df_Control])

df_Test["Purchase"].mean()

df_Control["Purchase"].mean()

################################################ ###
# Task 2: Define A/B Test Hypothesis
################################################ ###
# Step 1: Define the hypothesis.

# H0 : M1 = M2 (There is no difference between the control group and test group purchasing averages.)
# H1 : M1!= M2 (There is a difference between the purchasing averages of the control group and test group.)


# H0: "Maximum Bidding" campaign offered "Average Bidding" campaign with Control group offered
# There is no statistically significant difference between the mean number of purchases of the test group.

# H1: "Maximum Bidding" campaign presented "Average Bidding" campaign with Control group offered
# There is a statistically significant difference between the mean number of purchases of the test group.


# Step 2: Analyze the purchase (gain) averages for the control and test group

df.groupby("group").agg({"Purchase": "mean"})

################################################ ###
# TASK 3: Performing Hypothesis Testing
################################################ ###

# Step 1: Check the assumptions before testing the hypothesis. These are Assumption of Normality and Homogeneity of Variance.

# Test separately whether the control and test groups comply with the normality assumption via the Purchase variable.

# Normality Assumption :
# H0: Normal distribution assumption is provided.
# H1: Normal distribution assumption not provided
# p < 0.05 H0 RED
# p > 0.05 H0 CANNOT BE REJECTED
# Is the assumption of normality according to the test result provided for the control and test groups?
# Interpret the p-values obtained.


test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.5891
# HO cannot be denied. The values  the control group provide the assumption of normal distribution.

test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# Variance Homogeneity :
# H0: Variances are homogeneous.
# H1: Variances are not homogeneous.
# p < 0.05 H0 RED
# p > 0.05 H0 CANNOT BE REJECTED
# Test whether the homogeneity of variance is provided for the control and test groups over the Purchase variable.
# Is the assumption of normality provided according to the test result? Interpret the p-values obtained.

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.1083
# HO cannot be denied. The values  the Control and Test groups provide the assumption of variance homogeneity.
# Variances are Homogeneous.


# Step 2: Select the appropriate test according to the Normality Assumption and Variance Homogeneity results

# Independent two-sample t-test is performed as assumptions are provided.
# H0: M1 = M2 (There is no mean difference between the control group and test group purchase mean.)
# H1: M1 != M2 (There is a mean difference between the control group and test group purchase mean)
# p<0.05 HO RED , p>0.05 HO CANNOT BE REJECTED

test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Step 3: Purchasing control and test groups, taking into account the p_value obtained as a result of the test
#Comment if there is a statistically significant difference between the # means.

# p-value=0.3493
# HO cannot be denied. There is no statistically significant difference between the control and test group purchasing averages.