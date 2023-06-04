# Large Language Model

## How it works
A language model is built using supervised learning (X --> Y) to repeatedly prdict the next word.

`I love to eat bagel with cream cheese and lox.`

Input X = I love to eat
Output Y = Bagel

Input X = I love to eat bagel 
Oputput Y = with

Input X = I love to eat bagel with
Output Y = Cream Cheese

The sentence fragments are repeatedly used to train the model.

## Two types of LLMs

### Base LLM
Preditcs next word based on text training data

### Instruction Tuned LLM
Tries to follow instructions

## Getting from Base LLM to Instruction tuned LLM
Train base LLM with lots of data

Further train the model on
- Fine tune on examples of where the output follows an input instruction
- Obtain human feedback on the output generated and tag them useful, harmless etc to select good output.
- Tune LLM to generate highly rated output(using RLHF - Reinforcement Learning with Human Feedback)
