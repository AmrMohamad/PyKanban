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

- Allow you create a table with customized headers by coloring text and text background in the terminal.

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

- Easy move a card and put on any column of the table

- Add a card or delete it after creating the table

- Viewing the history of edited table

___

## How to use

### Installation

#### Step 1

```bash
git clone https://github.com/AmrMohamad/PyKanban.git
```

#### Step 2

```bash
python3 -m venv <type-virtual-environment-name-you-want>
```

#### Step 3

  To activate virtual environment

```bash
source env/bin/activate
```

#### Step 4

The following command will install the packages according to the configuration file <code>requirements.txt</code>

```bash
pip install -r requirements.txt
```

#### Step 5

To Run PyKanban

```bash
python3 pykanban.py
```

Or press Run button in VS Code

![run-button-vscode](./docs/run-button-vscode.png)

### Usage

After running , the first screen appear is :

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

#### For Create Table

It will ask you the name of new table to create a new folder in <code>./pykanban/data/</code> folder contains all new table data and the table be saved in csv file like this <code>latest.csv</code>.<br> After that, it starts asking you for the details of the table
