# firstcommit

#### the purpose of this algorithm
This is a deep learning algorithm that takes in images and classifies each image as the type of clothing it is.

#################

## describing the code :) 

dividing by 255.o normalizes the values between zero and one                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
 plt.subplot creates many smaller grids
 xtickxs and yticks are the axis values on the graphs, being set to null
 plt.grid when set to false is used to remove grid lines
 plt.imshow is used to set what the graph will look like using the parameters, this specific one   is gray
 plt.show is used to display our graph :)

################################

 Sequential is the model where each layer is built on top of the other
 Flatten is used to flatten the image a one row vector
 The dense layer are used for convoluting and pooling with relu using formula max(0,x)

#############################


#############################
 model.fit is used to train the model
 after training the model, we are able to predict the values of the test images using model.predict and storing this array in a variable





############################
 i then went to write two functions that show predictios
 the first function "plot image" plots a specified number of images showing what has been predicted
 the second function "plot_value_array" shows the accuracy with which it predicted a value.

##########################
I then call these functions for the first fifteen images notice that the plt methods are similar to those used in the first plt subplot    

#### the output
the main output of this algorithm is an image of the clothing with its label at the bottom.
a graph is also shown next to the image that shows how well the model predicted the images label against other labels
