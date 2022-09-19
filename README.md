# COVID19_Chatbot
DLAM Project

## 1. What is our topic?  
&ensp; We want to create a chatbot. In the dialogue, the user can ask questions about COVID-19 and the robot will give
the appropriate answers. Questions related to COVID-19 can be asked in multiple languages, and their corresponding
answers will be in the same ones. That is to say, by talking to the chatbot, users can get information about COVID-19,
such as news, public health and community discussions, this greatly increases the dissemination of COVID-19 knowledge.
(In fact, it is not intended to be used in a clinical setting, and should not be used to influence clinical outcomes.)  
&ensp; Moreover, since we call it a chatbot and not a simple question and answer system, it is certain that an interactive
dialogue can take place between the user and the bot. For this reason, we will integrate common answers to everyday
questions into the system as well, such as greetings.  

## 2. Why do we choose this topic?  
COVID-19 has made a huge impact on people’s lives. It is very important to know how to properly understand
COVID-19. However, many people do not have the time to read a lot of information about it. We hope that, with this
chatbot, people can get informations quickly, easily, and efficiently.  
What’s more, the existing chatbots lack in conversational context, so we’re going to create a chatbot framework and
build a conversational model for promoting COVID-19 information.  
It is also interesting to learn how to incorporate deep learning techniques in NLP so that it is possible to find the most
appropriate answer for a given question. This can be very helpful for those seeking information about a particular topic
(in our case information about COVID-19).  

## 3. How to make a COVID-Chatbot?  
**Preparing dataset for NLP**  
To train a Deep learning NLP network in supervised mode, we need labeled dataset, so as the chatbot seq2seq model
will learn how to process questions and generate corresponding answers.  
**Recurrent neural networks (RNN) or CNN**  
RNN neuron uses its internal memory to maintain information about the previous inputs and update the hidden states
accordingly, which allows them to make predictions for every element of a sequence. Convolutional neural networks
applied to encoder-decoder models.  
**Seq2Seq model**  
Many tasks in NLP can be performed using a Seq2Seq mapping models: machine translation, summarization, question
answering, and many more. An Encoder-Decoder model for recurrent neural networks is an architecture for sequence-to-
sequence prediction problems in the field of natural language processing NLP, it takes a sequence as input and generates
another sequence as output, It is comprised of two sub-modules, encoder and decoder.  
**Concrete steps:**
1. Firstly, we will have a look at two datasets for our COVID-chatbot. After that we gonna transform those dataset into JSON format for our
purpose.  
2. Next, we will build a chatbot framework to process responses. In this step, we will pre-process the data using NLP
techniques like tokenization and stemming, and then build and train our model by using deep learning techniques
such as deep neural networks.
3. Lastly, we will use metrics such as accuracy scores to evaluate our model. And we’ll use tflearn, a layer above
tensorflow, and of course Python.
