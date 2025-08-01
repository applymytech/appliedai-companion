# Converted PDF

Python for Software

Development

Hans-Petter Halvorsen

Python Software Development

Do you want to learn Software

Development?

OK Cancel

https://www.halvorsen.blog

Python for Software Development

Python for Software Development

Hans-Petter Halvorsen

2020

Python for Science and Engineering

(cid:13)cHans-Petter Halvorsen

September 9, 2020

1

Preface

Python is a popular programming language, and it is one of the most used pro-

gramming languages today.

Pythonworksonallthemainplatformsandoperatingsystemsusedtoday,such

Windows, macOS, and Linux.

Python is a multi-purpose programming language, which can be use for simu-

lation, creating web pages, communicate with database systems, etc.

My Blog/Web Site [1]:

https://www.halvorsen.blog

Here you find lots of technical resources about Technology, Programming, Soft-

ware Engineering, Automation and Control, Industrial IT, etc.

Here you find my Web page with Python resources:

https://www.halvorsen.blog/documents/programming/python/

These resources are a supplement to this textbook. Here you can download the

software, download code examples, etc.

This Textbook is written in LATEXusing Overleaf.

LATEXis a document preparation system used for the communication and publi-

cation of scientific documents.

2

For more information about LATEX:

https://www.latex-project.org

Overleafisaweb-basesLATEXsystem,meaningyoucanwriteyourLATEXdocuments

in your web browser, you co-work and share documents with others.

For more information about Overleaf:

https://www.overleaf.com

Python Books

You find other Python textbooks within different domains on my Python Web

page:

https://www.halvorsen.blog/documents/programming/python/

Python Books:

• Python Programming - This is a textbook in Python Programming

withlotsofPracticalExamplesandExercises. Youwilllearnthenecessary

foundation for basic programming with focus on Python.

• Python for Science and Engineering - This is a textbook in Python

ProgrammingwithlotsofExamples,Exercises,andPracticalApplications

within Mathematics, Simulations, etc. The focus is on numerical calcu-

lations in mathematics and engineering. Necessary theory is presented in

addition to many practical examples.

• Python for Control Engineering - This is a textbook in Python Pro-

gramming with lots of Examples, Exercises, and Practical Applications

within Mathematics, Simulations, Control Systems, DAQ, Database Sys-

tems, etc. The focus is on the use of Python within measurements, data

collection (DAQ), control technology, both analysis of control systems

(stability analysis, frequency response, ...) and implementation of control

systems (PID, etc.). Required theory is presented in addition to many

practical examples and exercises in Python.

• PythonforSoftwareDevelopment-ThisisatextbookinPythonPro-

gramming with lots of Examples, Exercises, and Practical Applications

within Software Systems, Software Development, Software Engineering,

Database Systems, Web Application Desktop Applications, GUI Applica-

tions,etc. ThefocusisontheuseofPythonforcreatingmodernSoftware

Systems. Required theory is presented in addition to many practical ex-

amples and exercises in Python.

3

Programming

The way we create software today has changed dramatically the last 30 years,

from the childhood of personal computers in the early 80s to today’s powerful

devices such as Smartphones, Tablets and PCs.

The Internet has also changed the way we use devices and software. We still

havetraditionaldesktopapplications, butWebSites, WebApplicationsandso-

called Apps for Smartphones, etc. are dominating the software market today.

We need to find and learn Programming Languages that are suitable for the

New Age of Programming.

We have today several thousand different Programming Languages today. I

guess you will need to learn more than one Programming Language to survive

in today’s software market.

You find lots of Programming Resources here:

https://www.halvorsen.blog/documents/programming/

Software Engineering

Software Engineering is the discipline for creating software applications. A

systematic approach to the design, development, testing, and maintenance of

software.

The main parts or phases in the Software Engineering process are:

• Planning

• Requirements Analysis

• Design

• Implementation

• Testing

• Deployment and Maintenance

You find lots of Software Engineering Resources here:

https://www.halvorsen.blog/documents/programming/software ngineering/

e

4

5

Contents

I Getting Started with Python 12

1 Introduction 13

1.1 The New Age of Programming . . . . . . . . . . . . . . . . . . . 13

1.2 MATLAB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2 What is Python? 19

2.1 Introduction to Python . . . . . . . . . . . . . . . . . . . . . . . 19

2.1.1 Interpreted vs. Compiled . . . . . . . . . . . . . . . . . . 20

2.2 Python Packages . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.2.1 Python Packages for Science and Numerical Computations 22

2.3 Anaconda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2.4 Python Editors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

2.4.1 Python IDLE . . . . . . . . . . . . . . . . . . . . . . . . . 23

2.4.2 Visual Studio Code. . . . . . . . . . . . . . . . . . . . . . 24

2.4.3 Spyder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

2.4.4 Visual Studio . . . . . . . . . . . . . . . . . . . . . . . . . 24

2.4.5 PyCharm . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

2.4.6 Wing Python IDE . . . . . . . . . . . . . . . . . . . . . . 25

2.4.7 Jupyter Notebook . . . . . . . . . . . . . . . . . . . . . . 25

2.5 Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

2.6 Installing Python . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

2.6.1 Python Windows 10 Store App . . . . . . . . . . . . . . . 26

2.6.2 Installing Anaconda . . . . . . . . . . . . . . . . . . . . . 26

2.6.3 Installing Visual Studio Code . . . . . . . . . . . . . . . . 26

3 Start using Python 28

3.1 Python IDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.2 My first Python program . . . . . . . . . . . . . . . . . . . . . . 28

3.3 Python Shell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.4 Running Python from the Console . . . . . . . . . . . . . . . . . 29

3.4.1 Opening the Console on macOS. . . . . . . . . . . . . . . 30

3.4.2 Opening the Console on Windows . . . . . . . . . . . . . 31

3.4.3 Add Python to Path . . . . . . . . . . . . . . . . . . . . . 31

3.5 Scripting Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

3.5.1 Run Python Scripts from the Python IDLE . . . . . . . . 33

3.5.2 Run Python Scripts from the Console (Terminal) macOS 34

3.5.3 Run Python Scripts from the Command Prompt in Win-

dows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

6

3.5.4 Run Python Scripts from Spyder . . . . . . . . . . . . . . 35

4 Basic Python Programming 38

4.1 Basic Python Program . . . . . . . . . . . . . . . . . . . . . . . . 38

4.1.1 Get Help . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

4.2 Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

4.2.1 Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

4.2.2 Strings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

4.2.3 String Input. . . . . . . . . . . . . . . . . . . . . . . . . . 42

4.3 Built-in Functions . . . . . . . . . . . . . . . . . . . . . . . . . . 42

4.4 Python Standard Library . . . . . . . . . . . . . . . . . . . . . . 43

4.5 Using Python Libraries, Packages and Modules . . . . . . . . . . 44

4.5.1 Python Packages . . . . . . . . . . . . . . . . . . . . . . . 46

4.6 Plotting in Python . . . . . . . . . . . . . . . . . . . . . . . . . . 46

4.6.1 Subplots . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

4.6.2 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

II Python Programming 52

5 Python Programming 53

5.1 If ... Else . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

5.2 Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

5.3 For Loops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

5.3.1 Nested For Loops . . . . . . . . . . . . . . . . . . . . . . . 59

5.4 While Loops. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

5.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

6 Creating Functions in Python 62

6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

6.2 Functions with multiple return values . . . . . . . . . . . . . . . 64

6.3 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

7 Creating Classes in Python 68

7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

7.2 The init () Function . . . . . . . . . . . . . . . . . . . . . . . . 69

7.3 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

8 Creating Python Modules 73

8.1 Python Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

8.2 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

9 File Handling in Python 76

9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

9.2 Write Data to a File . . . . . . . . . . . . . . . . . . . . . . . . . 76

9.3 Read Data from a File . . . . . . . . . . . . . . . . . . . . . . . . 77

9.4 Logging Data to File . . . . . . . . . . . . . . . . . . . . . . . . . 77

9.5 Web Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

9.6 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

7

10 Error Handling in Python 81

10.1 Introduction to Error Handling . . . . . . . . . . . . . . . . . . . 81

10.1.1 Syntax Errors . . . . . . . . . . . . . . . . . . . . . . . . . 81

10.1.2 Exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . 81

10.2 Exceptions Handling . . . . . . . . . . . . . . . . . . . . . . . . . 82

11 Debugging in Python 84

12 Installing and using Python Packages 85

12.1 What is PIP? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

III Python Environments and Distributions 86

13 Introduction to Python Environments and Distributions 87

13.1 Package and Environment Managers . . . . . . . . . . . . . . . . 88

13.1.1 PIP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

13.1.2 Conda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

13.2 Python Virtual Environments . . . . . . . . . . . . . . . . . . . . 89

14 Anaconda 90

14.1 Anaconda Navigator . . . . . . . . . . . . . . . . . . . . . . . . . 90

14.2 Anaconda Prompt . . . . . . . . . . . . . . . . . . . . . . . . . . 90

15 Enthought Canopy 93

IV Python Editors 94

16 Python Editors 95

17 Spyder 97

17.1 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98

18 Visual Studio Code 100

18.1 Introduction to Visual Studio Code . . . . . . . . . . . . . . . . . 100

18.2 Python in Visual Studio Code . . . . . . . . . . . . . . . . . . . . 101

19 Visual Studio 102

19.1 Introduction to Visual Studio . . . . . . . . . . . . . . . . . . . . 102

19.2 Work with Python in Visual Studio. . . . . . . . . . . . . . . . . 102

19.2.1 Make Visual Studio ready for Python Programming . . . 103

19.2.2 Python Interactive . . . . . . . . . . . . . . . . . . . . . . 103

19.2.3 New Python Project . . . . . . . . . . . . . . . . . . . . . 104

20 PyCharm 110

21 Wing Python IDE 112

22 Jupyter Notebook 114

22.1 JupyterHub . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

22.2 Microsoft Azure Notebooks . . . . . . . . . . . . . . . . . . . . . 115

8

V Data Acquisition (DAQ) with Python 117

23 Plotting Sensor Data 118

23.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

23.2 Introduction to Real-Time Plotting . . . . . . . . . . . . . . . . . 118

23.3 Real-Time Plotting with Animation . . . . . . . . . . . . . . . . 120

23.3.1 Speeding Up the Plot Animation . . . . . . . . . . . . . . 122

24 Data Acquisition (DAQ) with Python 125

24.1 Introduction to DAQ . . . . . . . . . . . . . . . . . . . . . . . . . 125

24.2 Data Acquisition using NI DAQ Devices . . . . . . . . . . . . . . 125

24.2.1 NI-DAQmx . . . . . . . . . . . . . . . . . . . . . . . . . . 127

24.2.2 Measurement Automation Explorer (MAX) . . . . . . . . 128

24.3 NI-DAQmx Python API . . . . . . . . . . . . . . . . . . . . . . . 128

24.3.1 Analog Write . . . . . . . . . . . . . . . . . . . . . . . . . 129

24.3.2 Analog Read . . . . . . . . . . . . . . . . . . . . . . . . . 129

24.3.3 Digital Write . . . . . . . . . . . . . . . . . . . . . . . . . 131

24.3.4 Digital Read . . . . . . . . . . . . . . . . . . . . . . . . . 131

24.4 Controlling LEDs . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

24.5 Read Data from Temperature Sensors . . . . . . . . . . . . . . . 134

24.5.1 Read Data from TMP36 Temperature Sensor . . . . . . . 134

24.5.2 Read Data from Thermistor . . . . . . . . . . . . . . . . . 138

24.5.3 Read Data NI TC-01 Thermocouple Device . . . . . . . . 142

24.6 Data Logging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

VI Python Database Development 144

25 Database Applications with Python 145

25.1 Structured Query Language (SQL) . . . . . . . . . . . . . . . . . 145

25.2 SQL Server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

25.3 MySQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

25.4 MongoDB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

26 Structured Query Language (SQL) 147

27 SQL Server with Python 148

27.1 Introduction to SQL Server . . . . . . . . . . . . . . . . . . . . . 148

27.2 SQL Server drivers for Python . . . . . . . . . . . . . . . . . . . 148

27.3 pyodbc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148

27.3.1 Installation of pyodbc . . . . . . . . . . . . . . . . . . . . 148

27.3.2 ODBC Drivers . . . . . . . . . . . . . . . . . . . . . . . . 148

27.4 SQL Server Python Examples . . . . . . . . . . . . . . . . . . . . 149

27.5 Stored Procedures . . . . . . . . . . . . . . . . . . . . . . . . . . 150

27.6 Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

27.7 pymssql . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

27.8 Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

28 MySQL with Python 151

9

29 MongoDB with Python 152

29.1 Introduction to MongoDB . . . . . . . . . . . . . . . . . . . . . . 152

29.2 MongoDB with Python . . . . . . . . . . . . . . . . . . . . . . . 152

29.2.1 PyMongo . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

29.3 Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . 153

VII Python Application Development 154

30 Development of Applications with Python 155

30.1 Mathematics, Science and Engineering . . . . . . . . . . . . . . . 156

30.2 Desktop GUI Applications . . . . . . . . . . . . . . . . . . . . . . 156

30.2.1 PyQt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

30.2.2 PySide2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

30.2.3 Tkinter . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

30.2.4 WxPython . . . . . . . . . . . . . . . . . . . . . . . . . . 158

30.3 Web Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

30.4 Database Applications . . . . . . . . . . . . . . . . . . . . . . . . 159

30.4.1 SQL Server . . . . . . . . . . . . . . . . . . . . . . . . . . 159

30.4.2 MySQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

30.4.3 MariaDB . . . . . . . . . . . . . . . . . . . . . . . . . . . 160

30.4.4 MongoDB . . . . . . . . . . . . . . . . . . . . . . . . . . . 160

31 Python Integration with Visual Studio 161

32 Python Integration with LabVIEW 162

32.1 What is LabVIEW? . . . . . . . . . . . . . . . . . . . . . . . . . 162

32.2 Using Python in LabVIEW . . . . . . . . . . . . . . . . . . . . . 162

33 Raspberry Pi and Python 167

33.1 What is Raspberry Pi? . . . . . . . . . . . . . . . . . . . . . . . . 167

34 Web Development with Python 168

34.1 Introduction to Web Development . . . . . . . . . . . . . . . . . 168

34.1.1 HTML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168

34.1.2 CSS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168

34.1.3 JavaScript . . . . . . . . . . . . . . . . . . . . . . . . . . . 168

34.2 Introduction to Web Frameworks . . . . . . . . . . . . . . . . . . 168

34.2.1 PHP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

34.2.2 ASP.NET . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

34.3 Django - Python-based Web Framework . . . . . . . . . . . . . . 169

35 Create GUI Applications 170

35.1 LabVIEW . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

35.2 Visual Studio and C# . . . . . . . . . . . . . . . . . . . . . . . . 170

35.3 Web Development . . . . . . . . . . . . . . . . . . . . . . . . . . 170

36 Machine Learning with Python 171

36.1 Introduction to Machine Learning . . . . . . . . . . . . . . . . . 171

10

VIII Python PyQt GUI Development 172

37 Getting Started with PyQt 173

37.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173

37.2 Introduction to Qt . . . . . . . . . . . . . . . . . . . . . . . . . . 173

37.3 Introduction to PyQt. . . . . . . . . . . . . . . . . . . . . . . . . 174

37.3.1 PyQtChart . . . . . . . . . . . . . . . . . . . . . . . . . . 174

37.4 Installing PyQt . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175

37.4.1 Installation of PyQt . . . . . . . . . . . . . . . . . . . . . 175

37.4.2 Installation of Qt Designer . . . . . . . . . . . . . . . . . 175

37.4.3 Installation of PyQtChart . . . . . . . . . . . . . . . . . . 175

37.5 PyQt Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

37.6 PyQt Widgets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

37.7 Event Handling in PyQt . . . . . . . . . . . . . . . . . . . . . . . 181

37.8 PyQt Designer . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184

37.9 PyQt Applications Examples . . . . . . . . . . . . . . . . . . . . 184

IX Resources 186

38 Python Resources 187

38.1 Python Distributions . . . . . . . . . . . . . . . . . . . . . . . . . 187

38.2 Python Libraries . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

38.3 Python Editors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

38.4 Python Tutorials . . . . . . . . . . . . . . . . . . . . . . . . . . . 188

38.5 Python in Visual Studio . . . . . . . . . . . . . . . . . . . . . . . 188

X Solutions to Exercises 191

11

Part I

Getting Started with

Python

12

Chapter 1

Introduction

With this textbook you will learn basic Python programming. The textbook

contains lots of examples and self-paced tasks that the users should go through

and solve in their own pace.

You will find additional resources on my blog/web site [1].

https://www.halvorsen.blog

My Web Site about Python is:

https://www.halvorsen.blog/documents/programming/python/

See Figure 1.1

1.1 The New Age of Programming

The way we create software today has changed dramatically the last 30 years,

from the childhood of personal computers in the early 80s to today’s powerful

devices such as Smartphones, Tablets and PCs.

The Internet has also changed the way we use devices and software. We still

havetraditionaldesktopapplications, butWebSites, WebApplicationsandso-

called Apps for Smartphones, etc. are dominating the software market today.

We need to find and learn Programming Languages that are suitable for the

New Age of Programming.

We have today several thousand different Programming Languages, so why

should we learn Python? I guess you will need to learn more than one Pro-

gramming Language to survive in today’s software market. Python is easy to

learn, so it it a good starting point for new programmers.

Python is an interpreted, high-level, general-purpose programming language.

Created by Guido van Rossum and first released in 1991 [2].

13

Figure 1.1: Web Site - Python

Python is a fairly old Programming Language (1991) compared to many other

ProgrammingLanguageslikeC#(2000),Swift(2014),Java(1995),PHP(1995).

Python has during the last 10 years become more and more popular. Today,

Python has become one of the most popular Programming Languages.

Therearemanydifferentrankingsregardingwhichprogramminglanguagewhich

is most popular. In most of these ranking, Python is in top 10.

One of these rankings is the IEEE Spectrum’s ranking of the top programming

languages [3].

From this ranking we see that Python is the most popular Programming Lan-

guage in 2018. See Figure 1.2

As we see in Figure 1.2 they categorize the different Programming Languages

into the following categories:

• Web

14

Figure 1.2: The Most Popular Programming Languages

• Mobile

• Enterprise

• Embedded

According to Figure 1.2 we see that Python can be used to program Web Ap-

plications, Enterprise Applications and Embedded Applications.

SofarPythonisnotusedornotoptimizedforcreatingMobileApplications. We

havetoday2majorMobileplatforms;iOSApplicationsaremainlyprogrammed

with the Swift Programming language, while Android Applications are mainly

programmed with either Java or Kotlin.

Another survey is the ”Stack Overflow Developer Survey 2018” [4]. See Figure

1.3.

Aswecanseefrom[5]andFigure1.4, Pythonbecomesmoreandmorepopular

year by year.

Based on Figure 1.4, the source [5] try to predict the future of Python, see

Figure 1.5.

Based on the surveys and statistics mention above, obviously Python is a pro-

gramming language that you should learn.

Lets summarize:

• Python is fun to learn and use and it is also named after the British

comedy group called Monty Python.

• Python has a simple and flexible code structure and the code is easy to

read.

15

Figure 1.3: The Top Programming Languages - Stack Overflow Survey

• Python is highly extendable due to its high number of free available

Python Packaged and Libraries

• Python can be used on all platforms (Windows, macOS and Linux).

• Pythonismulti-purposeandcanbeusedfortoprogramWebApplications,

Enterprise Applications and Embedded Applications, and within Data

Science and Engineering Applications.

• The popularity of Python is growing fast.

• Python is open source and free to use

• The growing Python community makes it easy to find documentation,

code examples and get help when needed

In general, Python is a multipurpose programming language that can be used

in many situations. But there is not one programming language which is best

in all kind of situations, so it is important that you know about and have skills

in different languages.

My list of recommendations (one of many):

• Visual Studio and C

• LabVIEW - a graphical programming language well suited for hardware

integration, taking measurements and data logging

• MATLAB - Numerical calculations and Scientific computing

• Python - Numerical calculations, and Scientific computing, etc.

• Web Programming, such as HTML, CSS, JavaScript and a Server-side

framework/programming language like PHP, ASP.NET (C or VB.NET),

Django (Python based)

16

Figure 1.4: The Incredible Growth of Python

• Databases (such as SQL Server and MySQL) and using the Structured

Query Language (SQL) or the upcoming NoSQL databases

• App Development for the 2 main platforms iOS (XCode using the Swift

Programming Language) and Android (Android Studio using the Java

Programming Language or Kotlin Programming language)

If you have skills in most of the tools, programming languages and frameworks

mention above, you are well suited for working as a full-time programmer or

software engineer.

1.2 MATLAB

If you are looking for MATLAB, please see the following:

https://www.halvorsen.blog/documents/programming/matlab/

17

Figure 1.5: The Future of Python

18

Chapter 2

What is Python?

2.1 Introduction to Python

Python is an open source and cross-platform programming language, that has

become increasingly popular over the last ten years. It was first released in

1991. Latest version is 3.7.0. CPython is the reference implementation of the

Pythonprogramminglanguage. WritteninC,CPythonisthedefaultandmost

widely-used implementation of the language.

Pythonisamulti-purposeprogramminglanguages(duetoitsmanyextensions),

examples are scientific computing and calculations, simulations, web develop-

ment (using, e.g., the Django Web framework), etc.

Python Home Page [6]:

https://www.python.org

The programming language is maintained and available from (Python Software

Foundation): https://www.python.orgHereyoucandownloadthebasicPython

features in one package, which includes the Python programming language in-

terpreter, and a basic code editor, or an integrated development environment,

called IDLE. See Figure 2.1

ButthisisjustthePythoncore, i.e. theinterpreteraverybasiceditor, andthe

minimum needed to create basic Python programs.

Typically you will need more features for solving your tasks. Then you can in-

stallanduseseparatePythonpackagescreatedbythirdparties. Thesepackages

need to be downloaded and installed separately (typically you use something

called PIP), or you choose to use, e.g., a distribution package like Anaconda.

Python is an object-oriented programming language (OOP), but you can use

Python in basic application without the need to know about or use the object-

oriented features in Python.

Pythonisaninterpretedprogramminglanguage,thismeansthatasadeveloper

19

Figure 2.1: IDLE - Basic Python Editor

you write Python (.py) files in a text editor and then put those files into the

python interpreter to be executed. Depending on the Editor you are using, this

is either done automatically, or you need to do it manually.

Here are some important Python sources: [6], [7], [8].

2.1.1 Interpreted vs. Compiled

WhatarethedifferencesbetweenInterpretedprogramminglanguagesandCom-

piled programming languages? What kind should you choose, and why should

you bother?

Programming languages generally fall into one of two categories: Compiled or

Interpreted. With a compiled language, code you enter is reduced to a set of

machine-specific instructions before being saved as an executable file.

Both approaches have their advantages and disadvantages.

20

With interpreted languages, the code is saved in the same format that you en-

tered. Compiled programs generally run faster than interpreted ones because

interpreted programs must be reduced to machine instructions at run-time. It

is usually easier to develop applications in an interpreted environment because

youdon’thavetorecompileyourapplicationeachtimeyouwanttotestasmall

section.

Python is an interpreted programming language, while e.g., C/C++ are trans-

latedbyrunningthesourcecodethroughacompiler, i.e., C/C++arecompiled

languages.

Interpreted languages, in contrast, must be parsed, interpreted, and executed

each time the program is run.

Another example of an interpreted programming language is PHP, which is

mainly used to create dynamic web pages and web applications.

Compiled languages are all translated by running the source code through a

compiler. Thisresultsinveryefficientcodethatcanbeexecutedanynumberof

times. The overhead for the translation is incurred just once, when the source

is compiled; thereafter, it need only be loaded and executed.

During the design of an application, you might need to decide whether to use a

compiled language or an interpreted language for the application source code.

Interpreted languages, in contrast, must be parsed, interpreted, and executed

each time the program is run

Thus, an interpreted language is generally more suited for doing ”ad hoc” cal-

culations or simulations, while compiled languages are better for permanent

applications where speed is in focus.

2.2 Python Packages

With Python you don’t get so much out of the box. Instead of having all of

its functionality built into its core, you need to install different packages for

different topics.

This approach has advantages and disadvantages. An disadvantage is that you

need to install these packages separately and then later import these modules

in your code.

This is also typical approach for open source software, because everybody can

create their own Python packages and distribute them. In that way you also

find Python packages for almost everything, from Scientific Computing to Web

Development.

21

These packages need to be downloaded and installed separately, or you choose

to use, e.g., a distribution package like Anaconda, where you typically get the

packages you need for scientific computing. With Anaconda you typically get

the same features as with MATLAB.

Lots of Python packages exists, depending on what you are going to solve.

We have Python packages for Desktop GUI Development, Database Develop-

ment, Web Development, Software Development, etc.

See an overview of Applications for Python:

https://www.python.org/about/apps/

See also the Python Package Index (PyPI) web site:

https://pypi.org

Here you can search for, download and install many hundreds Python Packages

within different topics and applications. You can also make your own Python

Packages and distribute them here.

2.2.1 Python Packages for Science and Numerical Com-

putations

SomeimportantPythonPackagesforScienceandNumericalComputationsare:

• NumPy - NumPy is the fundamental package for scientific computing

with Python [9]

• SciPy - SciPy is a free and open-source Python library used for scientific

computingandtechnicalcomputing. SciPycontainsmodulesforoptimiza-

tion,linearalgebra,integration,interpolation,specialfunctions,FFT,sig-

nalandimageprocessing,ODEsolversandothertaskscommoninscience

and engineering. [9]

• Matplotlib - Matplotlib is a Python 2D plotting library. [10]

• Pandas - Pandas Python Data Analysis Library [11]

These packages need to be downloaded and installed separately, or you choose

to use, e.g., a distribution package like Anaconda, where you typically get the

packages you need for scientific computing. With Anaconda you typically get

the same features as with MATLAB.

2.3 Anaconda

Anaconda is a distribution package, where you get Python compiler, Python

packages and the Spyder editor, all in one package.

Anaconda includes Python, the Jupyter Notebook, and other commonly used

packages for scientific computing and data science.

22

They offer a free version (Anaconda Distribution) and a paid version (Enter-

prise) Anaconda is available for Windows, macOS, and Linux

Web:

https://www.anaconda.com

Wikipedia:

https://en.wikipedia.org/wiki/Anaconda Python istribution)

