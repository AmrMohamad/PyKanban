# PyKanban

<p align="center">
    <img src="./docs/pykanban-logo.png"
         alt="PyKanban-logo"
         width="195px"
         style="display: block; margin: 0 auto"/><br>
         Easy way to create kanban table in terminal
</p>

___

## Table of Contents

- [Description](#description)
- [Motivation](#motivation)
- [Features](#features)
- [How to use](#how-to-use)
  - [Installation](#installation)
  - [Usage](#usage)
- [Fundamentals and Technologies are used]()
  - [Fundamentals]()
  - [Technologies]()
- [Code]()

___

## Description

PyKanban is a terminal application for creating a simple kanban board or any table for any purpose uses cards in an awesome terminal view
<p align="center">
    <img src="./docs/program-intro.png"
         alt="PyKanban-Program-Intro"
         width="90%"
         style="display: block; margin: 0 auto"/>
</p>

___

## Motivation

First, as is common among developers, it's awesome for using terminal applications. And I found all applications that help us for creating tables for organizing our tasks use GUI. So, I found it will be great if I try to develop a simple application that uses a terminal. Second, it's my final project for <a href="https://cs50.harvard.edu/python/2022/">CS50’s Introduction to Programming with Python</a>

___

## Features

- Allow you to create a table with customized headers by coloring text and text backgrounds in the terminal.

  <p align="center">
    <img src="./docs/header-table.png"
         alt="PyKanban-Program-Intro"
         width="70%"
         style="display: block; margin: 0 auto"/>
  </p>

- Create Cards in a terminal. (the best feature)

  <p align="center">
      <img src="./docs/card-image.png"
          alt="PyKanban-Program-Intro"
          width="60%"
          style="display: block; margin: 0 auto"/>
  </p>

- Easy move a card and put it on any column of the table

- Add a card or delete it after creating the table

- Viewing the history of edited table

___

## How to use

### Installation

#### Step 1

```terminal
git clone https://github.com/AmrMohamad/PyKanban.git
```

#### Step 2

```terminal
python3 -m venv <type-virtual-environment-name-you-want>
```

#### Step 3

  To activate virtual environment

```terminal
source env/bin/activate
```

#### Step 4

The following command will install the packages according to the configuration file <code>requirements.txt</code>

```terminal
pip install -r requirements.txt
```

#### Step 5

To Run PyKanban

```terminal
python3 pykanban.py
```

Or press Run button in VS Code

![run-button-vscode](./docs/run-button-vscode.png)

### Usage

After running, the first screen that appears is :

<p align="center">
    <img src="./docs/program-intro.png"
         alt="PyKanban-Program-Intro"
         width="90%"
         style="display: block; margin: 0 auto"/>
</p>

we have here 3 options: View Tables, Create Table, Exit

Enter the option number

#### For View Tables

If you have created a table before, a list of saved tables will appear

<img src="./docs/view-tables.png" width="50%" alt="list-of-tables">

explaining the 'Create Table' and turn back to ['View Tables'](#back-to-view-tables-option)

#### For Create Table

It will ask you for the name of the new table to create a new folder in <code>./pykanban/data/</code> folder containing all new table data and the table be saved in a CSV file like this <code>latest.csv</code>.<br> After that, it starts asking you for the details of the table

Input:

```terminal
Number of stages => 4
```

It will ask about the Name of each stage or header and their colors. When come to choosing the colors they must be in Hex values like that:

<img src="./docs/naming-stage.png" width="50%" alt="naming-stage">

If you enter color values correctly, it continues in the same way until the last (4th) stage because we the enter <code> Number of stages => 4 </code>

<img src="./docs/set-columns.png" width="42%" alt="set-columns">

But, If you enter a hex value in the wrong way, it will ask you again about the values of the stage like that:

<img src="./docs/hex-value-error.png" width="50%" alt="hex-value-error">

After setting the headers/columns/stages name of the table, you can add cards to Stages by asking about the number of cards per stage

<img src="./docs/ask-about-num-of-cards.png" width="50%" alt="ask-about-num-of-cards">

Input:

```terminal
How many cards do you want? 2
```

And depending on how many cards you choose to add, it will start asking you about each card's details like that:

```terminal
For 1st Card                    <====== First card start here
Enter the Title of Card, It's one title only !
==> Task 1
How many sub-titles do you want to add ? => 2
Enter the name of each sub-title
>>> Description
>>> Comment
Enter the content of each sub-title, The maximum is 244 characters per paragraph !
Do not hit enter for new line,
We handle it automatically
For Description :
>>> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Do not hit enter for new line,
We handle it automatically
For Comment :
>>> It should be ended on 7 Dec 2022         <====== First card end here
For 2nd Card                    <====== Second card start here
Enter the Title of Card, It's one title only !
==> 
```

And so on, the same way with the second card.

After you finished 1st Stage, it will ask about other stages, and it's up to you, you can add cards now or later

<img src="./docs/set-0-for-stages.png" width="50%" alt="set-0-for-stages">

The Final result:

<p align="center"><img src="./docs/table-in-terminal.png" width="85%" alt="table-in-terminal"></p>

⚠️ The Colors of the header showing/rendering in the terminal depend on the type of terminal ⚠️

In VS Code terminal (depending on your settings)

<p align="center"><img src="./docs/table-in-terminal.png" width="95%" alt="table-in-terminal"></p>

In macOS terminal

<p align="center"><img src="./docs/macOS-terminal.png" width="100%" alt="table-in-macOS-terminal"></p>

The limitations are:

- The limited Number per Table of Stages is:

  - The Maximum Stages is 5
  - The Minimum Stages is 2

- No limit to Cards to Stage

- Sub-titles per card:

  - At least 1 sub-title
  - the maximum is 5 sub-titles

- the content of each sub-title is limited to 244 characters

Now you have created a Kanban board in the terminal with PyKanban 😄

#### For Exit

It takes 5 seconds to exit from PyKanban to make sure everything its saved

<img src="./docs/count-to-exit.png" width="50%" alt="count-to-exit">

#### Back to View Tables option

<img src="./docs/demo-in-view-table-list.png" width="50%" alt="demo-in-view-table-list">

now after backing to main screen of PyKanban and choosing View Tables we can see <code>1: Dome</code> table

Enter the number of table in list. for example,

Input:

```terminal
Enter Number of Table to Open: 1
```

Now we can re-open the table that we created before

<p align="center"><img src="./docs/demo-table-with-options.png" width="95%" alt="demo-table-with-options"></p>

and as we can see there is options:

<p align="center"><img src="./docs/view-table-options.png" width="100%" alt="view-table-options"></p>

- [Add a Card](#add-a-card)
- [Move a Card](#move-a-card)
- [Delete a Card](#delete-a-card)
- [View History](#view-history)
- [Back to Main Screen](#back-to-main-screen)

##### Add a Card

##### Move a Card

##### Delete a Card

##### View History

##### Back to Main Screen
