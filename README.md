# Assignment 6 (Flask)

In this assignment, you will be focusing on the server-side logic (backend) where you will be tasked to implement the logic of a `Tip Calculator`. The client-side (frontend) has been implemented for you. All you need to do is to do calculation in the server-side.

## Setting Up

### Cloning Repository

To clone this repository, you could refer to the command below. Make sure you are in the right directory that you wanted it to be.

```
git clone https://github.com/projectxgen/assignment-6.git
```

### Virtual Environment

After cloning, you will need to set up virtual environment (if you want to, but it is a good practice). To set up virtual environment, make sure you have `virtualenv` installed in your local machine.

To set up virtual environment, make sure you are in the right directory as the repository that you just cloned, then type the command below.

```
virtualenv env
```

After running the command, you will see a folder named `env` is generated for you. To use the virtual environment, you will need to activate it with this command:

- For windows:
  
```
.\<name of virtual environment folder>\Scripts\activate
```

- For macbook:

```
source env/bin/activate
```

After successfully activating the `virtual environment`, you will see a bracket with the name of your virtual environment folder appear before the location of your folder at the terminal.

### Install Flask

Next, what you need to do is to install `Flask` **inside** the virtual environment. Else, it won't work.

Refer to the command below to install Flask:

```
pip install flask
```

### Run

After everything is installed, try to run this command to see if it works on your local machine.

```
python app.py
```

## Guide

First, all you need to do is to understand the HTML. You do not need to care about the styling. Focus on `value` and `name` in the `tag` in the `index.html` file.

After you look at the `index.html` file, click the link below to see how everything function when you combine both of it.

Please reach out to us if you face any difficulties. Good luck.

## Reference

Please refer to the link below in order to understand about how Flask communicate with the client-side to get the value of the button.

https://predictivehacks.com/?all-tips=how-to-add-action-buttons-in-flask