( d

SpyderandthePythonpackages(NumPy,SciPy,Matplotlib,...) mentionabove

+++ are included in the Anaconda Distribution.

2.4 Python Editors

An Editor is a program where you create your code (and where you can run

and test it). Most Editors have also features for Debugging. For simple Python

programsyoucanusetheIDLEEditor, butformoreadvancedprogramsabet-

ter editor is recommended.

Examples of Python Editors:

• Python IDLE

• Visual Studio Code

• Spyder

• Visual Studio

• PyCharm

• Wing Python IDE

• Jupyter Notebook

These editors are shortly described below and in more detail later in this text-

book.

Which editor you should use depends on your background, what kind of code

editors you have used previously, your programming skills, what your are going

to develop in Python, etc.

2.4.1 Python IDLE

The programming language is maintained and available from (Python Software

Foundation): https://www.python.orgHereyoucandownloadthebasicPython

features in one package, which includes the Python programming language in-

terpreter, and a basic code editor, or an integrated development environment,

called IDLE. See Figure 2.1

Web:

https://www.python.org

23

2.4.2 Visual Studio Code

VisualStudioCodeisasourcecodeeditordevelopedbyMicrosoftforWindows,

Linux and macOS.

Web:

https://code.visualstudio.com

Resources: Getting Started with Python in Visual Studio Code

2.4.3 Spyder

Spyder is an open source cross-platform integrated development environment

(IDE) for scientific programming in the Python language.

Web:

https://www.spyder-ide.org

Wikipedia:

https://en.wikipedia.org/wiki/Spyder software)

(

Spyder is included in the Anaconda Distribution.

2.4.4 Visual Studio

Microsoft Visual Studio is an integrated development environment (IDE) from

Microsoft. It is used to develop computer programs, as well as websites, web

apps,webservicesandmobileapps. Thedeafult(main)programminglanguage

in Visual studio is C, but many other programming languages are supported.

Visual studio is available for Windows and macOS.

Visual Studio (from 2017), has integrated support for Python, it is called

”Python Support in Visual Studio”.

Web:

https://visualstudio.microsoft.com

Wikipedia:

https://en.wikipedia.org/wiki/Microsoft isual tudio

V S

2.4.5 PyCharm

PyCharm is cross-platform, with Windows, macOS and Linux versions. The

Community Edition is free to use, while the Professional Edition (paid version)

has some extra features.

24

Web:

https://www.jetbrains.com/pycharm/

2.4.6 Wing Python IDE

The Wing Python IDE family of integrated development environments (IDEs)

fromWingwarewerecreatedspecificallyforthePythonprogramminglanguage.

3 different version of Wing exists [12]:

• Wing 101 – a very simplified free version, for teaching beginning pro-

grammers

• Wing Personal–freeversionthatomitssomefeatures,forstudentsand

hobbyists

• Wing Pro – a full-featured commercial (paid) version, for professional

programmers

2.4.7 Jupyter Notebook

TheJupyterNotebookisanopen-sourcewebapplicationthatallowsyoutocre-

ate and share documents that contain live code, equations, visualizations and

text.

Web:

http://jupyter.org

Wikipedia:

https://en.wikipedia.org/wiki/Project upyter

J

2.5 Resources

Here are some useful Python resources:

• The official Python Tutorial

- https://docs.python.org/3.7/tutorial/index.html

• The official Python Documentation

- https://docs.python.org/3.7/index.html

• Python Tutorial (w3schools.com) [13]

- https://www.w3schools.com/python/

2.6 Installing Python

The Python programming language is maintained and available from (Python

Software Foundation):

25

https://www.python.org

HereyoucandownloadthebasicPythonfeaturesinonepackage,whichincludes

the Python programming language interpreter, and a basic code editor, or an

integrated development environment, called IDLE. See Figure 2.1

For basic Python programming this is good enough.

For more advanced Python Programming you typically need a better Code Ed-

itor and additional Packages.

For the basic Python examples in the beginning, the basic Python software

from:

https://www.python.org is good enough.

I suggest you start with the basic Python software in order to learn the basics,

thenyoucanupgradetoabetterEditor,installadditionPythonpackages(either

manually or or install Anaconda where ”everything” is included).

2.6.1 Python Windows 10 Store App

Python 3.7 is also available in the Microsoft Store for Windows 10.

The Microsoft Store version of Python 3.7 is a simplified installer for running

scripts and packages.

Microsoft Store version of Python 3.7 is very basic but it’s good enough to run

the simple scripts.

Python 3.7 Microsoft Store edition will receive all updates automatically when

they are released and no manual action is required from your end.

In order to install the Microsoft Store version of Python just open Microsoft

Store in Windows 10 and search for Python.

2.6.2 Installing Anaconda

TheSpyderCodeEditorandthePythonpackages(suchasNumPy,SciPy,mat-

plotlib, etc) are included in the Anaconda Distribution.

Download and install from:

https://www.anaconda.com

2.6.3 Installing Visual Studio Code

Visual Studio Code code is a simple and easy to use editor that can be used for

many different programming languages.

26

Download and install from:

https://code.visualstudio.com

Getting Started with Python in Visual Studio Code:

https://code.visualstudio.com/docs/python/python-tutorial

27

Chapter 3

Start using Python

In this chapter we will start to use Python in some simple examples.

3.1 Python IDE

The basic code editor, or an integrated development environment, called IDLE.

See Figure 3.1.

Other Python Editors will be discussed more in detail later. For now you can

usethebasicPythonIDE(IDLE)orSpyderifyouhaveinstalledtheAnaconda

distribution package.

Figure 3.1: Python Shell / Python IDLE Editor

3.2 My first Python program

We will start using Python and create some code examples.

28

Example 3.2.1. Plotting in Python

Lets open your Python Editor and type the following:

1 print(”Hello World!”)

Listing 3.1: Hello World Python Example

[End of Example]

An extremely useful command is help(), which enters a help functionality to

explore all the stuff python lets you do, right from the interpreter. Press q to

close the help window and return to the Python prompt.

YoucanusePythonindifferentways,eitherin”interactive”modeorin”Script-

ing” mode.

The python program that you have installed will by default act as something

called an interpreter. An interpreter takes text commands and runs them as

you enter them - very handy for trying things out.

YocanrunPythoninteractivelyindifferentwayseitherusingtheConsolewhich

ispartoftheoperatingsystemorthePythonIDLEandthePythonShellwhich

is part of the basic Python installation from https://www.python.org.

3.3 Python Shell

In interactive Mode you use the Python Shell as seen in Figure 3.1.

Here you type one and one command at a time after the ”>>>” sign in the

Python Shell.

1 >>> print(”Hello World!”)

3.4 Running Python from the Console

A console (or ”terminal”, or ‘command prompt’) is a textual way to interact

with your OS (Operating System).

The python program that you have installed will by default act as something

called an interpreter. An interpreter takes text commands and runs them as

you enter them - very handy for trying things out.

BelowweseehowwecanrunPythonfromtheConsolewhichispartoftheOS.

29

3.4.1 Opening the Console on macOS

The standard console on macOS is a program called Terminal. Open Terminal

bynavigatingtoApplications,thenUtilities,thendouble-clicktheTerminalpro-

gram. Youcanalsoeasilysearchforitinthesystemsearchtoolinthetopright.

The command line Terminal is a tool for interacting with your computer. A

window will open with a command line prompt message, something like this:

Last login: Tue Dec 11 08:33:51 on console

computername:˜ username

Just type python at your console, hit Enter, and you should enter Python’s

Interpreter.

1 Last login: Tue Dec 11 12:34:16 on ttys000

2 Hans−Petter−Work−MacBook−Air:˜ hansha$ python

3 Python 3.6.5 |Anaconda, Inc.| (default , Apr 26 2018, 08:42:37)

4 [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE 401/final)] on

darwin

5 Type ”help”, ”copyright”, ”credits” or ”license” for more

information.

6 >>>

The prompt >>> on the last line indicates that you are now in an interactive

Python interpeter session, also called the “Python shell”. This is different from

the normal terminal command prompt!

You can now enter some code for python to run. Try:

>>> print(”Hello World”)

Se also Figure 3.2.

Figure 3.2: Console macOS

Try other Python commands, e.g.:

1 >>> a = 5

2 >>> b = 2

3 >>> x = 5

4 >>> y = 3∗a + b

5 >>> y

30

3.4.2 Opening the Console on Windows

Window’sconsoleiscalledtheCommandPrompt,namedcmd. Aneasywayto

get to it is by using the key combination Windows+R (Windows meaning the

windows logo button), which should open a Run dialog. Then type cmd and

hit Enter or click Ok.

You can also search for it from the start menu.

It should look like:

C:\Users\myusername>

Just type python in the Command Prompt, hit Enter, and you should enter

Python’s Interpreter. See Figure 3.3.

Figure 3.3: Command Prompt Windows

If you get an error message like this:

’python’isnotrecognizedasaninternalorexternalcommand,operableprogram

or batch file.

Then you need to add Python to your path. See instructions below.

Note! This is also an option during the setup. While installing you can se-

lect ”Add Python.exe to path”. This option is by default set to ”Off”. To get

thatoptionyouneedtoselect”Customize”,notusingthe”Default”installation.

3.4.3 Add Python to Path

In the Windows menu, search for “advanced system settings” and select View

advanced system settings.

In the window that appears, click Environment Variables... near the bottom

right. See Figure 3.4.

31

Figure 3.4: Windows System Properties

In the next window, find and select the user variable named Path and click

Edit... to change its value. See Figure 3.5.

Select ”New” and add the path where ”python.exe” is located. See Figure 3.6.

The Default Location is:

C:\Users\user\AppData\Local\Programs\Python\Python37−32\

Click Save and open the Command Prompt once more and enter ”python” to

verify it works. See Figure 3.3.

32

Figure 3.5: Windows System Properties

3.5 Scripting Mode

In ”Scripting” mode you can write a Python Program with multiple Python

commands and then save it as a file (.py).

3.5.1 Run Python Scripts from the Python IDLE

From the Python Shell you select File → New File, or you can open an existing

Pytho program or Python Script by selecting File → Open...

Lets create a new Script and type in the following:

1 print(”Hello”)

2 print(”World”)

3 print(”How are you?”)

In Figure 3.7 we see how this is done. As you see we can enter many Python

commands that together makes a Python program or Python script.

FromthePythonShellyouselectRun→RunModuleorhitF5inordertorun

or execute the Python Script. See Figure 3.8.

33

Figure 3.6: Windows System Properties

The IDLE editor is very basic, for more complicated tasks you typically may

prefer to use another editor like Spyder, Visual Studio Code, etc.

3.5.2 Run Python Scripts from the Console (Terminal)

macOS

From the Console (Terminal) on macOS:

1 $ cd /Users/username/Downloads

2 $ python helloworld.py

Note! Make sure you are at your system command prompt, which will have $

or > at the end, not in Python mode (which has >>> instead)!

See also Figure 3.9.

Then it responds with:

1 Hello

2 World

3 How are you?

34

Figure 3.7: Python Script

3.5.3 Run Python Scripts from the Command Prompt in

Windows

From Command Prompt in Window:

1 > cd /

2 > cd Temp

3 > python helloworld.py

Note! Make sure you are at your system command prompt, which will have >

at the end, not in Python mode (which has >>> instead)!

See also Figure 3.10.

Then it responds with:

1 Hello

2 World

3 How are you?

3.5.4 Run Python Scripts from Spyder

IfyouhaveinstalledtheAnacondadistributionpackageyoucanusetheSpyder

editor. See 3.11.

In the Spyder editor we have the Script Editor to the left and the interactive

Python Shell or the Console window to the right. See See 3.11.

35

Figure 3.8: Running a Python Script

Figure 3.9: Running Python Scripts from Console window on macOS

Figure 3.10: Running Python Scripts from Console window on macOS

36

Figure 3.11: Running a Python Script in Spyder

37

Chapter 4

Basic Python Programming

4.1 Basic Python Program

We will start using Python and create some code examples.

We use the basic IDLE editor (or another Python Editor)

Example 4.1.1. Hello World Example

Lets open your Python Editor and type the following:

1 print(”Hello World!”)

Listing 4.1: Hello World Python Example

[End of Example]

4.1.1 Get Help

An extremely useful command is help(), which enters a help functionality to

explore all the stuff python lets you do, right from the interpreter.

Press q to close the help window and return to the Python prompt.

4.2 Variables

Variablesaredefinedwiththeassignmentoperator,“=”. Pythonisdynamically

typed,meaningthatvariablescanbeassignedwithoutdeclaringtheirtype,and

thattheirtypecanchange. Valuescancomefromconstants, fromcomputation

involving values of other variables, or from the output of a function.

38

Example 4.2.1. Creating and using Variables in Python

We use the basic IDLE (or another Python Editor) and type the following:

1 >>> x = 3

2 >>> x

3 3

Listing 4.2: Using Variables in Python

Herewedefineavariableandsetsthevalueequalto3andthenprinttheresult

to the screen.

[End of Example]

YoucanwriteonecommandbytimeintheIDLE.IfyouquitIDLEthevariables

and data are lost. Therefore, if you want to write a somewhat longer program,

you are better off using a text editor to prepare the input for the interpreter

andrunningitwiththatfileasinputinstead. Thisisknownascreatingascript.

Python scripts or programs are save as a text file with the extension .py

Example 4.2.2. Calculations in Python

We can use variables in a calculation like this:

1 x = 3

2 y = 3∗x

3 print(y)

Listing 4.3: Using and Printing Variables in Python

We can implement the formula y =ax+b like this:

1 a = 2

2 b = 5

3 x = 3

4

5 y = a∗x + b

6

7 print(y)

Listing 4.4: Calculations in Python

Asseenintheexamples, youcanusetheprint() commandinordertoshowthe

values on the screen.

[End of Example]

39

A variable can have a short name (like x and y) or a more descriptive name

(sum, amount, etc).

You don need to define the variables before you use them (like you need to to

in, e.g., C/C++/C).

Figure 4.1 show these examples using the basic IDLE editor.

Figure 4.1: Basic Python

Here are some basic rules for Python variables:

• A variable name must start with a letter or the underscore character

• A variable name cannot start with a number

• Avariablenamecanonlycontainalpha-numericcharacters(A-z,0-9)and

underscores

• Variable names are case-sensitive, e.g., amount, Amount and AMOUNT

are three different variables.

4.2.1 Numbers

There are three numeric types in Python:

• int

• float

• complex

40

Variables of numeric types are created when you assign a value to them, so in

normal coding you don’t need to bother.

Example 4.2.3. Numeric Types in Python

1 x = 1 # int

2 y = 2.8 # float

3 z = 3 + 2j # complex

Listing 4.5: Numeric Types in Python

This means you just assign values to a variable without worrying about what

kind of data type it is.

1 print(type(x))

2 print(type(y))

3 print(type(z))

Listing 4.6: Check Data Types in Python

If you use the Spyder Editor, you can see the data types that a variable has

using the Variable Explorer (Figure 4.2):

Figure 4.2: Variable Editor in Spyder

[End of Example]

4.2.2 Strings

Strings in Python are surrounded by either single quotation marks, or double

quotation marks. ’Hello’ is the same as ”Hello”.

Stringscanbeoutputtoscreenusingtheprintfunction. Forexample: print(”Hello”).

Example 4.2.4. Using Strings in Python

Below we see examples of using strings in Python:

1 a = ”Hello World!”

2

3 print(a)

4

5 print(a[1])

6 print(a[2:5])

7 print(len(a))

8 print(a.lower())

41

9 print(a.upper())

10 print(a.replace(”H”, ”J”))

11 print(a.split(” ”))

Listing 4.7: Strings in Python

Asyouseeintheexample,therearemanybuilt-infunctionsformmanipulating

strings in Python. The Example shows only a few of them.

Strings in Python are arrays of bytes, and we can use index to get a specific

character within the string as shown in the example code.

[End of Example]

4.2.3 String Input

Python allows for command line input.

That means we are able to ask the user for input.

Example 4.2.5. String Input in Python

The following example asks for the user’s name, then, by using the input()

method, the program prints the name to the screen:

1 print(”Enter your name:”)

2 x = input()

3 print(”Hello , ” + x)

Listing 4.8: String Input

[End of Example]

4.3 Built-in Functions

Python consists of lots of built-in functions. Some examples are the print func-

tionthatwealreadyhaveused(perhapswithoutnoticingitisactuallyaBuilt-in

function).

Python also consists of different Modules, Libraries or Packages. These Mod-

ules, Libraries or Packages consists of lots of predefined functions for different

topics or areas, such as mathematics, plotting, handling database systems, etc.

See Section 4.4 for more information and details regarding this.

In another chapter we will learn to create our own functions from scratch.

42

4.4 Python Standard Library

Python allows you to split your program into modules that can be reused in

other Python programs. It comes with a large collection of standard modules

that you can use as the basis of your programs.

ThePython Standard Library consistsofdifferentmodulesforhandlingfile

I/O,basicmathematics,etc. Youdon’tneedtoinstalltheseseparately,butyou

need to important them when you want to use some of these modules or some

of the functions within these modules.

The math module has all the basic math functions you need, such as: Trigono-

metric functions: sin(x), cos(x), etc. Logarithmic functions: log(), log10(), etc.

Constants like pi, e, inf, nan, etc.

Example 4.4.1. Using the math module

We create some basic examples how to use a Library, a Package or a Module:

If we need only the sin() function, we can do like this:

1 from math import sin

2

3 x = 3.14

4 y = sin(x)

5

6 print(y)

If we need a few functions, we can do like this:

1 from math import sin , cos

2

3 x = 3.14

4 y = sin(x)

5 print(y)

6

7 y = cos(x)

8 print(y)

If we need many functions, we can do like this:

1 from math import ∗

2

3 x = 3.14

4 y = sin(x)

5 print(y)

6

7 y = cos(x)

8 print(y)

We can also use this alternative:

1 import math

2

3 x = 3.14

4 y = math.sin(x)

5

6 print(y)

43

We can also write it like this:

1 import math as mt

2

3 x = 3.14

4 y = mt.sin(x)

5

6 print(y)

[End of Example]

There are advantages and disadvantages with the different approaches. In your

program you may need to use functions from many different modules or pack-

ages. If you import the whole module instead of just the function(s) you need

you use more of the computer memory.

Very often we also need to import and use multiple libraries where the different

libraries have some functions with the same name but different use.

OtherusefulmodulesinthePython Standard Libraryarestatistics(where

you have functions like mean(), stdev(), etc.)

For more information about the functions in the Python Standard Library,

see:

https://docs.python.org/3/library/index.html

4.5 Using Python Libraries, Packages and Mod-

ules

Rather than having all of its functionality built into its core, Python was de-

signedtobehighlyextensible. Thisapproachhasadvantagesanddisadvantages.

A disadvantage is that you need to install these packages separately and then

later import these modules in your code.

Some important packages are:

• NumPy - NumPy is the fundamental package for scientific computing

with Python

• SciPy - SciPy is a free and open-source Python library used for scientific

computingandtechnicalcomputing. SciPycontainsmodulesforoptimiza-

tion,linearalgebra,integration,interpolation,specialfunctions,FFT,sig-

nalandimageprocessing,ODEsolversandothertaskscommoninscience

and engineering.

• Matplotlib - Matplotlib is a Python 2D plotting library

44

Lots of other packages exists, depending on what you are going to solve.

These packages need to be downloaded and installed separately, or you choose

to use, e.g., a distribution package like Anaconda.

Here you find an overview of the NumPy library:

https://www.numpy.org

Here you find an overview of the SciPy library:

https://www.scipy.org

Here you find an overview of the Matplotlib library:

https://matplotlib.org

You will learn the basics features in all these libraries. We will use all of the in

different examples and exercises throughout this textbook.

Example 4.5.1. Using libraries

In this example we use the NumPy library:

1 import numpy as np

2

3 x = 3

4

5 y = np.sin(x)

6

7 print(y)

In this example we use both the math module in the Python Standard Library

and the NumPy library:

1 import math as mt

2 import numpy as np

3

4 x = 3

5

6 y = mt.sin(x)

7

8 print(y)

9

10

11 y = np.sin(x)

12

13 print(y)

Note! As seen in this example we use a function called sin() which exists both

in the math module in the Python Standard Library and the NumPy library.

In this case they give the same results. In this case the following code is not

recommended:

1 from math import ∗

2 from numpy import ∗

3

4 x = 3

5

45

6 y = sin(x)

7

8 print(y)

9

10

11 y = sin(x)

12

13 print(y)

In this case it works, but assume you have 2 different functions with the same

name that have different meaning in 2 different libraries.

[End of Example]

4.5.1 Python Packages

InadditiontothePythonStandardLibrary,thereisagrowingcollectionofsev-

eral thousand components (from individual programs and modules to packages

and entire application development frameworks), available from the Python

Package Index.

Python Package Index (PYPI):

https://pypi.org

Here you can download and install individual Python packages.

AneasyalternativeistheAnacondaDistribution,wheremanyofthemostused

Python packages are included.

Anaconda:

https://www.anaconda.com/distribution/

4.6 Plotting in Python

Typically you need to create some plots or charts. In order to make plots or

charts in Python you will need an external library. The most used library is

Matplotlib.

Matplotlib is a Python 2D plotting library

Here you find an overview of the Matplotlib library:

https://matplotlib.org

If you are familiar with MATLAB and basic plotting in MATLAB, using the

Matplotlib is very similar.

The main difference from MATLAB is that you need to import the library,

either the whole library or one or more functions.

For simplicity we import the whole library like this:

1 import matplotlib.pyplot as plt

46

Plotting functions that you will use a lot:

• plot()

• title()

• xlabel()

• ylabel()

• axis()

• grid()

• subplot()

• legend()

• show()

Lets create some basic plotting examples using the Matplotlib library:

Example 4.6.1. Plotting in Python

In this example we have two arrays with data. We want to plot x vs. y. We

canassume xisatimeseries andyisthecorrespondingtemperatureindegrees

Celsius.

1 import matplotlib.pyplot as plt

2

3 x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

4

5 y = [5, 2,4, 4, 8, 7, 4, 8, 10, 9]

6

7 plt.plot(x,y)

8 plt.xlabel(’Time (s)’)

9 plt.ylabel(’Temperature (degC)’)

10 plt.show()

We get the plot as shown in Figure 4.3.

We can also write like this:

1 from matplotlib.pyplot import ∗

2

3 x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

4 y = [5, 2,4, 4, 8, 7, 4, 8, 10, 9]

5

6 plot(x,y)

7 xlabel(’Time (s)’)

8 ylabel(’Temperature (degC)’)

9 show()

This makes the code simpler to read. one problem with this approach appears

assuming we import and use multiple libraries and the different libraries have

some functions with the same name but different use.

47

Figure 4.3: Plotting in Python

[End of Example]

We have used 4 basic plotting function in the Matplotlib library:

• plot()

• xlabel()

• ylabel()

• show()

Example 4.6.2. Plotting a Sine Curve

1 import numpy as np

2 import matplotlib.pyplot as plt

3

4 x = [0, 1, 2, 3, 4, 5, 6, 7]

5

6 y = np.sin(x)

7

8 plt.plot(x, y)

9 plt.xlabel(’x’)

10 plt.ylabel(’y’)

11 plt.show()

This gives the following plot (see Figure 4.4):

A better solution will then be:

48

Figure 4.4: Plotting a Sine function in Python

1 import matplotlib.pyplot as plt

2 import numpy as np

3

4 xstart = 0

5 xstop = 2∗np.pi

6 increment = 0.1

7

8 x = np.arange(xstart ,xstop,increment)

9

10 y = np.sin(x)

11

12 plt.plot(x, y)

13 plt.xlabel(’x’)

14 plt.ylabel(’y’)

15 plt.show()

This gives the following plot (see Figure 4.5):

If you want grids you can use the grid() function.

[End of Example]

4.6.1 Subplots

Thesubplotcommandenablesyoutodisplaymultipleplotsinthesamewindow.

Typing ”subplot(m,n,p)” partitions the figure window into an m-by-n matrix

of small subplots and selects the subplot for the current plot. The plots are

numbered along the first row of the figure window, then the second row, and so

on. See Figure 4.6.

Example 4.6.3. Creating Subplots

49

Figure 4.5: Plotting a Sine function in Python - Better Implementation

We will create and plot sin() and cos() in 2 different subplots.

1 import matplotlib.pyplot as plt

2 import numpy as np

3

4 xstart = 0

5 xstop = 2∗np.pi

6 increment = 0.1

7

8 x = np.arange(xstart ,xstop,increment)

9

10 y = np.sin(x)

11

12 z = np.cos(x)

13

14

15 plt.subplot(2,1,1)

16 plt.plot(x, y, ’g’)

17 plt. title(’sin ’)

18 plt.xlabel(’x’)

19 plt.ylabel(’sin(x)’)

20 plt.grid()

21 plt.show()

22

23

24 plt.subplot(2,1,2)

25 plt.plot(x, z, ’r’)

26 plt. title(’cos’)

27 plt.xlabel(’x’)

28 plt.ylabel(’cos(x)’)

29 plt.grid()

30 plt.show()

[End of Example]

50

Figure 4.6: Creating Subplots in Python

4.6.2 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 4.6.1. Create sin(x) and cos(x) in 2 different plots

Create sin(x) and cos(x) in 2 different plots.

You should use all the Plotting functions listed below in your code:

• plot()

• title()

• xlabel()

• ylabel()

• axis()

• grid()

• legend()

• show()

[End of Exercise]

51

Part II

Python Programming

52

Chapter 5

Python Programming

WehavebeenthroughthebasicsinPython, suchasvariables, usingsomebasic

built-in functions, basic plotting, etc.

You may come far only using these thins, but to create real applications, you

need to know about and use features like:

• If ... Else

• For Loops

• While Loops

• Arrays ...

If you are familiar with one or more other programming language, these fea-

tures should be familiar and known to you. All programming languages have

these features built-in, but the syntax is slightly different from one language to

another.

5.1 If ... Else

An ”if statement” is written by using the if keyword.

Here are some Examples how you use a If sentences in Python:

Example 5.1.1. Using If ... Else in Python

Using If:

1 a = 5

2 b = 8

3

4 if a > b:

5 print(”a is greater than b”)

6

7 if b > a:

8 print(”b is greater than a”)

9

10 if a == b:

53

11 print(”a is equal to b”)

Listing 5.1: If

Try to change the values for a and b.

Using If - Else:

1 a = 5

2 b = 8

3

4 if a > b:

5 print(”a is greater than b”)

6 else:

7 print(”b is greater than a or a and b are equal”)

Listing 5.2: If - Else

Using Elif:

1 a = 5

2 b = 8

3

4 if a > b:

5 print(”a is greater than b”)

6 elif b > a:

7 print(”b is greater than a”)

8 elif a == b:

9 print(”a is equal to b”)

Listing 5.3: Elif

Note! Python uses ”elif” not ”elseif” like many other programming languages

do.

[End of Example]

5.2 Arrays

An array is a special variable, which can hold more than one value at a time.

Here are some Examples how you can create and use Arrays in Python:

Example 5.2.1. Arrays in Python

1 data = [1.6, 3.4, 5.5, 9.4]

2

3 N = len(data)

4

5 print(N)

6

7 print(data[2])

8

9 data[2] = 7.3

10

11 print(data[2])

54

12

13

14 for x in data:

15 print(x)

16

17

18 data.append(11.4)

19

20

21 N = len(data)

22

23 print(N)

24

25

26 for x in data:

27 print(x)

Listing 5.4: Using Arrays in Python

You define an array like this:

1 data = [1.6, 3.4, 5.5, 9.4]

You can also use text like this:

1 carlist = [”Volvo”, ”Tesla”, ”Ford”]

You can use Arrays in Loops like this:

1 for x in data:

2 print(x)

You can return the number of elements in the array like this:

1 N = len(data)

You can get a specific value inside the array like this:

1 index = 2

2 x = cars[index]

You can use the append() method to add an element to an array:

1 data.append(11.4)

[End of Example]

You have many built in methods you can use in combination with arrays, like

sort(), clear(), copy(), count(), insert(), remove(), etc.

You should look into test all these methods.

55

5.3 For Loops

A For loop is used for iterating over a sequence. I guess all your programs will

use one or more For loops. So if you have not used For loops before, make sure

to learn it now.

Below you see a basic example how you can use a For loop in Python:

1 for i in range(1, 10):

2 print(i)

The For loop is probably one of the most useful feature in Python (or in any

kind of programming language). Below you will see different examples how you

can use a For loop in Python.

Example 5.3.1. Using For Loops in Python

1 data = [1.6, 3.4, 5.5, 9.4]

2

3 for x in data:

4 print(x)

5

6

7 carlist = [”Volvo”, ”Tesla”, ”Ford”]

8

9 for car in carlist:

10 print(car)

Listing 5.5: Using For Loops in Python

The range() function is handy to use in For Loops:

1 N = 10

2

3 for x in range(N):

4 print(x)

Therange()functionreturnsasequenceofnumbers,startingfrom0bydefault,

and increments by 1 (by default), and ends at a specified number.

You can also use the range() function like this:

1 start = 4

2 stop= 12 #but not including

3

4 for x in range(start , stop):

5 print(x)

Finally, you can also use the range() function like this:

1 start = 4

2 stop = 12 #but not including

3 step = 2

4

5 for x in range(start , stop, step):

6 print(x)

56

You should try all these examples in order to learn the basic structure of a For

loop.

[End of Example]

Example 5.3.2. Using For Loops for Summation of Data

You typically want to use a For loop for find the sum of a given data set.

1 data = [1, 5, 6, 3, 12, 3]

2

3 sum = 0

4

5 #Find the Sum of all the numbers

6 for x in data:

7 sum = sum + x

8

9 print(sum)

10

11 #Find the Mean or Average of all the numbers

12

13 N = len(data)

14

15 mean = sum/N

16

17 print(mean)

This gives the following results:

1 30

2 5.0

[End of Example]

Example5.3.3. ImplementingFibonacciNumbersUsingaForLoopinPython

Fibonacci numbers are used in the analysis of financial markets, in strategies

suchasFibonacciretracement,andareusedincomputeralgorithmssuchasthe

Fibonacci search technique and the Fibonacci heap data structure.

Theyalsoappearinbiologicalsettings, suchasbranchingintrees, arrangement

of leaves on a stem, the fruitlets of a pineapple, the flowering of artichoke, an

uncurling fern and the arrangement of a pine cone.

In mathematics, Fibonacci numbers are the numbers in the following sequence:

0, 1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Bydefinition,thefirsttwoFibonaccinumbersare0and1,andeachsubsequent

number is the sum of the previous two.

Some sources omit the initial 0, instead beginning the sequence with two 1s.

57

Inmathematicalterms,thesequenceFnofFibonaccinumbersisdefinedbythe

recurrence relation

f =f +f (5.1)

n n−1 n−2

with seed values:

f =0,f =1

0 1

We will write a Python script that calculates the N first Fibonacci numbers.

The Python Script becomes like this:

1 N = 10

2

3 fib1 = 0

4 fib2 = 1

5

6 print(fib1)

7 print(fib2)

8

9 for k in range(N−2):

10 fib next = fib2 +fib1

11 fib1 = fib2

12 fib2 = fib next

13 print(fib next)

Listing 5.6: Fibonacci Numbers Using a For Loop in Python

Alternative solution:

1 N = 10

2

3 fib = [0, 1]

4

5

6 for k in range(N−2):

7 fib next = fib[k+1] +fib[k]

8 fib.append(fib next)

9

10 print(fib)

Listing 5.7: Fibonacci Numbers Using a For Loop in Python - Alt2

Another alternative solution:

1 N = 10

2

3 fib = []

4

5 for k in range(N):

6 fib.append(0)

7

8 fib[0] = 0

9 fib[1] = 1

10

58

11 for k in range(N−2):

12 fib[k+2] = fib[k+1] +fib[k]

13

14

15 print(fib)

Listing 5.8: Fibonacci Numbers Using a For Loop in Python - Alt3

Another alternative solution:

1 import numpy as np

2

3

4 N = 10

5

6 fib = np.zeros(N)

7

8 fib[0] = 0

9 fib[1] = 1

10

11 for k in range(N−2):

12 fib[k+2] = fib[k+1] +fib[k]

13

14

15 print(fib)

Listing 5.9: Fibonacci Numbers Using a For Loop in Python - Alt4

[End of Example]

5.3.1 Nested For Loops

In Python and other programming languages you can use one loop inside an-

other loop.

Syntax for nested For loops in Python:

1 for iterating var in sequence:

2 for iterating var in sequence:

3 statements(s)

4 statements(s)

Simple example:

1 for i in range(1, 10):

2 for k in range(1, 10):

3 print(i , k)

Exercise 5.3.1. Prime Numbers

The first 25 prime numbers (all the prime numbers less than 100) are:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,

89, 97

59

By definition a prime number has both 1 and itself as a divisor. If it has any

other divisor, it cannot be prime.

Anaturalnumber(1, 2, 3, 4, 5, 6, etc.) iscalledaprimenumber(oraprime)if

it is greater than 1 and cannot be written as a product of two natural numbers

that are both smaller than it.

Create a Python Script where you find all prime numbers between 1 and 200.

Tip! I guess this can be done in many different ways, but one way is to use 2

nested For Loops.

[End of Exercise]

5.4 While Loops

The while loop repeats a group of statements an indefinite number of times

under control of a logical condition.

Example 5.4.1. Using While Loops in Python

1 m = 8

2

3 while m > 2:

4 print (m)

5 m = m − 1

Listing 5.10: Using While Loops in Python

[End of Example]

5.5 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 5.5.1. Plot of Dynamic System

Given the autonomous system:

x˙ =ax (5.2)

Where:

1

a=−

T

60

where T is the time constant.

The solution for the differential equation is:

x(t)=eatx (5.3)

0

Set T=5 and the initial condition x(0)=1.

Create a Script inPython (.py file) where you plot the solution x(t) in the time

interval:

0≤t≤25

Add Grid, and proper Title and Axis Labels to the plot.

[End of Exercise]

61

Chapter 6

Creating Functions in

Python

6.1 Introduction

A function is a block of code which only runs when it is called. You can pass

data, known as parameters, into a function. A function can return data as a

result.

Previously we have been using many of the built-in functions in Python

If you are familiar with one or more other programming language, creating and

using functions should be familiar and known to you. All programming lan-

guageshasthepossibilitytocreatefunctions,butthesyntaxisslightlydifferent

from one language to another.

Some programming languages uses the term Method instead of a Function.

Functions and Methods behave in the same manner, but you could say that

MethodsarefunctionsthatbelongstoaClass. WewilllearnmoreaboutClasses

in Chapter 7.

Scripts vs. Functions

It is important to know the difference between a Script and a Function.

Scripts:

• A collection of commands that you would execute in the Editor

• Used for automating repetitive tasks

Functions:

• Operate on information (inputs) fed into them and return outputs

• Have a separate workspace and internal variables that is only valid inside

the function

62

• Your own user-defined functions work the same way as the built-in func-

tions you use all the time, such as plot(), rand(), mean(), std(), etc.

Pythonhavelotsofbuilt-infunctions,butveryoftenweneedtocreateourown

functions (we could refer to these functions as user-defined functions)

In Python a function is defined using the def keyword:

1 def FunctionName:

2 <statement−1>

3 .

4 .

5 <statement−N>

6 return ...

Example 6.1.1. Basic Function

Below you see a simple function created in Python:

1 def add(x,y):

2

3 return x + y

Listing 6.1: Basic Python Function

The function adds 2 numbers. The name of the function is add, and it returns

the answer using the return statement.

The statement return [expression] exits a function, optionally passing back an

expression to the caller. A return statement with no arguments is the same as

return None.

Note that you need to use a colon ”:” at the end of line where you define the

function.

Note also the indention used.

1 def add(x,y):

Here you see a Python script where we use the function:

1 def add(x,y):

2

3 return x + y

4

5

6 x = 2

7 y = 5

8

9 z = add(x,y)

10

11 print(z)

Listing 6.2: Creating and Using a Python Function

63

[End of Example]

Example 6.1.2. Create a Function in a separate File

WestartbycreatingaseparatePythonFile(myfunctions.py)forthefunction:

1 def average(x,y):

2

3 return (x + y)/2

Listing 6.3: Function calculating the Average

Next, we create a new Python File (e.g., testaverage.py) where we use the

function we created:

1 from myfunctions import average

2

3 a = 2

4 b = 3

5

6 c = average(a,b)

7

8 print(c)

Listing 6.4: Test of Average function

[End of Example]

6.2 Functions with multiple return values

Typically we want to return more than one value from a function.

Example 6.2.1. Create a Function Function with multiple return values

Create the following example:

1 def stat(x):

2

3 totalsum = 0

4

5 #Find the Sum of all the numbers

6 for x in data:

7 totalsum = totalsum + x

8

9

10 #Find the Mean or Average of all the numbers

11

12 N = len(data)

13

14 mean = totalsum/N

15

16

17 return totalsum, mean

18

19

20

64

21 data = [1, 5, 6, 3, 12, 3]

22

23

24 totalsum, mean = stat(data)

25

26 print(totalsum, mean)

Listing 6.5: Function with multiple return values

[End of Example]

6.3 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 6.3.1. Create Python Function

Create a function calcaverage that finds the average of two numbers.

[End of Exercise]

Exercise 6.3.2. Create Python functions for converting between radians and

degrees

Since most of the trigonometric functions require that the angle is expressed in

radians, we will create our own functions in order to convert between radians

and degrees.

It is quite easy to convert from radians to degrees or from degrees to radians.

We have that:

2π[radians]=360[degrees] (6.1)

This gives:

180

d[degrees]=r[radians]×( ) (6.2)

π

and

π

r[radians]=d[degrees]×( ) (6.3)

180

Create two functions that convert from radians to degrees (r2d(x)) and from

degrees to radians (d2r(x)) respectively.

These functions should be saved in one Python file .py.

Test the functions to make sure that they work as expected.

65

[End of Exercise]

Exercise 6.3.3. Create a Function that Implementing Fibonacci Numbers

Fibonacci numbers are used in the analysis of financial markets, in strategies

suchasFibonacciretracement,andareusedincomputeralgorithmssuchasthe

Fibonacci search technique and the Fibonacci heap data structure.

Theyalsoappearinbiologicalsettings, suchasbranchingintrees, arrangement

of leaves on a stem, the fruitlets of a pineapple, the flowering of artichoke, an

uncurling fern and the arrangement of a pine cone.

In mathematics, Fibonacci numbers are the numbers in the following sequence:

0, 1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Bydefinition,thefirsttwoFibonaccinumbersare0and1,andeachsubsequent

number is the sum of the previous two.

Some sources omit the initial 0, instead beginning the sequence with two 1s.

Inmathematicalterms,thesequenceFnofFibonaccinumbersisdefinedbythe

recurrence relation

f =f +f (6.4)

n n−1 n−2

with seed values:

f =0,f =1

0 1

Create a Function that Implementing the N first Fibonacci Numbers

[End of Exercise]

Exercise 6.3.4. Prime Numbers

The first 25 prime numbers (all the prime numbers less than 100) are:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,

89, 97

By definition a prime number has both 1 and itself as a divisor. If it has any

other divisor, it cannot be prime.

Anaturalnumber(1, 2, 3, 4, 5, 6, etc.) iscalledaprimenumber(oraprime)if

it is greater than 1 and cannot be written as a product of two natural numbers

that are both smaller than it.

Tip! I guess this can be implemented in many different ways, but one way is to

use 2 nested For Loops.

66

CreateaPythonfunctionwhereyoucheckifagivennumberisaprimenumber

or not.

You can check the function in the Command Window like this:

1 number = 4

2 checkifprime(number)

Then Python respond with True or False.

[End of Exercise]

67

Chapter 7

Creating Classes in Python

7.1 Introduction

Pythonisanobjectorientedprogramming(OOP)language. Almosteverything

in Python is an object, with its properties and methods.

Thefoundationforallobjectorientedprogramming(OOP)languagesareClasses.

To create a class, use the keyword class:

1 class ClassName:

2 <statement−1>

3 .

4 .

5 .

6 <statement−N>

Example 7.1.1. Simple Class Example

We will create a simple Class in Python.

1 class Car:

2 model = ”Volvo”

3 color = ”Blue”

4

5

6 car = Car()

7

8

9 print(car.model)

10 print(car.color)

Listing 7.1: Simple Python Class

The results will be in this case:

1 Volvo

2 Blue

68

Thisexampledon’tillustratethegoodthingswithclassessowewillcreatesome

more examples.

[End of Example]

Example 7.1.2. Python Class

Lets create the following Python Code:

1 class Car:

2 model = ””

3 color = ””

4

5 car = Car()

6

7 car.model = ”Volvo”

8 car.color = ”Blue”

9

10 print(car.color + ” ” + car.model)

11

12 car.model = ”Ford”

13 car.color = ”Green”

14

15 print(car.color + ” ” + car.model)

Listing 7.2: Python Class example

You should try these examples.

[End of Example]

7.2 The init () Function

In Python all classes have a built-in function called init (), which is always

executed when the class is being initiated.

In many other OOP languages we call this the Constructor.

Exercise 7.2.1. The init () Function

Wewillcreateasimpleexamplewhereweusethe init ()functiontoillustrate

the principle.

We change our previous Car example like this:

1 class Car:

2 def init (self , model, color):

3 self .model = model

4 self .color = color

5

6 car1 = Car(”Ford”, ”Green”)

7

8 print(car1.model)

9 print(car1.color)

10

11

69

12 car2 = Car(”Volvo”, ”Blue”)

13

14 print(car2.model)

15 print(car2.color)

Listing 7.3: Python Class Constructor Example

Lets extend the Class by defining a Function as well:

1 # Defining the Class Car

2 class Car:

3 def init (self , model, color):

4 self .model = model

5 self .color = color

6

7 def displayCar(self):

8 print(self .model)

9 print(self .color)

10

11

12 # Lets start using the Class

13

14 car1 = Car(”Tesla”, ”Red”)

15

16 car1.displayCar()

17

18

19 car2 = Car(”Ford”, ”Green”)

20

21 print(car2.model)

22 print(car2.color)

23

24

25 car3 = Car(”Volvo”, ”Blue”)

26

27 print(car3.model)

28 print(car3.color)

29

30 car3.color=”Black”

31

32 car3.displayCar()

Listing 7.4: Python Class with Function

As you see from the code we have now defined a Class ”Car” that has 2 Class

variables called ”model” and ”color”, and in addition we have defined a Func-

tion (or Method) called ”displayCar()”.

Its normal to use the term ”Method” for Functions that are defined within a

Class.

You declare class methods like normal functions with the exception that the

first argument to each method is self.

To create instances of a class, you call the class using class name and pass in

whatever arguments its init () method accepts.

For example:

70

1 car1 = Car(”Tesla”, ”Red”)

[End of Example]

Exercise 7.2.2. Create the Class in a separate Python file

We start by creating the Class and then we save the code in ”Car.py”:

1 # Defining the Class Car

2 class Car:

3 def init (self , model, color):

4 self .model = model

5 self .color = color

6

7 def displayCar(self):

8 print(self .model)

9 print(self .color)

Listing 7.5: Define Python Class in separate File

Then we create a Python Script (testCar.py) where we are using the Class:

1 # Importing the Car Class

2 from Car import Car

3

4 # Lets start using the Class

5

6 car1 = Car(”Tesla”, ”Red”)

7

8 car1.displayCar()

9

10

11 car2 = Car(”Ford”, ”Green”)

12

13 print(car2.model)

14 print(car2.color)

15

16

17 car3 = Car(”Volvo”, ”Blue”)

18

19 print(car3.model)

20 print(car3.color)

21

22 car3.color=”Black”

23

24 car3.displayCar()

Listing 7.6: Script that is using the Class

Notice the following line at the top:

1 from Car import Car

[language=Python]

[End of Example]

71

7.3 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 7.3.1. Create Python Class

Create a Python Class where you calculate the degrees in Fahrenheit based on

the temperature in Celsius and vice versa.

The formula for converting from Celsius to Fahrenheit is:

T =(T ×9/5)+32 (7.1)

f c

The formula for converting from Fahrenheit to Celsius is:

T =(T −32)×(5/9) (7.2)

c f

[End of Exercise]

72

Chapter 8

Creating Python Modules

Asyourprogramgetslonger,youmaywanttosplititintoseveralfilesforeasier

maintenance. Youmayalsowanttouseahandyfunctionthatyouhavewritten

in several programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them

in a script or in an interactive instance of the interpreter (the Python Console

window).

8.1 Python Modules

A module is a file containing Python definitions and statements. The file name

is the module name with the suffix .py appended.

Python allows you to split your program into modules that can be reused in

other Python programs. It comes with a large collection of standard modules

that you can use as the basis of your programs as we have seen examples of in

previous chapters. Not it is time to make your own modules from scratch.

Consider a module to be the same as a code library. A file containing a set of

functions you want to include in your application.

Previously you have been using different modules, libraries or packages created

bythePythonorganizationorbyothers. Hereyouwillcreateyourownmodules

from scratch.

Example 8.1.1. Create your first Python Module

We will create a Python module with 2 functions. The first function should

convert from Celsius to Fahrenheit and the other function should convert from

Fahrenheit to Celsius.

The formula for converting from Celsius to Fahrenheit is:

T =(T ×9/5)+32 (8.1)

f c

73

The formula for converting from Fahrenheit to Celsius is:

T =(T −32)×(5/9) (8.2)

c f

First,wecreateaPythonmodulewiththefollowingfunctions(fahrenheit.py):

1 def c2f(Tc):

2

3 Tf = (Tc ∗ 9/5) + 32

4 return Tf

5

6

7 def f2c(Tf):

8

9 Tc = (Tf − 32)∗(5/9)

10 return Tc

Listing 8.1: Fahrenheit Functions

Then,wecreateaPythonscriptfortestingthefunctions(testfahrenheit.py):

1 from fahrenheit import c2f , f2c

2

3 Tc = 0

4

5 Tf = c2f(Tc)

6

7 print(”Fahrenheit: ” + str(Tf))

8

9

10 Tf = 32

11

12 Tc = f2c(Tf)

13

14 print(”Celsius: ” + str(Tc))

Listing 8.2: Python Script testing the functions

The results becomes:

1 Fahrenheit: 32.0

2 Celsius: 0.0

8.2 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 8.2.1. Create Python Module for converting between radians and

degrees

Since most of the trigonometric functions require that the angle is expressed in

radians, we will create our own functions in order to convert between radians

74

and degrees.

It is quite easy to convert from radians to degrees or from degrees to radians.

We have that:

2π[radians]=360[degrees] (8.3)

This gives:

180

d[degrees]=r[radians]×( ) (8.4)

π

and

π

r[radians]=d[degrees]×( ) (8.5)

180

Create two functions that convert from radians to degrees (r2d(x)) and from

degrees to radians (d2r(x)) respectively.

These functions should be saved in one Python file .py.

Test the functions to make sure that they work as expected. You can choose to

make a new .py file to test these functions or you can use the Console window.

[End of Exercise]

75

Chapter 9

File Handling in Python

9.1 Introduction

Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.

The open() function takes two parameters; Filename, and Mode.

There are four different methods (modes) for opening a file:

• ”x” - Create - Creates the specified file, returns an error if the file exists

• ”w” - Write - Opens a file for writing, creates the file if it does not exist

• ”r” - Read - Default value. Opens a file for reading, error if the file does

not exist

• ”a” - Append - Opens a file for appending, creates the file if it does not

exist

In addition you can specify if the file should be handled as binary or text mode

• ”t” - Text - Default value. Text mode

• ”b” - Binary - Binary mode (e.g. images)

9.2 Write Data to a File

TocreateaNewfileinPython,usetheopen()method,withoneofthefollowing

parameters:

• ”x” - Create - Creates the specified file, returns an error if the file exists

• ”w” - Write - Opens a file for writing, creates the file if it does not exist

• ”a” - Append - Opens a file for appending, creates the file if it does not

exist

76

To write to an Existing file, you must add a parameter to the open() function:

• ”w” - Write - Opens a file for writing, creates the file if it does not exist

• ”a” - Append - Opens a file for appending, creates the file if it does not

exist

Example 9.2.1. Write Data to a File

1 f = open(”myfile.txt”, ”x”)

2

3 data = ”Helo World”

4

5 f.write(data)

6

7 f.close()

Listing 9.1: Write Data to a File

[End of Example]

9.3 Read Data from a File

To read to an existing file, you must add the following parameter to the open()

function:

• ”r” - Read - Default value. Opens a file for reading, error if the file does

not exist

Example 9.3.1. Read Data from a File

1 f = open(”myfile.txt”, ”r”)

2

3 data = f.read()

4

5 print(data)

6

7 f.close()

Listing 9.2: Read Data from a File

[End of Example]

9.4 Logging Data to File

Typically you want to write multiple data to the, e.g., assume you read some

temperaturedataatregularintervalsandthenyouwanttosavethetemperature

values to a File.

Example 9.4.1. Logging Data to File

77

1 data = [1.6, 3.4, 5.5, 9.4]

2

3 f = open(”myfile.txt”, ”x”)

4

5 for value in data:

6 record = str(value)

7 f.write(record)

8 f.write(”\n”)

9

10 f.close()

Listing 9.3: Logging Data to File

[End of Example]

Example 9.4.2. Read Logged Data from File

1 f = open(”myfile.txt”, ”r”)

2

3 for record in f:

4 record = record.replace(”\n”, ””)

5 print(record)

6

7 f.close()

Listing 9.4: Read Logged Data from File

[End of Example]

9.5 Web Resources

Below you find different useful resources for File Handling.

Python File Handling - w3school:

https://www.w3schools.com/python/python ile andling.asp

f h

Reading and Writing Files - python.org:

https://docs.python.org/3/tutorial/inputoutput.htmlreading-and-writing-files

9.6 Exercises

Below you find different self-paced Exercises that you should go through and

solve on your own. The only way to learn Python is to do lots of Exercises!

Exercise 9.6.1. Data Logging

AssumeyouhavethefollowingdatayouwanttologtoaFileasshowninTable

9.1.

Log these data to a File.

Create another Python Script that reads the same data.

78

[End of Exercise]

Exercise 9.6.2. Data Logging 2

AssumeyoureaddatafromaTemperaturesensorevery10secondsforaperiod

of let say 5 minutes.

Log the data to a File.

You can use the Random Generator in Python. An example of how to use the

Random Generator is shown below:

1 import random

2 for x in range(10):

3 data = random.randint(1,31)

4 print(data)

Listing 9.5: Read Data from a File

Make sure to log both the time and the temperature value

Create another Python Script that reads the same data.

You should also plot the data you read from the File.

[End of Exercise]

79

Table 9.1: Logged Data

Time Value

1 22

2 25

3 28

... ...

80

Chapter 10

Error Handling in Python

10.1 Introduction to Error Handling

So far error messages haven’t been discussed. You could say that we have 2

kinds of errors: syntax errors and exceptions.

10.1.1 Syntax Errors

Below we see an example of syntax errors:

1 >>> print(Hello World)

2 File ”<ipython−input−1−10cb182148e3>”, line 1

3 print(Hello World)

4 ˆ

5 SyntaxError: invalid syntax

In the example we have written print(Hello World) instead of print(”Hello

World”) and then the Python Interpreter gives us an error message.

10.1.2 Exceptions

Even if a statement or expression is syntactically correct, it may cause an error

when an attempt is made to execute it. Errors detected during execution are

called exceptions and are not unconditionally fatal: you will soon learn how to

handletheminPythonprograms. Mostexceptionsarenothandledbyprograms,

however, and result in error messages as shown here:

1 >>> 10 ∗ (1/0)

2 Traceback (most recent call last):

3

4 File ”<ipython−input−2−0b280f36835c>”, line 1, in <module>

5 10 ∗ (1/0)

6

7 ZeroDivisionError: division by zero

or:

1 >>> ’2’ + 2

2 Traceback (most recent call last):

3

81

4 File ”<ipython−input−3−d2b23a1db757>”, line 1, in <module>

5 ’2’ + 2

6

7 TypeError: must be str , not int

10.2 Exceptions Handling

It is possible to write programs that handle selected exceptions.

In Python we can use the following built-in Exceptions Handling features:

• The try block lets you test a block of code for errors.

• The except block lets you handle the error.

• Thefinallyblockletsyouexecutecode,regardlessoftheresultofthetry-

and except blocks.

Whenanerroroccurs,orexceptionaswecallit,Pythonwillnormallystopand

generate an error message.

These exceptions can be handled using the try - except statements.

Some basic example:

1 try:

2 10 ∗ (1/0)

3 except:

4 print(”The calculation failed”)

or:

1 try:

2 print(x)

3 except:

4 print(”x is not defined”)

You can also use multiple exceptions:

1 try:

2 print(x)

3 except NameError:

4 print(”x is not defined”)

5 except:

6 print(”Something is wrong”)

The finally block, if specified, will be executed regardless if the try block raises

an error or not.

Example:

82

1 x=2

2

3 try:

4 print(x)

5 except NameError:

6 print(”x is not defined”)

7 except:

8 print(”Something is wrong”)

9 finally:

10 print(”The Program is finished”)

Ingeneralyoushouldusetry-except-finallywhenyoutrytoopenaFile,read

or write to Files, connect to a Database, etc.

Example:

1 try:

2 f = open(”myfile.txt”)

3 f.write(”Lorum Ipsum”)

4 except:

5 print(”Something went wrong when writing to the file”)

6 finally:

7 f.close()

83

Chapter 11

Debugging in Python

Debugging is the process of finding and resolving defects or problems within

a computer program that prevent correct operation of computer software or a

system [14].

Debuggers are software tools which enable the programmer to monitor the ex-

ecution of a program, stop it, restart it, set breakpoints, and change values in

memory. The term debugger can also refer to the person who is doing the de-

bugging.

As a programmer, one of the first things that you need for serious program

development is a debugger.

Python has a built-in debugger that can be used if you are coding Python with

a basic text editor and running your Python programs from the command line.

A better option is to use the Debugging features integrated in your Python Ed-

itor. Debugging is typically integrated with the Python Editor you are using.

See the specific chapter for the different Python Editors.

84

Chapter 12

Installing and using Python

Packages

A package contains all the files you need for a module. Modules are Python

code libraries you can include in your project.

Since Python is open source you can find thousands of Python Packages that

you can install and use in your Python programs.

You can use a Python Distribution like Anaconda Distribution (or similar

Python Distributions) to download and install many common Python Pack-

ages as mentioned previously.

12.1 What is PIP?

PIP is a package manager for Python packages, or modules if you like. PIP is

a tool for installing Python packages.

IfyoudonothavePIPinstalled,youcandownloadandinstallitfromthispage:

https://pypi.org/project/pip/

PIP is typically used from the Command Prompt (Windows) or Terminal win-

dow (macOS).

Installing Python Packages:

1 pip install packagename

Uninstalling Python Packages:

1 pip uninstall packagename

Some Python Editors also have a graphical way of installing Python Packages,

like, e.g., Visual Studio.

85

Part III

Python Environments and

Distributions

86

Chapter 13

Introduction to Python

Environments and

Distributions

Python comes with many flavours and version.

Python is open source and everybody can bundle and distribute Python and

different Python Packages.

A Python environment is a context in which you run Python code and includes

Python Packages.

Anenvironmentconsistsofaninterpreter,alibrary(typicallythePythonStan-

dard Library), and a set of installed packages.

These components together determine which language constructs and syntax

are valid, what operating-system functionality you can access, and which pack-

ages you can use.

You can have multiple Python Environments on your Computer.

Some of them are:

• CPython distribution available from python.org

• Anaconda

• Enthought Canopy

• WinPython

• etc.

It is easy to start using Python by installing one of these Python Distributions.

87

But you can also install the core Python from:

https://www.python.org

Then install the additional Python Packages you need by using PIP.

https://pypi.org/project/pip/

13.1 Package and Environment Managers

The two most popular tools for installing Python Packages and setting up

Python environments are:

• PIP - a Python Package Manager

• Conda - a Package and Environment Manager (for Python and other lan-

guages)

13.1.1 PIP

Web:

https://pypi.org

PIP is typically used from the Command Prompt (Windows) or Terminal win-

dow (macOS).

Installing Python Packages:

1 pip install packagename

Uninstalling Python Packages:

1 pip uninstall packagename

13.1.2 Conda

Conda is an open source package management system and environment man-

agementsystemthatrunsonWindows,macOSandLinux. Condainstalls,runs

and updates packages and their dependencies.

TheCondapackageandenvironmentmanagerisincludedinallversionsofAna-

conda.

CondawascreatedforPythonprograms,butitcanpackageanddistributesoft-

ware for any language.

Condaallowsyoutotoalsocreateseparateenvironmentscontainingfiles,pack-

ages and their dependencies that will not interact with other environments.

88

Web:

https://conda.io/

Conda is part of or integrated with the Anaconda Python Distribution.

Web:

https://www.anaconda.com

13.2 Python Virtual Environments

Python ”Virtual Environments” allow Python packages to be installed in an

isolated location for a particular application, rather than being installed glob-

ally.

You can have multiple Python Environments on your computer.

Python Virtual Environments have their own installation directories and they

don’t share libraries with other virtual environments.

Python”VirtualEnvironments”ishandywhenyouhavedifferentPythonappli-

cationsthatneedsdifferentversionsofPythonordifferentversionofthePython

Packages you are using.

89

Chapter 14

Anaconda

Anaconda is not an Editor, but a Python Distribution package. Spyder is in-

cludedinthePythonDistributionpackage. YoucanalsouseAnacondatoinstall

other Editors or Python packages.

It is available for Windows, macOS and Linux.

Web:

https://www.anaconda.com

Wikipedia:

https://en.wikipedia.org/wiki/Anaconda Python istribution)

( d

14.1 Anaconda Navigator

Anaconda Navigator is a desktop graphical user interface (GUI) included in

Anaconda distribution that allows users to launch applications and manage

Python packages. The Anaconda Navigator can search for packages and install

them on your computer, run the packages and update them.

Figure 14.1 shows the Anaconda Navigator.

14.2 Anaconda Prompt

YoucanusetheAnacondaPromptifyouneedtoinstallextraPythonpackages,

etc.

Let say you want to install the Python Control Systems Library package. Just

enter the following in the Anaconda Prompt:

pip install control

90

Figure 14.1: Anaconda Navigator

Python Package Index, or just pip, is a tool used to handle and install Python

packages.

For for information about pip and different packages you can install, see the

following:

https://pypi.org

Figure14.2showswhereyoucanfindtheAnacondaPrompt. Windows: Search

for Anaconda Prompt in the Search field in the start menu.

91

Figure 14.2: Anaconda Navigator

92

Chapter 15

Enthought Canopy

Enthought Canopy is a Python Platform or Python Distribution for Scientists

and Engineers.

It is available for Windows, macOS and Linux.

Canopy is freely available to all users under the Canopy license. Canopy pro-

vides access to several hundreds Python packages, including NumPy, SciPy,

Pandas, Matplotlib, and IPython.

In addition, we have the Canopy Python Editor.

Enthought Canopy is a competitor to the Anaconda Python Distribution. It is

a matter of taste who you prefer.

Web:

https://www.enthought.com/product/canopy/

93

Part IV

Python Editors

94

Chapter 16

Python Editors

An Editor is a program where you create your code (and where you can run

and test it). Most Editors have also features for Debugging and IntelliSense.

In theory, you can use Windows Notepad for creating Python programs, but

in practice it is impossible to create programs without having an editor with

Debugging, IntelliSense, color formatting, etc.

For simple Python programs you can use the IDLE Editor, but for more ad-

vanced programs a better editor is recommended.

Examples of Python Editors:

• Spyder

• Visual Studio Code

• Visual Studio

• PyCharm

• Wing

• JupyterNotebook

We will give an overview of these Code Editors in the next chapters.

I guess hundreds of different editors can be used for Python Programming, ei-

ther out of the box or if you install an additional Extension that makes sure

you can use Python in that editor.

IfyoualreadyhaveafavoriteCodeEditor, itisagoodchangeyoucanusethat

one for Python programming.

Which editor you should use depends on your background, what kind of code

editors you have used previously, your programming skills, what your are going

to develop in Python, etc.

95

If you are familiar with MATLAB, Spyder is recommended. Also, if you want

to use Python for numerical calculations and computations, Spyder is a good

choice.

If you want to create Web Applications or other kinds of Applications, other

Editors are probably better to use.

For a list of ”Best Python Editors”, see [15].

96

Chapter 17

Spyder

Spyder - short for ”Scientific PYthon Development EnviRonment”.

Spyderisanopensourcecross-platformintegrateddevelopmentenvironment(IDE)

for scientific programming in the Python language.

Figure 17.1: Spyder Editor

The Spyder editor consists of the following parts or windows:

• Code Editor window

• iPython Console window

97

• Variable Explorer

• etc.

Web:

https://www.spyder-ide.org

If you have used MATLAB previously or want to use Python for scientific use,

Spyder is a good choice. it is easy to install using the Anaconda Distribution.

Web:

https://www.anaconda.com

17.1 Configuration

Typically you want to show figures and plots in separate windows.

Select Tools-Preferences as shown in Figure 17.2.

Figure 17.2: Python Tools-Preferences

Then select ”Automatic” as shown in Figure 17.3.

98

Figure 17.3: Python Preferences window

99

Chapter 18

Visual Studio Code

18.1 Introduction to Visual Studio Code

VisualStudioCodeisasimpleandeasytouseeditorthatcanbeusedformany

different programming languages.

Figure 18.1: Using Visual Studio Code as Python Editor

Right-Click and select ”Run Python File in Terminal”

Web:

https://code.visualstudio.com

Wikipedia:

https://en.wikipedia.org/wiki/Visual tudio ode

S C

100

18.2 Python in Visual Studio Code

In addition to Visual Studio Code you need to install the Python extension for

Visual Studio Code.

You must install a Python interpreter yourself separately from the extension.

For a quick install, use Python from python.org.

https://www.python.org

Python is an interpreted language, and in order to run Python code and get

Python IntelliSense within Visual Studio Code, you must tell Visual Studio

Code which interpreter to use.

Web:

https://code.visualstudio.com/docs/languages/python

101

Chapter 19

Visual Studio

19.1 Introduction to Visual Studio

Microsoft Visual Studio is an integrated development environment (IDE) from

Microsoft. It is used to develop computer programs, as well as websites, web

apps,webservicesandmobileapps. Thedefault(main)programminglanguage

in Visual studio is C, but many other programming languages are supported.

You could say Visual Studio is the big brother of Visual Studio Code.

Visual studio is available for Windows and macOS.

Visual Studio (from 2017), has integrated support for Python, it is called

”Python Support in Visual Studio”.

Web:

https://visualstudio.microsoft.com

Wikipedia:

https://en.wikipedia.org/wiki/Microsoft isual tudio

V S

Go to my Web Site to learn more about Visual Studio and C programming:

https://www.halvorsen.blog/

Visual Studio and C:

https://www.halvorsen.blog/documents/programming/csharp/

19.2 Work with Python in Visual Studio

Work with Python in Visual Studio:

https://docs.microsoft.com/visualstudio/python/

102

Figure 19.1: Using Visual Studio as Python Editor

19.2.1 Make Visual Studio ready for Python Program-

ming

Visual Studio is mainly for Windows. A MacOS version of Visual Studio do

exists, but it has lot less features than the Windows edition.

Note that Python support is available only on Visual Studio for Windows. If

you use Mac and Linux, you need to use Visual Studio Code. You could say

Visual Studio Code is a down-scaled version of Visual Studio.

Visual Studio (from 2017), has integrated support for Python, it is called

”Python Support in Visual Studio”. Even if it is integrated, you need to manu-

ally select which components you want to install on your computer. Make sure

to download and run the latest Visual Studio 2017 installer for Windows.

when you run the Visual Studio installer (either for the first time or if you

already have installed Visual Studio 2017 and want to modify it) the window

shown in Figure 19.2 pops up.

Theinstallerpresentsyouwithalistofsocalledworkloads,whicharegroupsof

related options for specific development areas. For Python, select the ”Python

development” workload and select Install (Figure 19.3).

19.2.2 Python Interactive

To quickly test Python support, launch Visual Studio, press Alt+I (or select

from the menu: Tools - Python - Python Interactive Window) to open the

Python Interactive window. See Figure 19.4.

Lets write something like this:

1 >>> a = 2

103

Figure 19.2: Installing Python Extension for Visual Studio

Figure 19.3: Python Development Workload

2 >>> b = 5

3 >>> x = 3

4 >>> y = a∗x + b

5 >>> y

19.2.3 New Python Project

Lets see how we can create a Python Application.

Startbyselectfromthemenu: File-New-Project... TheNewProjectwindow

pops up. See Figure 19.5.

We can create an ordinary Python Application (one or more Python Scripts),

we can choose to create a Web Application using either Web Frameworks like

Django or Flask, or we can create different Desktop GUI applications. We can

also create Games.

Example 19.2.1. Python Hello World Application in Visual Studio

104

Figure 19.4: Python Interactive

We start by creating a basic Hello World Python Application. See Figure 19.1.

SelectFile-New-Project... TheNewProjectwindowpopsup. SeeFigure19.5.

Name the project, e.g, ”PythonApplication1”.

In the Project Explorer, open the ”PythonApplication1.py” file and enter the

following Python code:

1 print(”Hello World”)

HitF5(ourclickthegreenarrow)inordertorunorexecutethePythonprogram.

You can also right click on the file and select ”Start without Debugging”.

[End of Example]

Example 19.2.2. Visual Studio Python Plotting

CreateanewPythonFilebyrightclickintheSolutionExplorerandselectAdd

- New Item... and then select ”Empty Python File”.

Enter the following Python Code:

1 import matplotlib.pyplot as plt

2 import numpy as np

3

4 xstart = 0

5 xstop = 2∗np.pi

6 increment = 0.1

7

8 x = np.arange(xstart ,xstop,increment)

9

10 y = np.sin(x)

11

12 plt.plot(x, y)

13 plt. title(’y=sin(x)’)

105

Figure 19.5: New Python Project

14 plt.xlabel(’x’)

15 plt.ylabel(’y’)

16 plt.grid()

17 plt.axis([0, 2∗np.pi, −1, 1])

18 plt.show()

See also Figure 19.6.

Make sure to select proper Python Environment. See Figure (19.7). Visual

Studio supports multiple Python Environments.

In this example we use the Matplotlib package for plotting, so we need to have

that package installed on the computer. You can install the Matplotlib package

in different Python Environments.

I have installed the Matplotlib package as part of the Anaconda distribution

setup, so I select ”Anaconda x.x.x” in the Python Environments window.

If you haven’t installed the Matplotlib package yet (either as part of Anaconda

ormanuallyusingPIP),youcanalsoeasilyinstallPythonpackagesfromVisual

studio. See Figure 19.8.

You can also easily see which Python Packages that are installed for the differ-

ent Python Environments. See Figure 19.9.

106

Figure 19.6: Python Plotting Example with Visual Studio

The good thing about using Visual Studio is that you have a graphical user

interface for everything, you don’t need to use the Command window etc. for

installing Python Packages, etc.

HitF5(ourclickthegreenarrow)inordertorunorexecutethePythonprogram.

You can also right click on the file and select ”Start without Debugging”.

We get the following results, see Figure 19.10.

[End of Example]

107

Figure 19.7: Select your Python Environment

Figure 19.8: Install Python Packages from Visual Studio

108

Figure19.9: InstallingPythonPackagesfordifferentPythonEnvironmentsfrom

Visual Studio

Figure 19.10: Python Plotting Example with Visual Studio

109

Chapter 20

PyCharm

PyCharm is cross-platform, with Windows, macOS and Linux versions. The

Community Edition is free to use, while the Professional Edition (paid version)

has some extra features.

The PyCharm Editor is shown in Figure 20.1.

Figure 20.1: PyCharm Python Editor

Web:

https://www.jetbrains.com/pycharm/

Wikipedia:

https://en.wikipedia.org/wiki/PyCharm

Anaconda and JetBrains also have a collaboration and offer what they call Py-

Charm for Anaconda. You can download it here:

110

https://www.jetbrains.com/pycharm/promo/anaconda/

We have code editors like Visual Studio and Visual Studio Code which can be

used for many different programming languages by installing different types of

plugins.

Editors like Spyder and PyCharm are tailor-made editors for the Python lan-

guage.

Spyder is light-weight IDE typically used for scientific use. PyCharm on the

other hand is full-blown IDE for software development in general by using the

Python language. It supports many plugins, it’s easier to program Django, etc.

111

Chapter 21

Wing Python IDE

The Wing Python IDE family of integrated development environments (IDEs)

fromWingwarewerecreatedspecificallyforthePythonprogramminglanguage.

3 different version of Wing exists [12]:

• Wing 101 – a very simplified free version, for teaching beginning pro-

grammers

• Wing Personal–freeversionthatomitssomefeatures,forstudentsand

hobbyists

• Wing Pro – a full-featured commercial (paid) version, for professional

programmers

Figure 21.1: Wing Python IDE

Web:

https://wingware.com

112

Wikipedia:

https://en.wikipedia.org/wiki/Wing DE

I

113

Chapter 22

Jupyter Notebook

TheJupyterNotebookisanopen-sourcewebapplicationthatallowsyoutocre-

ate and share documents that contain live code, equations, visualizations and

text.

TheNotebookhassupportforover40programminglanguages,includingPython.

Figure 22.1: Jupyter Notebook [16]

Web:

http://jupyter.org

Wikipedia:

https://en.wikipedia.org/wiki/Project upyter

J

114

22.1 JupyterHub

JupyterHub is a multi-user version of the notebook designed for companies,

classrooms and research labs [17].

JupyterHub runs in the cloud or on your own hardware.

JupyterHubisopen-sourceanddesignedtoberunonavarietyofinfrastructure.

This includes commercial cloud providers, virtual machines, or even your own

laptop hardware.

Web:

http://jupyter.org/hub

22.2 Microsoft Azure Notebooks

Microsoft Azure Notebooks is a version of Jupyter Notebook from Microsoft.

The good thing about Microsoft Azure Notebooks is that you have the infras-

tructure and everything up and running ready for you to use. You can use it

for free as well.

Web:

https://notebooks.azure.com

Example 22.2.1. Example Name

Figure 22.2 shows an overview of my Azure Notebook Projects.

Figure 22.2: Azure Notebook Projects

Figure 22.3 shows an overview of my Azure Notebook Project Notebooks.

Figure 22.4 shows an example of a simple Notebook.

[End of Example]

115

Figure 22.3: Azure Notebook Project Notebooks

Figure 22.4: Azure Notebook Example

116

Part V

Data Acquisition (DAQ)

with Python

117

Chapter 23

Plotting Sensor Data

23.1 Introduction

Typically we want to plot the data from the sensor. We can plot save the data

in an array and then plot the data at the end of the program, but more likely

we want to plot one value at the time inside the loop, so-called ”Real-Time

plotting”.

In this chapter we only show how you can plot the data from any given sensor

using this general approach. Instead of the actual sensor data we just use the

random generator in Python.

To read the actual sensor data you typically need a DAQ (Data Acquisition)

device connected to you PC or, e.g, a Raspberry Pi device. In all cases you

will typically need to install a driver from the vendor of the DAQ device or the

sensor you are using.

23.2 Introduction to Real-Time Plotting

You can also use the matplotlib for real-time plotting.

Example 23.2.1. Introduction to Real-Time Plotting

Here is a basic example:

1 import numpy as np

2 import matplotlib.pyplot as plt

3

4 plt.axis([0, 10, 0, 1])

5

6 delay = 1 #Seconds

7

8 for i in range(10):

9 y = np.random.random()

10 plt.scatter(i , y)

11 plt.pause(delay)

118

12

13 plt.show()

Listing 23.1: Real-Time Plotting in Python

We get the following plot as shown in Figure 23.1.

Figure 23.1: Real-Time Plotting with Python

You cannot see the the actual behavior of the plot by watching Figure 23.1, so

you need to run the Python program yourself.

If you run the code you see the plot is updated with a new value every second

as specified in the code.

[End of Example]

Note! If you use Anaconda and Spyder, you typically need to change the the

settings for how graphics are are displayed in Spyder.

Select Preferences from the menu, then IPython console in the list of categories

ontheleft,thenthetabGraphicsatthetop,andchangetheGraphicsback-end

from Inline to e.g. Automatic or Qt. See Figure 23.2.

119

Figure 23.2: Change how Graphics are displayed in the Spyder Editor

23.3 Real-Time Plotting with Animation

FormoreadvancedReal-Timeplotsweshouldusetheanimationmoduleinthe

matplotlib library (matplotlib.animation).

To create a real-time plot, we need to use the animation module in matplotlib.

We set up the figure and axes in the usual way, but we draw directly to the

axes, ax, when we want to create a new frame in the animation.

We need to use the FuncAnimation function:

1 ani = animation.FuncAnimation(fig , animate, fargs=(xs, ys),

interval=1000)

FuncAnimation is a special function within the animation module that lets us

automate updating the graph. We pass the FuncAnimation() a handle to the

figure we want to draw, fig, as well as the name of a function that should be

calledatregularintervals. Wecalledthisfunctionanimate()andisdefinedjust

above our FuncAnimation() call.

StillintheFuncAnimation()parameters, wesetfargs, whicharethearguments

we want to pass to our animate function (since we are not calling animate()

directly from within our own code). Then, we set interval, which is how long

we should wait between calls to animate() (in milliseconds).

Note: As an argument to FuncAnimation, notice that animate does not have

any parentheses. This is passing a reference to the function and not the result

of that function. If you accidentally add parentheses to animate here, animate

will be called immediately (only once), and you’ll likely get an error

120

Example 23.3.1. Real-Time Plotting with Animation

Below you find the Python Code for a basic example where we use the anima-

tion module in matplotlib.

Intheexampleweupdatetheploteverysecondsbysettingtheinterval=1000ms

as an input argument to the FuncAnaimation function.

1 import datetime as dt

2 import numpy as np

3 import matplotlib.pyplot as plt

4 import matplotlib.animation as animation

5

6 # Create figure for plotting

7 fig = plt.figure()

8 ax = fig.add subplot(1, 1, 1)

9 xs = []

10 ys = []

11

12

13 # This function is called periodically from FuncAnimation

14 def animate(i , xs, ys):

15

16 temp c = round(np.random.random() , 2)

17

18 # Add x and y to lists

19 xs.append(dt.datetime.now().strftime(’%H:%M:%S.%f ’))

20 ys.append(temp c)

21

22 # Limit x and y lists to 20 items

23 xs = xs[−20:]

24 ys = ys[−20:]

25

26 # Draw x and y lists

27 ax.clear()

28 ax.plot(xs, ys)

29

30 # Format plot

31 plt.xticks(rotation=45, ha=’right ’)

32 plt.subplots adjust(bottom=0.30)

33 plt. title(’Temperature Data’)

34 plt.ylabel(’Temperature (deg C)’)

35

36 # Set up plot to call animate() function periodically

37 ani = animation.FuncAnimation(fig , animate, fargs=(xs, ys),

interval=1000)

38 plt.show()

Listing 23.2: Real-Time Plotting with Animation

Figure23.3showsthefinalplotforthisexample. Youcannotseethetheactual

behavior of the plot by watching Figure 23.3, so you need to run the Python

program yourself.

[End of Example]

121

Figure 23.3: Real-Time Plotting with Animation

23.3.1 Speeding Up the Plot Animation

Clearing a graph and redrawing everything can be a time-consuming process in

terms of computer time. To remedy that, we are going to use a trick known as

blitting.

Blitting is an old computer graphics technique where several graphical bitmaps

are combined into one. This way, only one needed to be updated at a time,

saving the computer from having to redraw the whole scene every time.

MatplotliballowsustoenableblittinginFuncAnimation,butitmeansweneed

tore-writehowsomeoftheanimate()functionworks. Toreapthetruebenefits

ofblitting,weneedtosetastaticbackground,whichmeanstheaxescan’tscale

and we can’t show moving timestamps anymore. This means that you have to

take the good with the bad. So you have to choose whats most important for

you un your simulations.

Example 23.3.2. Real-Time Plotting with Animation with improved Perfor-

mance

Python Code:

1 import numpy as np

2 import matplotlib.pyplot as plt

3 import matplotlib.animation as animation

4

5 # Parameters

6 x len = 200 # Number of points to display

7 y range = [0, 20] # Range of possible Y values to display

8

122

9 # Create figure for plotting

10 fig = plt.figure()

11 ax = fig.add subplot(1, 1, 1)

12 xs = list(range(0, 200))

13 ys = [0] ∗ x len

14 ax.set ylim(y range)

15

16

17 # Create a blank line. We will update the line in animate

18 line , = ax.plot(xs, ys)

19

20 # Add labels

21 plt. title(’Temperature Data’)

22 plt.xlabel(’Samples’)

23 plt.ylabel(’Temperature (deg C)’)

24

25 # This function is called periodically from FuncAnimation

26 def animate(i , ys):

27

28 rand val = np.random.random()∗20 #Generate Random Values

between 0 and 20

29

30 temp c = round(rand val , 2)

31

32 #print (temp c)

33

34 # Add y to list

35 ys.append(temp c)

36

37 # Limit y list to set number of items

38 ys = ys[−x len:]

39

40 # Update line with new Y values

41 line.set ydata(ys)

42

43 return line ,

44

45 # Set up plot to call animate() function periodically

46 ani = animation.FuncAnimation(fig ,

47 animate,

48 fargs=(ys,) ,

49 interval=100,

50 blit=True)

51 plt.show()

Listing 23.3: Real-Time Plotting with Animation

Figure23.4showsthefinalplotforthisexample. Youcannotseethetheactual

behavior of the plot by watching Figure 23.4, so you need to run the Python

program yourself.

[End of Example]

For more information about Matplotlib:animations:

https://scipy-cookbook.readthedocs.io/items/Matplotlib nimations.html

A

123

Figure 23.4: Real-Time Plotting with Animation

Other resources:

https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/allplot-

sensor-data

https://stackoverflow.com/questions/11874767/how-do-i-plot-in-real-time-in-a-while-

loop-using-matplotlib

124

Chapter 24

Data Acquisition (DAQ)

with Python

Python is probably best suited for ”ad-hoc” numerical calculations, analysis,

simulations, etc., but can be used for many other purposes, even if other pro-

gramming languages are better suited.

24.1 Introduction to DAQ

To read sensor data you typically need a DAQ (Data Acquisition) device con-

nected to you PC or, e.g, a Raspberry Pi device. In all cases you will typically

need to install a driver from the vendor of the DAQ device or the sensor you

are using.

A DAQ System consists of 4 parts:

• Physical input/output signals, sensors

• DAQ device/hardware

• Driver software

• Yoursoftwareapplication(Applicationsoftware)-inthiscaseyourPython

application

Figure 24.1 shows the different steps involved in a DAQ system.

Hereyoufindmoreinformation,resources,videosandexamplesregardingDAQ:

https://www.halvorsen.blog/documents/technology/daq/

24.2 Data Acquisition using NI DAQ Devices

Here we will show how we can use Python to retrieve data from the physical

world using a DAQ device or an I/O module.

125

Figure 24.1: Data Acquisition (DAQ) System

We will use a DAQ device from National Instruments (NI).

Web:

http://www.ni.com/

DAQhardware: WEwilluseaNI-USB-600xDAQdevicefromNationalInstru-

ments, such as:

• NI-USB-6001

• NI-USB-6008

• NI-USB-6009

They are almost identical and the prices is not so bad either.

USB-6008:

http://www.ni.com/en-no/support/model.usb-6008.html

Figure 24.2 shows the USB-6008 DAQ device from NI.

Streaming Data from NI Data Acquisition (DAQmx) Devices into Python:

https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P8o0SAC

We assume we want to do the following: - We have a USB DAQ system from

NationalInstruments-WewanttostreamdatafrommyhardwareintoPython

to do data processing - We would like to log data to a file on the hard disk

The best way to do this is to use the NI-DAQmx Python API provided by Na-

tional Instruments (nidaqmx). The NI-DAQmx Python API is hosted on

GitHub.

The nidaqmx Python package is a wrapper around the NI-DAQmx C API us-

ingthectypesPythonlibrary,andonlysupportstheWindowsoperatingsystem.

A Python API for interacting with NI-DAQmx (GitHub):

https://github.com/ni/nidaqmx-python

126

Figure 24.2: USB-6008

For more information about NI DAQ:

ni.com/daq

For more information about Python Resources for NI Hardware and Software:

ni.com/python

Another option is to use the PyDAQmx Python package.

This package allows users to use data acquisition hardware from National In-

strument with python. It makes an interface between the NIDAQmx driver

and python. It currently works only on Windows. The package is not an open

source driver from NI acquisition hardware. You first need to install the driver

provided by NI.

Web:

https://pypi.org/project/PyDAQmx/

https://pythonhosted.org/PyDAQmx/

24.2.1 NI-DAQmx

NI-DAQmx is the software you use to communicate with and control your NI

data acquisition (DAQ) device.

NI-DAQmx supports only the Windows operating system.

You can download NI-DAQmx from this location:

https://www.ni.com/download

127

24.2.2 Measurement Automation Explorer (MAX)

Measurement Automation Explorer (MAX) is a software you can use it to

configure and test the DAQ device before you use it in Python (or other pro-

gramming languages).

MAX is included with NI-DAQmx software.

Figure 24.3 shows Measurement Automation Explorer (MAX).

Figure 24.3: Measurement Automation Explorer(MAX)

With MAX you can make sure your DAQ device works as expected before you

startusingitinyourPythonprogram. YoucanusetheTestPanelstotestyour

analog and digital inputs and outputs channels.

You can also change name of the unit, which you need to use in your Python

code.

24.3 NI-DAQmx Python API

In this section we will use the NI-DAQmx Python API provided by National

Instruments(nidaqmx). TheNI-DAQmx Python API ishostedonGitHub.

The nidaqmx Python package is a wrapper around the NI-DAQmx C API us-

ingthectypesPythonlibrary,andonlysupportstheWindowsoperatingsystem.

128

A Python API for interacting with NI-DAQmx (GitHub):

https://github.com/ni/nidaqmx-python

Other resources:

Control NI DAQ Device with Python and NI DAQmx:

https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z0000019Pf1SAE

Below 4 basic examples will be provided:

• Analog Write using NI DAQ Device

• Analog Read using NI DAQ Device

• Digital Write using NI DAQ Device

• Digital Read using NI DAQ Device

You can easily extend this examples to make them suit your needs. Typically

you need to include a while loop where you write and/or read from the DAQ

device inside the loop, e.g. read values from one or more sensors that are con-

nected to the DAQ device, you may want to create a control system reading

the process value and then later write the calculated control signal (e.g. using

a PID controller) back to the DAQ device and the process.

24.3.1 Analog Write

Example 24.3.1. Analog Write using NI DAQ Device

Python code:

1 import nidaqmx

2

3 with nidaqmx.Task() as task:

4 task.ao channels.add ao voltage chan(’Dev1/ao0’,’mychannel’

,0,5)

5

6 value = 3

7 task.start

8 task.write(value)

9 task.stop

Listing 24.1: Analog Write using NI DAQ Device

Note! The USB-6008 can only output a voltage signal between 0 and 5V.

[End of Example]

24.3.2 Analog Read

Example 24.3.2. Analog Read using NI DAQ Device

Python code:

129

1 import nidaqmx

2

3 with nidaqmx.Task() as task:

4 task.ai channels.add ai voltage chan(”Dev1/ai1”)

5

6 value = task.read()

7 print(value)

8 task.stop

Listing 24.2: Analog Read using NI DAQ Device

[End of Example]

Example 24.3.3. Analog Read with RSE

Python code:

1 import nidaqmx

2

3 from nidaqmx.constants import (

4 TerminalConfiguration)

5

6 with nidaqmx.Task() as task:

7 task.ai channels.add ai voltage chan(”Dev1/ai0”,

terminal config=TerminalConfiguration.RSE)

8

9 value = task.read()

10 print(value)

11 task.stop

Listing 24.3: Analog Read with RSE

[End of Example]

Example 24.3.4. Analog Read with Differential

Python code:

1 import nidaqmx

2

3 from nidaqmx.constants import (

4 TerminalConfiguration)

5

6 with nidaqmx.Task() as task:

7 task.ai channels.add ai voltage chan(”Dev1/ai0”,

terminal config=TerminalConfiguration.DIFFERENTIAL)

8

9 value = task.read()

10 print(value)

11 task.stop

Listing 24.4: Analog Read with Differential

[End of Example]

130

24.3.3 Digital Write

Example 24.3.5. Digital Write using NI DAQ Device

Python code:

1 import nidaqmx

2

3 with nidaqmx.Task() as task:

4 task.do channels.add do chan(”Dev1/port0/line0”)

5

6 value = True

7 task.start

8 task.write(value)

9 task.stop

Listing 24.5: Digital Write using NI DAQ Device

[End of Example]

24.3.4 Digital Read

Example 24.3.6. Digital Read using NI DAQ Device

Python code:

1 import nidaqmx

2

3 with nidaqmx.Task() as task:

4 task.di channels.add di chan(”Dev1/port0/line0”)

5

6 task.start

7 value = task.read()

8 print(value)

9 task.stop

Listing 24.6: Digital Read using NI DAQ Device

[End of Example]

Youshouldusethe”nidaqmx.stream readers”andnidaqmx.stream writersclasses

to increase the performance of your application, which accept pre-allocated

NumPy arrays.

https://nidaqmx-python.readthedocs.io/en/latest/stream readers.html#module-

nidaqmx.stream readers

https://nidaqmx-python.readthedocs.io/en/latest/stream writers.html#module-

nidaqmx.stream writers

131

24.4 Controlling LEDs

In this section we will see how we can control a LED from Python.

We will need the following equipment:

• PC with Python

• DAQ device

• Breadboard

• LED

• Resistor (e.g., 270ohm)

• Wires for connecting the components and create the circuit

Figure 24.4 shows an overview of LEDs.

Figure 24.4: LED Overview

A breadboard is used to wire electric components together. Figure 24.5 shows

how you should wire a LED using a Breadboard.

Figure 24.6 shows how you wire the LED and connect it to the DAQ device.

Python code for turning on the LED

Example 24.4.1. Controlling a LED from Python

Basic Python code:

1 import nidaqmx

2

3 with nidaqmx.Task() as task:

4 task.do channels.add do chan(”Dev1/port0/line0”)

5

6 value = True

7 task.start

8 task.write(value)

9 task.stop

Listing 24.7: Turn on a LED using Python

132

Figure 24.5: How to wire a LED on a Breadboard

Figure 24.6: Wire the LED and connect to the DAQ device

In this basic example we just turn on the LED.

Below you see an example where we turn the LED on and off inside a loop.

Python code:

1 import nidaqmx

2 import time

3

4

5 with nidaqmx.Task() as task:

6 task.do channels.add do chan(”Dev1/port0/line0”)

7

8 value = True

9 task.start

10

11 i = 1

12 while i < 10:

13

133

14 task.write(value)

15 time.sleep(1)

16 value = not value

17 task.write(value)

18 i = i+1

19

20 task.stop

Listing 24.8: Controlling a LED using Python

[End of Example]

24.5 Read Data from Temperature Sensors

In this section we will use Python to read values from a temperature sensor.

We will also use Python to plot real-time data from the sensor.

24.5.1 Read Data from TMP36 Temperature Sensor

TMP36isasmall, low-costtemperaturesensorandcostabout$1(youcanbuy

it “everywhere”).

We will need the following equipment:

• PC with Python

• DAQ device

• Breadboard

• TMP36 Temerature Sensor

• Wires for connecting the components and create the circuit

Figure 24.7 shows the TMP36 sensor.

We connect the TMP36 to LabVIEW using a USB DAQ Device from National

Instruments, e.g., USB-6001, USB-6008 or similar. I have used a breadboard

for the wiring.

Figure24.8showhowwecanwiretheTMP36togetherwiththeUSB-6008DAQ

device.

Figure 24.9 shows the TMP3x Datasheet.

We need to convert form Voltage (V) to degrees Celsius.

From the Datasheet (Figure 24.9) we have:

(x ,y )=(0.75V,25◦) (24.1)

1 1

134

Figure 24.7: TMP36 Temperature Sensor

(x ,y )=(1V,50◦) (24.2)

2 2

From the Datasheet (Figure 24.9) we see that there is a linear relationship

between Voltage and degrees Celsius (24.3):

y =ax+b (24.3)

We can find a and b using the following known formula (24.4):

y −y

y−y = 2 1(x−x ) (24.4)

1 x −x 1

2 1

By putting (24.1) and (24.2) into (24.4) we get:

50−25

y−25= (x−0.75) (24.5)

1−0.75

Then we get the following formula we can implement in our Python program:

y =100x−50 (24.6)

Example 24.5.1. Read TMP36 Temperature Data

Python code:

135

Figure 24.8: TMP36 tmp36 Wiring

1 import nidaqmx

2 import time

3

4 from nidaqmx.constants import (

5 TerminalConfiguration)

6

7

8 with nidaqmx.Task() as task:

9 task.ai channels.add ai voltage chan(”Dev1/ai0”,

terminal config=TerminalConfiguration.RSE)

10

11 i = 0

12 while i < 10:

13

14 voltage = task.read()

15

16 degreesC = 100∗voltage − 50

17

18 print(”Sample:”, i)

19 print(”Voltage Value:”, round(voltage ,2))

20 print(”Celsius Value:”, round(degreesC,1))

21 print(”\n”)

22 time.sleep(1)

23 i = i+1

24

25 task.stop

Listing 24.9: Read TMP36 Temperature Data

In the example an ordinary while loop in combination with the sleep() function

have been used to read one new value each second.

[End of Example]

Example 24.5.2. Real-Time Plotting of Temperature Data

136

Figure 24.9: TMP3x Datasheet

In this example we will plot the data from the sensor using the Real-time plot-

ting examples shown in Chapter 23.

We want to present the value from the sensor in degrees Celsius:

1. Read Signal from DAQ Device (0-5V)

2. Convert to degrees Celsius using information from the Datasheet

3. Show/Plot Values from the Sensor

The Python code becomes as follows:

1 import nidaqmx

2 import time

3 import datetime as dt

4 import numpy as np

5 import matplotlib.pyplot as plt

6 import matplotlib.animation as animation

7

8 from nidaqmx.constants import (

9 TerminalConfiguration)

10

11

12 # Create figure for plotting

13 fig = plt.figure()

14 ax = fig.add subplot(1, 1, 1)

15 xs = []

16 ys = []

17

18 # Initialize DAQ device

19 task = nidaqmx.Task()

20 task.ai channels.add ai voltage chan(”Dev1/ai0”, terminal config=

TerminalConfiguration.RSE)

137

21 task.start

22

23

24 # This function is called periodically from FuncAnimation

25 def readdaq(i , xs, ys):

26

27 #Read Value from DAQ device

28 voltage = task.read()

29

30 #Convert Voltage to degrees Celsius

31 degreesC = 100∗voltage − 50

32 temp c = round(degreesC, 1)

33 print(”Celsius Value:”, temp c)

34

35 # Add x and y to lists

36 xs.append(dt.datetime.now().strftime(’%H:%M:%S.%f ’))

37 ys.append(temp c)

38

39 # Limit x and y lists to 20 items

40 xs = xs[−20:]

41 ys = ys[−20:]

42

43 # Draw x and y lists

44 ax.clear()

45 ax.plot(xs, ys)

46

47 # Format plot

48 plt.xticks(rotation=45, ha=’right ’)

49 plt.subplots adjust(bottom=0.30)

50 plt. title(’Temperature Data’)

51 plt.ylabel(’Temperature (deg C)’)

52

53

54 # Set up plot to call readdaq() function periodically

55 ani = animation.FuncAnimation(fig , readdaq, fargs=(xs, ys),

interval=1000)

56 plt.show()

57 task.stop

Listing 24.10: Real-Time Plotting of Temperature Data

[End of Example]

24.5.2 Read Data from Thermistor

A Thermistor is an electronic component that changes resistance to tempera-

ture, a so-called Resistance Temperature Detectors (RTD). It is often used as a

temperature sensor.

Example 24.5.3. Read Thermistor Temperature Data

We will need the following equipment:

• PC with Python

• DAQ device

138

• Breadboard

• 10kohm Thermistor

• 10kohm Resistor

• Wires for connecting the components and create the circuit

Our Thermistor is a so-called NTC (Negative Temperature Coefficient). In a

NTC Thermistor, resistance decreases as the temperature rises.

There is an non-linear relationship between resistance and excitement. To find

the temperature we can use the following equation (Steinhart-Hart equation):

1

=A+Bln(R)+C(ln(R))3 (24.7)

T

K

whereA,BandCareconstantswiththefollowingvalues: A=0.001129148,B =

0.000234125,C =8.76741E−08

T is the temperature in Kelvin.

K

We want to solve the equation regarding the Temperature:

1

T = (24.8)

K A+Bln(R)+C(ln(R))3

The Temperature in degrees Celsius will then be:

T =T −273.15 (24.9)

C K

Wiring...

Figure 24.10 shows how we wire the components together.

Figure 24.10: Thermistor Wiring

139

Figure 24.11: Voltage Divider

The wiring is called a ”Voltage divider”.

Figure 24.11 shows a general Voltage Divider.

A general Voltage Divider has the following equation:

R

V =V 2 (24.10)

out inR +R

1 2

The Voltage Divider for our system becomes as shown in Figure 24.12.

Figure 24.12: Voltage Divider for our System

We then have the following equation:

R

V =V t (24.11)

out inR +R

0 t

140

where R is our 10kohm Thermistor and R is an ordinary 10kohm Resistor.

t 0

V in our case will be +5V which we get from the USB-6008 DAQ device as

in

shown in the wiring diagram.

V is the voltage we read using the DAQ device.

out

Since we need to find the Resistance R , which is used in the Steinhart-Hart

t

equation, we reformulate the formula:

V R

R = out 0 (24.12)

t V −V

in out

We har no ready to start making the Python program for this example.

The program include the following necessary steps:

1. We wire the circuit on the Breadboard and connect it to the DAQ device

2. We measure V using the DAQ

out

3. We calculate R using the Voltage Divider equation

t

R t = V V in o − ut V R o 0 ut

4. We use Steinhart-Hart equation for finding the Temperature

T = 1

K A+Bln(Rt)+C(ln(Rt))3

5. Finally we convert to degrees Celsius

T =T −273.15

C K

The Python code then becomes:

1 import nidaqmx

2 import numpy as np

3 import time

4

5 from nidaqmx.constants import (

6 TerminalConfiguration)

7

8

9 Vin = 5

10 Ro = 10000 # %10k Resistor

11

12

13 with nidaqmx.Task() as task:

14 task.ai channels.add ai voltage chan(”Dev1/ai0”,

terminal config=TerminalConfiguration.RSE)

15

16 i = 0

17 while i < 10:

18

19 Vout = task.read()

20

21 Rt = (Vout∗Ro)/(Vin−Vout) # Voltage Divider Equation

22 # Rt=10000; Used for Testing. Setting Rt=10k should give

TempC=25

23

141

24 # Steinhart constants

25 A = 0.001129148

26 B = 0.000234125

27 C = 0.0000000876741

28

29 # Steinhart−Hart Equation

30 TempK = 1 / (A + (B ∗ np.log(Rt)) + (C ∗ pow(np.log(Rt) ,3))

)

31

32 # Convert from Kelvin to Celsius

33 TempC = TempK − 273.15

34

35 print(”Sample:”, i)

36 print(”Voltage Value:”, round(Vout,2))

37 print(”Celsius Value:”, round(TempC,1))

38 print(”\n”)

39 time.sleep(1)

40 i = i+1

41

42 task.stop

Listing 24.11: Read Thermistor Temperature Data

[End of Example]

Example 24.5.4. Real-Time Plotting of Thermistor Temperature Data

Python code:

1 See previous examples

Listing 24.12: Real-Time Plotting of Thermistor Temperature Data

[End of Example]

24.5.3 Read Data NI TC-01 Thermocouple Device

InthischapterseveralexampleshavebeenshownusingaDAQdevicecombined

with different sensors and components.

Here some examples will be shown using a preset temperature sensor from Na-

tional Instruments called NI USB-TC01. This is a USB based temperature

without need for any kind of wiring, you just plug it in and make your Python

program. SincetheNIUSB-TC01iscompatiblewithNI-DAQmx, youcanpro-

gram it in the same way as other DAQ devices from NI.

Figure 24.13 shows the TC-01 Thermocouple Device from NI.

Example 24.5.5. Real-Time Plotting of Thermistor Temperature Data

Python code:

142

Figure 24.13: TC-01 Thermocouple Device

1 import nidaqmx

2

3 task = nidaqmx.Task()

4

5 task.ai channels.add ai thrmcpl chan(”TC01/ai0”)

6

7 task.start()

8

9 value = task.read()

10 print(round(value ,1))

11

12 task.stop()

13 task.close()

Listing 24.13: TC-01 Thermocouple Python Example

This is just a basic example, which you can easily extend using a while loop or

using some kind of plotting, etc..

[End of Example]

24.6 Data Logging

Python has several functions for creating, reading, updating, and deleting files.

143

Part VI

Python Database

Development

144

Chapter 25

Database Applications with

Python

Here we will learn how we can use Python for communication with a Database

system such as SQL Server or MySQL. We will learn how we connect to a

database, how we can insert data into the database and retrieve data from the

database.

A Database is a structured way to store lots of information. The information

is stored in different tables. Some of the most popular Database Systems today

are:

• SQL Server

• MySQL

• MariaDB

• MongoDB

• etc.

ER Diagram (Entity-Relationship Diagram) is used for design and modeling of

databases. Itspecifiestablesandrelationshipbetweenthem(PrimaryKeysand

Foreign Keys)

Figure 25.1 shows an example of an ER diagram consisting of two database

tables.

Here you can learn more about Database Systems, download examples and get

additional resources, see videos, etc.:

https://www.halvorsen.blog/documents/technology/database/

25.1 Structured Query Language (SQL)

StructuredQueryLanguage(SQL)isadatabaselanguagesupportedbymostof

theexistingdatabasesystemstoday. YouuseSQLtointeractwiththedatabase

145

Figure 25.1: ER Diagram Example

system, like insert data into the database and retrieve data from the database.

Here you can learn more about SQL, download examples and get additional

resources, see videos, etc.:

https://www.halvorsen.blog/documents/technology/database/

25.2 SQL Server

Here we will see how we can communicate with a SQL Server database from

Python.

25.3 MySQL

HerewewillseehowwecancommunicatewithaMySQLdatabasefromPython.

25.4 MongoDB

Here we will see how we can communicate with a MongoDB database from

Python.

MongoDB is a so-called NoSQL database. One of the most popular NoSQL

database systems is MongoDB.

You can download a free MongoDB database from:

https://www.mongodb.com

146

Chapter 26

Structured Query Language

(SQL)

...

147

Chapter 27

SQL Server with Python

27.1 Introduction to SQL Server

Here we will see how we can communicate with a SQL Server from Microsoft

using the Python programming language.

27.2 SQL Server drivers for Python

There are several python SQL drivers available. However, Microsoft places its

testing efforts and its confidence in pyodbc driver. Another driver is pymssql.

pyodbc is an open source Python module that can be used to accessing ODBC

databases.

27.3 pyodbc

pyODBC uses the Microsoft ODBC driver for SQL Server.

27.3.1 Installation of pyodbc

Install pyodbc using pip - Python package manager.

pip install pyodbc

27.3.2 ODBC Drivers

Microsoft have written and distributed multiple ODBC drivers for SQL Server:

You can use the ”ODBC Driver 17 for SQL Server” driver.

This driver supports SQL Server 2008 through 2019.

148

Note that the ”SQL Server Native Client ...” and earlier drivers are deprecated

and should not be used for new development.

The connection string can be written like this:

DRIVER=ODBCDriver17forSQLServer;SERVER=test;DATABASE=test;UID=user;PWD=password

27.4 SQL Server Python Examples

The cursor.execute function can be used to retrieve a result set from a query

against the SQL Database. This function accepts a query and returns a result

set.

Example 27.4.1. Basic SQL Server Example

The cursor.executefunctionis usedto retrieve aresult setfrom aquery against

the SQL Server Database. This function accepts a query and returns a result

set, which can be iterated over with the use of cursor.fetchone().

1 import pyodbc

2

3 server = ”NUCHPH\\SQLEXPRESS”

4 database = ”BOOKS”

5 username = ”sa”

6 password = ”xxx”

7 conn = pyodbc.connect(”DRIVER={ODBC Driver 17 for SQL Server};

SERVER=” + server + ”;DATABASE=” + database + ”;UID=” +

username + ”;PWD=” + password )

8

9 cursor = conn.cursor()

10

11 cursor.execute(”SELECT @@version;”)

12 row = cursor.fetchone()

13 while row:

14 print(row[0])

15 row = cursor.fetchone()

Listing 27.1: Basic SQL Server Example

Example 27.4.2. Getting Data from a Table in SQL Server

Below you find a basic example where data are retrieved from the SQL Server.

1 import pyodbc

2

3 server = ”NUCHPH\\SQLEXPRESS”

4 database = ”BOOKS”

5 username = ”sa”

6 password = ”xxx”

7 conn = pyodbc.connect(”DRIVER={ODBC Driver 17 for SQL Server};

SERVER=” + server + ”;DATABASE=” + database + ”;UID=” +

username + ”;PWD=” + password )

8

149

9 cursor = conn.cursor()

10

11

12 for row in cursor.execute(”select BookId, Title , Isbn from BOOK”):

13 print(row.BookId, row.Title , row.Isbn)

Listing 27.2: Getting Data from SQL Server

[End of Example]

27.5 Stored Procedures

27.6 Resources

https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-

Windows

27.7 pymssql

Resources:

https://pypi.org/project/pymssql/

http://www.pymssql.org/

27.8 Resources

https://docs.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server

150

Chapter 28

MySQL with Python

...

151

Chapter 29

MongoDB with Python

Here we will learn how we can use Python for communication with MongDB.

We will learn how we connect to a database, how we can insert data into the

database and retrieve data from the database.

29.1 Introduction to MongoDB

Here we will see how we can communicate with a MongoDB database from

Python.

MongoDB is a so-called NoSQL database. One of the most popular NoSQL

database systems is MongoDB.

You can download a free MongoDB database from:

https://www.mongodb.com

29.2 MongoDB with Python

Here we will see how we can communicate with a MongoDB database from

Python.

Python needs a MongoDB driver to access the MongoDB database. Many dif-

ferent drivers do exists, so you just need to choose one.

29.2.1 PyMongo

ThePyMongodistributioncontainstoolsforinteractingwithMongoDBdatabase

from Python

https://pypi.org/project/pymongo/

Installation is done using PIP:

152

1 python −m pip install pymongo

29.3 Additional Resources

Tutorials:

https://www.w3schools.com/python/python ongodb etstarted.asp

m g

153

Part VII

Python Application

Development

154

Chapter 30

Development of

Applications with Python

Python is popular within computation, but can be used within many other

applications and can be integrated and used in combination with other pro-

gramming languages, e.g., for development of Web Applications, etc.

Python is probably best suited for ”ad-hoc” numerical calculations, analysis,

simulations, etc., but can be used for many other purposes, even if other pro-

gramming languages are better suited.

Python can be used for creating Web pages (in combination with HTML, CSS,

JavaScript). Pythonisthentypicallyusedontheserver-side,whileHTML,CSS

and JavaScript are used on the client-side.

An example is Django, which is a server-side Python framework used for creat-

ing dynamic web pages.

Python can also be used for programming and creating Raspberry Pi applica-

tions.

In general, Python is a multipurpose programming language that can be used

in many situations. But there is not one programming language which is best

in all kind of situations, so it is important that you know about and have skills

in different languages.

My list of recommendations:

• Visual Studio and C

• LabVIEW - a graphical programming language well suited for hardware

integration, taking measurements and data logging

• MATLAB - Numerical calculations and Scientific computing

• Python - Numerical calculations, and Scientific computing, etc.

155

• Web Programming, such as HTML, CSS, JavaScript and a Server-side

framework/programming language like PHP, ASP.NET

• Databases (such as SQL Server and MySQL) and using the Structured

Query Language (SQL)

• App Development for the 2 main platforms iOS (XCode using the Swift

Programming Language) and Android (Android Studio using the Java

Programming Language or Kotlin Programming language)

If you have skills in most of the tools, programming languages and frameworks

mention above, you are well suited for working as a full-time programmer or

software engineer.

A good resource or starting point for creating Applications for Python is:

Applications for Python [18]:

https://www.python.org/about/apps/

30.1 Mathematics, Science and Engineering

Python is probably best suited for ”ad-hoc” numerical calculations, analysis,

simulations, etc. These kinds of applications has also been the main focus in

this textbook. Other kinds of applications will briefly be covered in this chap-

ter. More details will be covered in later chapters and in other textbooks in

my Python textbooks series, which you can read more of in the Preface of this

textbook.

TheSciPyisacollectionofpackagesformathematics, science, andengineering,

which has been thoroughly reviewed earlier in this textbook.

30.2 Desktop GUI Applications

Python don’t come with builtin tools for creating traditional desktop GUI ap-

plications, so you need to use an external GUI packages for this purpose.

In my opinion, tools like Visual Studio where you can create professional GUI

applicationsusingeithertheCorVB.NETlanguagesinoneintegratedpackages

is a better choice.

AnothergoodalternativeisLabVIEW,whichhaspowerfulGUIfeaturesincom-

bination with extensive hardware integration.

Other tools (Integrated Programming Environments, IDE) and programming

languages for GUI applications os Xcode on macOS, which can be used for cre-

ating macOS desktop applications and apps for iPhone and iPad.

156

ForAndroiddevelopmentyouhaveAndroidStudio. Hereyoucanuseprogram-

ming languages like Java and Kotlin.

Since this is a Python textbook, lets go back to the options we have if we want

to create desktop GUI applications with Python.

Python has different desktop GUI frameworks like:

• PyQt

• Tkinter

• WxPython

• PyGUI

• PySide2

• Kivy

These are just some of the options we have, for a comprehensive overview of

GUI frameworks for Python see the following:

https://docs.python.org/3/library/othergui.htmlother-gui-packages

https://wiki.python.org/moin/GuiProgramming

PyQt and wxPython, all have a modern look and feel and more widgets than

Tkinter.

ThisisalsoabitofaproblemwhenitcomestodesktopGUIdevelopmentwith

Python. You have so many choices, and sometimes its better better with one

good option than many half good options.

30.2.1 PyQt

PyQtbringstogethertheQtC++cross-platformapplicationframeworkandthe

cross-platforminterpretedlanguagePython. Qtisacross-platformGUItoolkit.

Qt also includes Qt Designer, a graphical user interface designer. PyQt is able

to generate Python code from Qt Designer. It is also possible to add new GUI

controls written in Python to Qt Designer.

For more information about PyQt:

https://riverbankcomputing.com/software/pyqt/intro

For more information about Qt:

https://www.qt.io

157

PyQt Tutorials:

https://likegeeks.com/pyqt5-tutorial/

https://build-system.fman.io/pyqt5-tutorial

30.2.2 PySide2

PySide2 is the official Python module from the Qt for Python project, which

provides access to the complete Qt framework.

The originally PySide framework was originally released by Nokia, then owner

of Qt. After Nokia sold Qt in 2011, PySide was no longer maintained. Then

PySide2 was established and maintained by a community. Finally, in 2016, the

Qt company committed to officially support the PySide2 project.

So basically, PySide2 is very similar to PyQt.

ThedownsidewithPySide2(August2019)isthatitisstillin”beta”(Technical

Preview).

For more information about PySide2:

https://pypi.org/project/PySide2/

https://wiki.qt.io/Qt or ython

f P

30.2.3 Tkinter

Another popular GUI framework is Tkinter.

For more information about Tkinter:

https://docs.python.org/2/library/tkinter.html

30.2.4 WxPython

WxPython is a cross-platform GUI toolkit for the Python language.

For more information about WxPython:

https://www.wxpython.org

https://wiki.wxpython.org/Getting

158

30.3 Web Applications

Python can be used for creating Web pages (in combination with HTML, CSS,

JavaScript). Pythonisthentypicallyusedontheserver-side,whileHTML,CSS

and JavaScript are used on the client-side.

An example is Django, which is a server-side Python framework used for creat-

ing dynamic web pages.

Read more about Django here:

https://www.djangoproject.com

Other popular web application frameworks and programming languages are

ASP.NET and PHP.

You may read more about web programming in general here:

https://www.halvorsen.blog/documents/programming/web/

30.4 Database Applications

Python can be used for communication with a database system such as SQL

Server or MySQL. Python has different packages for communication with dif-

ferent database systems, both SQL databases (e.g., SQL Server, MySQL, Mari-

aDB, etc.) and so-called NoSQL databases (e.g., MongoDB).

HereyoucanlearnmoreaboutDatabaseSystemsandSQL,downloadexamples

and get additional resources, see videos, etc.:

https://www.halvorsen.blog/documents/technology/database/

30.4.1 SQL Server

SQLServerisaDatabaseSystemfromMicrosoft. SQLServercomesindifferent

editions, for basic, personal use SQL Server Express is recommended because it

is simple to use and it is free.

Read more about SQL Server here:

https://www.halvorsen.blog/documents/technology/database/sql erver.php

s

30.4.2 MySQL

MySQL is an open-source and widely used Relational Database Management

System (RDBMS).

MySQL comes in different editions, both paid (Enterprise) and free versions

(Community).

159

In addition to the Database itself, the MySQL Workbench is nice to have.

MySQL Workbench visual database design tool, used for Datbase Modelling,

etc. Another handy tool is phpMyAdmin. phpMyAdmin is a free software tool

written in PHP, intended to handle the administration of MySQL.

Read more about MySQL here:

https://www.halvorsen.blog/documents/technology/database/mysql.php

30.4.3 MariaDB

MariaDB is a spinoff from the more famous MySQL Database System.

The MariaDB database server is published as free and open source software.

MariaDB has compatibility with MySQL in most situations. MariaDB is said

to have slightly better performance than MySQL.

Read more about MariaDB here:

https://www.halvorsen.blog/documents/technology/database/mariadb.php

30.4.4 MongoDB

MongoDB is a general purpose, document-based, distributed database.

MongoDB is a cross-platform document-oriented database program. Classified

as a NoSQL database program.

You can download MongoDB from:

https://www.mongodb.com

160

Chapter 31

Python Integration with

Visual Studio

Microsoft Visual Studio is an integrated development environment (IDE) from

Microsoft. It is used to develop computer programs, as well as websites, web

apps,webservicesandmobileapps. Thedeafult(main)programminglanguage

in Visual studio is C, but many other programming languages are supported.

Visual studio is available for Windows and macOS.

Visual Studio (from Visual Studio 2017), has integrated support for Python, it

is called ”Python Support in Visual Studio”.

Web:

https://visualstudio.microsoft.com

Wikipedia:

https://en.wikipedia.org/wiki/Microsoft isual tudio

V S

Here you can learn more about Visual studio and C, download examples and

get additional resources, see videos, etc.:

https://www.halvorsen.blog/documents/programming/csharp/

ForanintroductiontothePythonintegrationinVisualStudio, seeChapter19.

161

Chapter 32

Python Integration with

LabVIEW

32.1 What is LabVIEW?

LabVIEW is a graphical programming language well suited for hardware inte-

gration, taking measurements and data logging.

Go to my web site in order to learn more about LabVIEW:

https://www.halvorsen.blog

https://www.halvorsen.blog/documents/programming/labview/

HeryoufindinformationaboutLabVIEW,youfindlotsofresourcesliketraining

material, videos, code examples, etc.

32.2 Using Python in LabVIEW

LabVIEWisafullyfunctionalprogramminglanguagewhichyoucanusetocre-

ate many different kinds of applications. In addition it cal also integrate with

many other programming languages like MATLAB and Python.

Web:

http://zone.ni.com/reference/en-XX/help/371361R-01/glang/python pal/

Use the Python functions to call Python code from LabVIEW. See Figure 32.1

Note! LabVIEW supports calling Python version 2.7 and 3.6. Although un-

supported versions might work with the LabVIEW Python functions, NI rec-

ommends using supported versions of Python only.

Ensure that the bitness of Python corresponds to the bitness of LabVIEW in-

stalled on the machine. This means if you have LabVIEW 32 bit, you should

use Python 32 bit and if you have LabVIEW 64 bit, you should use Python 64

162

bit.

TorunthePythoncode,LabVIEWrequiresthePythonsharedlibraries(DLLs)

in the system path.

ForWindows: IfyouinstallPython3.6,addthedirectorycontainingpython36.dll

to the system path. If you install Python 2.7, add the directory containing

python27.dll to the system path.

For detailed instructions regarding Installing Python for Calling Python Code:

http://www.ni.com/product-documentation/54295/en/

LabVIEW functions for dealing with Python: Open Python Session Python

Node Close Python Session

Figure 32.1: Python Integration in LabVIEW

The ”Python Node” calls a Python function directly.

Here I will present some examples how we can integrate an existing Python

script or Python function.

Example 32.2.1. Python Integration in LabVIEW

We want to use Python to covert between Ceslius and Fahrenheit (and vice

versa).

The formula for converting from Celsius to Fahrenheit is:

T =(T ×9/5)+32 (32.1)

f c

The formula for converting from Fahrenheit to Celsius is:

T =(T −32)×(5/9) (32.2)

c f

First,wecreateaPythonmodulewiththefollowingfunctions(fahrenheit.py):

1 def c2f(Tc):

2

163

3 Tf = (Tc ∗ 9/5) + 32

4 return Tf

5

6

7 def f2c(Tf):

8

9 Tc = (Tf − 32)∗(5/9)

10 return Tc

Listing 32.1: Python Functions

Then, we create a Python script for testing the functions (test ahrenheit.py):

f

1 from fahrenheit import c2f , f2c

2

3 Tc = 0

4

5 Tf = c2f(Tc)

6

7 print(”Fahrenheit: ” + str(Tf))

8

9

10 Tf = 32

11

12 Tc = f2c(Tf)

13

14 print(”Celsius: ” + str(Tc))

Listing 32.2: Testing the Functions

The results becomes:

1 Fahrenheit: 32.0

2 Celsius: 0.0

Lets make the LabVIEW program that call these Python functions:

In Figure 32.2 we see the Front Panel.

In Figure 32.3 we see the Block Diagram.

In Figure 32.4 we see LabVIEW Code for calling both Python func-

tions (c2f and f2c) from LabVIEW.

[End of Example]

164

Figure 32.2: Python Integration in LabVIEW

Figure 32.3: Python Integration in LabVIEW

165

Figure 32.4: Python Integration in LabVIEW

166

Chapter 33

Raspberry Pi and Python

33.1 What is Raspberry Pi?

The Raspberry Pi is a credit-card-sized computer that plugs into your TV and

a keyboard. It is a capable little computer which can be used in electronics

projects, and for many of the things that your desktop PC does.

Raspberry Pi is very popular in IoT projects and applications.

For more information and resources regarding Raspberry Pi:

https://www.halvorsen.blog/documents/technology/iot/raspberry pi.php

Other Resources:

https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-

with-the-raspberry-pi/programming-in-python

First,beforeyoustartprogrammingPythononaRaspberryPidevice,youneed

to install an operating system like Raspbian. Raspbian is a Linux distribution

tailor made for Raspberry Pi.

Raspbian comes also pre-installed Python.

For more information about Raspbian:

https://www.raspberrypi.org/downloads/raspbian/

167

Chapter 34

Web Development with

Python

34.1 Introduction to Web Development

The basic building blocks for creating Web pages are the following:

• HTML

• CSS

• JavaScript

Here you find more information, resources, videos and examples regarding Web

Development:

https://www.halvorsen.blog/documents/programming/web/

34.1.1 HTML

Hereyoufindmoreinformation,resources,videosandexamplesregardingHTML:

https://www.halvorsen.blog/documents/programming/web/html.php

34.1.2 CSS

34.1.3 JavaScript

34.2 Introduction to Web Frameworks

The basic building blocks for creating Web pages are the following:

• HTML

• CSS

• JavaScript

168

InadditionyoutypicallyneedaWebFrameworkforcreatingdynamicwebpages

that communicate with a Database, etc.

We divide Web Development into 2 parts: Server-side development and client-

side development.

On the server-side we have different Web Development Frameworks like:

• PHP

• ASP.NET

• ... Manyothers,includingdifferentPythonWebDevelopmentFrameworks

34.2.1 PHP

Hereyoufindmoreinformation,resources,videosandexamplesregardingPHP:

https://www.halvorsen.blog/documents/programming/web/php.php

34.2.2 ASP.NET

Hereyoufindmoreinformation,resources,videosandexamplesregardingASP.NET:

https://www.halvorsen.blog/documents/programming/web/asp et.php

n

There are different Python Frameworks you can use for creating Web Applica-

tions with Python.

Django Bottle Flask

34.3 Django - Python-based Web Framework

Django - Python-based Web Framework.

169

Chapter 35

Create GUI Applications

Here are some programming environments and programming languages for cre-

ating GUI applications presented.

35.1 LabVIEW

Here you find more information, resources, videos and examples regarding Lab-

VIEW:

https://www.halvorsen.blog/documents/programming/labview/

35.2 Visual Studio and C#

Here you find more information, resources, videos and examples regarding Vi-

sual Studio and C#:

https://www.halvorsen.blog/documents/programming/csharp/

35.3 Web Development

Here you find more information, resources, videos and examples regarding Web

Development:

https://www.halvorsen.blog/documents/programming/web/

Hereyoufindmoreinformation,resources,videosandexamplesregardingHTML:

https://www.halvorsen.blog/documents/programming/web/html.php

Hereyoufindmoreinformation,resources,videosandexamplesregardingPHP:

https://www.halvorsen.blog/documents/programming/web/php.php

Hereyoufindmoreinformation,resources,videosandexamplesregardingASP.NET:

https://www.halvorsen.blog/documents/programming/web/asp et.php

n

170

Chapter 36

Machine Learning with

Python

36.1 Introduction to Machine Learning

Here you can learn more about Machine Learning, download examples and get

additional resources, see videos, etc.:

https://www.halvorsen.blog/documents/technology/machine earning/

l

171

Part VIII

Python PyQt GUI

Development

172

Chapter 37

Getting Started with PyQt

37.1 Introduction

PyQt brings together the Qt C++ cross-platform application framework and

the cross-platform interpreted language Python.

Qt is a cross-platform GUI toolkit.

Qt also includes Qt Designer, a graphical user interface designer. PyQt is able

to generate Python code from Qt Designer. It is also possible to add new GUI

controls written in Python to Qt Designer.

37.2 Introduction to Qt

Qt (pronounced ”cute”) is a free and open-source widget toolkit for creating

graphicaluserinterfacesaswellascross-platformapplicationsthatrunonvari-

oussoftwareandhardwareplatformssuchasLinux,Windows,macOS,Android

or embedded systems with little or no change in the underlying codebase while

still being a native application with native capabilities and speed.

QtiscurrentlybeingdevelopedbyTheQtCompany. Qtwasoriginallycreated

by the Norwegian company Trolltech.

IfyouwanttouseQtinsidePythonyouwillneedaPythonlibrarythatletyou

interfacewithQt’sC++API.Manysuchbindings/librariesdoexist. Themost

used Qt Python library is PyQt. We will use PyQt in this chapter.

Another Qt Python library is PySide2. PySide2 is the official Python module

from the ”Qt for Python” project, which provides access to the complete Qt

framework.

The originally PySide framework was originally released by Nokia, then owner

of Qt. After Nokia sold Qt in 2011, PySide was no longer maintained. Then

173

PySide2 was established and maintained by a community. Finally, in 2016, the

Qt company committed to officially support the PySide2 project.

So basically, PySide2 is very similar to PyQt.

ThedownsidewithPySide2(August2019)isthatitisstillin”beta”(Technical

Preview).

For more information about Qt, see the resources below.

Wikipedia:

https://en.wikipedia.org/wiki/Qt software)

(

The Qt Company web site:

https://www.qt.io

37.3 Introduction to PyQt

PyQt is a set of Python bindings for The Qt Company’s Qt application frame-

work and runs on all platforms supported by Qt including Windows, OS X,

Linux, iOS and Android. PyQt5 supports Qt v5.

PyQt is developed and maintened by Riverbank Computing.

For more information about PyQt, see the resources below.

Riverbank Computing web site:

https://riverbankcomputing.com/software/pyqt/

Here are some PyQt Tutorials:

https://likegeeks.com/pyqt5-tutorial/

https://build-system.fman.io/pyqt5-tutorial

https://data-flair.training/blogs/python-pyqt5-tutorial/

https://www.guru99.com/pyqt-tutorial.html

https://pythonspot.com/gui/

37.3.1 PyQtChart

PyQt don’t include any types of charts. In order to use charts or plotting, you

can use PyQtChart.

PyQtChartisasetofPythonbindingsforTheQtCompany’sQtChartslibrary.

The bindings sit on top of PyQt5 and are implemented as a single module.

174

https://www.riverbankcomputing.com/software/pyqtchart/

37.4 Installing PyQt

37.4.1 Installation of PyQt

Use PIP in order to install PyQt5:

pip3 install PyQt5

PIP is a tool for installing Python packages.

The Python Package Index (PyPI) is a repository of software for the Python

programming language. Package authors use PyPI to distribute their software.

For more information about PIP and installing Python Packages:

https://packaging.python.org/tutorials/installing-packages/

For more information about PyPI:

https://pypi.org

For more information about PyQt5:

https://pypi.org/project/PyQt5/

37.4.2 Installation of Qt Designer

Qt Designer is a tool for quickly building graphical user interfaces with widgets

from the Qt GUI framework. It gives you a simple drag-and-drop interface for

laying out components such as buttons, text fields, combo boxes and more.

This gives the the plot shown in Figure 37.1.

You can download and install the Qt Designer from this web site:

https://build-system.fman.io/qt-designer-download

37.4.3 Installation of PyQtChart

Use PIP in order to install PyQtChart:

pip3 install PyQtChart

175

Figure 37.1: Qt Designer

37.5 PyQt Basics

Below we see a basic PyQt application created in Python.

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget

3 if name == ” main ”:

4 application = QApplication(sys.argv)

5 window = QWidget()

6 window.resize(300,200)

7 window.setWindowTitle(”Hello World”)

8 window.show()

9 sys.exit(application.exec ())

Listing 37.1: Basic PyQt Application

If you are using macOS, the Python code above gives the basic application

shown in Figure 37.2.

If you are using Windows, the Python code above gives the basic application

shown in Figure 37.3.

For the first, with the same Python code we can create cross-platform applica-

tion.

Lets go through the code in detail:

1 from PyQt5.QtWidgets import QApplication, QWidget

ThisstatementimportsallthenecessarymodulesyouneedtocreateyourGUI.

176

Figure 37.2: Basic PyQt Application on macOS

TheQtWidgetsmodulecontainsallthemajorwidgetsthatyouwillbeusingin

this tutorial.

1 application = QApplication(sys.argv)

The first thing you need to create is an object of the QApplication class. All

PyQt GUI application must create an instance of QApplication.

sys.argv is the list of command-line parameters that you can pass to the appli-

cation when launching it through the shell or while automating the interface.

If you don’t need to pass any arguments to QApplications, you can use [].

1 application = QApplication([])

Then we need to create an object of the QWidget class. QWidget is the foun-

dation for all UI objects in Qt. Typically, everything you see in an an PyQt

application is a widget, examples: Label, ComboBox, CheckBox, RadioButton,

PushButton, etc.

1 window = QWidget()

1 window.resize(300,200)

TheresizemethodoftheQWidgetclassallowsyoutosetthedimensionsofany

widget. In this case, you have resized the window to 300px by 200px.

Notethatwidgetscouldbenestedtogether,theoutermostwidget(i.e.,thewid-

get with no parent) is called a Window.

Use the setWindowTitle() method to set a title for your window.

177

Figure 37.3: Basic PyQt Application on Windows

1 window.setWindowTitle(”Hello World”)

When all the settings are done, we need to show the window on the screen by

using the show() method:

1 window.show()

The final piece of code is:

1 sys.exit(application.exec ())

The app.exec () method starts the event loop inside Qt/C++. PyQt is mainly

written in C++ and uses the event loop mechanism to implement parallel exe-

cution. app.exec ()passesthecontrolovertoQtwhichwillexittheapplication

only when the user closes it from the GUI.

37.6 PyQt Widgets

QWidget is the foundation for all UI objects in Qt. Typically, everything you

seeinananPyQtapplicationisawidget,examples: Label,ComboBox,Check-

Box, RadioButton, PushButton, etc.

Lets make some code examples using some of these widgets.

Example 37.6.1. Label (QLabel)

A basic Label example:

178

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget, QLabel

3 if name == ” main ”:

4 application = QApplication(sys.argv)

5 window = QWidget()

6 window.resize(300,200)

7 window.setWindowTitle(”Hello World”)

8

9 label = QLabel(window)

10 label.setText(”This is a Label”)

11 label.move(100,50)

12

13 window.show()

14 sys.exit(application.exec ())

Listing 37.2: QLabel Example

This gives the window as shown in Figure 37.4.

Figure 37.4: QLabel Example

[End of Example]

Example 37.6.2. TextBox (QLineEdit)

A basic TextBox example:

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

3 if name == ” main ”:

4 application = QApplication(sys.argv)

5 window = QWidget()

6 window.resize(300,200)

7 window.setWindowTitle(”Hello World”)

8

9 inputbox = QLineEdit(window)

10 inputbox.setText(”Please enter your Name”)

179

11 inputbox.resize(200, 20)

12 inputbox.move(20,50)

13

14 window.show()

15 sys.exit(application.exec ())

Listing 37.3: QLineEdit EXample

This gives the window as shown in Figure 37.5.

Figure 37.5: QLineEdit Example

You can use the following if you want a read-only field:

1 inputbox.setReadOnly(True)

[End of Example]

Example 37.6.3. ComboBox (QComboBox)

A basic ComboBox box example:

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget, QComboBox

3 if name == ” main ”:

4 application = QApplication(sys.argv)

5 window = QWidget()

6 window.resize(300,200)

7 window.setWindowTitle(”Hello World”)

8

9 combobox = QComboBox(window)

10 combobox.addItems([”item one”, ”item two”, ”item three”])

11 combobox.move(100,50)

12

13 window.show()

14 sys.exit(application.exec ())

Listing 37.4: QLineEdit Example

180

This gives the window as shown in Figure 37.6.

Figure 37.6: QComboBox Example

We can change the visual appearance by using the following:

1 application.setStyle(’Fusion’)

[End of Example]

37.7 Event Handling in PyQt

PyQt uses a mechanism called signals to let you react to events such as the

user clicking a button.

Example:

1 self .btnShowData.clicked.connect(self .btnShowData clicked)

You need to define a function that is called when the signal occurs. This func-

tion is called a slot in PyQt.

Example:

1 def btnShowData clicked(self):

2 temp = np.random.randint(20,50)

3 self .txtTemp.setText(str(temp))

Example 37.7.1. Button Click

Below you see a basic Push Button example:

181

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

3

4 def button clicked():

5 print(”You clicked the Button”)

6

7 if name == ” main ”:

8 application = QApplication(sys.argv)

9 application.setStyle(’Fusion’)

10 window = QWidget()

11 window.resize(300,200)

12 window.setWindowTitle(”Hello World”)

13

14 button = QPushButton(window)

15 button.setText(”Click Me”)

16 button.move(100,50)

17 button.clicked.connect(button clicked)

18

19 window.show()

20 sys.exit(application.exec ())

Listing 37.5: Button Click

[End of Example]

Example 37.7.2. MessageBox (QMessageBox)

MessageBox example:

1 import sys

2 from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,

QMessageBox

3

4 def button clicked():

5 messagebox = QMessageBox()

6 messagebox.setText(’You clicked the button! ’)

7 messagebox.exec ()

8

9 if name == ” main ”:

10 application = QApplication(sys.argv)

11 application.setStyle(’Fusion’)

12 window = QWidget()

13 window.resize(300,200)

14 window.setWindowTitle(”Hello World”)

15

16 button = QPushButton(window)

17 button.setText(”Click Me”)

18 button.move(100,50)

19 button.clicked.connect(button clicked)

20

21 window.show()

22 sys.exit(application.exec ())

Listing 37.6: MessageBox Example

This gives the window as shown in Figure 37.7.

182

Figure 37.7: QMessageBox Example

[End of Example]

Example 37.7.3. Combining different Widgets and Event Handling Example

In this example we combine different Widgets and some Event Handling:

1 import sys

2 import numpy as np

3 from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,

QLineEdit, QMessageBox

4

5 class Application(QWidget):

6

7 def init (self):

8 super(). init ()

9 self .initUI()

10

11 def initUI(self):

12 self .setWindowTitle(”PyQt Example”)

13 self .resize(400, 300)

14

15

16 self .txtName = QLineEdit(self)

17 self .txtName.setText(”Please enter your Name”)

18 self .txtName.move(20, 20)

19 self .txtName.resize(200, 20)

20

21 self .btnShowName = QPushButton(”Show Name”, self)

22 self .btnShowName.move(15,60)

23 self .btnShowName.clicked.connect(self .btnShowName clicked)

24

25 self .show()

26

27

28 def btnShowName clicked(self):

29 self .showMessage()

30

31 def showMessage(self):

183

32

33 name = self .txtName.text()

34 text = ”Is your Name ” + name + ”?”

35 reply = QMessageBox.question(self , ’Message’, text ,

QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

36

37 if reply == QMessageBox.No:

38 self .txtName.setText(”Please enter your Name”)

39

40

41 if name == ’ main ’:

42 app = QApplication(sys.argv)

43 app.setStyle(’Fusion’)

44 window = Application()

45 sys.exit(app.exec ())

Listing 37.7: Combining different Widgets and Event Handling Example

This gives the window as shown in Figure 37.8.

Figure 37.8: PyQt Application Example

[End of Example]

37.8 PyQt Designer

...

37.9 PyQt Applications Examples

Here some real-life examples of PyQt will be provided.

184

Some examples are:

• Logging Data from a Sensor and presenting the values on the screen

• Simulation of a system and presenting values on the screen

• Control System

• etc.

Example 37.9.1. Example Name

...

1 ...

2 ...

Listing 37.8: xxx

Example 37.9.2. Example Name

...

1 ...

2 ...

Listing 37.9: xxx

Example 37.9.3. Example Name

...

1 ...

2 ...

Listing 37.10: xxx

185

Part IX

Resources

186

Chapter 38

Python Resources

Here you find my Web page with Python resources [1]:

https://www.halvorsen.blog/documents/programming/python/

Python Home Page [6]:

https://www.python.org

Python Standard Library [19]:

https://docs.python.org/3/library/index.html

38.1 Python Distributions

Anaconda:

https://www.anaconda.com

38.2 Python Libraries

NumPy Library:

http://www.numpy.org

SciPy Library:

https://www.scipy.org

Matplotlib Library:

https://matplotlib.org

38.3 Python Editors

Spyder:

https://www.spyder-ide.org

187

Visual studio Code:

https://code.visualstudio.com

Visual Studio:

https://visualstudio.microsoft.com

PyCharm:

https://www.jetbrains.com/pycharm/

Wing:

https://wingware.com

Jupyter Notebook:

http://jupyter.org

38.4 Python Tutorials

Python Tutorial - w3schools.com [13]:

https://www.w3schools.com/python/

The Python Guru [20]:

https://thepythonguru.com

Wikibooks - A Beginner’s Python Tutorial:

https://en.wikibooks.org/wiki/A eginner

B

TutorialsPoints - Python Tutorial:

https://www.tutorialspoint.com/python/

The Hitchhiker’s Guide to Python:

https://docs.python-guide.org

Google’s Python Class:

https://developers.google.com/edu/python/

38.5 Python in Visual Studio

Work with Python in Visual Studio

https://docs.microsoft.com/visualstudio/python/

188

Bibliography

[1] H.-P. Halvorsen, “Technology blog - https://www.halvorsen.blog,” 2018.

[2] H.-P.Halvorsen,“Technologyblog-https://en.wikipedia.org/wiki/Python programming anguage),(cid:48)(cid:48)2018.

( l

[3] T. . T. P. Languages, “The 2018 top programming languages

- https://spectrum.ieee.org/at-work/innovation/the-2018-top-

programming-languages,” 2018.

[4] S. Overflow, “Stack overflow developer survey 2018 -

https://insights.stackoverflow.com/survey/2018/,” 2018.

[5] stackoverflow.blog, “The incredible growth of python -

https://stackoverflow.blog/2017/09/06/incredible-growth-python/,”

2018.

[6] python.org, “python.org - https://www.python.org,” 2018.

[7] python.org,“Thepythontutorial-https://docs.python.org/3.7/tutorial/,”

2018.

[8] python.org,“Python3.7.1documentation-https://docs.python.org/3.7/,”

2018.

[9] scipy.org, “Scipy - https://www.scipy.org,” 2018.

[10] matplotlib.org, “Matplotlib - https://matplotlib.org,” 2018.

[11] pandas, “pandas - http://pandas.pydata.org,” 2018.

[12] Wingware, “Wingware python ide - https://wingware.com,” 2018.

[13] w3schools.com, “Python tutorial - https://www.w3schools.com/python/,”

2018.

[14] Wikipedia,“Debugging-https://en.wikipedia.org/wiki/Debugging,”2018.

[15] TechBeamers, “Get the best python ide -

https://www.techbeamers.com/best-python-ide-python-programming/,”

2018.

[16] Jupyter, “Jupyter - https://jupyter.org,” 2018.

[17] JupyterHub, “Jupyterhub - http://jupyter.org/hub,” 2018.

189

[18] python.org, “Applications for python -

https://www.python.org/about/apps/,” 2018.

[19] python.org, “The python standard library -

https://docs.python.org/3/library/,” 2018.

[20] T. P. Guru, “The python guru - https://thepythonguru.com,” 2018.

190

Part X

Solutions to Exercises

191

Start using Python

Simulation and Plotting of Dynamic System

Given the autonomous system:

x˙ =ax (1)

Where:

1

a=−

T

where T is the time constant.

The solution for the differential equation is:

x(t)=eatx (2)

0

Set T=5 and the initial condition x(0)=1.

Create a Script inPython (.py file) where you plot the solution x(t) in the time

interval:

0≤t≤25

Add Grid, and proper Title and Axis Labels to the plot.

Python Script:

1 import math as mt

2 import numpy as np

3 import matplotlib.pyplot as plt

4

5

6 # Model Parameters

7 T = 5

8 a = −1/T

9

10 # Simulation Parameters

11 x0 = 1

12 t = 0

13

14 tstart = 0

192

15 tstop = 25

16

17 increment = 1

18

19 x = []

20 x = np.zeros(tstop+1)

21

22 t = np.arange(tstart ,tstop+1,increment)

23

24

25 # Define the Function

26 for k in range(tstop):

27 x[k] = mt.exp(a∗t[k]) ∗ x0

28

29

30 # Plot the Simulation Results

31 plt.plot(t,x)

32 plt. title(’Simulation of Dynamic System’)

33 plt.xlabel(’t’)

34 plt.ylabel(’x’)

35 plt.grid()

36 plt.axis([0, 25, 0, 1])

37 plt.show()

The simulation gives the results as shown in Figure 1.

Figure 1: Simulation of Dynamic System

[End of Exercise]

193

Mathematics in Python

Create Mathematical Expressions in Python

Create a function that calculates the following mathematical expression:

(cid:112)

z =3x2+ x2+y2+eln(x) (3)

Test with different values for x and y.

We create a Python Module with a Python Function (mymathfunctions.py):

1 import math as mt

2

3 def calcexpression(x,y):

4

5 z = 3∗x∗∗2 + mt.sqrt(x∗∗2 + y∗∗2) + mt.exp(mt.log(x))

6 return z

Then we can create a Python Script in order to test the function:

1 import mymathfunctions as mymath

2

3 x = 2

4 y = 2

5

6 z = mymath.calcexpression(x,y)

7

8 print(z)

The results become:

1 16.82842712474619

[End of Solution]

Create advanced Mathematical Expressions in Python

Create the following expression in Python:

ln(ax2+bx+c)−sin(ax2+bx+c)

f(x)= (4)

4πx2+cos(x−2)(ax2+bx+c)

194

Given a=1,b=3,c=5 Find f(9)

(The answer should be f(9)=0.0044)

Tip! You should split the expressions into different parts, such as:

poly =ax2+bx+c

num=...

den=...

f =...

This makes the expression simpler to read and understand, and you minimize

the risk of making an error while typing the expression in Python.

When you got the correct answer try to change to, e.g., a=2,b=8,c=6

Find f(9)

Python Script:

1 ...

[End of Solution]

195

Discrete Systems

Bacteria Population

In this task we will simulate a simple model of a bacteria population in a jar.

The model is as follows:

birth rate=bx (5)

death rate=px2 (6)

Then the total rate of change of bacteria population is:

x˙ =bx−px2 (7)

Set b=1/hour and p=0.5 bacteria-hour

We will simulate the number of bacteria in the jar after 1 hour, assuming that

initially there are 100 bacteria present.

Find the discrete model using the Euler Forward method by hand and imple-

ment and simulate the system in Python using a For Loop.

We can use e.g., the Euler Approximation:

x −x

x˙ ≈ k+1 k (8)

T

s

T - Sampling Interval

s

Then we get:

196

x −x

k+1 k =bx −px2 (9)

T k k

s

This gives the following discrete differential equation:

x =x +T (bx −px2) (10)

k+1 k s k k

Now we are ready to simulate the system.

Python Script:

1 # Simulation of Bacteria Population

2 import numpy as np

3 import matplotlib.pyplot as plt

4

5 # Model Parameters

6 b = 1

7 p = 0.5

8

9 # Simulation Parameters

10 Ts = 0.01

11 Tstop = 1

12 xk = 100

13 N = int(Tstop/Ts) # Simulation length

14 data = []

15 data.append(xk)

16

17

18 # Simulation

19 for k in range(N):

20 xk1 = xk + Ts∗ (b ∗ xk − p ∗ xk∗∗2);

21 xk = xk1

22 data.append(xk1)

23

24 # Plot the Simulation Results

25 t = np.arange(0,Tstop+Ts,Ts)

26

27 plt.plot(t,data)

28 plt. title(’Simulation of Bacteria Population’)

29 plt.xlabel(’t [s] ’)

30 plt.ylabel(’x’)

31 plt.grid()

32 plt.axis([0, 1, 0, 100])

33 plt.show()

The simulation gives the results as shown in Figure 2.

[End of Solution]

197

Figure 2: Simulation of Bacteria Population

Simulation with 2 variables

Given the following system:

dx

1 =−x (11)

dt 2

dx

2 =x (12)

dt 1

Find the discrete system and simulate the discrete system in Python. Solve the

equations, e.g., in the time span [-1 1] with initial values [1, 1].

Python Script:

1 # Simulation with 2 Variables

2 import numpy as np

3 import matplotlib.pyplot as plt

4

5 # Model Parameters

6 b = 1

7 p = 0.5

8

9 # Simulation Parameters

10 Ts = 0.1

11 Tstart = −1

12 Tstop = 1

13 x1k = 1

14 x2k = 1

15 N = int((Tstop−Tstart)/Ts) # Simulation length

16 datax1 = []

198

17 datax2 = []

18 datax1.append(x1k)

19 datax2.append(x2k)

20

21

22 # Simulation

23 for k in range(N):

24 x1k1 = x1k − Ts ∗ x2k

25 x2k1 = x2k + Ts ∗ x1k

26

27 x1k = x1k1

28 x2k = x2k1

29 datax1.append(x1k1)

30 datax2.append(x2k1)

31

32 # Plot the Simulation Results

33 t = np.arange(Tstart ,Tstop+Ts,Ts)

34

35 plt.plot(t,datax1, t, datax2)

36 plt. title(’Simulation with 2 Variables’)

37 plt.xlabel(’t [s] ’)

38 plt.ylabel(’x’)

39 plt.grid()

40 plt.axis([−1, 1, −1.5, 1.5])

41 plt.show()

The simulation gives the results as shown in Figure 2.

Figure 3: Simulation Example with 2 Variables

Alternative Solution:

1 # Simulation with 2 Variables

2 import numpy as np

3 import matplotlib.pyplot as plt

4

5 # Model Parameters

199

6 b = 1

7 p = 0.5

8

9 # Simulation Parameters

10 Ts = 0.1

11 Tstart = −1

12 Tstop = 1

13 N = int((Tstop−Tstart)/Ts) # Simulation length

14 x1 = np.zeros(N+2)

15 x2 = np.zeros(N+2)

16 x1[0] = 1

17 x2[0] = 1

18

19

20 # Simulation

21 for k in range(N+1):

22 x1[k+1] = x1[k] − Ts ∗ x2[k]

23 x2[k+1] = x2[k] + Ts ∗ x1[k]

24

25

26 # Plot the Simulation Results

27 t = np.arange(Tstart ,Tstop+2∗Ts,Ts)

28

29 plt.plot(t,x1, t, x2)

30 plt. title(’Simulation with 2 Variables’)

31 plt.xlabel(’t [s] ’)

32 plt.ylabel(’x’)

33 plt.grid()

34 plt.axis([−1, 1, −1.5, 1.5])

35 plt.show()

Choose the approach that fits you. You should also check the time that the

simulation take. For larger simulations, this second alternative may be better.

[End of Solution]

200

Python for Software Development



## Tables

### Table from Page 1

| Python for Software           |
| Development                   |
|:------------------------------|
| Hans-Petter Halvorsen         |
| Python Software Development   |
| Do you want to learn Software |
| Development?                  |
| OK Cancel                     |
| https://www.halvorsen.blog    |

### Table from Page 1

| Python Software Development   |
|:------------------------------|
| Do you want to learn Software |
| Development?                  |
| OK Cancel                     |

### Table from Page 2

|                                 |
|:--------------------------------|
| Python for Software Development |

### Table from Page 33

| Last login: Tue Dec 11 08:33:51 on console   |
|:---------------------------------------------|
| computername:˜ username                      |

### Table from Page 33

| Last login: Tue Dec 11 12:34:16 on ttys000                      |
|:----------------------------------------------------------------|
| Hans−Petter−Work−MacBook−Air:˜ hansha$ python                   |
| Python 3.6.5 |Anaconda, Inc.| (default , Apr 26 2018, 08:42:37) |
| [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE 401/final)] on  |
| darwin                                                          |
| Type ”help”, ”copyright”, ”credits” or ”license” for more       |
| information.                                                    |
| >>>                                                             |

### Table from Page 33

| >>> a = 5       |
|:----------------|
| >>> b = 2       |
| >>> x = 5       |
| >>> y = 3∗a + b |
| >>> y           |

### Table from Page 36

| print(”Hello”)        |
|:----------------------|
| print(”World”)        |
| print(”How are you?”) |

### Table from Page 37

| $ cd /Users/username/Downloads   |
|:---------------------------------|
| $ python helloworld.py           |

### Table from Page 37

| Hello        |
|:-------------|
| World        |
| How are you? |

### Table from Page 38

| > cd /                 |
|:-----------------------|
| > cd Temp              |
| > python helloworld.py |

### Table from Page 38

| Hello        |
|:-------------|
| World        |
| How are you? |

### Table from Page 42

| >>> x = 3   |
|:------------|
| >>> x       |
| 3           |

### Table from Page 42

| x = 3    |
|:---------|
| y = 3∗x  |
| print(y) |

### Table from Page 42

| a = 2       |
|:------------|
| b = 5       |
| x = 3       |
|             |
| y = a∗x + b |
|             |
| print(y)    |

### Table from Page 44

| x = 1 # int          |
|:---------------------|
| y = 2.8 # float      |
| z = 3 + 2j # complex |

### Table from Page 44

| print(type(x))   |
|:-----------------|
| print(type(y))   |
| print(type(z))   |

### Table from Page 44

| a = ”Hello World!”   |
|:---------------------|
|                      |
| print(a)             |
|                      |
| print(a[1])          |
| print(a[2:5])        |
| print(len(a))        |
| print(a.lower())     |

### Table from Page 45

| print(a.upper())           |
|:---------------------------|
| print(a.replace(”H”, ”J”)) |
| print(a.split(” ”))        |

### Table from Page 45

| print(”Enter your name:”)   |
|:----------------------------|
| x = input()                 |
| print(”Hello , ” + x)       |

### Table from Page 46

| from math import sin   |
|:-----------------------|
|                        |
| x = 3.14               |
| y = sin(x)             |
|                        |
| print(y)               |

### Table from Page 46

| from math import sin , cos   |
|:-----------------------------|
|                              |
| x = 3.14                     |
| y = sin(x)                   |
| print(y)                     |
|                              |
| y = cos(x)                   |
| print(y)                     |

### Table from Page 46

| from math import ∗   |
|:---------------------|
|                      |
| x = 3.14             |
| y = sin(x)           |
| print(y)             |
|                      |
| y = cos(x)           |
| print(y)             |

### Table from Page 46

| import math     |
|:----------------|
|                 |
| x = 3.14        |
| y = math.sin(x) |
|                 |
| print(y)        |

### Table from Page 47

| import math as mt   |
|:--------------------|
|                     |
| x = 3.14            |
| y = mt.sin(x)       |
|                     |
| print(y)            |

### Table from Page 48

| import numpy as np   |
|:---------------------|
|                      |
| x = 3                |
|                      |
| y = np.sin(x)        |
|                      |
| print(y)             |

### Table from Page 48

| import math as mt   |
|:--------------------|
| import numpy as np  |
|                     |
| x = 3               |
|                     |
| y = mt.sin(x)       |
|                     |
| print(y)            |
|                     |
|                     |
| y = np.sin(x)       |
|                     |
| print(y)            |

### Table from Page 48

| from math import ∗   |
|:---------------------|
| from numpy import ∗  |
|                      |
| x = 3                |
|                      |

### Table from Page 49

| y = sin(x)   |
|:-------------|
|              |
| print(y)     |
|              |
|              |
| y = sin(x)   |
|              |
| print(y)     |

### Table from Page 50

| import matplotlib.pyplot as plt     |
|:------------------------------------|
|                                     |
| x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
|                                     |
| y = [5, 2,4, 4, 8, 7, 4, 8, 10, 9]  |
|                                     |
| plt.plot(x,y)                       |
| plt.xlabel(’Time (s)’)              |
| plt.ylabel(’Temperature (degC)’)    |
| plt.show()                          |

### Table from Page 50

| from matplotlib.pyplot import ∗     |
|:------------------------------------|
|                                     |
| x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| y = [5, 2,4, 4, 8, 7, 4, 8, 10, 9]  |
|                                     |
| plot(x,y)                           |
| xlabel(’Time (s)’)                  |
| ylabel(’Temperature (degC)’)        |
| show()                              |

### Table from Page 51

| import numpy as np              |
|:--------------------------------|
| import matplotlib.pyplot as plt |
|                                 |
| x = [0, 1, 2, 3, 4, 5, 6, 7]    |
|                                 |
| y = np.sin(x)                   |
|                                 |
| plt.plot(x, y)                  |
| plt.xlabel(’x’)                 |
| plt.ylabel(’y’)                 |
| plt.show()                      |

### Table from Page 52

| import matplotlib.pyplot as plt        |
|:---------------------------------------|
| import numpy as np                     |
|                                        |
| xstart = 0                             |
| xstop = 2∗np.pi                        |
| increment = 0.1                        |
|                                        |
| x = np.arange(xstart ,xstop,increment) |
|                                        |
| y = np.sin(x)                          |
|                                        |
| plt.plot(x, y)                         |
| plt.xlabel(’x’)                        |
| plt.ylabel(’y’)                        |
| plt.show()                             |

### Table from Page 53

| import matplotlib.pyplot as plt        |
|:---------------------------------------|
| import numpy as np                     |
|                                        |
| xstart = 0                             |
| xstop = 2∗np.pi                        |
| increment = 0.1                        |
|                                        |
| x = np.arange(xstart ,xstop,increment) |
|                                        |
| y = np.sin(x)                          |
|                                        |
| z = np.cos(x)                          |
|                                        |
|                                        |
| plt.subplot(2,1,1)                     |
| plt.plot(x, y, ’g’)                    |
| plt. title(’sin ’)                     |
| plt.xlabel(’x’)                        |
| plt.ylabel(’sin(x)’)                   |
| plt.grid()                             |
| plt.show()                             |
|                                        |
|                                        |
| plt.subplot(2,1,2)                     |
| plt.plot(x, z, ’r’)                    |
| plt. title(’cos’)                      |
| plt.xlabel(’x’)                        |
| plt.ylabel(’cos(x)’)                   |
| plt.grid()                             |
| plt.show()                             |

### Table from Page 56

| a = 5                        |
|:-----------------------------|
| b = 8                        |
|                              |
| if a > b:                    |
| print(”a is greater than b”) |
|                              |
| if b > a:                    |
| print(”b is greater than a”) |
|                              |
| if a == b:                   |

### Table from Page 57

| a = 5                                             |
|:--------------------------------------------------|
| b = 8                                             |
|                                                   |
| if a > b:                                         |
| print(”a is greater than b”)                      |
| else:                                             |
| print(”b is greater than a or a and b are equal”) |

### Table from Page 57

| a = 5                        |
|:-----------------------------|
| b = 8                        |
|                              |
| if a > b:                    |
| print(”a is greater than b”) |
| elif b > a:                  |
| print(”b is greater than a”) |
| elif a == b:                 |
| print(”a is equal to b”)     |

### Table from Page 57

| data = [1.6, 3.4, 5.5, 9.4]   |
|:------------------------------|
|                               |
| N = len(data)                 |
|                               |
| print(N)                      |
|                               |
| print(data[2])                |
|                               |
| data[2] = 7.3                 |
|                               |
| print(data[2])                |

### Table from Page 58

|                   |
|:------------------|
|                   |
| for x in data:    |
| print(x)          |
|                   |
|                   |
| data.append(11.4) |
|                   |
|                   |
| N = len(data)     |
|                   |
| print(N)          |
|                   |
|                   |
| for x in data:    |
| print(x)          |

### Table from Page 58

| for x in data:   |
|:-----------------|
| print(x)         |

### Table from Page 58

| index = 2       |
|:----------------|
| x = cars[index] |

### Table from Page 59

| for i in range(1, 10):   |
|:-------------------------|
| print(i)                 |

### Table from Page 59

| data = [1.6, 3.4, 5.5, 9.4]          |
|:-------------------------------------|
|                                      |
| for x in data:                       |
| print(x)                             |
|                                      |
|                                      |
| carlist = [”Volvo”, ”Tesla”, ”Ford”] |
|                                      |
| for car in carlist:                  |
| print(car)                           |

### Table from Page 59

| N = 10             |
|:-------------------|
|                    |
| for x in range(N): |
| print(x)           |

### Table from Page 59

| start = 4                     |
|:------------------------------|
| stop= 12 #but not including   |
|                               |
| for x in range(start , stop): |
| print(x)                      |

### Table from Page 59

| start = 4                           |
|:------------------------------------|
| stop = 12 #but not including        |
| step = 2                            |
|                                     |
| for x in range(start , stop, step): |
| print(x)                            |

### Table from Page 60

| data = [1, 5, 6, 3, 12, 3]                   |
|:---------------------------------------------|
|                                              |
| sum = 0                                      |
|                                              |
| #Find the Sum of all the numbers             |
| for x in data:                               |
| sum = sum + x                                |
|                                              |
| print(sum)                                   |
|                                              |
| #Find the Mean or Average of all the numbers |
|                                              |
| N = len(data)                                |
|                                              |
| mean = sum/N                                 |
|                                              |
| print(mean)                                  |

### Table from Page 60

|   30 |
|-----:|
|    5 |

### Table from Page 61

| N = 10                |
|:----------------------|
|                       |
| fib1 = 0              |
| fib2 = 1              |
|                       |
| print(fib1)           |
| print(fib2)           |
|                       |
| for k in range(N−2):  |
| fib next = fib2 +fib1 |
| fib1 = fib2           |
| fib2 = fib next       |
| print(fib next)       |

### Table from Page 61

| N = 10                      |
|:----------------------------|
|                             |
| fib = [0, 1]                |
|                             |
|                             |
| for k in range(N−2):        |
| fib next = fib[k+1] +fib[k] |
| fib.append(fib next)        |
|                             |
| print(fib)                  |

### Table from Page 61

| N = 10             |
|:-------------------|
|                    |
| fib = []           |
|                    |
| for k in range(N): |
| fib.append(0)      |
|                    |
| fib[0] = 0         |
| fib[1] = 1         |
|                    |

### Table from Page 62

| for k in range(N−2):        |
|:----------------------------|
| fib[k+2] = fib[k+1] +fib[k] |
|                             |
|                             |
| print(fib)                  |

### Table from Page 62

| import numpy as np          |
|:----------------------------|
|                             |
|                             |
| N = 10                      |
|                             |
| fib = np.zeros(N)           |
|                             |
| fib[0] = 0                  |
| fib[1] = 1                  |
|                             |
| for k in range(N−2):        |
| fib[k+2] = fib[k+1] +fib[k] |
|                             |
|                             |
| print(fib)                  |

### Table from Page 62

| for iterating var in sequence:   |
|:---------------------------------|
| for iterating var in sequence:   |
| statements(s)                    |
| statements(s)                    |

### Table from Page 62

| for i in range(1, 10):   |
|:-------------------------|
| for k in range(1, 10):   |
| print(i , k)             |

### Table from Page 63

| m = 8        |
|:-------------|
|              |
| while m > 2: |
| print (m)    |
| m = m − 1    |

### Table from Page 66

| def FunctionName:   |
|:--------------------|
| <statement−1>       |
| .                   |
| .                   |
| <statement−N>       |
| return ...          |

### Table from Page 66

| def add(x,y):   |
|:----------------|
|                 |
| return x + y    |

### Table from Page 66

| def add(x,y):   |
|:----------------|
|                 |
| return x + y    |
|                 |
|                 |
| x = 2           |
| y = 5           |
|                 |
| z = add(x,y)    |
|                 |
| print(z)        |

### Table from Page 67

| def average(x,y):   |
|:--------------------|
|                     |
| return (x + y)/2    |

### Table from Page 67

| from myfunctions import average   |
|:----------------------------------|
|                                   |
| a = 2                             |
| b = 3                             |
|                                   |
| c = average(a,b)                  |
|                                   |
| print(c)                          |

### Table from Page 67

| def stat(x):                                 |
|:---------------------------------------------|
|                                              |
| totalsum = 0                                 |
|                                              |
| #Find the Sum of all the numbers             |
| for x in data:                               |
| totalsum = totalsum + x                      |
|                                              |
|                                              |
| #Find the Mean or Average of all the numbers |
|                                              |
| N = len(data)                                |
|                                              |
| mean = totalsum/N                            |
|                                              |
|                                              |
| return totalsum, mean                        |
|                                              |
|                                              |
|                                              |

### Table from Page 68

| data = [1, 5, 6, 3, 12, 3]   |
|:-----------------------------|
|                              |
|                              |
| totalsum, mean = stat(data)  |
|                              |
| print(totalsum, mean)        |

### Table from Page 70

| number = 4           |
|:---------------------|
| checkifprime(number) |

### Table from Page 71

| class ClassName:   |
|:-------------------|
| <statement−1>      |
| .                  |
| .                  |
| .                  |
| <statement−N>      |

### Table from Page 71

| class Car:       |
|:-----------------|
| model = ”Volvo”  |
| color = ”Blue”   |
|                  |
|                  |
| car = Car()      |
|                  |
|                  |
| print(car.model) |
| print(car.color) |

### Table from Page 71

| Volvo   |
|:--------|
| Blue    |

### Table from Page 72

| class Car:                         |
|:-----------------------------------|
| model = ””                         |
| color = ””                         |
|                                    |
| car = Car()                        |
|                                    |
| car.model = ”Volvo”                |
| car.color = ”Blue”                 |
|                                    |
| print(car.color + ” ” + car.model) |
|                                    |
| car.model = ”Ford”                 |
| car.color = ”Green”                |
|                                    |
| print(car.color + ” ” + car.model) |

### Table from Page 72

| class Car:                      |
|:--------------------------------|
| def init (self , model, color): |
| self .model = model             |
| self .color = color             |
|                                 |
| car1 = Car(”Ford”, ”Green”)     |
|                                 |
| print(car1.model)               |
| print(car1.color)               |
|                                 |
|                                 |

### Table from Page 73

| car2 = Car(”Volvo”, ”Blue”)   |
|:------------------------------|
|                               |
| print(car2.model)             |
| print(car2.color)             |

### Table from Page 73

| # Defining the Class Car        |
|:--------------------------------|
| class Car:                      |
| def init (self , model, color): |
| self .model = model             |
| self .color = color             |
|                                 |
| def displayCar(self):           |
| print(self .model)              |
| print(self .color)              |
|                                 |
|                                 |
| # Lets start using the Class    |
|                                 |
| car1 = Car(”Tesla”, ”Red”)      |
|                                 |
| car1.displayCar()               |
|                                 |
|                                 |
| car2 = Car(”Ford”, ”Green”)     |
|                                 |
| print(car2.model)               |
| print(car2.color)               |
|                                 |
|                                 |
| car3 = Car(”Volvo”, ”Blue”)     |
|                                 |
| print(car3.model)               |
| print(car3.color)               |
|                                 |
| car3.color=”Black”              |
|                                 |
| car3.displayCar()               |

### Table from Page 74

| # Defining the Class Car        |
|:--------------------------------|
| class Car:                      |
| def init (self , model, color): |
| self .model = model             |
| self .color = color             |
|                                 |
| def displayCar(self):           |
| print(self .model)              |
| print(self .color)              |

### Table from Page 74

| # Importing the Car Class    |
|:-----------------------------|
| from Car import Car          |
|                              |
| # Lets start using the Class |
|                              |
| car1 = Car(”Tesla”, ”Red”)   |
|                              |
| car1.displayCar()            |
|                              |
|                              |
| car2 = Car(”Ford”, ”Green”)  |
|                              |
| print(car2.model)            |
| print(car2.color)            |
|                              |
|                              |
| car3 = Car(”Volvo”, ”Blue”)  |
|                              |
| print(car3.model)            |
| print(car3.color)            |
|                              |
| car3.color=”Black”           |
|                              |
| car3.displayCar()            |

### Table from Page 77

| def c2f(Tc):         |
|:---------------------|
|                      |
| Tf = (Tc ∗ 9/5) + 32 |
| return Tf            |
|                      |
|                      |
| def f2c(Tf):         |
|                      |
| Tc = (Tf − 32)∗(5/9) |
| return Tc            |

### Table from Page 77

| from fahrenheit import c2f , f2c   |
|:-----------------------------------|
|                                    |
| Tc = 0                             |
|                                    |
| Tf = c2f(Tc)                       |
|                                    |
| print(”Fahrenheit: ” + str(Tf))    |
|                                    |
|                                    |
| Tf = 32                            |
|                                    |
| Tc = f2c(Tf)                       |
|                                    |
| print(”Celsius: ” + str(Tc))       |

### Table from Page 77

| Fahrenheit: 32.0   |
|:-------------------|
| Celsius: 0.0       |

### Table from Page 80

| f = open(”myfile.txt”, ”x”)   |
|:------------------------------|
|                               |
| data = ”Helo World”           |
|                               |
| f.write(data)                 |
|                               |
| f.close()                     |

### Table from Page 80

| f = open(”myfile.txt”, ”r”)   |
|:------------------------------|
|                               |
| data = f.read()               |
|                               |
| print(data)                   |
|                               |
| f.close()                     |

### Table from Page 81

| data = [1.6, 3.4, 5.5, 9.4]   |
|:------------------------------|
|                               |
| f = open(”myfile.txt”, ”x”)   |
|                               |
| for value in data:            |
| record = str(value)           |
| f.write(record)               |
| f.write(”\n”)                 |
|                               |
| f.close()                     |

### Table from Page 81

| f = open(”myfile.txt”, ”r”)       |
|:----------------------------------|
|                                   |
| for record in f:                  |
| record = record.replace(”\n”, ””) |
| print(record)                     |
|                                   |
| f.close()                         |

### Table from Page 82

| import random               |
|:----------------------------|
| for x in range(10):         |
| data = random.randint(1,31) |
| print(data)                 |

### Table from Page 84

| >>> print(Hello World)                        |
|:----------------------------------------------|
| File ”<ipython−input−1−10cb182148e3>”, line 1 |
| print(Hello World)                            |
| ˆ                                             |
| SyntaxError: invalid syntax                   |

### Table from Page 84

| >>> 10 ∗ (1/0)                                             |
|:-----------------------------------------------------------|
| Traceback (most recent call last):                         |
|                                                            |
| File ”<ipython−input−2−0b280f36835c>”, line 1, in <module> |
| 10 ∗ (1/0)                                                 |
|                                                            |
| ZeroDivisionError: division by zero                        |

### Table from Page 84

| >>> ’2’ + 2                        |
|:-----------------------------------|
| Traceback (most recent call last): |
|                                    |

### Table from Page 85

| File ”<ipython−input−3−d2b23a1db757>”, line 1, in <module>   |
|:-------------------------------------------------------------|
| ’2’ + 2                                                      |
|                                                              |
| TypeError: must be str , not int                             |

### Table from Page 85

| try:                            |
|:--------------------------------|
| 10 ∗ (1/0)                      |
| except:                         |
| print(”The calculation failed”) |

### Table from Page 85

| try:                      |
|:--------------------------|
| print(x)                  |
| except:                   |
| print(”x is not defined”) |

### Table from Page 85

| try:                        |
|:----------------------------|
| print(x)                    |
| except NameError:           |
| print(”x is not defined”)   |
| except:                     |
| print(”Something is wrong”) |

### Table from Page 86

| x=2                              |
|:---------------------------------|
|                                  |
| try:                             |
| print(x)                         |
| except NameError:                |
| print(”x is not defined”)        |
| except:                          |
| print(”Something is wrong”)      |
| finally:                         |
| print(”The Program is finished”) |

### Table from Page 86

| try:                                                   |
|:-------------------------------------------------------|
| f = open(”myfile.txt”)                                 |
| f.write(”Lorum Ipsum”)                                 |
| except:                                                |
| print(”Something went wrong when writing to the file”) |
| finally:                                               |
| f.close()                                              |

### Table from Page 107

| >>> b = 5       |
|:----------------|
| >>> x = 3       |
| >>> y = a∗x + b |
| >>> y           |

### Table from Page 108

| import matplotlib.pyplot as plt        |
|:---------------------------------------|
| import numpy as np                     |
|                                        |
| xstart = 0                             |
| xstop = 2∗np.pi                        |
| increment = 0.1                        |
|                                        |
| x = np.arange(xstart ,xstop,increment) |
|                                        |
| y = np.sin(x)                          |
|                                        |
| plt.plot(x, y)                         |
| plt. title(’y=sin(x)’)                 |

### Table from Page 109

| plt.xlabel(’x’)               |
|:------------------------------|
| plt.ylabel(’y’)               |
| plt.grid()                    |
| plt.axis([0, 2∗np.pi, −1, 1]) |
| plt.show()                    |

### Table from Page 121

| import numpy as np              |
|:--------------------------------|
| import matplotlib.pyplot as plt |
|                                 |
| plt.axis([0, 10, 0, 1])         |
|                                 |
| delay = 1 #Seconds              |
|                                 |
| for i in range(10):             |
| y = np.random.random()          |
| plt.scatter(i , y)              |
| plt.pause(delay)                |

### Table from Page 122

|            |
|:-----------|
| plt.show() |

### Table from Page 123

| ani = animation.FuncAnimation(fig , animate, fargs=(xs, ys),   |
|:---------------------------------------------------------------|
| interval=1000)                                                 |

### Table from Page 124

| import datetime as dt                                        |
|:-------------------------------------------------------------|
| import numpy as np                                           |
| import matplotlib.pyplot as plt                              |
| import matplotlib.animation as animation                     |
|                                                              |
| # Create figure for plotting                                 |
| fig = plt.figure()                                           |
| ax = fig.add subplot(1, 1, 1)                                |
| xs = []                                                      |
| ys = []                                                      |
|                                                              |
|                                                              |
| # This function is called periodically from FuncAnimation    |
| def animate(i , xs, ys):                                     |
|                                                              |
| temp c = round(np.random.random() , 2)                       |
|                                                              |
| # Add x and y to lists                                       |
| xs.append(dt.datetime.now().strftime(’%H:%M:%S.%f ’))        |
| ys.append(temp c)                                            |
|                                                              |
| # Limit x and y lists to 20 items                            |
| xs = xs[−20:]                                                |
| ys = ys[−20:]                                                |
|                                                              |
| # Draw x and y lists                                         |
| ax.clear()                                                   |
| ax.plot(xs, ys)                                              |
|                                                              |
| # Format plot                                                |
| plt.xticks(rotation=45, ha=’right ’)                         |
| plt.subplots adjust(bottom=0.30)                             |
| plt. title(’Temperature Data’)                               |
| plt.ylabel(’Temperature (deg C)’)                            |
|                                                              |
| # Set up plot to call animate() function periodically        |
| ani = animation.FuncAnimation(fig , animate, fargs=(xs, ys), |
| interval=1000)                                               |
| plt.show()                                                   |

### Table from Page 125

| import numpy as np                                        |
|:----------------------------------------------------------|
| import matplotlib.pyplot as plt                           |
| import matplotlib.animation as animation                  |
|                                                           |
| # Parameters                                              |
| x len = 200 # Number of points to display                 |
| y range = [0, 20] # Range of possible Y values to display |
|                                                           |

### Table from Page 126

| # Create figure for plotting                              |
|:----------------------------------------------------------|
| fig = plt.figure()                                        |
| ax = fig.add subplot(1, 1, 1)                             |
| xs = list(range(0, 200))                                  |
| ys = [0] ∗ x len                                          |
| ax.set ylim(y range)                                      |
|                                                           |
|                                                           |
| # Create a blank line. We will update the line in animate |
| line , = ax.plot(xs, ys)                                  |
|                                                           |
| # Add labels                                              |
| plt. title(’Temperature Data’)                            |
| plt.xlabel(’Samples’)                                     |
| plt.ylabel(’Temperature (deg C)’)                         |
|                                                           |
| # This function is called periodically from FuncAnimation |
| def animate(i , ys):                                      |
|                                                           |
| rand val = np.random.random()∗20 #Generate Random Values  |
| between 0 and 20                                          |
|                                                           |
| temp c = round(rand val , 2)                              |
|                                                           |
| #print (temp c)                                           |
|                                                           |
| # Add y to list                                           |
| ys.append(temp c)                                         |
|                                                           |
| # Limit y list to set number of items                     |
| ys = ys[−x len:]                                          |
|                                                           |
| # Update line with new Y values                           |
| line.set ydata(ys)                                        |
|                                                           |
| return line ,                                             |
|                                                           |
| # Set up plot to call animate() function periodically     |
| ani = animation.FuncAnimation(fig ,                       |
| animate,                                                  |
| fargs=(ys,) ,                                             |
| interval=100,                                             |
| blit=True)                                                |
| plt.show()                                                |

### Table from Page 132

| import nidaqmx                                              |
|:------------------------------------------------------------|
|                                                             |
| with nidaqmx.Task() as task:                                |
| task.ao channels.add ao voltage chan(’Dev1/ao0’,’mychannel’ |
| ,0,5)                                                       |
|                                                             |
| value = 3                                                   |
| task.start                                                  |
| task.write(value)                                           |
| task.stop                                                   |

### Table from Page 133

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.ai channels.add ai voltage chan(”Dev1/ai1”) |
|                                                  |
| value = task.read()                              |
| print(value)                                     |
| task.stop                                        |

### Table from Page 133

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| from nidaqmx.constants import (                  |
| TerminalConfiguration)                           |
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.ai channels.add ai voltage chan(”Dev1/ai0”, |
| terminal config=TerminalConfiguration.RSE)       |
|                                                  |
| value = task.read()                              |
| print(value)                                     |
| task.stop                                        |

### Table from Page 133

| import nidaqmx                                      |
|:----------------------------------------------------|
|                                                     |
| from nidaqmx.constants import (                     |
| TerminalConfiguration)                              |
|                                                     |
| with nidaqmx.Task() as task:                        |
| task.ai channels.add ai voltage chan(”Dev1/ai0”,    |
| terminal config=TerminalConfiguration.DIFFERENTIAL) |
|                                                     |
| value = task.read()                                 |
| print(value)                                        |
| task.stop                                           |

### Table from Page 134

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.do channels.add do chan(”Dev1/port0/line0”) |
|                                                  |
| value = True                                     |
| task.start                                       |
| task.write(value)                                |
| task.stop                                        |

### Table from Page 134

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.di channels.add di chan(”Dev1/port0/line0”) |
|                                                  |
| task.start                                       |
| value = task.read()                              |
| print(value)                                     |
| task.stop                                        |

### Table from Page 135

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.do channels.add do chan(”Dev1/port0/line0”) |
|                                                  |
| value = True                                     |
| task.start                                       |
| task.write(value)                                |
| task.stop                                        |

### Table from Page 136

| import nidaqmx                                   |
|:-------------------------------------------------|
| import time                                      |
|                                                  |
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.do channels.add do chan(”Dev1/port0/line0”) |
|                                                  |
| value = True                                     |
| task.start                                       |
|                                                  |
| i = 1                                            |
| while i < 10:                                    |
|                                                  |

### Table from Page 137

| task.write(value)   |
|:--------------------|
| time.sleep(1)       |
| value = not value   |
| task.write(value)   |
| i = i+1             |
|                     |
| task.stop           |

### Table from Page 139

| import nidaqmx                                   |
|:-------------------------------------------------|
| import time                                      |
|                                                  |
| from nidaqmx.constants import (                  |
| TerminalConfiguration)                           |
|                                                  |
|                                                  |
| with nidaqmx.Task() as task:                     |
| task.ai channels.add ai voltage chan(”Dev1/ai0”, |
| terminal config=TerminalConfiguration.RSE)       |
|                                                  |
| i = 0                                            |
| while i < 10:                                    |
|                                                  |
| voltage = task.read()                            |
|                                                  |
| degreesC = 100∗voltage − 50                      |
|                                                  |
| print(”Sample:”, i)                              |
| print(”Voltage Value:”, round(voltage ,2))       |
| print(”Celsius Value:”, round(degreesC,1))       |
| print(”\n”)                                      |
| time.sleep(1)                                    |
| i = i+1                                          |
|                                                  |
| task.stop                                        |

### Table from Page 140

| import nidaqmx                                                    |
|:------------------------------------------------------------------|
| import time                                                       |
| import datetime as dt                                             |
| import numpy as np                                                |
| import matplotlib.pyplot as plt                                   |
| import matplotlib.animation as animation                          |
|                                                                   |
| from nidaqmx.constants import (                                   |
| TerminalConfiguration)                                            |
|                                                                   |
|                                                                   |
| # Create figure for plotting                                      |
| fig = plt.figure()                                                |
| ax = fig.add subplot(1, 1, 1)                                     |
| xs = []                                                           |
| ys = []                                                           |
|                                                                   |
| # Initialize DAQ device                                           |
| task = nidaqmx.Task()                                             |
| task.ai channels.add ai voltage chan(”Dev1/ai0”, terminal config= |
| TerminalConfiguration.RSE)                                        |

### Table from Page 141

| task.start                                                   |
|:-------------------------------------------------------------|
|                                                              |
|                                                              |
| # This function is called periodically from FuncAnimation    |
| def readdaq(i , xs, ys):                                     |
|                                                              |
| #Read Value from DAQ device                                  |
| voltage = task.read()                                        |
|                                                              |
| #Convert Voltage to degrees Celsius                          |
| degreesC = 100∗voltage − 50                                  |
| temp c = round(degreesC, 1)                                  |
| print(”Celsius Value:”, temp c)                              |
|                                                              |
| # Add x and y to lists                                       |
| xs.append(dt.datetime.now().strftime(’%H:%M:%S.%f ’))        |
| ys.append(temp c)                                            |
|                                                              |
| # Limit x and y lists to 20 items                            |
| xs = xs[−20:]                                                |
| ys = ys[−20:]                                                |
|                                                              |
| # Draw x and y lists                                         |
| ax.clear()                                                   |
| ax.plot(xs, ys)                                              |
|                                                              |
| # Format plot                                                |
| plt.xticks(rotation=45, ha=’right ’)                         |
| plt.subplots adjust(bottom=0.30)                             |
| plt. title(’Temperature Data’)                               |
| plt.ylabel(’Temperature (deg C)’)                            |
|                                                              |
|                                                              |
| # Set up plot to call readdaq() function periodically        |
| ani = animation.FuncAnimation(fig , readdaq, fargs=(xs, ys), |
| interval=1000)                                               |
| plt.show()                                                   |
| task.stop                                                    |

### Table from Page 144

| import nidaqmx                                           |
|:---------------------------------------------------------|
| import numpy as np                                       |
| import time                                              |
|                                                          |
| from nidaqmx.constants import (                          |
| TerminalConfiguration)                                   |
|                                                          |
|                                                          |
| Vin = 5                                                  |
| Ro = 10000 # %10k Resistor                               |
|                                                          |
|                                                          |
| with nidaqmx.Task() as task:                             |
| task.ai channels.add ai voltage chan(”Dev1/ai0”,         |
| terminal config=TerminalConfiguration.RSE)               |
|                                                          |
| i = 0                                                    |
| while i < 10:                                            |
|                                                          |
| Vout = task.read()                                       |
|                                                          |
| Rt = (Vout∗Ro)/(Vin−Vout) # Voltage Divider Equation     |
| # Rt=10000; Used for Testing. Setting Rt=10k should give |
| TempC=25                                                 |
|                                                          |

### Table from Page 145

| # Steinhart constants                                        |
|:-------------------------------------------------------------|
| A = 0.001129148                                              |
| B = 0.000234125                                              |
| C = 0.0000000876741                                          |
|                                                              |
| # Steinhart−Hart Equation                                    |
| TempK = 1 / (A + (B ∗ np.log(Rt)) + (C ∗ pow(np.log(Rt) ,3)) |
| )                                                            |
|                                                              |
| # Convert from Kelvin to Celsius                             |
| TempC = TempK − 273.15                                       |
|                                                              |
| print(”Sample:”, i)                                          |
| print(”Voltage Value:”, round(Vout,2))                       |
| print(”Celsius Value:”, round(TempC,1))                      |
| print(”\n”)                                                  |
| time.sleep(1)                                                |
| i = i+1                                                      |
|                                                              |
| task.stop                                                    |

### Table from Page 146

| import nidaqmx                                   |
|:-------------------------------------------------|
|                                                  |
| task = nidaqmx.Task()                            |
|                                                  |
| task.ai channels.add ai thrmcpl chan(”TC01/ai0”) |
|                                                  |
| task.start()                                     |
|                                                  |
| value = task.read()                              |
| print(round(value ,1))                           |
|                                                  |
| task.stop()                                      |
| task.close()                                     |

### Table from Page 152

| import pyodbc                                                  |
|:---------------------------------------------------------------|
|                                                                |
| server = ”NUCHPH\\SQLEXPRESS”                                  |
| database = ”BOOKS”                                             |
| username = ”sa”                                                |
| password = ”xxx”                                               |
| conn = pyodbc.connect(”DRIVER={ODBC Driver 17 for SQL Server}; |
| SERVER=” + server + ”;DATABASE=” + database + ”;UID=” +        |
| username + ”;PWD=” + password )                                |
|                                                                |
| cursor = conn.cursor()                                         |
|                                                                |
| cursor.execute(”SELECT @@version;”)                            |
| row = cursor.fetchone()                                        |
| while row:                                                     |
| print(row[0])                                                  |
| row = cursor.fetchone()                                        |

### Table from Page 152

| import pyodbc                                                  |
|:---------------------------------------------------------------|
|                                                                |
| server = ”NUCHPH\\SQLEXPRESS”                                  |
| database = ”BOOKS”                                             |
| username = ”sa”                                                |
| password = ”xxx”                                               |
| conn = pyodbc.connect(”DRIVER={ODBC Driver 17 for SQL Server}; |
| SERVER=” + server + ”;DATABASE=” + database + ”;UID=” +        |
| username + ”;PWD=” + password )                                |
|                                                                |

### Table from Page 153

| cursor = conn.cursor()                                              |
|:--------------------------------------------------------------------|
|                                                                     |
|                                                                     |
| for row in cursor.execute(”select BookId, Title , Isbn from BOOK”): |
| print(row.BookId, row.Title , row.Isbn)                             |

### Table from Page 166

| def c2f(Tc):   |
|:---------------|
|                |

### Table from Page 167

| Tf = (Tc ∗ 9/5) + 32   |
|:-----------------------|
| return Tf              |
|                        |
|                        |
| def f2c(Tf):           |
|                        |
| Tc = (Tf − 32)∗(5/9)   |
| return Tc              |

### Table from Page 167

| from fahrenheit import c2f , f2c   |
|:-----------------------------------|
|                                    |
| Tc = 0                             |
|                                    |
| Tf = c2f(Tc)                       |
|                                    |
| print(”Fahrenheit: ” + str(Tf))    |
|                                    |
|                                    |
| Tf = 32                            |
|                                    |
| Tc = f2c(Tf)                       |
|                                    |
| print(”Celsius: ” + str(Tc))       |

### Table from Page 167

| Fahrenheit: 32.0   |
|:-------------------|
| Celsius: 0.0       |

### Table from Page 179

| import sys                                        |
|:--------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget |
| if name == ” main ”:                              |
| application = QApplication(sys.argv)              |
| window = QWidget()                                |
| window.resize(300,200)                            |
| window.setWindowTitle(”Hello World”)              |
| window.show()                                     |
| sys.exit(application.exec ())                     |

### Table from Page 182

| import sys                                                |
|:----------------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget, QLabel |
| if name == ” main ”:                                      |
| application = QApplication(sys.argv)                      |
| window = QWidget()                                        |
| window.resize(300,200)                                    |
| window.setWindowTitle(”Hello World”)                      |
|                                                           |
| label = QLabel(window)                                    |
| label.setText(”This is a Label”)                          |
| label.move(100,50)                                        |
|                                                           |
| window.show()                                             |
| sys.exit(application.exec ())                             |

### Table from Page 182

| import sys                                                   |
|:-------------------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit |
| if name == ” main ”:                                         |
| application = QApplication(sys.argv)                         |
| window = QWidget()                                           |
| window.resize(300,200)                                       |
| window.setWindowTitle(”Hello World”)                         |
|                                                              |
| inputbox = QLineEdit(window)                                 |
| inputbox.setText(”Please enter your Name”)                   |

### Table from Page 183

| inputbox.resize(200, 20)      |
|:------------------------------|
| inputbox.move(20,50)          |
|                               |
| window.show()                 |
| sys.exit(application.exec ()) |

### Table from Page 183

| import sys                                                   |
|:-------------------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget, QComboBox |
| if name == ” main ”:                                         |
| application = QApplication(sys.argv)                         |
| window = QWidget()                                           |
| window.resize(300,200)                                       |
| window.setWindowTitle(”Hello World”)                         |
|                                                              |
| combobox = QComboBox(window)                                 |
| combobox.addItems([”item one”, ”item two”, ”item three”])    |
| combobox.move(100,50)                                        |
|                                                              |
| window.show()                                                |
| sys.exit(application.exec ())                                |

### Table from Page 184

| def btnShowData clicked(self):   |
|:---------------------------------|
| temp = np.random.randint(20,50)  |
| self .txtTemp.setText(str(temp)) |

### Table from Page 185

| import sys                                                     |
|:---------------------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget, QPushButton |
|                                                                |
| def button clicked():                                          |
| print(”You clicked the Button”)                                |
|                                                                |
| if name == ” main ”:                                           |
| application = QApplication(sys.argv)                           |
| application.setStyle(’Fusion’)                                 |
| window = QWidget()                                             |
| window.resize(300,200)                                         |
| window.setWindowTitle(”Hello World”)                           |
|                                                                |
| button = QPushButton(window)                                   |
| button.setText(”Click Me”)                                     |
| button.move(100,50)                                            |
| button.clicked.connect(button clicked)                         |
|                                                                |
| window.show()                                                  |
| sys.exit(application.exec ())                                  |

### Table from Page 185

| import sys                                                      |
|:----------------------------------------------------------------|
| from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, |
| QMessageBox                                                     |
|                                                                 |
| def button clicked():                                           |
| messagebox = QMessageBox()                                      |
| messagebox.setText(’You clicked the button! ’)                  |
| messagebox.exec ()                                              |
|                                                                 |
| if name == ” main ”:                                            |
| application = QApplication(sys.argv)                            |
| application.setStyle(’Fusion’)                                  |
| window = QWidget()                                              |
| window.resize(300,200)                                          |
| window.setWindowTitle(”Hello World”)                            |
|                                                                 |
| button = QPushButton(window)                                    |
| button.setText(”Click Me”)                                      |
| button.move(100,50)                                             |
| button.clicked.connect(button clicked)                          |
|                                                                 |
| window.show()                                                   |
| sys.exit(application.exec ())                                   |

### Table from Page 186

| import sys                                                      |
|:----------------------------------------------------------------|
| import numpy as np                                              |
| from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, |
| QLineEdit, QMessageBox                                          |
|                                                                 |
| class Application(QWidget):                                     |
|                                                                 |
| def init (self):                                                |
| super(). init ()                                                |
| self .initUI()                                                  |
|                                                                 |
| def initUI(self):                                               |
| self .setWindowTitle(”PyQt Example”)                            |
| self .resize(400, 300)                                          |
|                                                                 |
|                                                                 |
| self .txtName = QLineEdit(self)                                 |
| self .txtName.setText(”Please enter your Name”)                 |
| self .txtName.move(20, 20)                                      |
| self .txtName.resize(200, 20)                                   |
|                                                                 |
| self .btnShowName = QPushButton(”Show Name”, self)              |
| self .btnShowName.move(15,60)                                   |
| self .btnShowName.clicked.connect(self .btnShowName clicked)    |
|                                                                 |
| self .show()                                                    |
|                                                                 |
|                                                                 |
| def btnShowName clicked(self):                                  |
| self .showMessage()                                             |
|                                                                 |
| def showMessage(self):                                          |

### Table from Page 187

|                                                       |
|:------------------------------------------------------|
| name = self .txtName.text()                           |
| text = ”Is your Name ” + name + ”?”                   |
| reply = QMessageBox.question(self , ’Message’, text , |
| QMessageBox.Yes | QMessageBox.No, QMessageBox.No)     |
|                                                       |
| if reply == QMessageBox.No:                           |
| self .txtName.setText(”Please enter your Name”)       |
|                                                       |
|                                                       |
| if name == ’ main ’:                                  |
| app = QApplication(sys.argv)                          |
| app.setStyle(’Fusion’)                                |
| window = Application()                                |
| sys.exit(app.exec ())                                 |

### Table from Page 188

| ...   |
|:------|
| ...   |

### Table from Page 188

| ...   |
|:------|
| ...   |

### Table from Page 188

| ...   |
|:------|
| ...   |

### Table from Page 195

| import math as mt               |
|:--------------------------------|
| import numpy as np              |
| import matplotlib.pyplot as plt |
|                                 |
|                                 |
| # Model Parameters              |
| T = 5                           |
| a = −1/T                        |
|                                 |
| # Simulation Parameters         |
| x0 = 1                          |
| t = 0                           |
|                                 |
| tstart = 0                      |

### Table from Page 196

| tstop = 25                                 |
|:-------------------------------------------|
|                                            |
| increment = 1                              |
|                                            |
| x = []                                     |
| x = np.zeros(tstop+1)                      |
|                                            |
| t = np.arange(tstart ,tstop+1,increment)   |
|                                            |
|                                            |
| # Define the Function                      |
| for k in range(tstop):                     |
| x[k] = mt.exp(a∗t[k]) ∗ x0                 |
|                                            |
|                                            |
| # Plot the Simulation Results              |
| plt.plot(t,x)                              |
| plt. title(’Simulation of Dynamic System’) |
| plt.xlabel(’t’)                            |
| plt.ylabel(’x’)                            |
| plt.grid()                                 |
| plt.axis([0, 25, 0, 1])                    |
| plt.show()                                 |

### Table from Page 197

| import math as mt                                     |
|:------------------------------------------------------|
|                                                       |
| def calcexpression(x,y):                              |
|                                                       |
| z = 3∗x∗∗2 + mt.sqrt(x∗∗2 + y∗∗2) + mt.exp(mt.log(x)) |
| return z                                              |

### Table from Page 197

| import mymathfunctions as mymath   |
|:-----------------------------------|
|                                    |
| x = 2                              |
| y = 2                              |
|                                    |
| z = mymath.calcexpression(x,y)     |
|                                    |
| print(z)                           |

### Table from Page 200

| # Simulation of Bacteria Population             |
|:------------------------------------------------|
| import numpy as np                              |
| import matplotlib.pyplot as plt                 |
|                                                 |
| # Model Parameters                              |
| b = 1                                           |
| p = 0.5                                         |
|                                                 |
| # Simulation Parameters                         |
| Ts = 0.01                                       |
| Tstop = 1                                       |
| xk = 100                                        |
| N = int(Tstop/Ts) # Simulation length           |
| data = []                                       |
| data.append(xk)                                 |
|                                                 |
|                                                 |
| # Simulation                                    |
| for k in range(N):                              |
| xk1 = xk + Ts∗ (b ∗ xk − p ∗ xk∗∗2);            |
| xk = xk1                                        |
| data.append(xk1)                                |
|                                                 |
| # Plot the Simulation Results                   |
| t = np.arange(0,Tstop+Ts,Ts)                    |
|                                                 |
| plt.plot(t,data)                                |
| plt. title(’Simulation of Bacteria Population’) |
| plt.xlabel(’t [s] ’)                            |
| plt.ylabel(’x’)                                 |
| plt.grid()                                      |
| plt.axis([0, 1, 0, 100])                        |
| plt.show()                                      |

### Table from Page 201

| # Simulation with 2 Variables                  |
|:-----------------------------------------------|
| import numpy as np                             |
| import matplotlib.pyplot as plt                |
|                                                |
| # Model Parameters                             |
| b = 1                                          |
| p = 0.5                                        |
|                                                |
| # Simulation Parameters                        |
| Ts = 0.1                                       |
| Tstart = −1                                    |
| Tstop = 1                                      |
| x1k = 1                                        |
| x2k = 1                                        |
| N = int((Tstop−Tstart)/Ts) # Simulation length |
| datax1 = []                                    |

### Table from Page 202

| datax2 = []                               |
|:------------------------------------------|
| datax1.append(x1k)                        |
| datax2.append(x2k)                        |
|                                           |
|                                           |
| # Simulation                              |
| for k in range(N):                        |
| x1k1 = x1k − Ts ∗ x2k                     |
| x2k1 = x2k + Ts ∗ x1k                     |
|                                           |
| x1k = x1k1                                |
| x2k = x2k1                                |
| datax1.append(x1k1)                       |
| datax2.append(x2k1)                       |
|                                           |
| # Plot the Simulation Results             |
| t = np.arange(Tstart ,Tstop+Ts,Ts)        |
|                                           |
| plt.plot(t,datax1, t, datax2)             |
| plt. title(’Simulation with 2 Variables’) |
| plt.xlabel(’t [s] ’)                      |
| plt.ylabel(’x’)                           |
| plt.grid()                                |
| plt.axis([−1, 1, −1.5, 1.5])              |
| plt.show()                                |

### Table from Page 202

| # Simulation with 2 Variables   |
|:--------------------------------|
| import numpy as np              |
| import matplotlib.pyplot as plt |
|                                 |
| # Model Parameters              |

### Table from Page 203

| b = 1                                          |
|:-----------------------------------------------|
| p = 0.5                                        |
|                                                |
| # Simulation Parameters                        |
| Ts = 0.1                                       |
| Tstart = −1                                    |
| Tstop = 1                                      |
| N = int((Tstop−Tstart)/Ts) # Simulation length |
| x1 = np.zeros(N+2)                             |
| x2 = np.zeros(N+2)                             |
| x1[0] = 1                                      |
| x2[0] = 1                                      |
|                                                |
|                                                |
| # Simulation                                   |
| for k in range(N+1):                           |
| x1[k+1] = x1[k] − Ts ∗ x2[k]                   |
| x2[k+1] = x2[k] + Ts ∗ x1[k]                   |
|                                                |
|                                                |
| # Plot the Simulation Results                  |
| t = np.arange(Tstart ,Tstop+2∗Ts,Ts)           |
|                                                |
| plt.plot(t,x1, t, x2)                          |
| plt. title(’Simulation with 2 Variables’)      |
| plt.xlabel(’t [s] ’)                           |
| plt.ylabel(’x’)                                |
| plt.grid()                                     |
| plt.axis([−1, 1, −1.5, 1.5])                   |
| plt.show()                                     |

### Table from Page 204

|                                 |
|:--------------------------------|
| Python for Software Development |

