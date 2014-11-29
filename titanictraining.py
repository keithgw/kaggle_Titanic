"""Use Titanic Data to predict who will survive

VARIABLE DESCRIPTIONS:
survival        Survival
                (0 = No; 1 = Yes)
pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)

SPECIAL NOTES:
Pclass is a proxy for socio-economic status (SES)
 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

Age is in Years; Fractional if Age less than One (1)
 If the Age is Estimated, it is in the form xx.5

With respect to the family relation variables (i.e. sibsp and parch)
some relations were ignored.  The following are the definitions used
for sibsp and parch.

Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
Parent:   Mother or Father of Passenger Aboard Titanic
Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic

Other family relatives excluded from this study include cousins,
nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
only with a nanny, therefore parch=0 for them.  As well, some
travelled with very close friends or neighbors in a village, however,
the definitions do not support such relations.

data has column headers:
PassengerId    Survived    Pclass    Name                    Sex    Age    SibSp    Parch    Ticket    Fare    Cabin    Embarked
1              0           3         Brand, Mr. Owen Harris  male   22     1        0        A/5 21171 7.25             S
"""

from numpy import loadtxt, size, where

# load data as string, skip name, ticket, cabin
data = loadtxt('train.csv', dtype=str, delimiter=',', skiprows=1, usecols=[0,1,2,5,6,7,8,10,12])

# Variables for column indices
PASSENGER_ID = 0
SURVIVED = 1
P_CLASS = 2
SEX = 3
AGE = 4
SIB_SP = 5
PARCH = 6
FARE = 7
EMBARKED = 8
BREAK = '=' * 90

# calculate proportion of survivors P(survival)
number_passengers = float(data[:, PASSENGER_ID].size)
number_survivors = sum(data[:,SURVIVED].astype(float))
proportion_survivors = number_survivors / number_passengers

# calculate sex survival rates
# H0: P(survival|female) = P(survival)
women_only = data[:, SEX] == 'female'
men_only = data[:, SEX] == 'male'
female_survivors = sum(data[where(women_only)[0], SURVIVED].astype(float))
male_survivors = sum(data[where(men_only)[0], SURVIVED].astype(float))
proportion_female_survivors = female_survivors / sum(women_only)
proportion_male_survivors = male_survivors / sum(men_only)

# make a two-way table for sex vs survival
print '{0:^10}{1:^10}{2:^10}{3:^10}'.format('', 'Survived', '!Survive', 'Row Total')
print '{0:^10}{1:^10.0f}{2:^10.0f}{3:^10}'.format('female', female_survivors, 
                                                    sum(women_only) - female_survivors, 
                                                    sum(women_only))
print '{0:^10}{1:^10.0f}{2:^10.0f}{3:^10}'.format('male', male_survivors, 
                                                    sum(men_only) - male_survivors, 
                                                    sum(men_only))
print '{0:^10}{1:^10.0f}{2:^10.0f}{3:^10.0f}'.format('Col Total', number_survivors, 
                                                    number_passengers - number_survivors, 
                                                    number_passengers)
# analysis of sex dependence on survival
print BREAK
print 'The probability of survival, P(survival), is {}%.'.format((proportion_survivors * 100).round(2))
print 'The female survival rate, P(survival|female), is {}%.'.format((proportion_female_survivors * 100).round(2))
print 'The male survival rate, P(survival|male), is {}%.'.format((proportion_male_survivors * 100).round(2))
print 'The null hypothesis, P(survival|female) = P(survival) can be rejected'
print 'Being female provides a {:.2f}X probability of survival'.format(proportion_female_survivors/proportion_survivors)
print BREAK

# calculate class survival rates
first_class = data[:, P_CLASS] == '1'
second_class = data[:, P_CLASS] == '2'
third_class = data[:, P_CLASS] == '3'
first_class_survivors = sum(data[where(first_class)[0], SURVIVED].astype(float))
second_class_survivors = sum(data[where(second_class)[0], SURVIVED].astype(float))
third_class_survivors = sum(data[where(third_class)[0], SURVIVED].astype(float))
first_class_rate = first_class_survivors / sum(first_class)
second_class_rate = second_class_survivors / sum(second_class)
third_class_rate = third_class_survivors / sum(third_class)

# make a two-way table for survival dependence on class
print '{0:^10}{1:^10}{2:^10}{3:^10}'.format('', 'Survived', '!Survive', 'Row Total')